# HyConCheck – Forschungsdesign

Stand: 17.09.2026 – angeglichen an den vollständigen Forschungsauftrag [HYCONCHECK_MASTER_PROMPT.md](HYCONCHECK_MASTER_PROMPT.md). Der Wortlaut der Forschungsfragen, Hypothesen, Baselines, Regeln und Metriken folgt dem Master-Prompt; Paragraphenangaben (§) verweisen auf dessen Abschnitte. Alle Bausteine sind zum jetzigen Stand **offen**: es liegen keine Rechercheergebnisse, Daten, Implementierungen oder Experimente in diesem Repository vor.

## 1. Forschungsziel und Kernumfang (§3)

Ziel ist die Entwicklung und experimentelle Validierung eines hybriden Verfahrens zur automatisierten Erkennung semantischer, temporaler und statusbezogener Widersprüche über heterogene IT-Projektdokumente hinweg. Kernumfang: Anforderungen und Spezifikationen; Besprechungsprotokolle; Statusberichte; Projektpläne und Meilensteinübersichten; Tickets einschließlich Statusinformationen. Andere Dokumenttypen nur als klar gekennzeichnete explorative Robustheitsfälle; der Kernumfang wird nicht stillschweigend verändert.

## 2. Forschungsproblem und Wissenslücke (§4) – Status: zu überprüfende Annahme

Der Konfliktstatus zweier oder mehrerer Aussagen hängt nicht nur von ihrer sprachlichen Semantik ab. Berücksichtigt werden müssen insbesondere: Entitätsidentität, Aussageinhalt, Attribute und Werte, Gültigkeitszeitraum, zeitliche Beziehungen, Dokumentversion, Statuszustand, Statusübergänge, Provenienz, dokumentübergreifende Beziehungen.

Annahme des Forschungsantrags: Bestehende Einzelverfahren betrachten diese Dimensionen häufig getrennt oder bewerten nur einzelne Textpaare. HyConCheck untersucht deshalb, ob eine gemeinsame Evidenzrepräsentation und eine hybride Fusions- und Entscheidungslogik diese Informationen zuverlässiger kombinieren können.

**Behandlung in diesem Repository (§39.5):** Die behauptete Wissenslücke ist eine durch Literaturrecherche zu überprüfende Annahme. Sie gilt erst dann als konkretisiert, wenn das Rechercheprotokoll (BL-001) ausgeführt, die Quellen im Quellenregister (`references/`) mit vollständiger Provenienz erfasst und die Lücke mit Bezug auf die tatsächlich geprüften Arbeiten begründet ist (BL-004). Das Ergebnis kann die Annahme bestätigen, einschränken oder verwerfen.

## 3. Zentrale technische Eigenentwicklung (§5)

Der zentrale Forschungsgegenstand ist nicht lediglich die Nutzung bestehender LLMs oder NLI-Modelle. Zu entwickeln und experimentell zu untersuchen sind insbesondere:

### A. Evidenzrepräsentation

Eine Evidenzgraph-Struktur, die mindestens Beziehungen zwischen Aussagen, Entitäten, Attributen, Werten, Zeitpunkten und Zeitintervallen, Statuszuständen, Dokumentversionen, Provenienz sowie Dokumenten und Fundstellen abbilden kann. Die genaue Graphrepräsentation ist Forschungsgegenstand und darf aufgrund experimenteller Ergebnisse verändert werden. – Status: offen (AP5; Vorarbeiten AP4).

### B. Temporale und statusbezogene Konsistenz

Verfahren, die unterscheiden können zwischen: echtem gleichzeitigem Widerspruch, zulässigem Statuswechsel, zeitlicher Fortschreibung, neuer Dokumentversion, Ergänzung, veralteter Information, fehlendem Kontext, unklarem Fall. – Status: offen (AP4/AP5).

### C. Hybride Evidenzfusion

Alternative Verfahren zur Kombination von regelbasierter Evidenz, Embedding-Signalen, NLI-Scores, optionalen LLM-Signalen, Entitätsbeziehungen, temporalen Bedingungen, Statusbedingungen, Graphpfaden und Provenienzinformation. Insbesondere: ob probabilistische Modellsignale und symbolische beziehungsweise harte Konsistenzbedingungen sinnvoll kalibriert werden können. – Status: offen (AP5/AP6).

### D. Nachvollziehbare Entscheidung

