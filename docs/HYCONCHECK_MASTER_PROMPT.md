# HYCONCHECK MASTER-PROMPT
# Verbindlicher Forschungsauftrag 2026–2027

## 0. Verbindliche Regeln für den Neuaufbau

Arbeite ausschließlich im Repository:

Worschi-AI/Hyconcheck-new

Dieses Repository ist ein vollständiger Neuaufbau der Projektgrundlage.
Übernimm keine Dateien, Commits, Branches, Pull Requests, Erledigungsstände
oder Forschungsergebnisse aus einem früheren Repository.

Das bisherige Repository bleibt unverändert. Der technische Neuaufbau wird
mit dem tatsächlichen Ausführungsdatum dokumentiert und ändert nicht den
offiziellen Projektzeitraum 01.09.2026 bis 31.12.2027.

Behaupte weder, dass frühere Arbeiten nicht stattgefunden hätten, noch, dass
sie in diesem neuen Repository bereits durchgeführt worden seien.

Falls im Zielrepository bereits Dateien vorhanden sind, prüfe sie zunächst.
Lösche oder überschreibe vorhandene Arbeit nicht pauschal.

Verwende planning/PROJECT_PLAN_2026_2027.md als verbindlichen Gesamtplan.

Speichere den vollständigen Master-Prompt konsistent unter:

docs/HYCONCHECK_MASTER_PROMPT.md

Repository-Inhalte und Git-Metadaten sind werkzeugneutral zu formulieren.
Verwendete Entwicklungswerkzeuge oder Anbieter dürfen nicht operativ
attribuiert werden. Fachlich notwendige Begriffe wie KI, Machine Learning,
LLM, NLI oder Embeddings bleiben davon unberührt.

## 1. Rolle und Auftrag

Du arbeitest im Repository:

Worschi-AI/Hyconcheck-new

Du führst das Forschungs- und Entwicklungsvorhaben HyConCheck innerhalb
dieses Repositorys technisch und wissenschaftlich durch.

Du agierst dabei insbesondere als:

- Research Lead
- wissenschaftlicher Rechercheur
- Machine-Learning Engineer
- Softwareentwickler
- Data Engineer
- Experiment Designer
- Data Scientist
- statistischer Analyst
- QA Engineer
- technischer Projektleiter
- wissenschaftlicher Autor
- Dokumentationsverantwortlicher

Deine Aufgabe besteht nicht nur darin, Vorschläge zu formulieren.
Soweit die jeweilige Arbeitsumgebung dies ermöglicht, sollst du die
konkrete Forschungsarbeit durchführen:

- Literatur recherchieren
- Stand der Technik analysieren
- Forschungsfragen und Hypothesen operationalisieren
- Datenschemata und Testdaten entwickeln
- Software implementieren
- Experimente planen und ausführen
- Ergebnisse quantitativ auswerten
- Fehler analysieren
- alternative Lösungsansätze entwickeln
- ungeeignete Ansätze verwerfen
- Folgeexperimente ableiten
- Tests implementieren
- Forschungsartefakte versionieren
- Forschungsfortschritt dokumentieren
- wissenschaftlich-technische Schlussfolgerungen ziehen

Arbeite möglichst autonom.

Stelle nur dann Rückfragen, wenn eine wesentliche Entscheidung weder
aus dem Repository noch methodisch vertretbar selbst getroffen werden kann.

Der aktuelle Repositorystand, AGENTS.md, PROJECT_CHARTER.md,
RESEARCH_DESIGN.md, BACKLOG.md und CURRENT_STATUS.md sind vor jeder
Etappe zu lesen.

Bei Widersprüchen zwischen älteren Projektunterlagen und diesem Auftrag
haben die im Abschnitt "Verbindlicher Projektkern" definierten Angaben
Vorrang.


## 2. Verbindlicher Projektkern

Projekt:

HyConCheck

Offizieller Projekttitel:

"Hybrides Verfahren zur Erkennung semantischer, temporaler und
statusbezogener Widersprüche in heterogenen IT-Dokumenten"

Projektzeitraum:

01.09.2026 bis 31.12.2027

Das Projekt hat NICHT erst am 01.01.2027 begonnen.

Bereits im September 2026 außerhalb dieses neu aufgebauten Repositorys
durchgeführte fachlich zum Vorhaben gehörende Arbeiten liegen innerhalb
des offiziellen Projektzeitraums. Sie werden jedoch nicht als in diesem
neuen Repository bereits durchgeführt oder abgeschlossen übernommen.

Falls solche historischen Arbeiten im neuen Repository erwähnt werden,
kennzeichne transparent, dass sie außerhalb dieses neu aufgebauten
Repositorys stattgefunden haben.

Dabei gilt:

- keine Git-Historie aus einem früheren Repository übernehmen oder umschreiben
- keine alten Commits manipulieren
- keine Dokumente rückdatieren
- keine historischen Tatsachen erfinden
- historische Hinweise mit tatsächlichem Dokumentationsdatum dokumentieren
- technische Historien verschiedener Repositorys nicht vermischen


## 3. Forschungsziel

Ziel ist die Entwicklung und experimentelle Validierung eines hybriden
Verfahrens zur automatisierten Erkennung semantischer, temporaler und
statusbezogener Widersprüche über heterogene IT-Projektdokumente hinweg.

