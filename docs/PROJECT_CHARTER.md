# HyConCheck – Projektauftrag (Project Charter)

| | |
|---|---|
| Vorhaben | HyConCheck – hybride Konsistenzprüfung technischer Dokumentenbestände |
| Projektzeitraum | 01.09.2026 – 31.12.2027 (16 Monate) |
| Planungsvolumen | 2.560 Planstunden (2026: 640 h, 2027: 1.920 h) |
| Stand dieses Dokuments | 17.09.2026 – Erstfassung zur Projekteinrichtung |

## 1. Ausgangslage

Technische Dokumentenbestände (Anforderungen, Spezifikationen, Schnittstellenbeschreibungen, Normenverweise, Statusberichte) entstehen verteilt, über lange Zeiträume und in unterschiedlichen Formaten. Dabei entstehen Inkonsistenzen: widersprüchliche Werte, veraltete Statusangaben, unvereinbare Verbindlichkeitsgrade, unklare Zuständigkeiten oder unverträgliche Schnittstellenannahmen. Solche Inkonsistenzen werden heute überwiegend manuell und spät gefunden.

HyConCheck geht von der Arbeitshypothese aus, dass ein **hybrides Verfahren** – regel- und strukturbasierte Analyse kombiniert mit ML-Verfahren (u. a. NLI, Embeddings, LLM-gestützte Extraktion) und einer Fusion der Einzelbefunde über einen Evidenzgraphen – Inkonsistenzen zuverlässiger, typisierter und besser belegbar erkennt als Einzelverfahren.

Die präzise Fassung der Forschungslücke ist **offen** und Gegenstand von AP1 (siehe [RESEARCH_DESIGN.md](RESEARCH_DESIGN.md)).

## 2. Ziele

### 2.1 Projektziele

1. Eine operationalisierte Taxonomie von Inkonsistenztypen entlang der fünf verbindlichen Obertypen (siehe Abschnitt 4).
2. Ein Benchmark mit Ground Truth, der die Taxonomie abdeckt und eine reproduzierbare Evaluation erlaubt.
3. Nachvollziehbare Baselines je Verfahrensfamilie.
4. Ein Evidenzgraph als gemeinsames Repräsentationsmodell für Befunde und Belege.
5. Eine Fusionsstufe, die Einzelbefunde zu bewerteten, belegten Inkonsistenzmeldungen zusammenführt.
6. Eine integrierte, evaluierte Prototyp-Architektur.
7. Dokumentation, Reproduzierbarkeit und Dissemination der Ergebnisse.

### 2.2 Nicht-Ziele

- Kein Produktivsystem und keine Produktentwicklung.
- Keine Übernahme oder Weiterführung früherer Repositorys, Ergebnisse oder Erledigungsstände.
- Keine Bewertung von Personen oder Organisationen anhand der gefundenen Inkonsistenzen.

## 3. Ergebnisse (Deliverables)

| Nr. | Ergebnis | AP | Status |
|---|---|---|---|
| D1 | Rechercheprotokoll, Stand der Technik, präzisierte Forschungslücke, H1–H7 | AP1 | offen |
| D2 | Taxonomie V1 (operationalisiert) und Annotationsrichtlinie | AP2 | offen |
| D3 | Benchmark-Korpus und Ground Truth mit Qualitätskennzahlen | AP3 | offen |
| D4 | Baselines (Implementierung, Konfiguration, Ergebnisse) | AP4 | offen |
| D5 | Evidenzgraph-Modell und Fusionsverfahren | AP5 | offen |
| D6 | Integrierte Architektur, Gesamtevaluation, Hypothesenprüfung | AP6 | offen |
| D7 | Abschlussdokumentation, Reproduzierbarkeitspaket, Publikationen | AP7 | offen |

## 4. Verbindlicher fachlicher Rahmen

### 4.1 Taxonomie-Obertypen

1. Fakt und Wert
2. Zeit und Status
3. Modalität und Norm
4. Akteur und Verantwortung
5. Abhängigkeit und Schnittstelle

