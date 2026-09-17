# HyConCheck – Backlog

Stand: 17.09.2026 – gegliedert nach den Arbeitspaketen des Forschungsantrags (Master-Prompt §25) und den fachlichen Abhängigkeiten im [Projektplan](PROJECT_PLAN_2026_2027.md).

Statuswerte: `offen`, `in Arbeit`, `blockiert`, `abgeschlossen`. Ein Eintrag wird nur mit vorliegendem, geprüftem Artefakt auf `abgeschlossen` gesetzt. Es werden keine Aufwände je Eintrag geführt (Planstunden nur auf AP-Ebene, Planwerte).

## Nächste fachliche Etappe

**BL-002 – Recherche gemäß Rechercheprotokoll durchführen (AP1).** BL-001 (Protokoll) ist abgeschlossen; AP1 bleibt offen.

## Einrichtung (Repository)

| ID | Titel | Status | Artefakt |
|---|---|---|---|
| BL-000 | Projektgrundlage im Repository einrichten (Dokumente, Struktur, Prüfungen) | abgeschlossen | Repository-Stand 17.09.2026, Commit „Projektgrundlage für HyConCheck einrichten“ |
| BL-000a | Vollständigen Master-Prompt übernehmen und Projektgrundlage daran angleichen | abgeschlossen | `docs/HYCONCHECK_MASTER_PROMPT.md` (byte-identisch zur Quelle), ADR-0002, Commit „Projektgrundlage an vollständigen Forschungsauftrag angleichen“ |

## AP1 – Technischen Lösungsraum analysieren; Widerspruchstaxonomie und formale Kriterien entwickeln

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-001 | Rechercheprotokoll und Suchstrategie für den Stand der Technik definieren: Fragestellungen, Recherchethemen nach §34, Suchbegriffe, Quellen/Datenbanken, Quellenpriorität (§34), Ein-/Ausschlusskriterien, Screening-Verfahren, Provenienz- und Dokumentationsform | abgeschlossen (17.09.2026) | `references/RESEARCH_PROTOCOL.md` (V1.0); Vorlagen `references/LITERATURE_SEARCH_LOG.md`, `references/SOURCES.md`, `references/LITERATURE_MATRIX.csv` (leer). Abgeschlossen ist nur die Protokolldefinition – keine Recherche durchgeführt, kein Stand der Technik bewertet, keine Lücke bestätigt, AP1 offen. |
| BL-002 | Recherche gemäß `references/RESEARCH_PROTOCOL.md` durchführen: Suchläufe in den definierten Systemen (Abschnitte 5, 6, 19), Screening (Abschnitt 10), Snowballing (Abschnitt 18) bis Stopkriterium (Abschnitt 17); Quellen mit vollständiger Provenienz erfassen (keine ungeprüften Quellen) | offen – nächste fachliche Etappe | `references/LITERATURE_SEARCH_LOG.md`, `references/SOURCES.md`, `references/LITERATURE_MATRIX.csv` |
| BL-003 | Technischen Lösungsraum und Stand der Technik strukturiert auswerten (Verfahren, Benchmarks, Taxonomien, Evidenzrepräsentation, Fusion, Kalibrierung) | offen | `docs/STATE_OF_THE_ART.md` |
| BL-004 | Wissenslücke (§4) durch Literaturrecherche überprüfen: `gestützt` / `präzisiert` / `widerlegt` mit Belegen über Source-IDs (Protokoll Abschnitt 16); Ergebnis begründen | offen | Abschnitt in `docs/RESEARCH_DESIGN.md`, ADR |
| BL-005 | Forschungsfragen F1–F6 und Hypothesen H1–H7 operationalisieren: Metriken, Entscheidungskriterien, geplante Experimente je Hypothese (kein Umformulieren, keine Vorwegnahme von Ergebnissen) | offen | `docs/RESEARCH_DESIGN.md`, `experiments/REGISTER.md` |
| BL-010 | Obertypen operationalisieren: Definition, Entscheidungstest, Ein-/Ausschlusskriterien, Grenzfälle, Abgrenzung je Obertyp (§9) | offen | `docs/TAXONOMY_V1.md` |
| BL-011 | Synthetische Positiv-, Negativ- und unklare Beispiele je Obertyp erstellen (als synthetisch gekennzeichnet) | offen | `docs/TAXONOMY_V1.md` |
| BL-012 | Sekundärtags für Fortschreibung, fehlenden Kontext, Versionswechsel, Mehrdeutigkeit festlegen; Entscheidungslabels Widerspruch / kein Widerspruch / unklar verankern | offen | `docs/TAXONOMY_V1.md`, ADR |
| BL-013 | Formale Kriterien für semantische, temporale und Statuskonflikte festlegen (Unterscheidungsklassen nach §5B) | offen | `docs/FORMAL_CRITERIA.md` |
| BL-014 | Annotationsleitfaden V1 erstellen (§12: Annotationsregeln, Umgang mit schwierigen/unklaren Fällen, Taxonomie-Version) | offen | `docs/ANNOTATION_GUIDELINE.md` |
| BL-015 | Qualitäts-Gate AP1→AP2 dokumentieren (§35) | offen | `status/CURRENT_STATUS.md` |

