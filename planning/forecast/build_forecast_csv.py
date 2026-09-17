"""Erzeugt die maschinenlesbaren Forecast-Artefakte aus der Planungsquelle.

Liest die Tabellenblätter "Tagesplanung" und "Subaktivitäten" der bereitgestellten
Planungsquelle (HyConCheck_Zeitnachweis.xlsx) ausschließlich lesend und schreibt
forecast_daily.csv, forecast_subactivities.csv und forecast_summary.csv in dieses
Verzeichnis. Es werden nur Planwerte übernommen; Ist-Stunden, Erledigungsgrade oder
Personennamen werden nicht erzeugt bzw. nicht übernommen (Master-Prompt §25, §39.7).

Aufruf (Pfad zur Quelldatei wird nur als Argument übergeben, nicht gespeichert):
    py planning/forecast/build_forecast_csv.py <pfad-zur-quelldatei.xlsx>

Verwendet nur die Python-Standardbibliothek.
"""

from __future__ import annotations

import csv
import hashlib
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
}
AP_IDS = {f"AP{i}" for i in range(1, 8)}
CATEGORY = {"Puffer / kein FuE": "BUFFER", "Feiertag": "HOLIDAY"}
STAGE_RE = re.compile(r"\s*\(geplante Etappe \d+/\d+\)\s*$")
WEEKDAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_sheets(path: Path) -> dict[str, list[dict[str, object]]]:
    """Gibt je Tabellenblatt eine Liste von Zeilen (Spaltenbuchstabe -> Wert) zurück."""
    z = zipfile.ZipFile(path, "r")
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    targets = {r.get("Id"): r.get("Target") for r in rels.findall("pr:Relationship", NS)}
    sst: list[str] = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            sst.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    styles = ET.fromstring(z.read("xl/styles.xml"))
    numfmts = {int(n.get("numFmtId")): n.get("formatCode", "") for n in styles.iter("{%s}numFmt" % NS["m"])}
    xf_fmt = [int(xf.get("numFmtId", "0")) for xf in styles.find("m:cellXfs", NS)]
    builtin_date = {14, 15, 16, 17, 18, 19, 20, 21, 22, 45, 46, 47}

    def is_date(style: str | None) -> bool:
        if style is None:
            return False
        fmt = xf_fmt[int(style)]
        return fmt in builtin_date or bool(re.search(r"[dmy]", numfmts.get(fmt, ""), flags=re.I))

    sheets: dict[str, list[dict[str, object]]] = {}
    for s in wb.find("m:sheets", NS):
        name = s.get("name")
        target = targets[s.get("{%s}id" % NS["r"])]
        root = ET.fromstring(z.read("xl/" + target.lstrip("/")))
        rows: list[dict[str, object]] = []
        for row in root.find("m:sheetData", NS):
            cells: dict[str, object] = {}
            for c in row:
                col = re.match(r"[A-Z]+", c.get("r")).group(0)
                t, v = c.get("t"), c.find("m:v", NS)
                if c.find("m:f", NS) is not None:
                    raise SystemExit(f"Formel in {name}!{c.get('r')} – Quelle enthält Formeln, Abbruch")
                if v is None:
                    cells[col] = None
                elif t == "s":
                    cells[col] = sst[int(v.text)]
                elif t == "b":
                    cells[col] = bool(int(v.text))
                else:
                    num = float(v.text)
                    if is_date(c.get("s")):
                        cells[col] = datetime(1899, 12, 30) + timedelta(days=num)
                    else:
                        cells[col] = int(num) if num.is_integer() else num
            rows.append(cells)
        sheets[name] = rows
    return sheets