Die Obertypen sind vorgegeben. Ihre Operationalisierung beginnt in diesem Repository neu; kein Obertyp ist abgeschlossen ([TAXONOMY_V1.md](TAXONOMY_V1.md)).

### 4.2 Offene Kernfragen

Forschungslücke, H1–H7, Taxonomie-Operationalisierung, Benchmark, Ground Truth, Baselines, Evidenzgraph, Fusion und finale Architektur sind offen und werden schrittweise über die Arbeitspakete erarbeitet.

## 5. Arbeitspakete und Planstunden

| AP | Bezeichnung | Planstunden | Anteil |
|---|---|---:|---:|
| AP1 | Stand der Technik und Forschungsdesign | 200 | 7,8 % |
| AP2 | Taxonomie und Annotationsrichtlinie | 300 | 11,7 % |
| AP3 | Benchmark und Ground Truth | 400 | 15,6 % |
| AP4 | Baselines und Einzelverfahren | 420 | 16,4 % |
| AP5 | Evidenzgraph und Fusion | 460 | 18,0 % |
| AP6 | Integrierte Architektur und Evaluation | 520 | 20,3 % |
| AP7 | Dissemination, Dokumentation und Abschluss | 260 | 10,2 % |
| **Summe** | | **2.560** | 100 % |

Jahresscheiben: 2026 = 640 h, 2027 = 1.920 h. Zeitliche Einordnung und Meilensteine: [planning/PROJECT_PLAN_2026_2027.md](../planning/PROJECT_PLAN_2026_2027.md).

**Hinweis:** Alle Stundenangaben sind Planwerte. Sie begründen keine Aussage über tatsächlich geleistete Personenstunden. Ein Zeitnachweis liegt derzeit nicht vor (offene Planungsgrundlage).

## 6. Rahmenbedingungen und Regeln

- Vollständiger technischer Neuaufbau ([ADR-0001](decisions/ADR-0001-neuaufbau-ohne-uebernahme.md)).
- Arbeitsregeln, Git-Regeln und Qualitätsprüfungen: [AGENTS.md](../AGENTS.md).
- Verbindlicher Arbeitsauftrag je Sitzung: [HYCONCHECK_MASTER_PROMPT.md](HYCONCHECK_MASTER_PROMPT.md).
- Statusführung: [status/CURRENT_STATUS.md](../status/CURRENT_STATUS.md), [status/DAILY_LOG.md](../status/DAILY_LOG.md), [planning/BACKLOG.md](../planning/BACKLOG.md).

## 7. Risiken (Erstfassung)

| Risiko | Auswirkung | Gegenmaßnahme |
|---|---|---|
| Forschungslücke bleibt zu unscharf | Hypothesen nicht prüfbar | AP1 mit Rechercheprotokoll und expliziter Lückenformulierung abschließen, bevor AP3 beginnt |
| Taxonomie nicht trennscharf | geringe Annotator-Übereinstimmung, unbrauchbare Ground Truth | Annotationsrichtlinie mit Abgrenzungsregeln und Pilotannotation in AP2 |
| Keine geeigneten, lizenzkonformen Dokumentbestände | Benchmark nicht erstellbar | Datenherkunft und Lizenz früh klären (AP1/AP3), Alternativen dokumentieren |
| Planstunden werden als Ist-Stunden missverstanden | falsche Berichterstattung | klare Kennzeichnung als Planwerte; Ist-Stunden nur aus Zeitnachweis |
| Aufwand für Ground Truth unterschätzt | Verzögerung AP4–AP6 | AP3 mit größtem Einzelbudget vor AP4; Umfang stufenweise festlegen |

## 8. Kommunikation und Berichte

- Tageslog je Arbeitstag, Statusdokument bei jeder inhaltlichen Änderung.
- Entscheidungen als ADR.
- Berichtsformat nach [AGENTS.md](../AGENTS.md), Abschnitt 9.