## AP2 – Benchmarkmethodik und Testdatengenerator; Grenzfälle erzeugen; Ground Truth definieren

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-020 | Benchmarkmethodik und Datenschema festlegen (Pflichtfelder je Fall nach §10; Fallarten nach §10) | offen | `data/SCHEMA.md`, ADR |
| BL-021 | Testdatengenerator entwickeln (synthetische Fälle, eindeutig als synthetisch gekennzeichnet) | offen | `src/`, `configs/`, `tests/` |
| BL-022 | Positive, negative und schwierige Grenzfälle erzeugen: Versionsfortschreibungen, Statusänderungen, temporale Grenzfälle, Entitätsmehrdeutigkeiten, dokumentübergreifende Konflikte, unklare Fälle | offen | `data/` |
| BL-023 | Zulässigkeit, Anonymisierung und getrennte Dokumentation anonymisierter realer Beispiele prüfen (nur falls verwendet) | offen | `data/README.md`, ADR |
| BL-024 | Ground Truth annotieren und dokumentieren (§12); zeitlich getrennte Blind-Reannotation für festgelegten Anteil | offen | `data/`, `results/` |
| BL-025 | Gruppierten Train/Validation/Test-Split 60/20/20 nach Szenario-ID erstellen; Testsplit einfrieren; Schutzregeln (§11) technisch verankern | offen | `data/splits/`, `tests/`, ADR |
| BL-026 | Benchmark und Ground Truth versionieren (M2) | offen | `data/`, ADR |
| BL-027 | Qualitäts-Gate AP2→AP3 dokumentieren (§35) | offen | `status/CURRENT_STATUS.md` |

## AP3 – Baselines implementieren; Evaluationspipeline entwickeln; Verfahren experimentell vergleichen

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-030 | Evaluationspipeline und Experimentframework implementieren (EXP-YYYY-NNNN, Pflichtfelder §18, Metriken §16, Aufschlüsselungen) | offen | `src/`, `experiments/`, `tests/` |
| BL-031 | B0 – einfache String-/Keyword-/regelbasierte Referenz | offen | `src/`, `configs/`, `results/` |
| BL-032 | B1 – regelbasiertes Konsistenzverfahren | offen | `src/`, `configs/`, `results/` |
| BL-033 | B2 – Embedding-basierte Kandidatensuche beziehungsweise Klassifikation | offen | `src/`, `configs/`, `results/` |
| BL-034 | B3 – Natural-Language-Inference-Verfahren | offen | `src/`, `configs/`, `results/` |
| BL-035 | B4 – direkte LLM-basierte Klassifikation, sofern ohne zusätzliche unverhältnismäßige Kosten technisch verfügbar (§13, §33) | offen | `src/`, `configs/`, `results/` |
| BL-036 | Baselines auf Entwicklungs-/Validationsdaten reproduzierbar vergleichen (M3); Fehleranalyse nach §20 | offen | `experiments/`, `results/` |
| BL-037 | Qualitäts-Gate AP3→AP4/AP5 dokumentieren (§35) | offen | `status/CURRENT_STATUS.md` |

## AP4 – Entitätsauflösung; Extraktion und Normalisierung von Attributen, Zeitintervallen, Statuszuständen, Provenienz

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-040 | Aussagen- und Entitätsextraktion sowie Entity Resolution entwickeln und testen (Risiko §17: falsches vs. zu striktes Matching) | offen | `src/`, `tests/`, `experiments/` |
| BL-041 | Attributextraktion entwickeln und testen | offen | `src/`, `tests/` |
| BL-042 | Zeitnormalisierung (Zeitpunkte, Zeitintervalle, relative Angaben, Gültigkeit) entwickeln und testen (Risiko §17) | offen | `src/`, `tests/`, `experiments/` |
| BL-043 | Statusextraktion und Statusübergangsmodell entwickeln und testen | offen | `src/`, `tests/`, `experiments/` |
| BL-044 | Provenienzerfassung (Dokument, Version, Fundstelle) entwickeln und testen | offen | `src/`, `tests/` |
| BL-045 | Komponenten experimentell untersuchen (M4); Fehlerfortpflanzung erste Messung (H7-Bezug) | offen | `experiments/`, `results/` |

