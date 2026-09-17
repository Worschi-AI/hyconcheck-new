# HyConCheck – Backlog

Stand: 17.09.2026.

Statuswerte: `offen`, `in Arbeit`, `blockiert`, `abgeschlossen`. Ein Eintrag wird nur mit vorliegendem, geprüftem Artefakt auf `abgeschlossen` gesetzt. Reihenfolge innerhalb eines AP entspricht der geplanten Bearbeitungsreihenfolge; Aufwandsangaben sind bewusst nicht enthalten (Planstunden nur auf AP-Ebene, siehe [PROJECT_PLAN_2026_2027.md](PROJECT_PLAN_2026_2027.md)).

## Nächste Etappe

**BL-001 – Definition des Rechercheprotokolls und der Suchstrategie für den Stand der Technik.**

## Einrichtung

| ID | Titel | AP | Status | Artefakt |
|---|---|---|---|---|
| BL-000 | Projektgrundlage im Repository einrichten (Dokumente, Struktur, Prüfungen) | – | abgeschlossen | Dieses Repository, Stand 17.09.2026 |

## AP1 – Stand der Technik und Forschungsdesign

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-001 | Rechercheprotokoll und Suchstrategie für den Stand der Technik definieren (Fragestellungen, Suchbegriffe, Quellen/Datenbanken, Ein-/Ausschlusskriterien, Screening, Dokumentationsform) | offen | `docs/RESEARCH_PROTOCOL.md`, Ablagestruktur in `references/` |
| BL-002 | Recherche gemäß Protokoll durchführen und Quellen erfassen | offen | `references/` (Quellenliste, Screening-Protokoll) |
| BL-003 | Stand der Technik strukturiert auswerten (Verfahren, Benchmarks, Taxonomien, Evidenzrepräsentation) | offen | `docs/STATE_OF_THE_ART.md` |
| BL-004 | Forschungslücke formulieren und begründen | offen | Abschnitt in `docs/RESEARCH_DESIGN.md`, ADR |
| BL-005 | Hypothesen H1–H7 mit Metriken und Entscheidungskriterien formulieren | offen | Abschnitt in `docs/RESEARCH_DESIGN.md`, ADR |

## AP2 – Taxonomie und Annotationsrichtlinie

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-010 | Definitionen und Abgrenzungen der fünf Obertypen ausarbeiten | offen | `docs/TAXONOMY_V1.md` |
| BL-011 | Untertypen je Obertyp definieren | offen | `docs/TAXONOMY_V1.md` |
| BL-012 | Annotationsrichtlinie mit Entscheidungsregeln und Beispielen erstellen | offen | `docs/ANNOTATION_GUIDELINE.md` |
| BL-013 | Pilotannotation durchführen und Übereinstimmung auswerten | offen | `experiments/`, `results/` |
| BL-014 | Querschnittsfragen der Taxonomie entscheiden (Mehrfachzuordnung, Schweregrad, Bezugseinheit, Sprache) | offen | ADR |

## AP3 – Benchmark und Ground Truth

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-020 | Datenquellen identifizieren, Lizenz und Eignung prüfen | offen | `data/README.md`, ADR |
| BL-021 | Aufbereitungspipeline und Datenschema festlegen | offen | `src/`, `configs/`, `data/` |
| BL-022 | Annotation, Adjudikation und Qualitätskennzahlen | offen | `data/`, `results/` |
| BL-023 | Benchmark versionieren und Aufteilung festlegen | offen | `data/`, ADR |

## AP4 – Baselines und Einzelverfahren

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-030 | Einheitliche Verfahrensschnittstelle und Auswertungsrahmen definieren | offen | `src/`, `tests/` |
| BL-031 | Regelbasierte Baseline | offen | `src/`, `configs/`, `results/` |
| BL-032 | Embedding-basierte Baseline | offen | `src/`, `configs/`, `results/` |
| BL-033 | NLI-basierte Baseline | offen | `src/`, `configs/`, `results/` |
| BL-034 | LLM-basierte Baseline | offen | `src/`, `configs/`, `results/` |
| BL-035 | Auswertung der Baselines je Obertyp | offen | `results/` |

## AP5 – Evidenzgraph und Fusion

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-040 | Schema des Evidenzgraphen festlegen | offen | `docs/`, ADR |
| BL-041 | Evidenzgraph implementieren und aus Baseline-Befunden befüllen | offen | `src/` |
| BL-042 | Fusionsverfahren entwerfen und implementieren | offen | `src/`, ADR |
| BL-043 | Fusion gegen Baselines evaluieren | offen | `experiments/`, `results/` |

## AP6 – Integrierte Architektur und Evaluation

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-050 | Architektur integrieren | offen | `src/`, ADR |
| BL-051 | Gesamtevaluation und Fehleranalyse | offen | `experiments/`, `results/` |
| BL-052 | Hypothesen H1–H7 prüfen | offen | `results/`, `docs/RESEARCH_DESIGN.md` |
| BL-053 | Finale Architektur dokumentieren | offen | `docs/`, ADR |

## AP7 – Dissemination, Dokumentation und Abschluss

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-060 | Reproduzierbarkeitspaket erstellen | offen | Repository |
| BL-061 | Abschlussdokumentation | offen | `docs/` |
| BL-062 | Publikationen/Vorträge vorbereiten | offen | `docs/` |
| BL-063 | Projektabschluss | offen | `status/` |

## Offene Planungsgrundlagen

| ID | Thema | Status |
|---|---|---|
| OP-001 | `HyConCheck_Zeitnachweis.xlsx` liegt nicht vor; Ablage und Auswertung eines Zeitnachweises sind ungeklärt | offen |
