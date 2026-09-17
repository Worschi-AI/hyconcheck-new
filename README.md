# HyConCheck

Technischer Neuaufbau des Forschungsvorhabens **HyConCheck** – hybride Konsistenzprüfung technischer Dokumentenbestände.

| Eckdaten | |
|---|---|
| Projektzeitraum | 01.09.2026 – 31.12.2027 |
| Planungsvolumen | 2.560 Planstunden (2026: 640 h, 2027: 1.920 h) |
| Arbeitspakete | AP1 – AP7 (siehe [Projektplan](planning/PROJECT_PLAN_2026_2027.md)) |
| Aktueller Stand | siehe [status/CURRENT_STATUS.md](status/CURRENT_STATUS.md) |
| Nächste fachliche Etappe | BL-001 – Rechercheprotokoll und Suchstrategie für den Stand der Technik |

## Arbeitsverständnis

HyConCheck untersucht, wie Inkonsistenzen in technischen Dokumentenbeständen – etwa Widersprüche zwischen Anforderungen, Spezifikationen, Schnittstellenbeschreibungen und Statusangaben – mit hybriden Verfahren erkannt, typisiert und nachvollziehbar belegt werden können. „Hybrid“ meint dabei die Kombination regel- und strukturbasierter Analyse mit Verfahren des Machine Learning (z. B. NLI, Embeddings, LLM-gestützte Extraktion) sowie deren Zusammenführung über einen Evidenzgraphen und eine Fusionsstufe.

Die präzise Fassung der Forschungslücke, der Hypothesen H1–H7, des Benchmarks, der Ground Truth, der Baselines, des Evidenzgraphen, der Fusion und der finalen Architektur ist **offen** und wird in diesem Repository von Grund auf neu erarbeitet. Details: [docs/RESEARCH_DESIGN.md](docs/RESEARCH_DESIGN.md).

## Taxonomie – fünf verbindliche Obertypen

1. Fakt und Wert
2. Zeit und Status
3. Modalität und Norm
4. Akteur und Verantwortung
5. Abhängigkeit und Schnittstelle

Die Operationalisierung aller Obertypen beginnt hier neu; kein Obertyp ist abgeschlossen. Siehe [docs/TAXONOMY_V1.md](docs/TAXONOMY_V1.md).

## Neuaufbau ohne Übernahme

Dieses Repository übernimmt **keine** Dateien, Commits, Erledigungsstände oder Forschungsergebnisse aus früheren Repositorys. Begründung und Konsequenzen: [ADR-0001](docs/decisions/ADR-0001-neuaufbau-ohne-uebernahme.md).

## Repository-Struktur

```
AGENTS.md                      Arbeitsregeln für alle Mitwirkenden und Werkzeuge
README.md                      Diese Übersicht
configs/                       Konfigurationen für Experimente und Pipelines
data/                          Datenbestände (Rohdaten, Annotationen, Ground Truth) – noch leer
docs/                          Fachliche Grundlagendokumente
  HYCONCHECK_MASTER_PROMPT.md  Verbindlicher Arbeitsauftrag für jede Arbeitssitzung
  PROJECT_CHARTER.md           Projektauftrag
  RESEARCH_DESIGN.md           Forschungsdesign (Lücke, H1–H7, Benchmark, Evaluation)
  TAXONOMY_V1.md               Taxonomie V1 (Obertypen, Operationalisierung)
  decisions/                   Architektur- und Projektentscheidungen (ADR)
experiments/                   Experimentdefinitionen und -protokolle – noch leer
planning/                      Projektplan und Backlog
references/                    Literatur- und Quellenverwaltung – noch leer
results/                       Auswertungen und Ergebnisse – noch leer
src/                           Quellcode – noch leer
status/                        Aktueller Stand und Tageslog
tests/                         Tests und Qualitätsprüfungen
```

## Qualitätsprüfungen

```bash
py tests/check_repo_conventions.py
```

Die Prüfung stellt sicher, dass die Pflichtdateien vorhanden sind, keine unzulässigen Werkzeug-/Anbieterhinweise enthalten sind, interne Links auflösbar sind und die Planstundensummen konsistent bleiben.

## Hinweis zu Planstunden

Alle Stundenangaben in diesem Repository sind **Planwerte**. Aus ihnen werden keine tatsächlich geleisteten Personenstunden abgeleitet. Ein Zeitnachweis (`HyConCheck_Zeitnachweis.xlsx`) liegt derzeit nicht vor; dies ist als offene Planungsgrundlage im [Projektplan](planning/PROJECT_PLAN_2026_2027.md) dokumentiert.