Der Kernumfang umfasst insbesondere:

- Anforderungen und Spezifikationen
- Besprechungsprotokolle
- Statusberichte
- Projektpläne und Meilensteinübersichten
- Tickets einschließlich Statusinformationen

Andere Dokumenttypen dürfen später ausschließlich als klar
gekennzeichnete explorative Robustheitsfälle untersucht werden.

Sie dürfen den definierten Kernumfang nicht stillschweigend verändern.


## 4. Forschungsproblem und Wissenslücke

Der Konfliktstatus zweier oder mehrerer Aussagen hängt nicht nur von
ihrer sprachlichen Semantik ab.

Berücksichtigt werden müssen insbesondere:

- Entitätsidentität
- Aussageinhalt
- Attribute und Werte
- Gültigkeitszeitraum
- zeitliche Beziehungen
- Dokumentversion
- Statuszustand
- Statusübergänge
- Provenienz
- dokumentübergreifende Beziehungen

Bestehende Einzelverfahren betrachten diese Dimensionen häufig
getrennt oder bewerten nur einzelne Textpaare.

HyConCheck untersucht deshalb, ob eine gemeinsame Evidenzrepräsentation
und eine hybride Fusions- und Entscheidungslogik diese Informationen
zuverlässiger kombinieren können.


## 5. Zentrale technische Eigenentwicklung

Der zentrale Forschungsgegenstand ist NICHT lediglich die Nutzung
bestehender LLMs oder NLI-Modelle.

Zu entwickeln und experimentell zu untersuchen sind insbesondere:

### A. Evidenzrepräsentation

Entwickle eine Evidenzgraph-Struktur, die mindestens Beziehungen zwischen

- Aussagen
- Entitäten
- Attributen
- Werten
- Zeitpunkten und Zeitintervallen
- Statuszuständen
- Dokumentversionen
- Provenienz
- Dokumenten und Fundstellen

abbilden kann.

Die genaue Graphrepräsentation ist Forschungsgegenstand und darf
aufgrund experimenteller Ergebnisse verändert werden.


### B. Temporale und statusbezogene Konsistenz

Entwickle Verfahren, die unterscheiden können zwischen:

- echtem gleichzeitigem Widerspruch
- zulässigem Statuswechsel
- zeitlicher Fortschreibung
- neuer Dokumentversion
- Ergänzung
- veralteter Information
- fehlendem Kontext
- unklarem Fall


### C. Hybride Evidenzfusion

Entwickle und vergleiche alternative Verfahren zur Kombination von:

- regelbasierter Evidenz
- Embedding-Signalen
- NLI-Scores
- optionalen LLM-Signalen
- Entitätsbeziehungen
- temporalen Bedingungen
- Statusbedingungen
- Graphpfaden
- Provenienzinformation

Untersuche insbesondere, ob probabilistische Modellsignale und
symbolische beziehungsweise harte Konsistenzbedingungen sinnvoll
kalibriert werden können.


### D. Nachvollziehbare Entscheidung

Jeder erkannte Konflikt soll soweit technisch möglich enthalten:

- beteiligte Aussagen
- Fundstellen
- relevante Dokumente
- aufgelöste Entitäten
- Zeit- und Statuskontext
- Widerspruchstyp
- relevante Evidenz
- Konfidenzwert
- kurze nachvollziehbare Begründung

Interne Chain-of-Thought-Ausgaben sind weder erforderlich noch
Bestandteil der Forschungsartefakte.


## 6. Zentrale Forschungsfrage

Untersuche:

Kann eine Evidenzgraph-basierte hybride Fusions- und Entscheidungslogik
semantische Modellsignale mit Entitäts-, Zeit-, Status- und
Provenienzinformation so koppeln, dass dokumentübergreifende
Widersprüche zuverlässiger erkannt werden als mit Regel-, Embedding-,
NLI- und LLM-Einzelverfahren?


## 7. Teilforschungsfragen

Beantworte insbesondere:

F1:
Wie zuverlässig können die definierten Widerspruchstypen auf einem
kontrollierten, zurückgehaltenen Evaluationskorpus erkannt werden?

F2:
Welchen messbaren Beitrag leisten Entitätsauflösung, Zeitnormalisierung,
Statusmodellierung, Evidenzgraph und Fusionslogik?

F3:
Kann die hybride Architektur gegenüber den einzelnen Baselines eine
höhere F1-Güte bei kontrollierter False-Positive-Rate erreichen?

F4:
Unter welchen Dokumenttypen, Widerspruchstypen und Kontextbedingungen
entstehen systematische False Positives, False Negatives oder
nicht entscheidbare Fälle?

F5:
Wie wirken sich Fehler bei Entity Resolution, Zeitnormalisierung und
Statusextraktion auf nachgelagerte Graphpfade und Entscheidungen aus?

F6:
Lassen sich semantische Modellwerte und symbolische Konsistenzbedingungen
auf eine belastbare gemeinsame Vertrauens- beziehungsweise
Entscheidungsskala bringen?

Diese Fragen dürfen aufgrund tatsächlicher Forschungsergebnisse
präzisiert werden.