Jeder erkannte Konflikt soll soweit technisch möglich enthalten: beteiligte Aussagen, Fundstellen, relevante Dokumente, aufgelöste Entitäten, Zeit- und Statuskontext, Widerspruchstyp, relevante Evidenz, Konfidenzwert, kurze nachvollziehbare Begründung. Interne Chain-of-Thought-Ausgaben sind weder erforderlich noch Bestandteil der Forschungsartefakte. – Status: offen.

## 4. Zentrale Forschungsfrage (§6)

Kann eine Evidenzgraph-basierte hybride Fusions- und Entscheidungslogik semantische Modellsignale mit Entitäts-, Zeit-, Status- und Provenienzinformation so koppeln, dass dokumentübergreifende Widersprüche zuverlässiger erkannt werden als mit Regel-, Embedding-, NLI- und LLM-Einzelverfahren?

## 5. Teilforschungsfragen F1–F6 (§7)

| ID | Frage | Status |
|---|---|---|
| F1 | Wie zuverlässig können die definierten Widerspruchstypen auf einem kontrollierten, zurückgehaltenen Evaluationskorpus erkannt werden? | offen |
| F2 | Welchen messbaren Beitrag leisten Entitätsauflösung, Zeitnormalisierung, Statusmodellierung, Evidenzgraph und Fusionslogik? | offen |
| F3 | Kann die hybride Architektur gegenüber den einzelnen Baselines eine höhere F1-Güte bei kontrollierter False-Positive-Rate erreichen? | offen |
| F4 | Unter welchen Dokumenttypen, Widerspruchstypen und Kontextbedingungen entstehen systematische False Positives, False Negatives oder nicht entscheidbare Fälle? | offen |
| F5 | Wie wirken sich Fehler bei Entity Resolution, Zeitnormalisierung und Statusextraktion auf nachgelagerte Graphpfade und Entscheidungen aus? | offen |
| F6 | Lassen sich semantische Modellwerte und symbolische Konsistenzbedingungen auf eine belastbare gemeinsame Vertrauens- beziehungsweise Entscheidungsskala bringen? | offen |

Diese Fragen dürfen aufgrund tatsächlicher Forschungsergebnisse präzisiert werden. Der grundlegende Forschungsgegenstand darf jedoch nicht ohne Dokumentation verändert werden.

## 6. Ausgangshypothesen H1–H7 (§8) – Status: ungeprüft

Die folgenden Aussagen sind zu prüfende Hypothesen und niemals vorweggenommene Ergebnisse. Jede Hypothese darf bestätigt, widerlegt oder präzisiert werden. Ein negatives Ergebnis ist ein gültiges Forschungsergebnis.

| ID | Hypothese (Wortlaut Master-Prompt) | Status |
|---|---|---|
| H1 | Die hybride Architektur erreicht auf dem kontrollierten Benchmark eine höhere Widerspruchs-F1 als die stärkste Einzelbaseline. | ungeprüft |
| H2 | Entitätsauflösung reduziert Fehlentscheidungen bei Aussagen über semantisch identische, aber unterschiedlich bezeichnete Objekte. | ungeprüft |
| H3 | Explizite temporale Modellierung reduziert False Positives bei Fortschreibungen und legitimen Zustandsänderungen. | ungeprüft |
| H4 | Die explizite Statusmodellierung verbessert die Unterscheidung zwischen Statuswiderspruch und zulässigem Statusübergang. | ungeprüft |
| H5 | Graphbasierte Evidenz verbessert insbesondere Fälle, deren Entscheidung mehrere Aussagen oder Dokumente erfordert. | ungeprüft |
| H6 | Eine kalibrierte Fusion mehrerer Evidenzarten ist zuverlässiger als die Konfidenz eines einzelnen Modells. | ungeprüft |
| H7 | Fehler in Entitätsextraktion und Zeitnormalisierung können sich über Graphrelationen fortpflanzen und dadurch zusätzliche falsche Konflikte erzeugen. | ungeprüft |

Die Zuordnung von Metriken, Entscheidungskriterien und Experimenten je Hypothese ist offen und erfolgt im Experimentregister (`experiments/`), sobald Benchmark und Baselines vorliegen. Statuswerte: `ungeprüft` → `in Prüfung` → `bestätigt` / `widerlegt` / `präzisiert` (jeweils nur mit reproduzierbarem Experiment).

## 7. Widerspruchstaxonomie (§9)

Fünf verbindliche Obertypen: Fakt und Wert; Zeit und Status; Modalität und Norm; Akteur und Verantwortung; Abhängigkeit und Schnittstelle. Anforderungen an die Operationalisierung, Entscheidungslabels und Sonderkennzeichnungen: [TAXONOMY_V1.md](TAXONOMY_V1.md). Operationalisierung offen (AP1); kein Obertyp abgeschlossen.

