"""Konventionsprüfung des HyConCheck-Repositorys (kein Unit-Test).

Prüft gegen den verbindlichen Master-Prompt (docs/HYCONCHECK_MASTER_PROMPT.md):
1. Pflichtdateien und Pflichtverzeichnisse (§27) sind vorhanden.
2. Keine operativen Hinweise auf Entwicklungsassistenten oder Anbieter (§0, §39.12).
3. Relative Markdown-Links verweisen auf vorhandene Dateien/Verzeichnisse.
4. Der Master-Prompt ist vollständig: Hauptabschnitte §0–§39 lückenlos, Marker
   F1–F6, H1–H7, B0–B4, M1–M7, Definition of Done, Abschnitt 39.
5. H1–H7 und F1–F6 stehen mit unverändertem Wortlaut im Forschungsdesign (§7, §8).
6. AP-Inhalte (§25) stehen wörtlich in Projektplan und Projektauftrag; Planstunden
   je AP, Jahresscheiben und Gesamtsumme sind korrekt.
7. Kein Taxonomie-Obertyp ist als abgeschlossen markiert (§9, §39.6).
8. Keine Hypothese ist ohne Experimentregister als bestätigt/widerlegt geführt (§8, §23).
9. Forecast-Regel: Statusdokumente behaupten nicht, der Zeitnachweis fehle; die
   Forecast-Integration (BL-090) gilt nur als abgeschlossen, wenn alle
   Forecast-Artefakte vorliegen und konsistent sind (§39.7, §39.8).
10. Forecast-Artefakte (planning/forecast/): README, forecast_daily.csv (386 Zeilen),
    forecast_subactivities.csv (66 Zeilen), forecast_summary.csv vorhanden; keine
    Namensspalte, keine lokalen Pfade; AP-Summen 200/300/400/420/460/520/260,
    2026 = 640, 2027 = 1920, Gesamt = 2560 (Tages-, Subaktivitaets- und
    Summary-Ebene); Tagessumme je Datum 0 oder 8; Nicht-AP-Zeilen 0 Stunden;
    AP-Titel je AP eindeutig und blattuebergreifend konsistent; README nennt den
    verifizierten SHA-256 und den Hinweis "keine Ist-Aussage" (§25, §39.7).

Aufruf: py tests/check_repo_conventions.py
Exit-Code 0 bei Erfolg, 1 bei mindestens einem Befund.
"""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "docs/HYCONCHECK_MASTER_PROMPT.md"
PLAN = ROOT / "planning/PROJECT_PLAN_2026_2027.md"
CHARTER = ROOT / "docs/PROJECT_CHARTER.md"
DESIGN = ROOT / "docs/RESEARCH_DESIGN.md"
BACKLOG = ROOT / "planning/BACKLOG.md"
STATUS = ROOT / "status/CURRENT_STATUS.md"

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "docs/HYCONCHECK_MASTER_PROMPT.md",
    "docs/PROJECT_CHARTER.md",
    "docs/RESEARCH_DESIGN.md",
    "docs/TAXONOMY_V1.md",
    "planning/BACKLOG.md",
    "planning/PROJECT_PLAN_2026_2027.md",
    "status/CURRENT_STATUS.md",
    "status/DAILY_LOG.md",
    "docs/decisions/ADR-0000-vorlage.md",
    "docs/decisions/ADR-0001-neuaufbau-ohne-uebernahme.md",
    "docs/decisions/ADR-0002-master-prompt-als-massgebliche-quelle.md",
    "planning/forecast/README.md",
    "planning/forecast/forecast_daily.csv",
    "planning/forecast/forecast_subactivities.csv",
    "planning/forecast/forecast_summary.csv",
]

REQUIRED_DIRS = [
    "references",
    "data",
    "experiments",
    "configs",
    "results",
    "tests",
    "src",
    "docs/decisions",
]

# Namen von Entwicklungsassistenten und Anbietern, die nicht operativ genannt
# werden dürfen. Als Fragmente, damit zusammengesetzte Schreibweisen gefunden werden.
FORBIDDEN_TERMS = [
    "cla" + "ude",
    "anthro" + "pic",
    "chat" + "gpt",
    "co" + "dex",
    "open" + "ai",
    "copi" + "lot",
    "gem" + "ini",
]