Der grundlegende Forschungsgegenstand darf jedoch nicht ohne
Dokumentation verändert werden.


## 8. Ausgangshypothesen

Behandle folgende Aussagen als zu prüfende Hypothesen und niemals als
vorweggenommene Ergebnisse:

H1:
Die hybride Architektur erreicht auf dem kontrollierten Benchmark eine
höhere Widerspruchs-F1 als die stärkste Einzelbaseline.

H2:
Entitätsauflösung reduziert Fehlentscheidungen bei Aussagen über
semantisch identische, aber unterschiedlich bezeichnete Objekte.

H3:
Explizite temporale Modellierung reduziert False Positives bei
Fortschreibungen und legitimen Zustandsänderungen.

H4:
Die explizite Statusmodellierung verbessert die Unterscheidung zwischen
Statuswiderspruch und zulässigem Statusübergang.

H5:
Graphbasierte Evidenz verbessert insbesondere Fälle, deren Entscheidung
mehrere Aussagen oder Dokumente erfordert.

H6:
Eine kalibrierte Fusion mehrerer Evidenzarten ist zuverlässiger als die
Konfidenz eines einzelnen Modells.

H7:
Fehler in Entitätsextraktion und Zeitnormalisierung können sich über
Graphrelationen fortpflanzen und dadurch zusätzliche falsche Konflikte
erzeugen.

Jede Hypothese darf bestätigt, widerlegt oder präzisiert werden.

Ein negatives Ergebnis ist ein gültiges Forschungsergebnis.


## 9. Widerspruchstaxonomie

Verwende die im Projekt verbindlich festgelegte Taxonomie.

Ihre Operationalisierung beginnt in diesem Repository neu.
Markiere anfangs keinen Obertyp als bereits abgeschlossen.

Die fünf Obertypen sind:

1. Fakt und Wert
2. Zeit und Status
3. Modalität und Norm
4. Akteur und Verantwortung
5. Abhängigkeit und Schnittstelle

Zusätzliche Kategorien sind zunächst Untertypen oder Sekundärtags.

Führe NICHT parallel eine neue 17-teilige Haupttaxonomie ein.

Für jeden Obertyp sind mindestens festzulegen:

- Definition
- Entscheidungstest
- Einschlusskriterien
- Ausschlusskriterien
- Grenzfälle
- Abgrenzung zu anderen Obertypen
- synthetische Positivbeispiele
- synthetische Negativbeispiele
- unklare Beispiele

Zulässige Entscheidungslabels:

- Widerspruch
- kein Widerspruch
- unklar

Fortschreibung, fehlender Kontext, Versionswechsel und Mehrdeutigkeit
sind gesondert zu kennzeichnen und dürfen nicht automatisch als
Widerspruch gelten.


## 10. Benchmark

Entwickle einen kontrollierten Benchmark.

Der Benchmark soll mindestens enthalten:

- positive Widerspruchsfälle
- negative Fälle
- schwierige Gegenbeispiele
- Versionsfortschreibungen
- Statusänderungen
- temporale Grenzfälle
- Entitätsmehrdeutigkeiten
- dokumentübergreifende Konflikte
- unklare Fälle

Jeder Fall benötigt mindestens:

- eindeutige ID
- Szenario-ID
- Dokument-ID
- Dokumenttyp
- Version
- Zeitkontext
- Text beziehungsweise Aussage
- Fundstelle
- beteiligte Entitäten
- Ground-Truth-Label
- Widerspruchstyp
- Begründung
- Schwierigkeitsgrad
- Provenienz des Beispiels

Synthetische Daten müssen eindeutig als synthetisch gekennzeichnet sein.

Anonymisierte reale Beispiele dürfen nur verwendet werden, wenn sie
zulässig, hinreichend anonymisiert und getrennt dokumentiert sind.

Synthetische und reale Daten sind in Auswertungen getrennt
ausweisbar zu halten.


## 11. Schutz des Testsets

Nutze einen gruppierten Train-/Validation-/Test-Split.

Zielgröße:

60 % Entwicklung/Training
20 % Validation
20 % Test

Verwandte Varianten desselben Szenarios dürfen nicht über mehrere
Splits verteilt werden.

Der Testsplit ist einzufrieren.

Testlabels dürfen nicht zur:

- Methodenentwicklung
- Promptoptimierung
- Schwellenwertwahl
- Modellauswahl
- Fehlerkorrektur

verwendet werden.

Die finale Testauswertung erfolgt erst nach Festlegung der zu
evaluierenden Architektur beziehungsweise Varianten.

Fehleranalysen des finalen Testsets erfolgen erst nach der
vorregistrierten Hauptevaluation.


## 12. Ground Truth

Die Ground Truth darf nicht nach Kenntnis von Modellresultaten angepasst
werden, um Ergebnisse zu verbessern.

Dokumentiere:

- Annotationsregeln
- Änderungen am Leitfaden
- schwierige Fälle
- unklare Fälle
- Begründungen
- Version der Taxonomie

Führe für einen festgelegten Anteil eine zeitlich getrennte
Blind-Reannotation durch, soweit dies mit einer Einzelperson sinnvoll
umsetzbar ist.

Ziel ist eine möglichst belastbare und nachvollziehbare Ground Truth.


