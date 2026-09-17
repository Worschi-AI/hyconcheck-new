# HyConCheck – Master-Arbeitsauftrag

Dieses Dokument ist der verbindliche Rahmen für jede Arbeitssitzung im Repository. Es wird zu Beginn jeder Sitzung zusammen mit [AGENTS.md](../AGENTS.md), [status/CURRENT_STATUS.md](../status/CURRENT_STATUS.md) und [planning/BACKLOG.md](../planning/BACKLOG.md) gelesen.

## 1. Projektidentität

- **Vorhaben:** HyConCheck – hybride Konsistenzprüfung technischer Dokumentenbestände.
- **Charakter:** Forschungs- und Entwicklungsvorhaben mit dem Ziel eines nachvollziehbar evaluierten Verfahrens und einer prototypischen Architektur.
- **Projektzeitraum:** 01.09.2026 – 31.12.2027.
- **Repository:** vollständiger technischer Neuaufbau; keine Übernahme aus früheren Repositorys.

## 2. Verbindliche Rahmenbedingungen

1. Arbeit ausschließlich im aktuellen lokalen Repository, auf dem angewiesenen Branch.
2. Keine Branches, Pull Requests oder Pushes ohne ausdrückliche Anweisung.
3. Lokale Git-Identität verwenden; keine Commit-Trailer, keine Werkzeug-/Anbieterattribution.
4. Keine operativen Hinweise auf Entwicklungsassistenten oder deren Anbieter in Repository-Dateien. Fachbegriffe (KI, Machine Learning, LLM, NLI, Embeddings) sind zulässig.
5. Stundenangaben sind Planwerte. Keine fiktiven Ist-Stunden, keine fiktiven Stundenzettel.
6. Keine erfundenen Quellen, Zitate, Messwerte oder Ergebnisse. Unbekanntes wird als offen markiert.
7. Kein Taxonomie-Obertyp, kein Arbeitspaket und kein Backlog-Eintrag wird ohne geprüftes Artefakt als abgeschlossen geführt.

## 3. Fachlicher Rahmen

### 3.1 Taxonomie – fünf verbindliche Obertypen

1. Fakt und Wert
2. Zeit und Status
3. Modalität und Norm
4. Akteur und Verantwortung
5. Abhängigkeit und Schnittstelle

Die Obertypen sind gesetzt; ihre Operationalisierung (Definitionen, Abgrenzungen, Untertypen, Annotationsregeln, Beispiele) beginnt neu und ist in [TAXONOMY_V1.md](TAXONOMY_V1.md) zu entwickeln.

### 3.2 Arbeitspakete und Planstunden

| AP | Bezeichnung | Planstunden |
|---|---|---:|
| AP1 | Stand der Technik und Forschungsdesign | 200 |
| AP2 | Taxonomie und Annotationsrichtlinie | 300 |
| AP3 | Benchmark und Ground Truth | 400 |
| AP4 | Baselines und Einzelverfahren | 420 |
| AP5 | Evidenzgraph und Fusion | 460 |
| AP6 | Integrierte Architektur und Evaluation | 520 |
| AP7 | Dissemination, Dokumentation und Abschluss | 260 |
| **Summe** | | **2.560** |

Jahresscheiben: 2026 = 640 Planstunden, 2027 = 1.920 Planstunden. Details in [planning/PROJECT_PLAN_2026_2027.md](../planning/PROJECT_PLAN_2026_2027.md).

### 3.3 Offene Kernfragen

Zum jetzigen Stand sind **offen** und werden im Projektverlauf erarbeitet:

- Forschungslücke (präzise Fassung)
- Hypothesen H1–H7
- Taxonomie (Operationalisierung aller fünf Obertypen)
- Benchmark
- Ground Truth
- Baselines
- Evidenzgraph
- Fusion
- Finale Architektur

Siehe [RESEARCH_DESIGN.md](RESEARCH_DESIGN.md).

## 4. Arbeitsweise je Sitzung

1. Stand lesen: `status/CURRENT_STATUS.md`, `status/DAILY_LOG.md`, `planning/BACKLOG.md`.
2. Genau die angewiesene Etappe bearbeiten; Scope nicht eigenmächtig erweitern oder verengen.
3. Ergebnisse als Artefakte im Repository ablegen (Dokument, Code, Konfiguration, Protokoll).
4. Entscheidungen als ADR in `docs/decisions/` dokumentieren.
5. Qualitätsprüfungen ausführen (`py tests/check_repo_conventions.py`, `git diff --check`, ggf. weitere).
6. Status und Backlog aktualisieren, Tageslog ergänzen.
7. Lokal committen (nur wenn angewiesen), nicht pushen.
8. Nach dem Berichtsformat in [AGENTS.md](../AGENTS.md) berichten.

## 5. Nächste fachliche Etappe

**BL-001 – Definition des Rechercheprotokolls und der Suchstrategie für den Stand der Technik (AP1).**

Erwartete Artefakte: Rechercheprotokoll (Fragestellungen, Suchbegriffe, Datenbanken, Ein-/Ausschlusskriterien, Screening-Verfahren, Dokumentationsform) in `docs/` sowie eine Ablagestruktur für Quellen in `references/`.

## 6. Was in dieser Phase nicht geschieht

- Keine Experimente, keine Modellläufe, keine Datenerhebung vor Vorliegen des Rechercheprotokolls und eines Experimentprotokolls.
- Keine Festlegung der finalen Architektur.
- Keine Übernahme früherer Ergebnisse als „bereits erledigt“.