TEXT_SUFFIXES = {".md", ".py", ".txt", ".yaml", ".yml", ".json", ".toml", ".cfg", ".ini", ".csv"}

PLANNED_HOURS = {"AP1": 200, "AP2": 300, "AP3": 400, "AP4": 420, "AP5": 460, "AP6": 520, "AP7": 260}
PLANNED_YEARS = {"2026": 640, "2027": 1920}
PLANNED_TOTAL = 2560

TAXONOMY_TYPES = [
    "Fakt und Wert",
    "Zeit und Status",
    "Modalität und Norm",
    "Akteur und Verantwortung",
    "Abhängigkeit und Schnittstelle",
]

MASTER_MARKERS = (
    [f"F{i}:" for i in range(1, 7)]
    + [f"H{i}:" for i in range(1, 8)]
    + [f"B{i}:" for i in range(0, 5)]
    + [f"M{i}:" for i in range(1, 8)]
    + ["## 37. Definition of Done", "## 39. Unmittelbarer Auftrag"]
)

# Dokumente, die den aktuellen Stand beschreiben (historische Einträge im
# Tageslog und in ADRs sind ausgenommen).
CURRENT_STATE_DOCS = [
    "README.md",
    "AGENTS.md",
    "docs/PROJECT_CHARTER.md",
    "planning/PROJECT_PLAN_2026_2027.md",
    "planning/BACKLOG.md",
    "status/CURRENT_STATUS.md",
]
FORECAST_DIR = ROOT / "planning/forecast"
FORECAST_README = FORECAST_DIR / "README.md"
FORECAST_DAILY = FORECAST_DIR / "forecast_daily.csv"
FORECAST_SUB = FORECAST_DIR / "forecast_subactivities.csv"
FORECAST_SUMMARY = FORECAST_DIR / "forecast_summary.csv"
FORECAST_SOURCE_SHA256 = "b647994cde8ab4c992865dd8b1c2a8872801646786ff19fafc15952273acf48f"
FORECAST_DAILY_ROWS = 386
FORECAST_SUB_ROWS = 66
FORECAST_DAILY_FIELDS = [
    "date", "weekday", "iso_week", "year", "month", "work_package", "ap_title",
    "planned_activity_raw", "subactivity", "planned_artifact", "planned_hours", "category",
]
FORECAST_SUB_FIELDS = ["work_package", "ap_title", "subactivity", "planned_hours", "planned_artifact"]
FORECAST_SUMMARY_FIELDS = ["scope", "work_package", "year", "planned_hours"]
FORECAST_NO_ACTUALS_HINT = "keine Ist-Aussage"
FORECAST_SENTENCE = (
    "Die Forecast-Quelle wurde bereitgestellt; ihre kontrollierte Prüfung und "
    "Integration erfolgt in einer separaten Etappe"
)

findings: list[str] = []