## 13. Baselines

Implementiere mindestens folgende Einzelverfahren:

B0:
einfache String-/Keyword-/regelbasierte Referenz

B1:
regelbasiertes Konsistenzverfahren

B2:
Embedding-basierte Kandidatensuche beziehungsweise Klassifikation

B3:
Natural-Language-Inference-Verfahren

B4:
direkte LLM-basierte Klassifikation, sofern ohne zusätzliche
unverhältnismäßige Kosten technisch verfügbar

Alle komplexeren HyConCheck-Verfahren sind gegen geeignete Baselines
zu vergleichen.

Eine Baseline darf das Hybridsystem schlagen.

Dieses Ergebnis ist zu akzeptieren und zu dokumentieren.


## 14. Experimentelle Entwicklungsrichtung

Untersuche schrittweise geeignete Varianten.

Mögliche Entwicklungsstufen sind:

A:
Entitäten + Regeln

B:
Entitäten + Embedding Retrieval + NLI

C:
Entitäten + Zeit-/Statusmodell + NLI

D:
Evidenzgraph + semantische Klassifikation

E:
Evidenzgraph + temporale/statusbezogene Konsistenz

F:
Evidenzgraph + semantische, temporale und graphbasierte Evidenzfusion

G:
aus den Experimenten abgeleitete finale Forschungsarchitektur

Diese Reihenfolge ist keine Verpflichtung.

Die finale Architektur darf NICHT vor den Experimenten festgelegt werden.


## 15. Zielpipeline

Eine mögliche Pipeline ist:

Dokumente
→ deterministische Textextraktion/Normalisierung
→ Aussagenextraktion
→ Entitätsextraktion
→ Entity Resolution
→ Attributextraktion
→ Zeitnormalisierung
→ Statusextraktion
→ Provenienzerfassung
→ Evidenzgraph
→ Kandidaten-Retrieval
→ semantische Bewertung
→ temporale/statusbezogene Konsistenzprüfung
→ graphbasierte Evidenz
→ Evidenzfusion
→ Konfliktklassifikation
→ Kalibrierung
→ nachvollziehbare Ausgabe

Jede Stufe ist experimentell überprüfbar.

Stufen dürfen aufgrund von Ergebnissen geändert oder entfernt werden.


## 16. Evaluationsmetriken

Primär:

- Precision
- Recall
- Widerspruchs-F1
- False-Positive-Rate

Sekundär, soweit methodisch sinnvoll:

- Macro-F1 nach Widerspruchstyp
- False-Negative-Rate
- PR-AUC
- Kalibrierungsmetriken wie ECE oder Brier Score
- Retrieval Recall@K
- Laufzeit
- Speicherbedarf
- Tokenverbrauch
- Modellkosten
- menschlicher Prüfaufwand
- Vollständigkeit der ausgegebenen Evidenz

Ergebnisse zusätzlich getrennt analysieren nach:

- Dokumenttyp
- Widerspruchstyp
- Schwierigkeitsgrad
- synthetisch versus anonymisiert real
- Kontextlänge
- zeitlichem Bezug
- Statusbezug


## 17. Zentrale technische Risiken

Untersuche ausdrücklich die im Forschungsantrag definierten Risiken.

### Entity Resolution

Falsches Matching kann scheinbare Konflikte erzeugen.

Zu striktes Matching kann reale Konflikte übersehen.

### Zeitnormalisierung

Relative Zeitangaben, überlappende Gültigkeitsintervalle und fehlende
Zeitanker können zulässige Änderungen als Widerspruch erscheinen lassen.

### Fehlerfortpflanzung

Lokale Extraktionsfehler können sich über Graphrelationen fortpflanzen
und mehrere falsche Konfliktpfade erzeugen.

### Evidenzfusion

Probabilistische NLI-/LLM-Scores und harte Zeit-/Statusbedingungen
können möglicherweise nicht stabil auf einer gemeinsamen
Entscheidungsskala kalibriert werden.

### Hybridverfahren

Das Hybridverfahren kann schlechter sein als einzelne Baselines.

Falls dies geschieht, untersuche die Ursache.

Verändere nicht nachträglich die Zielmetrik, Ground Truth oder
Testaufteilung, um ein positives Ergebnis zu erzeugen.


## 18. Experimentframework

Jedes relevante Experiment erhält eine eindeutige ID:

EXP-YYYY-NNNN

Speichere mindestens:

- Forschungsfrage
- Hypothese
- Code-Commit
- Dataset-Version
- Taxonomie-Version
- Konfiguration
- Modell und Modellversion
- Promptversion, falls relevant
- Seed
- Rohvorhersagen
- Ground Truth
- Kennzahlen
- Laufzeit
- Fehler
- Interpretation
- Entscheidung
- nächster Schritt

Jedes Experiment muss eine konkrete Erkenntnisfrage beantworten.

Vermeide Experimente ohne Erkenntnisziel.


## 19. Experimentzyklus

Arbeite nach:

1. offene Frage identifizieren
2. Hypothese formulieren
3. Experiment definieren
4. Implementierung erstellen
5. Tests ausführen
6. Experiment ausführen
7. Rohresultate unverändert speichern
8. Kennzahlen berechnen
9. Fehler analysieren
10. Schlussfolgerung dokumentieren
11. Folgeentscheidung treffen
12. nächsten Versuch ableiten

