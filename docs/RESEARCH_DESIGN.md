# HyConCheck – Forschungsdesign

Stand: 17.09.2026 – Rahmenfassung zur Projekteinrichtung. Dieses Dokument legt fest, **welche** Bausteine das Forschungsdesign hat und **wie** sie erarbeitet werden. Die Inhalte selbst sind – mit Ausnahme der vorgegebenen Taxonomie-Obertypen und Arbeitspakete – offen und werden im Projektverlauf gefüllt.

## 1. Gegenstand

Hybride Erkennung, Typisierung und Belegung von Inkonsistenzen in technischen Dokumentenbeständen. „Hybrid“ bezeichnet die Kombination von

- regel- und strukturbasierten Verfahren (z. B. Extraktion von Werten, Zeitangaben, Modalverben, Akteuren, Verweisen; Abgleich über Regeln und Constraints),
- ML-Verfahren (z. B. NLI zur Widerspruchserkennung zwischen Aussagepaaren, Embeddings zur Kandidatenfindung, LLM-gestützte Extraktion und Normalisierung),
- einer gemeinsamen Repräsentation der Befunde und Belege (Evidenzgraph) und
- einer Fusionsstufe, die Einzelbefunde zu bewerteten Inkonsistenzmeldungen zusammenführt.

## 2. Forschungslücke

**Status: offen.**

Die Forschungslücke wird in AP1 auf Basis eines dokumentierten Rechercheprotokolls (BL-001) und einer systematischen Erhebung des Stands der Technik formuliert. Sie wird erst dann als festgelegt geführt, wenn

1. das Rechercheprotokoll vorliegt und ausgeführt wurde,
2. die relevanten Arbeiten in `references/` erfasst und bewertet sind und
3. die Lücke in einem eigenen Abschnitt dieses Dokuments mit Bezug auf die erfassten Arbeiten begründet ist.

Leitfragen für die Formulierung:

- Welche Inkonsistenztypen werden von bestehenden Verfahren adressiert, welche nicht?
- Welche Verfahren kombinieren symbolische und ML-basierte Analyse, und wie werden Befunde zusammengeführt?
- Welche Benchmarks existieren, welche Taxonomie liegt ihnen zugrunde, und wie belastbar ist deren Ground Truth?
- Wie werden Belege (Evidenz) für gemeldete Inkonsistenzen repräsentiert und bewertet?

## 3. Hypothesen H1–H7

**Status: offen.** Die Hypothesen werden nach Formulierung der Forschungslücke in AP1 aufgestellt und in AP6 geprüft. Jede Hypothese muss

- eine prüfbare Aussage enthalten,
- einem oder mehreren Bausteinen (Taxonomie, Benchmark, Baselines, Evidenzgraph, Fusion, Architektur) zugeordnet sein,
- Metriken und ein Entscheidungskriterium (Annahme/Ablehnung) benennen und
- einem Experiment bzw. einer Auswertung in `experiments/` und `results/` zugeordnet werden.

| Hypothese | Aussage | Baustein | Metrik/Kriterium | Status |
|---|---|---|---|---|
| H1 | offen | offen | offen | offen |
| H2 | offen | offen | offen | offen |
| H3 | offen | offen | offen | offen |
| H4 | offen | offen | offen | offen |
| H5 | offen | offen | offen | offen |
| H6 | offen | offen | offen | offen |
| H7 | offen | offen | offen | offen |

## 4. Taxonomie

**Status: Obertypen gesetzt, Operationalisierung offen.**

Die fünf Obertypen sind verbindlich: Fakt und Wert; Zeit und Status; Modalität und Norm; Akteur und Verantwortung; Abhängigkeit und Schnittstelle. Definitionen, Abgrenzungen, Untertypen, Annotationsregeln und Beispiele werden in [TAXONOMY_V1.md](TAXONOMY_V1.md) erarbeitet (AP2). Kein Obertyp ist abgeschlossen.

## 5. Benchmark und Ground Truth

**Status: offen.** Zu klären in AP3 (Vorarbeiten in AP1/AP2):

- Dokumentquellen: Herkunft, Lizenz, Domäne(n), Sprache(n), Formate.
- Einheiten: Dokumentpaare, Aussagepaare, Dokumentbestände; Positiv- und Negativbeispiele je Obertyp.
- Annotationsprozess: Richtlinie, Annotatoren, Übereinstimmungsmaße, Adjudikation.
- Aufteilung: Entwicklungs-/Testdaten, Vermeidung von Leckagen.
- Qualitätskennzahlen und Versionierung des Benchmarks.

## 6. Baselines

**Status: offen.** Zu klären in AP4: Auswahl je Verfahrensfamilie (regelbasiert, Embedding-basiert, NLI-basiert, LLM-basiert), einheitliche Ein-/Ausgabeschnittstelle, Konfigurationen in `configs/`, Ergebnisse in `results/`.

## 7. Evidenzgraph

**Status: offen.** Zu klären in AP5: Knoten- und Kantentypen (Aussagen, Entitäten, Werte, Zeitangaben, Akteure, Verweise, Befunde, Belege), Herkunftsinformation, Konfidenzen, Serialisierung, Anfragen.

## 8. Fusion

**Status: offen.** Zu klären in AP5: Zusammenführung von Einzelbefunden (Gewichtung, Kalibrierung, Konfliktauflösung, Erklärbarkeit), Bewertung gegen Baselines.

## 9. Finale Architektur

**Status: offen.** Wird in AP6 aus den evaluierten Bausteinen abgeleitet und als ADR-Reihe in `docs/decisions/` begründet. Keine Vorfestlegung in der Grundlagenphase.

## 10. Evaluation

- Jede Hypothese erhält mindestens ein Experimentprotokoll in `experiments/` (Ziel, Hypothesenbezug, Daten, Konfiguration, Metriken, Abbruchkriterien).
- Ergebnisse werden mit Konfiguration, Datenversion und Code-Versionsstand in `results/` abgelegt.
- Metriken werden je Obertyp und gesamt berichtet; Fehleranalysen sind Teil der Auswertung.
- In der Grundlagenphase werden **keine Experimente** durchgeführt.

## 11. Bezug zu den Arbeitspaketen

| Baustein | AP |
|---|---|
| Rechercheprotokoll, Stand der Technik, Forschungslücke, H1–H7 | AP1 |
| Taxonomie-Operationalisierung, Annotationsrichtlinie | AP2 |
| Benchmark, Ground Truth | AP3 |
| Baselines | AP4 |
| Evidenzgraph, Fusion | AP5 |
| Integrierte Architektur, Gesamtevaluation, Hypothesenprüfung | AP6 |
| Dokumentation, Reproduzierbarkeit, Dissemination | AP7 |