def report(msg: str) -> None:
    findings.append(msg)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def tracked_text_files() -> list[Path]:
    """Versionierte und neu hinzugefügte Textdateien (ohne .git)."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        ).stdout
        paths = [ROOT / line for line in out.splitlines() if line.strip()]
    except (subprocess.CalledProcessError, FileNotFoundError):
        paths = [p for p in ROOT.rglob("*") if ".git" not in p.parts]
    return [p for p in paths if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES]


def check_required() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            report(f"Pflichtdatei fehlt: {rel}")
    for rel in REQUIRED_DIRS:
        if not (ROOT / rel).is_dir():
            report(f"Pflichtverzeichnis fehlt: {rel}")


def check_forbidden_terms(files: list[Path]) -> None:
    this_file = Path(__file__).resolve()
    for path in files:
        if path.resolve() == this_file:
            continue
        for lineno, line in enumerate(read(path).splitlines(), start=1):
            lowered = line.lower()
            for term in FORBIDDEN_TERMS:
                if term in lowered:
                    report(
                        f"Unzulässiger Werkzeug-/Anbieterhinweis '{term}' in "
                        f"{path.relative_to(ROOT).as_posix()}:{lineno}"
                    )


LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_links(files: list[Path]) -> None:
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        for match in LINK_RE.finditer(read(path)):
            target = match.group(1)
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target_path = target.split("#", 1)[0]
            if target_path and not (path.parent / target_path).resolve().exists():
                report(
                    f"Interner Link nicht auflösbar in "
                    f"{path.relative_to(ROOT).as_posix()}: {target}"
                )


def master_text() -> str | None:
    if not MASTER.is_file():
        report("Master-Prompt fehlt")
        return None
    return read(MASTER)


def check_master_completeness(text: str) -> None:
    numbers = [int(m.group(1)) for m in re.finditer(r"^## (\d+)\.", text, flags=re.M)]
    if numbers != list(range(0, 40)):
        report(f"Master-Prompt: Hauptabschnitte nicht lückenlos 0–39, gefunden: {numbers}")
    for marker in MASTER_MARKERS:
        if marker not in text:
            report(f"Master-Prompt: Marker '{marker}' fehlt")


def labelled_blocks(text: str, prefix: str, ids: list[str]) -> dict[str, str]:
    """Absätze nach Zeilen der Form 'H1:' / 'F1:' / 'AP1 – … Stunden geplant'."""
    lines = text.splitlines()
    blocks: dict[str, str] = {}
    for label in ids:
        pattern = re.compile(rf"^{re.escape(prefix)}{re.escape(label)}\b")
        for i, line in enumerate(lines):
            if pattern.match(line.strip()) and (
                line.strip().endswith(":") or "Stunden geplant" in line
            ):
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                para: list[str] = []
                while j < len(lines) and lines[j].strip():
                    para.append(lines[j].strip())
                    j += 1
                blocks[label] = norm(" ".join(para))
                break
    return blocks


def check_wording(master: str) -> None:
    if not DESIGN.is_file():
        return
    design = norm(read(DESIGN))
    hyps = labelled_blocks(master, "", [f"H{i}" for i in range(1, 8)])
    qs = labelled_blocks(master, "", [f"F{i}" for i in range(1, 7)])
    for label, expected in {**hyps, **qs}.items():
        if not expected:
            report(f"Master-Prompt: Wortlaut zu {label} nicht extrahierbar")
        elif expected not in design:
            report(f"Forschungsdesign: Wortlaut von {label} fehlt oder wurde verändert")
    for group, expected_ids in (("H", 7), ("F", 6)):
        found = len([k for k in (hyps if group == "H" else qs) if k.startswith(group)])
        if found != expected_ids:
            report(f"Master-Prompt: nur {found} von {expected_ids} {group}-Einträgen gefunden")


def check_work_packages(master: str) -> None:
    aps = labelled_blocks(master, "", list(PLANNED_HOURS))
    if len(aps) != len(PLANNED_HOURS):
        report(f"Master-Prompt: nur {len(aps)} von {len(PLANNED_HOURS)} AP-Beschreibungen (§25) extrahierbar")
    hours_re = re.compile(r"^(AP[1-7]) – (\d[\d.]*) Stunden geplant", flags=re.M)
    master_hours = {m.group(1): int(m.group(2).replace(".", "")) for m in hours_re.finditer(master)}
    for ap, expected in PLANNED_HOURS.items():
        if master_hours.get(ap) != expected:
            report(f"Master-Prompt: {ap} Planstunden {master_hours.get(ap)} ≠ erwartet {expected}")
    for doc in (PLAN, CHARTER):
        if not doc.is_file():
            continue
        text = norm(read(doc))
        for ap, wording in aps.items():
            if wording and wording not in text:
                report(f"{doc.relative_to(ROOT).as_posix()}: Wortlaut der AP-Inhalte von {ap} (§25) fehlt")


ROW_RE = re.compile(r"^\|\s*(AP[1-7]|2026|2027|Gesamt)\s*\|(.*)\|\s*$")


def check_planned_hours() -> None:
    if not PLAN.is_file():
        return
    ap_total: dict[str, int] = {}
    years: dict[str, int] = {}
    for line in read(PLAN).splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        cells = [c.strip().strip("*") for c in m.group(2).split("|")]
        nums = [c for c in cells if re.fullmatch(r"\d{1,3}(\.\d{3})*", c)]
        if not nums:
            continue
        value = int(nums[-1].replace(".", ""))
        key = m.group(1)
        if key.startswith("AP"):
            ap_total.setdefault(key, value)
        else:
            years.setdefault(key, value)
    for ap, expected in PLANNED_HOURS.items():
        if ap not in ap_total:
            report(f"Projektplan: Zeile für {ap} nicht gefunden oder nicht auswertbar")
        elif ap_total[ap] != expected:
            report(f"Projektplan: {ap} = {ap_total[ap]}, erwartet {expected}")
    if ap_total and sum(ap_total.values()) != PLANNED_TOTAL:
        report(f"Projektplan: Summe AP1–AP7 = {sum(ap_total.values())}, erwartet {PLANNED_TOTAL}")
    for year, expected in PLANNED_YEARS.items():
        if years.get(year) != expected:
            report(f"Projektplan: Jahresscheibe {year} = {years.get(year)}, erwartet {expected}")
    if years.get("Gesamt") != PLANNED_TOTAL:
        report(f"Projektplan: Gesamt = {years.get('Gesamt')}, erwartet {PLANNED_TOTAL}")


def check_taxonomy_status() -> None:
    tax = ROOT / "docs/TAXONOMY_V1.md"
    if not tax.is_file():
        return
    text = read(tax)
    for name in TAXONOMY_TYPES:
        if name not in text:
            report(f"Taxonomie: Obertyp '{name}' nicht in TAXONOMY_V1.md enthalten")
    for line in text.splitlines():
        if line.startswith("|") and any(t in line for t in TAXONOMY_TYPES):
            if re.search(r"\|\s*abgeschlossen\s*\|?\s*$", line):
                report(f"Taxonomie: Obertyp als abgeschlossen markiert: {line.strip()}")


def check_hypothesis_status() -> None:
    if not DESIGN.is_file():
        return
    register = ROOT / "experiments/REGISTER.md"
    for line in read(DESIGN).splitlines():
        if re.match(r"^\|\s*H[1-7]\s*\|", line) and re.search(
            r"\|\s*(bestätigt|widerlegt)\s*\|?\s*$", line
        ):
            if not register.is_file():
                report(f"Forschungsdesign: Hypothese ohne Experimentregister als bewertet geführt: {line.strip()}")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), list(reader)


def check_forecast() -> list[str]:
    """Prüft die Forecast-Artefakte (§39.7); gibt die Forecast-Befunde zusätzlich zurück."""
    local: list[str] = []

    def rep(msg: str) -> None:
        local.append(msg)
        report(msg)

    for path in (FORECAST_README, FORECAST_DAILY, FORECAST_SUB, FORECAST_SUMMARY):
        if not path.is_file():
            rep(f"Forecast: {path.relative_to(ROOT).as_posix()} fehlt")
    if local:
        return local

    d_fields, daily = read_csv(FORECAST_DAILY)
    s_fields, subs = read_csv(FORECAST_SUB)
    m_fields, summary = read_csv(FORECAST_SUMMARY)
    for name, fields, expected in (
        ("forecast_daily.csv", d_fields, FORECAST_DAILY_FIELDS),
        ("forecast_subactivities.csv", s_fields, FORECAST_SUB_FIELDS),
        ("forecast_summary.csv", m_fields, FORECAST_SUMMARY_FIELDS),
    ):
        missing = [f for f in expected if f not in fields]
        if missing:
            rep(f"Forecast: {name} ohne Pflichtfelder {missing}")
        personal = [f for f in fields if re.match(r"(name|person|mitarbeiter|bearbeiter)", f, flags=re.I)]
        if personal:
            rep(f"Forecast: {name} enthält personenbezogene Spalte {personal}")
    for path in (FORECAST_DAILY, FORECAST_SUB, FORECAST_SUMMARY, FORECAST_README):
        if re.search(r"[A-Za-z]:\\|[A-Za-z]:/|/Users/|\\Users\\", read(path)):
            rep(f"Forecast: {path.name} enthält einen lokalen Dateipfad")
    if len(daily) != FORECAST_DAILY_ROWS:
        rep(f"Forecast: forecast_daily.csv hat {len(daily)} Datenzeilen, erwartet {FORECAST_DAILY_ROWS}")
    if len(subs) != FORECAST_SUB_ROWS:
        rep(f"Forecast: forecast_subactivities.csv hat {len(subs)} Datenzeilen, erwartet {FORECAST_SUB_ROWS}")
    if local:
        return local

    ap_daily: dict[str, int] = {ap: 0 for ap in PLANNED_HOURS}
    year_daily: dict[str, int] = {}
    ap_year: dict[tuple[str, str], int] = {}
    per_date: dict[str, int] = {}
    titles_daily: dict[str, set[str]] = {}
    stage_re = re.compile(r"\s*\(geplante Etappe \d+/\d+\)\s*$")
    for i, row in enumerate(daily, start=2):
        try:
            hours = int(row["planned_hours"])
        except ValueError:
            rep(f"Forecast: forecast_daily.csv:{i} planned_hours nicht numerisch")
            continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["date"]):
            rep(f"Forecast: forecast_daily.csv:{i} Datum nicht ISO: {row['date']}")
        cat, ap = row["category"], row["work_package"]
        if cat not in ("AP", "BUFFER", "HOLIDAY"):
            rep(f"Forecast: forecast_daily.csv:{i} unzulässige category {cat}")
        per_date[row["date"]] = per_date.get(row["date"], 0) + hours
        if cat == "AP":
            if ap not in PLANNED_HOURS:
                rep(f"Forecast: forecast_daily.csv:{i} AP-Zeile ohne gültiges Arbeitspaket ({ap})")
                continue
            ap_daily[ap] += hours
            year_daily[row["year"]] = year_daily.get(row["year"], 0) + hours
            ap_year[(ap, row["year"])] = ap_year.get((ap, row["year"]), 0) + hours
            titles_daily.setdefault(ap, set()).add(row["ap_title"])
            if stage_re.sub("", row["planned_activity_raw"]) != row["subactivity"]:
                rep(f"Forecast: forecast_daily.csv:{i} subactivity ≠ planned_activity_raw ohne Etappenkennung")
        else:
            if hours != 0:
                rep(f"Forecast: forecast_daily.csv:{i} Nicht-AP-Zeile mit {hours} Stunden")
            if ap:
                rep(f"Forecast: forecast_daily.csv:{i} Nicht-AP-Zeile mit Arbeitspaket {ap}")
    bad_days = sorted(d for d, h in per_date.items() if h not in (0, 8))
    if bad_days:
        rep(f"Forecast: Tagessumme ≠ 0/8 an {len(bad_days)} Tagen, z. B. {bad_days[:5]}")
    for ap, expected in PLANNED_HOURS.items():
        if ap_daily.get(ap) != expected:
            rep(f"Forecast: Tagesplanung {ap} = {ap_daily.get(ap)}, erwartet {expected}")
    for year, expected in PLANNED_YEARS.items():
        if year_daily.get(year) != expected:
            rep(f"Forecast: Tagesplanung Jahr {year} = {year_daily.get(year)}, erwartet {expected}")
    if sum(ap_daily.values()) != PLANNED_TOTAL:
        rep(f"Forecast: Tagesplanung Gesamt = {sum(ap_daily.values())}, erwartet {PLANNED_TOTAL}")
    for ap, titles in titles_daily.items():
        if len(titles) != 1:
            rep(f"Forecast: {ap} hat mehrere AP-Titel in forecast_daily.csv: {sorted(titles)}")

    ap_sub: dict[str, int] = {}
    titles_sub: dict[str, set[str]] = {}
    sub_keys: set[tuple[str, str]] = set()
    for i, row in enumerate(subs, start=2):
        ap = row["work_package"]
        if ap not in PLANNED_HOURS:
            rep(f"Forecast: forecast_subactivities.csv:{i} ungültiges Arbeitspaket {ap}")
            continue
        try:
            ap_sub[ap] = ap_sub.get(ap, 0) + int(row["planned_hours"])
        except ValueError:
            rep(f"Forecast: forecast_subactivities.csv:{i} planned_hours nicht numerisch")
        titles_sub.setdefault(ap, set()).add(row["ap_title"])
        sub_keys.add((ap, row["subactivity"]))
    for ap, expected in PLANNED_HOURS.items():
        if ap_sub.get(ap) != expected:
            rep(f"Forecast: Subaktivitäten {ap} = {ap_sub.get(ap)}, erwartet {expected}")
        if titles_sub.get(ap) and titles_daily.get(ap) and titles_sub[ap] != titles_daily[ap]:
            rep(f"Forecast: AP-Titel von {ap} in Tagesplanung und Subaktivitäten verschieden")
    daily_keys = {(r["work_package"], r["subactivity"]) for r in daily if r["category"] == "AP"}
    if daily_keys - sub_keys:
        rep(f"Forecast: Tagesplanungs-Subaktivitäten ohne Eintrag in Subaktivitäten: {sorted(daily_keys - sub_keys)[:3]}")
    if sub_keys - daily_keys:
        rep(f"Forecast: Subaktivitäten ohne Tagesplanungszeile: {sorted(sub_keys - daily_keys)[:3]}")

    summ = {(r["scope"], r["work_package"], r["year"]): r["planned_hours"] for r in summary}
    expected_summary: dict[tuple[str, str, str], int] = {("total", "ALL", "ALL"): PLANNED_TOTAL}
    expected_summary.update({("work_package", ap, "ALL"): h for ap, h in PLANNED_HOURS.items()})
    expected_summary.update({("year", "ALL", y): h for y, h in PLANNED_YEARS.items()})
    expected_summary.update({("work_package_year", ap, y): h for (ap, y), h in ap_year.items()})
    for key, expected in expected_summary.items():
        if summ.get(key) != str(expected):
            rep(f"Forecast: forecast_summary.csv {key} = {summ.get(key)}, erwartet {expected}")

    readme = read(FORECAST_README)
    if FORECAST_SOURCE_SHA256 not in readme:
        rep("Forecast: README nennt nicht den verifizierten SHA-256 der Quelle")
    if FORECAST_NO_ACTUALS_HINT not in readme or "Ist-Stunden" not in readme:
        rep("Forecast: README ohne Hinweis, dass der Forecast keine Ist-Aussage ist")
    return local


def check_forecast_rule(forecast_findings: list[str]) -> None:
    missing_re = re.compile(r"Zeitnachweis[^\n]{0,80}(nicht vor|nicht vorhanden|fehlt)", flags=re.I)
    for rel in CURRENT_STATE_DOCS:
        path = ROOT / rel
        if not path.is_file():
            continue
        for lineno, line in enumerate(read(path).splitlines(), start=1):
            if missing_re.search(line):
                report(f"{rel}:{lineno}: behauptet fehlenden Zeitnachweis; Forecast-Quelle ist bereitgestellt")
    integrated = FORECAST_DIR.is_dir() and not forecast_findings
    if not integrated:
        for doc in (PLAN, STATUS):
            if doc.is_file() and FORECAST_SENTENCE not in norm(read(doc)):
                report(f"{doc.relative_to(ROOT).as_posix()}: Forecast-Hinweis fehlt (Forecast nicht integriert)")
    if BACKLOG.is_file():
        for line in read(BACKLOG).splitlines():
            if not line.startswith("| BL-090"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            status = cells[2].lower() if len(cells) > 2 else ""
            done = status.startswith("abgeschlossen")
            if done and not integrated:
                report("Backlog: BL-090 als abgeschlossen geführt, aber Forecast-Artefakte fehlen oder sind inkonsistent")
            if not done and integrated:
                report("Backlog: Forecast-Artefakte vollständig und konsistent, BL-090 aber nicht als abgeschlossen geführt")


def main() -> int:
    files = tracked_text_files()
    check_required()
    check_forbidden_terms(files)
    check_links(files)
    master = master_text()
    if master is not None:
        check_master_completeness(master)
        check_wording(master)
        check_work_packages(master)
    check_planned_hours()
    check_taxonomy_status()
    check_hypothesis_status()
    forecast_findings = check_forecast()
    check_forecast_rule(forecast_findings)

    if findings:
        print("Befunde:")
        for f in findings:
            print(f"  - {f}")
        print(f"\n{len(findings)} Befund(e).")
        return 1
    print(f"Alle Prüfungen bestanden ({len(files)} Textdateien geprüft).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