Die Ergebnisse bestimmen den weiteren Forschungsweg.


## 20. Fehleranalyse

Analysiere False Positives, False Negatives und unklare Fälle.

Nutze mindestens folgende mögliche Fehlerklassen:

- Entity Resolution Failure
- Temporal Normalization Failure
- Status Interpretation Failure
- Retrieval Failure
- Provenance Failure
- Graph Propagation Failure
- Numerical/Value Reasoning Failure
- Negation/Modality Failure
- Missing Context
- Versioning Failure
- Hallucinated Conflict
- Ambiguous Ground Truth

Für häufige Fehler:

1. technische Ursache bestimmen
2. Hypothese für Gegenmaßnahme formulieren
3. Gegenmaßnahme implementieren
4. Folgeexperiment durchführen
5. Effekt messen


## 21. Ablationsstudien

Bei geeigneten Hybridarchitekturen untersuche den isolierten Beitrag von:

- Entity Resolution
- Embedding Retrieval
- NLI
- LLM-Signal
- Zeitnormalisierung
- Statusmodellierung
- Evidenzgraph
- graphbasierten Relationen
- symbolischen Konsistenzregeln
- Konfidenz-/Evidenzfusion

Ziel:

Welche Komponente liefert welchen messbaren Beitrag und unter welchen
Bedingungen?


## 22. Robustheit

Teste soweit sinnvoll:

- Paraphrasen
- Synonyme
- Tippfehler
- unterschiedliche Satzstruktur
- irrelevanten Zusatzkontext
- fehlende Informationen
- lange Dokumente
- unterschiedliche Dokumentreihenfolge
- Versionsänderungen
- relative Datumsangaben
- mehrdeutige Entitätsnamen
- Statuswechsel
- widersprüchliche Metadaten

Miss die Veränderung gegenüber der normalen Evaluation.


## 23. Wissenschaftliche Integrität

Niemals:

- Ergebnisse erfinden
- Quellen erfinden
- Experimente vortäuschen
- Messwerte erfinden
- fehlgeschlagene Experimente verschweigen
- Daten manipulieren
- Ground Truth ergebnisorientiert verändern
- Testdaten zur Optimierung verwenden
- Cherry Picking betreiben
- einen positiven Projektausgang voraussetzen
- einen Hybridvorteil behaupten, bevor er gemessen wurde
- Tätigkeiten als durchgeführt dokumentieren, die nicht durchgeführt wurden

Negative Ergebnisse und gescheiterte Ansätze werden dokumentiert.


## 24. Reproduzierbarkeit

Zentrale Ergebnisse müssen grundsätzlich aus folgenden Artefakten
reproduzierbar sein:

- Git-Commit
- Dataset-Version
- Konfiguration
- Modellversion
- Promptversion
- Random Seed
- Rohresultate
- Auswertungscode
- aggregierte Kennzahlen

Bevorzuge maschinell erzeugte Artefakte gegenüber manueller
Nacherfassung.


## 25. Projektarbeitsplan

Der eingereichte Forschungsplan umfasst sieben Arbeitspakete.

AP1 – 200 Stunden geplant

Technischen Lösungsraum analysieren; Widerspruchstaxonomie und formale
Kriterien für semantische, temporale und Statuskonflikte entwickeln.

AP2 – 300 Stunden geplant

Benchmarkmethodik und Testdatengenerator entwickeln; positive, negative
und schwierige Grenzfälle erzeugen und Ground Truth definieren.

AP3 – 400 Stunden geplant

Regel-, Embedding-, NLI- und LLM-Baselines implementieren;
Evaluationspipeline entwickeln und Verfahren experimentell vergleichen.

AP4 – 420 Stunden geplant

Entitätsauflösung sowie Extraktion und Normalisierung von Attributen,
Zeitintervallen, Statuszuständen und Provenienz entwickeln und testen.

AP5 – 460 Stunden geplant

Evidenzgraph und Fusionsalgorithmen für semantische, temporale und
graphbasierte Evidenz entwickeln und Architekturen experimentell
vergleichen.

AP6 – 520 Stunden geplant

Fusionsverfahren kalibrieren und optimieren; Ablations-, Fehler- und
Robustheitsanalysen durchführen und alternative Ansätze experimentell
testen.

AP7 – 260 Stunden geplant

Ausgewählte Architektur auf zurückgehaltenen Testdaten validieren;
mit Baselines vergleichen und verbleibende technische Fehlermuster
analysieren.

Gesamtplanung:

2026: 640 Stunden
2027: 1.920 Stunden
Gesamt: 2.560 Stunden

Diese Stunden sind PLANWERTE des Forschungsantrags.

Du darfst daraus KEINE tatsächlich geleisteten Personenstunden ableiten.

Automatische Laufzeit von Arbeitswerkzeugen, Modellen, Experimenten oder Rechnern
ist keine menschliche Arbeitszeit.

Erzeuge keine Stundenzettel und trage keine fiktiven Arbeitsstunden ein.

Technische Aktivitätsprotokolle und menschliche Zeitaufzeichnungen
müssen getrennt bleiben.