## AP5 – Evidenzgraph und Fusionsalgorithmen; Architekturen experimentell vergleichen

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-050 | Evidenzgraph-Schema festlegen (§5A: Aussagen, Entitäten, Attribute, Werte, Zeitpunkte/-intervalle, Statuszustände, Dokumentversionen, Provenienz, Dokumente/Fundstellen) | offen | `docs/`, ADR |
| BL-051 | Evidenzgraph implementieren und aus AP4-Ausgaben befüllen | offen | `src/`, `tests/` |
| BL-052 | Kandidaten-Retrieval und graphbasierte Evidenz (Graphpfade) implementieren | offen | `src/` |
| BL-053 | Temporale/statusbezogene Konsistenzprüfung implementieren (§5B Unterscheidungsklassen) | offen | `src/` |
| BL-054 | Alternative Fusionsverfahren implementieren (§5C) und Architekturvarianten nach §14 (Stufen D–F) experimentell vergleichen; nachvollziehbare Ausgabe nach §5D | offen | `src/`, `experiments/`, `results/` |
| BL-055 | Architekturvergleich gegen Baselines (M5); Entscheidung dokumentieren | offen | `results/`, ADR |

## AP6 – Fusionsverfahren kalibrieren und optimieren; Ablations-, Fehler- und Robustheitsanalysen; alternative Ansätze

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-060 | Kalibrierung der Evidenzfusion (Kalibrierungsmetriken §16; F6/H6) | offen | `experiments/`, `results/` |
| BL-061 | Ablationsstudien nach §21 | offen | `experiments/`, `results/` |
| BL-062 | Fehleranalysen nach §20 mit Gegenmaßnahmen-Zyklus | offen | `experiments/`, `results/` |
| BL-063 | Robustheitstests nach §22 | offen | `experiments/`, `results/` |
| BL-064 | Alternative Ansätze experimentell testen; Auswahl der zu validierenden Architektur (Stufe G) dokumentieren | offen | ADR |
| BL-065 | Qualitäts-Gate AP6→AP7 dokumentieren (§35), inkl. Leakage-Prüfung | offen | `status/CURRENT_STATUS.md` |

## AP7 – Ausgewählte Architektur auf zurückgehaltenen Testdaten validieren; Baselinevergleich; Fehlermuster

| ID | Titel | Status | Artefakt (geplant) |
|---|---|---|---|
| BL-070 | Hauptevaluation vorregistrieren (Architektur/Varianten, Metriken, Kriterien) vor Zugriff auf das Testset | offen | `experiments/`, ADR |
| BL-071 | Finale Evaluation auf dem eingefrorenen Testset (M7); Vergleich mit Baselines B0–B4 | offen | `results/` |
| BL-072 | Fehleranalyse des Testsets nach der Hauptevaluation; verbleibende technische Fehlermuster | offen | `results/` |
| BL-073 | Forschungsfragen beantworten, Hypothesen bewerten, Limitationen dokumentieren, Abschlussfrage (§38) beantworten | offen | `docs/RESEARCH_DESIGN.md`, `docs/FINAL_REPORT.md` |
| BL-074 | Abschlussbericht und Reproduzierbarkeitsprüfung nach Definition of Done (§37) | offen | `docs/FINAL_REPORT.md`, Repository |

## Planung und Fortschrittskontrolle

| ID | Titel | Status | Artefakt |
|---|---|---|---|
| BL-090 | Forecast-Quelle kontrolliert prüfen und integrieren (§39.7): Tabellenblätter Tagesplanung und Subaktivitäten prüfen, Quelldatei unverändert aufbewahren, Angaben ausschließlich als Forecast integrieren, maschinenlesbare Planungsübersicht erstellen; danach Prüfskript anpassen | abgeschlossen (17.09.2026) | `planning/forecast/README.md`, `forecast_daily.csv`, `forecast_subactivities.csv`, `forecast_summary.csv`, `build_forecast_csv.py`; Projektplan Abschnitt 2a; Prüfskript erweitert. Abgeschlossen ist ausschließlich die Repository-Etappe „Forecast integrieren“ – kein FuE-Arbeitspaket und keine geplante Forecast-Tätigkeit gilt damit als abgeschlossen. |
| BL-091 | Wöchentlicher Soll-Ist-Abgleich der geplanten Artefakte und Arbeitspakettermine gegen den Forecast (wiederkehrend, §39.10; „Ist“ = vorliegende Artefakte, keine Stunden) | offen – erster Abgleich ausstehend | Projektplan Abschnitt 6/7, `status/CURRENT_STATUS.md` |
| BL-092 | Monatliche Aktualisierung der Abschlussprognose (wiederkehrend, §39.10) | offen | Projektplan, `status/CURRENT_STATUS.md` |