def build(source: Path) -> None:
    sheets = load_sheets(source)
    daily_rows = sheets["Tagesplanung"]
    sub_rows = sheets["Subaktivitäten"]
    header = daily_rows[0]
    expected = ["Datum", "Wochentag", "KW", "Jahr", "Monat", "Name", "Projekt", "Arbeitspaket", "AP-Titel", "Tätigkeit", "Geplantes Artefakt", "H"]
    if [header.get(k) for k in "ABCDEFGHIJKL"] != expected:
        raise SystemExit(f"Unerwartete Spalten in Tagesplanung: {header}")
    if [sub_rows[0].get(k) for k in "ABCDE"] != ["Arbeitspaket", "AP-Titel", "Subaktivität", "Planstunden", "Geplantes Artefakt"]:
        raise SystemExit(f"Unerwartete Spalten in Subaktivitäten: {sub_rows[0]}")

    daily_out: list[dict[str, object]] = []
    for c in daily_rows[1:]:
        date: datetime = c["A"]  # type: ignore[assignment]
        label = str(c.get("H") or "")
        activity = str(c.get("J") or "")
        is_ap = label in AP_IDS
        daily_out.append(
            {
                "date": date.strftime("%Y-%m-%d"),
                "weekday": WEEKDAYS[date.weekday()],
                "iso_week": date.isocalendar()[1],
                "year": date.year,
                "month": date.month,
                "work_package": label if is_ap else "",
                "ap_title": (c.get("I") or "") if is_ap else "",
                "planned_activity_raw": activity,
                "subactivity": STAGE_RE.sub("", activity),
                "planned_artifact": c.get("K") or "",
                "planned_hours": int(c.get("L") or 0),
                "category": "AP" if is_ap else CATEGORY.get(label, "BUFFER"),
                "source_label": label,
            }
        )
        # Spalte F (Name) wird bewusst nicht übernommen.

    sub_out = [
        {
            "work_package": c["A"],
            "ap_title": c["B"],
            "subactivity": c["C"],
            "planned_hours": int(c["D"]),
            "planned_artifact": c["E"],
        }
        for c in sub_rows[1:]
    ]

    ap_h: dict[str, int] = defaultdict(int)
    yr_h: dict[int, int] = defaultdict(int)
    ap_yr: dict[tuple[str, int], int] = defaultdict(int)
    cat_h: dict[str, int] = defaultdict(int)
    for r in daily_out:
        h = int(r["planned_hours"])
        cat_h[str(r["category"])] += h
        if r["category"] == "AP":
            ap_h[str(r["work_package"])] += h
            yr_h[int(r["year"])] += h
            ap_yr[(str(r["work_package"]), int(r["year"]))] += h
    summary: list[dict[str, object]] = []
    for ap in sorted(ap_h):
        summary.append({"scope": "work_package", "work_package": ap, "year": "ALL", "planned_hours": ap_h[ap]})
    for y in sorted(yr_h):
        summary.append({"scope": "year", "work_package": "ALL", "year": y, "planned_hours": yr_h[y]})
    for (ap, y) in sorted(ap_yr):
        summary.append({"scope": "work_package_year", "work_package": ap, "year": y, "planned_hours": ap_yr[(ap, y)]})
    for cat in ("BUFFER", "HOLIDAY"):
        summary.append({"scope": "category", "work_package": cat, "year": "ALL", "planned_hours": cat_h.get(cat, 0)})
    summary.append({"scope": "total", "work_package": "ALL", "year": "ALL", "planned_hours": sum(ap_h.values())})

    def write(name: str, rows: list[dict[str, object]]) -> None:
        with (OUT_DIR / name).open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), lineterminator="\n")
            w.writeheader()
            w.writerows(rows)

    write("forecast_daily.csv", daily_out)
    write("forecast_subactivities.csv", sub_out)
    write("forecast_summary.csv", summary)
    print(f"Quelle SHA-256: {sha256(source)}")
    print(f"forecast_daily.csv: {len(daily_out)} Zeilen; forecast_subactivities.csv: {len(sub_out)} Zeilen; forecast_summary.csv: {len(summary)} Zeilen")
    print("AP:", dict(sorted(ap_h.items())), "Jahr:", dict(sorted(yr_h.items())), "Gesamt:", sum(ap_h.values()))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    build(Path(sys.argv[1]))