## 8. Benchmark (§10) – Status: offen (AP2)

Der kontrollierte Benchmark soll mindestens enthalten: positive Widerspruchsfälle, negative Fälle, schwierige Gegenbeispiele, Versionsfortschreibungen, Statusänderungen, temporale Grenzfälle, Entitätsmehrdeutigkeiten, dokumentübergreifende Konflikte, unklare Fälle.

Jeder Fall benötigt mindestens: eindeutige ID, Szenario-ID, Dokument-ID, Dokumenttyp, Version, Zeitkontext, Text beziehungsweise Aussage, Fundstelle, beteiligte Entitäten, Ground-Truth-Label, Widerspruchstyp, Begründung, Schwierigkeitsgrad, Provenienz des Beispiels.

Synthetische Daten müssen eindeutig als synthetisch gekennzeichnet sein. Anonymisierte reale Beispiele dürfen nur verwendet werden, wenn sie zulässig, hinreichend anonymisiert und getrennt dokumentiert sind. Synthetische und reale Daten sind in Auswertungen getrennt ausweisbar zu halten.

## 9. Schutz des Testsets (§11) – verbindlich ab Erstellung des Benchmarks

- Gruppierter Train-/Validation-/Test-Split; Zielgröße 60 % Entwicklung/Training, 20 % Validation, 20 % Test.
- Verwandte Varianten desselben Szenarios dürfen nicht über mehrere Splits verteilt werden (Gruppierung nach Szenario-ID).
- Der Testsplit ist einzufrieren.
- Testlabels dürfen nicht zur Methodenentwicklung, Promptoptimierung, Schwellenwertwahl, Modellauswahl oder Fehlerkorrektur verwendet werden.
- Die finale Testauswertung erfolgt erst nach Festlegung der zu evaluierenden Architektur beziehungsweise Varianten.
- Fehleranalysen des finalen Testsets erfolgen erst nach der vorregistrierten Hauptevaluation.

## 10. Ground Truth (§12) – Status: offen (AP2)

Die Ground Truth darf nicht nach Kenntnis von Modellresultaten angepasst werden, um Ergebnisse zu verbessern. Zu dokumentieren: Annotationsregeln, Änderungen am Leitfaden, schwierige Fälle, unklare Fälle, Begründungen, Version der Taxonomie. Für einen festgelegten Anteil wird eine zeitlich getrennte Blind-Reannotation durchgeführt, soweit dies mit einer Einzelperson sinnvoll umsetzbar ist. Ziel ist eine möglichst belastbare und nachvollziehbare Ground Truth.

## 11. Baselines B0–B4 (§13) – Status: offen (AP3)

| ID | Verfahren | Status |
|---|---|---|
| B0 | einfache String-/Keyword-/regelbasierte Referenz | offen |
| B1 | regelbasiertes Konsistenzverfahren | offen |
| B2 | Embedding-basierte Kandidatensuche beziehungsweise Klassifikation | offen |
| B3 | Natural-Language-Inference-Verfahren | offen |
| B4 | direkte LLM-basierte Klassifikation, sofern ohne zusätzliche unverhältnismäßige Kosten technisch verfügbar | offen |

Alle komplexeren HyConCheck-Verfahren sind gegen geeignete Baselines zu vergleichen. Eine Baseline darf das Hybridsystem schlagen; dieses Ergebnis ist zu akzeptieren und zu dokumentieren.

## 12. Experimentelle Entwicklungsrichtung (§14) – Status: offen

Mögliche Entwicklungsstufen: **A** Entitäten + Regeln · **B** Entitäten + Embedding Retrieval + NLI · **C** Entitäten + Zeit-/Statusmodell + NLI · **D** Evidenzgraph + semantische Klassifikation · **E** Evidenzgraph + temporale/statusbezogene Konsistenz · **F** Evidenzgraph + semantische, temporale und graphbasierte Evidenzfusion · **G** aus den Experimenten abgeleitete finale Forschungsarchitektur.

Diese Reihenfolge ist keine Verpflichtung. Die finale Architektur darf nicht vor den Experimenten festgelegt werden.

## 13. Zielpipeline (§15) – mögliche Pipeline, jede Stufe experimentell überprüfbar

