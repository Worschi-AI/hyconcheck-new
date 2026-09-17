"""Qualitätsprüfung der Repository-Konventionen für HyConCheck.

Prüft:
1. Pflichtdateien und Pflichtverzeichnisse sind vorhanden.
2. Keine operativen Hinweise auf Entwicklungsassistenten oder deren Anbieter
   in versionierten Textdateien.
3. Relative Markdown-Links verweisen auf vorhandene Dateien/Verzeichnisse.
4. Planstunden im Projektplan sind in sich konsistent (AP-Summen, Jahresscheiben).
5. Kein Taxonomie-Obertyp ist in TAXONOMY_V1.md als abgeschlossen markiert.
6. Fehlender Zeitnachweis ist als offene Planungsgrundlage dokumentiert.

Aufruf: py tests/check_repo_conventions.py
Exit-Code 0 bei Erfolg, 1 bei mindestens einem Befund.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "docs/HYCONCHECK_MASTER_PROMPT.md",
    "docs/PROJECT_CHARTER.md",
    "docs/RESEARCH_DESIGN.md",
    "docs/TAXONOMY_V1.md",
    "planning/PROJECT_PLAN_2026_2027.md",
    "planning/BACKLOG.md",
    "status/CURRENT_STATUS.md",
    "status/DAILY_LOG.md",
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

# Namen von Entwicklungsassistenten und Anbietern, die in Repository-Dateien
# nicht operativ genannt werden dürfen. Bewusst als Fragmente, damit auch
# zusammengesetzte Schreibweisen gefunden werden.
FORBIDDEN_TERMS = [
    "cla" + "ude",
    "anthro" + "pic",
    "chat" + "gpt",
    "co" + "dex",
    "open" + "ai",
    "copi" + "lot",
    "gem" + "ini",
]

TEXT_SUFFIXES = {".md", ".py", ".txt", ".yaml", ".yml", ".json", ".toml", ".cfg", ".ini"}

PLANNED_HOURS = {
    "AP1": 200,
    "AP2": 300,
    "AP3": 400,
    "AP4": 420,
    "AP5": 460,
    "AP6": 520,
    "AP7": 260,
}
PLANNED_2026 = 640
PLANNED_2027 = 1920
PLANNED_TOTAL = 2560

TAXONOMY_TYPES = [
    "Fakt und Wert",
    "Zeit und Status",
    "Modalität und Norm",
    "Akteur und Verantwortung",
    "Abhängigkeit und Schnittstelle",
]

findings: list[str] = []


def report(msg: str) -> None:
    findings.append(msg)


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
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), start=1):
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
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                report(
                    f"Interner Link nicht auflösbar in "
                    f"{path.relative_to(ROOT).as_posix()}: {target}"
                )


ROW_RE = re.compile(r"^\|\s*(AP[1-7])\s*\|(.*)\|\s*$")


def check_planned_hours() -> None:
    plan = ROOT / "planning/PROJECT_PLAN_2026_2027.md"
    if not plan.is_file():
        return
    seen: dict[str, tuple[int, int, int]] = {}
    for line in plan.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        nums = [c for c in cells if re.fullmatch(r"\d{1,3}(\.\d{3})*", c)]
        if len(nums) < 3:
            continue
        y2026, y2027, total = (int(n.replace(".", "")) for n in nums[-3:])
        seen[m.group(1)] = (y2026, y2027, total)

    for ap, expected in PLANNED_HOURS.items():
        if ap not in seen:
            report(f"Projektplan: Zeile für {ap} nicht gefunden oder nicht auswertbar")
            continue
        y2026, y2027, total = seen[ap]
        if total != expected:
            report(f"Projektplan: {ap} Gesamt = {total}, erwartet {expected}")
        if y2026 + y2027 != total:
            report(f"Projektplan: {ap} Jahreswerte {y2026}+{y2027} ≠ Gesamt {total}")

    if seen:
        s2026 = sum(v[0] for v in seen.values())
        s2027 = sum(v[1] for v in seen.values())
        stotal = sum(v[2] for v in seen.values())
        if s2026 != PLANNED_2026:
            report(f"Projektplan: Summe 2026 = {s2026}, erwartet {PLANNED_2026}")
        if s2027 != PLANNED_2027:
            report(f"Projektplan: Summe 2027 = {s2027}, erwartet {PLANNED_2027}")
        if stotal != PLANNED_TOTAL:
            report(f"Projektplan: Gesamtsumme = {stotal}, erwartet {PLANNED_TOTAL}")


def check_taxonomy_status() -> None:
    tax = ROOT / "docs/TAXONOMY_V1.md"
    if not tax.is_file():
        return
    text = tax.read_text(encoding="utf-8")
    for name in TAXONOMY_TYPES:
        if name not in text:
            report(f"Taxonomie: Obertyp '{name}' nicht in TAXONOMY_V1.md enthalten")
    for line in text.splitlines():
        if line.startswith("|") and any(t in line for t in TAXONOMY_TYPES):
            if re.search(r"\|\s*abgeschlossen\s*\|?\s*$", line):
                report(f"Taxonomie: Obertyp als abgeschlossen markiert: {line.strip()}")


def check_timesheet_documented() -> None:
    timesheet = ROOT / "HyConCheck_Zeitnachweis.xlsx"
    plan = ROOT / "planning/PROJECT_PLAN_2026_2027.md"
    if timesheet.exists():
        return
    if plan.is_file() and "HyConCheck_Zeitnachweis.xlsx" not in plan.read_text(encoding="utf-8"):
        report("Zeitnachweis fehlt, ist aber im Projektplan nicht als offene Planungsgrundlage dokumentiert")


def main() -> int:
    files = tracked_text_files()
    check_required()
    check_forbidden_terms(files)
    check_links(files)
    check_planned_hours()
    check_taxonomy_status()
    check_timesheet_documented()

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
