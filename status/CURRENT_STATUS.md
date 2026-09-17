# HyConCheck – Aktueller Stand

Stand: **17.09.2026**
Branch: `work/master-prompt-alignment` (ausgehend von `main` @ `588584e`)
Projektzeitraum: 01.09.2026 – 31.12.2027
Maßgebliche Quelle: [docs/HYCONCHECK_MASTER_PROMPT.md](../docs/HYCONCHECK_MASTER_PROMPT.md)

## Gesamtstand

In diesem Repository ist die Projektgrundlage eingerichtet (BL-000) und an den vollständigen Forschungsauftrag angeglichen (BL-000a, [ADR-0002](../docs/decisions/ADR-0002-master-prompt-als-massgebliche-quelle.md)). Das Repository ist ein vollständiger Neuaufbau ohne Übernahme früherer Dateien, Commits, Erledigungsstände oder Forschungsergebnisse ([ADR-0001](../docs/decisions/ADR-0001-neuaufbau-ohne-uebernahme.md)).

**In diesem Repository** liegen noch keine Rechercheergebnisse, Daten, Implementierungen oder Experimente vor. Fachlich zum Vorhaben gehörende Arbeiten, die seit September 2026 außerhalb dieses Repositorys stattgefunden haben, liegen im Projektzeitraum, werden hier aber nicht als durchgeführt oder abgeschlossen geführt.

## Stand je Arbeitspaket (§25)

| AP | Inhalt (Kurz) | Planstunden | Status |
|---|---|---:|---|
| AP1 | Lösungsraum, Widerspruchstaxonomie, formale Kriterien | 200 | offen – nächste Etappe BL-001 |
| AP2 | Benchmarkmethodik, Testdatengenerator, Ground Truth | 300 | offen |
| AP3 | Baselines B0–B4, Evaluationspipeline, Vergleich | 400 | offen |
| AP4 | Entitätsauflösung; Attribut-, Zeit-, Status-, Provenienzverarbeitung | 420 | offen |
| AP5 | Evidenzgraph, Fusionsalgorithmen, Architekturvergleich | 460 | offen |
| AP6 | Kalibrierung, Ablation, Fehler- und Robustheitsanalysen | 520 | offen |
| AP7 | Validierung auf zurückgehaltenen Testdaten, Baselinevergleich | 260 | offen |

Planstunden sind Planwerte des Forschungsantrags; Ist-Stunden werden hier nicht geführt.

## Stand je Meilenstein (§36)

| MS | Status |
|---|---|
| M1 Taxonomie und Entscheidungskriterien operationalisiert | offen |
| M2 Benchmark und Ground Truth versioniert | offen |
| M3 Baselines reproduzierbar evaluiert | offen |
| M4 Entitäts-, Zeit-, Status-, Provenienzrepräsentation untersucht | offen |
| M5 Evidenzgraph-/Fusionsarchitekturen gegen Baselines verglichen | offen |
| M6 Kalibrierung, Fehleranalysen, Ablationen, Robustheitstests | offen |
| M7 Finale Evaluation auf Testset | offen |

## Stand der Forschungsbausteine

| Baustein | Status |
|---|---|
| Wissenslücke (§4) | zu überprüfende Annahme; Überprüfung durch Literaturrecherche offen (BL-004) |
| Zentrale Forschungsfrage, F1–F6 | übernommen; offen |
| Hypothesen H1–H7 | übernommen; **ungeprüft** |
| Taxonomie-Obertypen (5) | verbindlich; Operationalisierung nicht begonnen |
| Benchmark, Ground Truth, Split | offen |
| Baselines B0–B4 | offen |
| Evidenzgraph, Fusion, Architektur | offen; keine Vorfestlegung |
| Experimente | keine durchgeführt |

## Stand je Taxonomie-Obertyp

| Obertyp | Status |
|---|---|
| Fakt und Wert | offen |
| Zeit und Status | offen |
| Modalität und Norm | offen |
| Akteur und Verantwortung | offen |
| Abhängigkeit und Schnittstelle | offen |

Kein Obertyp ist abgeschlossen; die Operationalisierung beginnt in AP1.

## Qualitäts-Gates (§35)

Noch kein AP-Übergang; kein Gate geprüft.

## Forecast und Fortschrittskontrolle (§39.10)

- Die Forecast-Quelle wurde bereitgestellt; ihre kontrollierte Prüfung und Integration erfolgt in einer separaten Etappe (BL-090). Im Repository liegen daher noch keine AP-Termine, keine Jahresverteilung je AP und keine Abschlussprognose vor.
- Wöchentlicher Soll-Ist-Abgleich (BL-091) und monatliche Abschlussprognose (BL-092): eingerichtet als wiederkehrende Backlog-Einträge; erster Abgleich noch nicht erfolgt.
- Terminrisiken und Gegenmaßnahmen: [Projektplan, Abschnitt 7](../planning/PROJECT_PLAN_2026_2027.md).

## Offene Planungsgrundlagen

- BL-090 Forecast-Integration (siehe oben).

## Offene methodische Punkte

- Überprüfung der Wissenslücke (BL-004), Operationalisierung von F1–F6/H1–H7 (BL-005), Taxonomie-Operationalisierung (BL-010 bis BL-014), Benchmark-Schema (BL-020), Verfügbarkeit einer kostenfreien LLM-Baseline B4 (BL-035, §33).

## Qualitätsprüfungen (letzter Lauf 17.09.2026)

- `py tests/check_repo_conventions.py`: bestanden
- `git diff --check`: bestanden
- `python -m pytest`, `ruff check .`: noch nicht anwendbar (kein ausführbarer Projektcode in `src/`), siehe [tests/README.md](../tests/README.md)

## Nächste Etappe

**BL-001 – Definition des Rechercheprotokolls und der Suchstrategie für den Stand der Technik (AP1).**

## Verweise

- [Projektauftrag](../docs/PROJECT_CHARTER.md) · [Forschungsdesign](../docs/RESEARCH_DESIGN.md) · [Taxonomie V1](../docs/TAXONOMY_V1.md) · [Projektplan](../planning/PROJECT_PLAN_2026_2027.md) · [Backlog](../planning/BACKLOG.md) · [Forschungsjournal](DAILY_LOG.md) · [Entscheidungen](../docs/decisions/README.md)