Dokumente → deterministische Textextraktion/Normalisierung → Aussagenextraktion → Entitätsextraktion → Entity Resolution → Attributextraktion → Zeitnormalisierung → Statusextraktion → Provenienzerfassung → Evidenzgraph → Kandidaten-Retrieval → semantische Bewertung → temporale/statusbezogene Konsistenzprüfung → graphbasierte Evidenz → Evidenzfusion → Konfliktklassifikation → Kalibrierung → nachvollziehbare Ausgabe.

Stufen dürfen aufgrund von Ergebnissen geändert oder entfernt werden.

## 14. Evaluationsmetriken (§16)

**Primär:** Precision, Recall, Widerspruchs-F1, False-Positive-Rate.

**Sekundär, soweit methodisch sinnvoll:** Macro-F1 nach Widerspruchstyp, False-Negative-Rate, PR-AUC, Kalibrierungsmetriken wie ECE oder Brier Score, Retrieval Recall@K, Laufzeit, Speicherbedarf, Tokenverbrauch, Modellkosten, menschlicher Prüfaufwand, Vollständigkeit der ausgegebenen Evidenz.

**Getrennte Analyse nach:** Dokumenttyp, Widerspruchstyp, Schwierigkeitsgrad, synthetisch versus anonymisiert real, Kontextlänge, zeitlichem Bezug, Statusbezug.

## 15. Zentrale technische Risiken (§17)

- **Entity Resolution:** Falsches Matching kann scheinbare Konflikte erzeugen; zu striktes Matching kann reale Konflikte übersehen.
- **Zeitnormalisierung:** Relative Zeitangaben, überlappende Gültigkeitsintervalle und fehlende Zeitanker können zulässige Änderungen als Widerspruch erscheinen lassen.
- **Fehlerfortpflanzung:** Lokale Extraktionsfehler können sich über Graphrelationen fortpflanzen und mehrere falsche Konfliktpfade erzeugen.
- **Evidenzfusion:** Probabilistische NLI-/LLM-Scores und harte Zeit-/Statusbedingungen können möglicherweise nicht stabil auf einer gemeinsamen Entscheidungsskala kalibriert werden.
- **Hybridverfahren:** Das Hybridverfahren kann schlechter sein als einzelne Baselines. Falls dies geschieht, wird die Ursache untersucht; Zielmetrik, Ground Truth oder Testaufteilung werden nicht nachträglich verändert, um ein positives Ergebnis zu erzeugen.

## 16. Experimentframework (§18)

Jedes relevante Experiment erhält eine eindeutige ID `EXP-YYYY-NNNN` und speichert mindestens: Forschungsfrage, Hypothese, Code-Commit, Dataset-Version, Taxonomie-Version, Konfiguration, Modell und Modellversion, Promptversion (falls relevant), Seed, Rohvorhersagen, Ground Truth, Kennzahlen, Laufzeit, Fehler, Interpretation, Entscheidung, nächster Schritt. Jedes Experiment muss eine konkrete Erkenntnisfrage beantworten; Experimente ohne Erkenntnisziel werden vermieden. Ablage: [experiments/](../experiments/), Ergebnisse in [results/](../results/).

## 17. Experimentzyklus (§19)

1. offene Frage identifizieren · 2. Hypothese formulieren · 3. Experiment definieren · 4. Implementierung erstellen · 5. Tests ausführen · 6. Experiment ausführen · 7. Rohresultate unverändert speichern · 8. Kennzahlen berechnen · 9. Fehler analysieren · 10. Schlussfolgerung dokumentieren · 11. Folgeentscheidung treffen · 12. nächsten Versuch ableiten. Die Ergebnisse bestimmen den weiteren Forschungsweg.

## 18. Fehleranalyse (§20)

False Positives, False Negatives und unklare Fälle werden mindestens nach folgenden Fehlerklassen analysiert: Entity Resolution Failure, Temporal Normalization Failure, Status Interpretation Failure, Retrieval Failure, Provenance Failure, Graph Propagation Failure, Numerical/Value Reasoning Failure, Negation/Modality Failure, Missing Context, Versioning Failure, Hallucinated Conflict, Ambiguous Ground Truth.

Für häufige Fehler: 1. technische Ursache bestimmen · 2. Hypothese für Gegenmaßnahme formulieren · 3. Gegenmaßnahme implementieren · 4. Folgeexperiment durchführen · 5. Effekt messen.

## 19. Ablationsstudien (§21)

Bei geeigneten Hybridarchitekturen wird der isolierte Beitrag untersucht von: Entity Resolution, Embedding Retrieval, NLI, LLM-Signal, Zeitnormalisierung, Statusmodellierung, Evidenzgraph, graphbasierten Relationen, symbolischen Konsistenzregeln, Konfidenz-/Evidenzfusion. Ziel: Welche Komponente liefert welchen messbaren Beitrag und unter welchen Bedingungen?