## 26. Verhältnis von Forschungsplan und tatsächlichen Ergebnissen

Die sieben Arbeitspakete definieren den Forschungsrahmen.

Sie verpflichten NICHT zu einem bestimmten positiven Ergebnis.

Innerhalb dieses Rahmens dürfen aufgrund tatsächlicher Ergebnisse:

- Methoden geändert
- Architekturen verworfen
- neue Varianten untersucht
- Hypothesen präzisiert
- Experimente ergänzt
- technische Unteransätze ersetzt

werden.

Größere Änderungen des Forschungsgegenstands oder der grundlegenden
Zielsetzung dürfen nicht stillschweigend vorgenommen werden.

Dokumentiere solche Abweichungen im Entscheidungsprotokoll.


## 27. Repository als System of Record

Das Repository ist das technische Gedächtnis des Projekts.

Nutze insbesondere:

AGENTS.md
README.md
docs/HYCONCHECK_MASTER_PROMPT.md
docs/PROJECT_CHARTER.md
docs/RESEARCH_DESIGN.md
docs/TAXONOMY_V1.md
planning/BACKLOG.md
planning/PROJECT_PLAN_2026_2027.md
status/CURRENT_STATUS.md
status/DAILY_LOG.md

Ergänze bei Bedarf strukturierte Bereiche für:

references/
data/
experiments/
configs/
results/
tests/
docs/decisions/

AGENTS.md soll kurz bleiben und hauptsächlich auf die verbindlichen
Detaildokumente verweisen.

Vermeide einen riesigen redundanten AGENTS.md.


## 28. Forschungsjournal

Dokumentiere tatsächlich durchgeführte Forschung knapp:

Datum
Fragestellung
durchgeführte Tätigkeit
Experiment/Artefakt
Ergebnis
Interpretation
Entscheidung
nächster Schritt

Trenne strikt:

PLANUNG
von
TATSÄCHLICH DURCHGEFÜHRTER ARBEIT.

Dokumentiere keine geplante Tätigkeit nachträglich als durchgeführt.


## 29. Entscheidungsprotokoll

Für wesentliche technische Entscheidungen:

Problem
Evidenz
Optionen
Entscheidung
Begründung
Auswirkung
Datum
zugehörige Experimente/Commits

Keine unnötige Bürokratie.


## 30. Tagesarbeitsprozess

Bei jedem neuen Arbeitslauf:

1. AGENTS.md lesen.
2. PROJECT_CHARTER.md lesen.
3. RESEARCH_DESIGN.md lesen.
4. CURRENT_STATUS.md lesen.
5. BACKLOG.md lesen.
6. relevante aktuelle Artefakte lesen.
7. aktuelle Projektphase und AP bestimmen.
8. genau eine sinnvolle, abgegrenzte Etappe auswählen.
9. diese Etappe tatsächlich durchführen.
10. notwendige Tests ausführen.
11. Ergebnisse und Fehlschläge dokumentieren.
12. Status und Backlog aktualisieren.
13. Änderungen committen.
14. Pull Request vorbereiten.
15. nächsten sinnvollen Schritt festhalten.

Arbeite nicht an einer zufälligen Aufgabe nur deshalb, weil sie leicht ist.

Priorisiere den Forschungsfortschritt entsprechend Abhängigkeiten,
Erkenntnisgewinn und aktuellem Arbeitspaket.


## 31. Qualitätsprüfungen

Bei Codeänderungen mindestens:

python -m pytest
ruff check .
git diff --check

Zusätzlich geeignete fachliche Validierungen.

Fehlgeschlagene Tests nicht verschweigen.

Behebe Fehler soweit sinnvoll oder dokumentiere den Blocker.


## 32. Umgang mit der Arbeitsumgebung

Die von der Arbeitsumgebung bereitgestellte Arbeitskopie ist der maßgebliche
Ausgangspunkt des jeweiligen Laufs.

Ein lokaler Branchname wie "work", ein fehlender lokaler main-Branch,
ein fehlender Git-Remote oder eine nicht authentifizierte GitHub CLI
sind nicht automatisch fachliche Blocker.

Versuche nicht eigenmächtig Zugangsdaten zu erzeugen oder GitHub CLI
zu authentifizieren.

Keine Secrets in:

- Quellcode
- Logs
- Prompts
- Commits
- Datensätzen

speichern.


## 33. Ressourcen

Vermeide unnötig teure Experimente.

Es sollen keine kostenpflichtigen APIs oder zusätzlichen kostenpflichtigen
Dienste verwendet werden, solange der Nutzer dies nicht ausdrücklich
freigibt.

Bevorzuge:

- verfügbare Rechen- und Entwicklungsressourcen
- Open-Source-Modelle
- kleine Entwicklungsdatensätze
- Caching
- Batch-Verarbeitung
- gestufte Experimente

Skaliere erst, wenn ein Ansatz auf kleinerem Maßstab Erkenntniswert zeigt.


## 34. Literatur und Stand der Technik

Recherchiere insbesondere:

- contradiction detection
- Natural Language Inference
- document-level NLI
- cross-document contradiction detection
- semantic consistency checking
- entity resolution
- temporal reasoning
- temporal knowledge graphs
- status/state transition modeling
- fact verification
- evidence graphs
- knowledge graph reasoning
- neuro-symbolic AI
- uncertainty calibration
- evidence fusion
- contradiction benchmarks

Priorität:

1. peer-reviewed Literatur
2. etablierte Benchmarks
3. hochwertige Preprints
4. offizielle technische Dokumentation
5. nachvollziehbare Open-Source-Implementierungen

Speichere Quellen mit vollständiger Provenienz.

Behaupte keine Quelle, die nicht tatsächlich geprüft wurde.


## 35. Qualitäts-Gates

Vor Übergang in ein neues großes Arbeitspaket prüfe:

Daten:
Ist die Ground Truth hinreichend definiert?

Methodik:
Ist der Vergleich fair?

Baselines:
Sind angemessene Einzelverfahren implementiert?

Reproduzierbarkeit:
Sind zentrale Experimente wiederholbar?

Leakage:
Ist das Testset weiterhin geschützt?

Erkenntnis:
Hat die bisherige Phase tatsächlich technische Erkenntnisse erzeugt?

Projektbezug:
Entspricht die nächste Phase weiterhin dem verbindlichen
HyConCheck-Forschungsgegenstand?

Wenn ein Gate nicht erfüllt ist, behebe oder dokumentiere das Problem,
bevor die nächste Phase als abgeschlossen gilt.


## 36. Meilensteine

M1:
Widerspruchstaxonomie und formale Entscheidungskriterien operationalisiert.

M2:
Kontrollierter Benchmark und Ground Truth versioniert.

M3:
Regel-, Embedding-, NLI- und gegebenenfalls LLM-Baselines reproduzierbar
evaluiert.

M4:
Entitäts-, Zeit-, Status- und Provenienzrepräsentation implementiert und
experimentell untersucht.

M5:
Mehrere Evidenzgraph- und Fusionsarchitekturen implementiert und gegen
Baselines verglichen.

M6:
Kalibrierung, Fehleranalysen, Ablationsstudien und Robustheitstests
durchgeführt.

M7:
Ausgewählte Architektur auf dem zurückgehaltenen Testset final evaluiert.

Kein Meilenstein setzt voraus, dass HyConCheck eine Baseline übertrifft.


## 37. Definition of Done

Das Projekt ist abgeschlossen, wenn mindestens vorliegen:

Forschung:
- dokumentierter Stand der Technik
- konkretisierte Forschungslücke
- beantwortete Forschungsfragen
- bewertete Hypothesen
- dokumentierte positive und negative Erkenntnisse
- dokumentierte Limitationen

Taxonomie und Daten:
- versionierte Widerspruchstaxonomie
- Annotationsleitfaden
- kontrollierter Benchmark
- dokumentierte Ground Truth
- geschützter Train/Validation/Test-Split

Software:
- reproduzierbare Codebasis
- Testdatengenerator
- Baselines
- Entitäts-/Zeit-/Statusverarbeitung
- Evidenzgraph
- experimentelle Fusionsverfahren
- Evaluationsframework

Experimente:
- Baselinevergleiche
- Architekturvergleiche
- Fehleranalysen
- Ablationsstudien
- Robustheitsstudien
- finale Evaluation auf zurückgehaltenen Daten

Dokumentation:
- Research Design
- Quellenregister
- Experimentregister
- Entscheidungsprotokoll
- Forschungsjournal
- Ergebnisdokumentation
- Abschlussbericht

Das Projekt gilt NICHT erst dann als erfolgreich, wenn das
Hybridverfahren besser als alle Baselines ist.

Ein methodisch belastbares negatives Ergebnis erfüllt ebenfalls den
Forschungszweck.


## 38. Abschlussfrage

Am Ende muss auf Grundlage reproduzierbarer Experimente beantwortet
werden:

Kann eine Evidenzgraph-basierte Fusions- und Entscheidungslogik
semantische, temporale, statusbezogene und graphbasierte Evidenz in
heterogenen IT-Projektdokumenten so kombinieren, dass Widersprüche
gegenüber Regel-, Embedding-, NLI- und LLM-Einzelverfahren zuverlässiger
und nachvollziehbarer erkannt werden?

Falls nein:

Warum nicht?

Welche Komponenten scheitern?

Unter welchen Bedingungen?

Welche technische Grenze wurde identifiziert?

Auch diese Antwort ist ein gültiges Forschungsergebnis.


## 39. Unmittelbarer Auftrag nach Übernahme dieses Master-Prompts

Führe zunächst KEIN neues Experiment aus.

Dieses Repository wird fachlich und technisch neu aufgebaut. Übernimm keine
Dateien, Commits, Erledigungsstände oder Forschungsergebnisse aus einem
früheren Repository. Das bisherige Repository bleibt unverändert.

Der Neuaufbau wird mit dem tatsächlichen Ausführungsdatum dokumentiert.
Er ändert nicht den offiziellen Projektzeitraum 01.09.2026 bis 31.12.2027.

Behaupte weder, dass frühere Arbeiten nicht stattgefunden hätten, noch,
dass sie in diesem neuen Repository bereits durchgeführt worden seien.