## 20. Robustheit (§22)

Soweit sinnvoll werden getestet: Paraphrasen, Synonyme, Tippfehler, unterschiedliche Satzstruktur, irrelevanter Zusatzkontext, fehlende Informationen, lange Dokumente, unterschiedliche Dokumentreihenfolge, Versionsänderungen, relative Datumsangaben, mehrdeutige Entitätsnamen, Statuswechsel, widersprüchliche Metadaten. Gemessen wird die Veränderung gegenüber der normalen Evaluation.

## 21. Wissenschaftliche Integrität (§23) und Reproduzierbarkeit (§24)

Niemals: Ergebnisse, Quellen, Messwerte erfinden; Experimente vortäuschen; fehlgeschlagene Experimente verschweigen; Daten manipulieren; Ground Truth ergebnisorientiert verändern; Testdaten zur Optimierung verwenden; Cherry Picking; einen positiven Projektausgang voraussetzen; einen Hybridvorteil behaupten, bevor er gemessen wurde; Tätigkeiten als durchgeführt dokumentieren, die nicht durchgeführt wurden. Negative Ergebnisse und gescheiterte Ansätze werden dokumentiert.

Zentrale Ergebnisse müssen aus Git-Commit, Dataset-Version, Konfiguration, Modellversion, Promptversion, Random Seed, Rohresultaten, Auswertungscode und aggregierten Kennzahlen reproduzierbar sein. Maschinell erzeugte Artefakte werden gegenüber manueller Nacherfassung bevorzugt.

## 22. Literatur und Stand der Technik (§34)

Recherchethemen: contradiction detection, Natural Language Inference, document-level NLI, cross-document contradiction detection, semantic consistency checking, entity resolution, temporal reasoning, temporal knowledge graphs, status/state transition modeling, fact verification, evidence graphs, knowledge graph reasoning, neuro-symbolic AI, uncertainty calibration, evidence fusion, contradiction benchmarks.

Quellenpriorität: 1. peer-reviewed Literatur, 2. etablierte Benchmarks, 3. hochwertige Preprints, 4. offizielle technische Dokumentation, 5. nachvollziehbare Open-Source-Implementierungen. Quellen werden mit vollständiger Provenienz gespeichert; keine Quelle wird behauptet, die nicht tatsächlich geprüft wurde. Rechercheprotokoll und Suchstrategie: [references/RESEARCH_PROTOCOL.md](../references/RESEARCH_PROTOCOL.md) (BL-001, V1.0); Durchführung der Recherche: BL-002 (in Arbeit; Tranche BL-002.1 Cluster A–E abgeschlossen, Zwischenauswertung in `references/reviews/`; Cluster F–P offen).

## 23. Qualitäts-Gates (§35), Meilensteine (§36), Definition of Done (§37), Abschlussfrage (§38)

Verbindlich verankert in [PROJECT_CHARTER.md](PROJECT_CHARTER.md) (Abschnitte 8–11) und im [Projektplan](../planning/PROJECT_PLAN_2026_2027.md); Wortlaut im Master-Prompt.

## 24. Zuordnung der Bausteine zu den Arbeitspaketen (§25)

| Baustein | AP |
|---|---|
| Technischer Lösungsraum, Stand der Technik, Überprüfung der Wissenslücke, Widerspruchstaxonomie, formale Kriterien | AP1 |
| Benchmarkmethodik, Testdatengenerator, Grenzfälle, Ground Truth, Split und Testset-Schutz | AP2 |
| Baselines B0–B4, Evaluationspipeline, experimenteller Vergleich | AP3 |
| Entitätsauflösung; Extraktion und Normalisierung von Attributen, Zeitintervallen, Statuszuständen, Provenienz | AP4 |
| Evidenzgraph, Fusionsalgorithmen, Architekturvergleich (Entwicklungsstufen D–F) | AP5 |
| Kalibrierung und Optimierung, Ablations-, Fehler- und Robustheitsanalysen, alternative Ansätze | AP6 |
| Validierung der ausgewählten Architektur auf zurückgehaltenen Testdaten, Baselinevergleich, Fehlermuster (Stufe G) | AP7 |

## 25. Was in der Grundlagenphase nicht geschieht (§39)

Keine Experimente, keine Modellläufe, keine Datenerhebung, keine fachliche Operationalisierung der Obertypen, keine Festlegung der finalen Architektur, keine Übernahme früherer Ergebnisse.