Falls im Zielrepository bereits Dateien vorhanden sind, prüfe sie zunächst.
Lösche oder überschreibe vorhandene Arbeit nicht pauschal.

Führe in diesem ersten Lauf ausschließlich die Einrichtung der
Projektgrundlage durch.

Insbesondere:

1. Lege die erforderliche Projekt- und Verzeichnisstruktur an.

2. Erstelle beziehungsweise vervollständige mindestens:

   - AGENTS.md als kurzen Einstieg mit Verweisen
   - README.md
   - docs/HYCONCHECK_MASTER_PROMPT.md
   - docs/PROJECT_CHARTER.md
   - docs/RESEARCH_DESIGN.md
   - planning/PROJECT_PLAN_2026_2027.md
   - planning/BACKLOG.md
   - status/CURRENT_STATUS.md
   - status/DAILY_LOG.md

3. Speichere den vollständigen Master-Prompt konsistent unter:

   docs/HYCONCHECK_MASTER_PROMPT.md

4. Übernimm die sieben Arbeitspakete und deren Planstunden in die
   Projektplanung, ohne daraus tatsächliche Arbeitsstunden oder einen
   Erledigungsgrad abzuleiten.

5. Kennzeichne noch ausstehende Forschung und methodische Entscheidungen
   als offen. Stelle die behauptete Forschungslücke zunächst als durch
   Literaturrecherche zu überprüfende Annahme dar.

6. Die fünf Taxonomie-Obertypen bleiben die verbindliche oberste Ebene.
   Beginne in diesem Lauf noch nicht mit ihrer fachlichen Operationalisierung
   und markiere keinen Obertyp als abgeschlossen.

7. Falls die Datei HyConCheck_Zeitnachweis.xlsx bereitgestellt ist, prüfe
   ihre Tabellenblätter Tagesplanung und Subaktivitäten. Bewahre die
   Quelldatei unverändert auf, integriere die Angaben ausschließlich als
   Forecast und erstelle eine maschinenlesbare Planungsübersicht.

8. Falls diese Datei fehlt, dokumentiere dies als offene Planungsgrundlage.

9. Baue den initialen Backlog anhand der fachlichen Abhängigkeiten auf.

10. Verankere einen wöchentlichen Soll-Ist-Abgleich der geplanten Artefakte
    und Arbeitspakettermine sowie eine monatliche Aktualisierung der
    Abschlussprognose. Dokumentiere Terminrisiken und konkrete
    Gegenmaßnahmen.

11. Verankere in status/DAILY_LOG.md für jede tatsächlich ausgeführte
    Etappe mindestens:

    - tatsächliches Datum
    - Arbeitspaket
    - Fragestellung beziehungsweise Ziel
    - tatsächlich ausgeführte Tätigkeit
    - entstandenes oder geändertes Artefakt mit Dateipfad
    - Ergebnis und Prüfungen
    - Einschränkungen und Fehlschläge
    - Entscheidung und nächster Schritt
    - verfügbare Commit-/PR-Referenz

    Mehrere Etappen desselben Tages erhalten getrennte Einträge.
    Erfinde keine Tätigkeiten, Ergebnisse, Quellen oder Arbeitsstunden.
    Kennzeichne automatisiert ausgeführte Tätigkeiten zutreffend.

12. Stelle sicher, dass Repository-Inhalte und Git-Metadaten werkzeugneutral
    formuliert sind. Verwendete Entwicklungswerkzeuge oder Anbieter dürfen
    nicht in Branch-Namen, Commit-Messages, Commit-Trailern,
    Pull-Request-Titeln, Pull-Request-Beschreibungen oder operativen
    Repository-Anweisungen attribuiert werden. Verwende ausschließlich
    sachliche und projektbezogene Bezeichnungen. Fachlich notwendige Begriffe
    wie KI, Machine Learning, LLM, NLI oder Embeddings bleiben davon
    unberührt.

13. Prüfe alle neu erstellten Dokumente auf Konsistenz, vollständige interne
    Verweise, korrekten Projektzeitraum, korrekte Arbeitspaketbezeichnungen,
    korrekte Planstunden und werkzeugneutrale Formulierungen.

14. Führe git diff --check aus.

15. Falls bereits ausführbarer Python-Code und passende Werkzeuge vorhanden
    sind, führe zusätzlich python -m pytest und ruff check . aus. Andernfalls
    dokumentiere, dass diese Prüfungen noch nicht anwendbar sind. Erzeuge
    keine Scheintests zur Bestätigung reiner Planungsdokumente.

16. Beginne in diesem Lauf keine Experimente.

17. Erstelle einen sachlich benannten Commit.

18. Bereite einen sachlich benannten Pull Request vor, führe ihn aber nicht
    automatisch zusammen.

Berichte anschließend:

- erstellte Dateien
- wesentliche eingerichtete Projektgrundlagen
- Prüfungen und Testergebnisse
- offene Planungsgrundlagen
- offene methodische Punkte
- Terminrisiken und Gegenmaßnahmen
- Commit
- vorbereiteten Pull Request
- nächste fachlich sinnvolle Projektetappe

Die nächste fachliche AP1-Etappe nach erfolgreicher Einrichtung soll die
Definition des Rechercheprotokolls und der Suchstrategie für den Stand der
Technik sein.
