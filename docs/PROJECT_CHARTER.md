# HyConCheck – Projektauftrag (Project Charter)

Stand: 17.09.2026 – angeglichen an den vollständigen Forschungsauftrag [HYCONCHECK_MASTER_PROMPT.md](HYCONCHECK_MASTER_PROMPT.md). Bei Abweichungen gilt der Master-Prompt, insbesondere §2 „Verbindlicher Projektkern“.

| | |
|---|---|
| Projekt | HyConCheck |
| Offizieller Projekttitel | „Hybrides Verfahren zur Erkennung semantischer, temporaler und statusbezogener Widersprüche in heterogenen IT-Dokumenten“ |
| Projektzeitraum | 01.09.2026 bis 31.12.2027 |
| Planungsvolumen | 2.560 Planstunden (2026: 640 h, 2027: 1.920 h) – Planwerte des Forschungsantrags |
| Repository | Worschi-AI/Hyconcheck-new (vollständiger Neuaufbau der Projektgrundlage) |

## 1. Rolle und Auftrag (Master-Prompt §1)

Das Forschungs- und Entwicklungsvorhaben wird innerhalb dieses Repositorys technisch und wissenschaftlich durchgeführt – in den Rollen Research Lead, wissenschaftlicher Rechercheur, Machine-Learning Engineer, Softwareentwickler, Data Engineer, Experiment Designer, Data Scientist, statistischer Analyst, QA Engineer, technischer Projektleiter, wissenschaftlicher Autor und Dokumentationsverantwortlicher. Die Aufgabe besteht nicht nur im Formulieren von Vorschlägen, sondern – soweit die Arbeitsumgebung dies ermöglicht – in der tatsächlichen Durchführung der Forschungsarbeit (Literatur, Stand der Technik, Operationalisierung, Datenschemata, Implementierung, Experimente, Auswertung, Fehleranalyse, Tests, Versionierung, Dokumentation, Schlussfolgerungen). Rückfragen nur, wenn eine wesentliche Entscheidung weder aus dem Repository noch methodisch vertretbar selbst getroffen werden kann.

## 2. Verbindlicher Projektkern (§2)

- Das Projekt hat am 01.09.2026 begonnen, nicht erst am 01.01.2027.
- Bereits im September 2026 außerhalb dieses neu aufgebauten Repositorys durchgeführte, fachlich zum Vorhaben gehörende Arbeiten liegen innerhalb des offiziellen Projektzeitraums. Sie werden nicht als in diesem Repository durchgeführt oder abgeschlossen übernommen; werden sie erwähnt, ist transparent zu kennzeichnen, dass sie außerhalb dieses Repositorys stattgefunden haben.
- Keine Git-Historie aus einem früheren Repository übernehmen oder umschreiben, keine alten Commits manipulieren, keine Dokumente rückdatieren, keine historischen Tatsachen erfinden, historische Hinweise mit tatsächlichem Dokumentationsdatum dokumentieren, technische Historien verschiedener Repositorys nicht vermischen.

## 3. Forschungsziel und Kernumfang (§3)

Ziel ist die Entwicklung und experimentelle Validierung eines hybriden Verfahrens zur automatisierten Erkennung semantischer, temporaler und statusbezogener Widersprüche über heterogene IT-Projektdokumente hinweg.

Kernumfang:

- Anforderungen und Spezifikationen
- Besprechungsprotokolle
- Statusberichte
- Projektpläne und Meilensteinübersichten
- Tickets einschließlich Statusinformationen

Andere Dokumenttypen dürfen später ausschließlich als klar gekennzeichnete explorative Robustheitsfälle untersucht werden und verändern den Kernumfang nicht stillschweigend.

## 4. Forschungsproblem, Forschungsfrage, Hypothesen

Forschungsproblem und Wissenslücke (§4), zentrale Forschungsfrage (§6), Teilforschungsfragen F1–F6 (§7) und Ausgangshypothesen H1–H7 (§8) sind vollständig in [RESEARCH_DESIGN.md](RESEARCH_DESIGN.md) übernommen. Die Wissenslücke wird als durch Literaturrecherche zu überprüfende Annahme behandelt (§39.5). H1–H7 sind ungeprüft; sie dürfen bestätigt, widerlegt oder präzisiert werden, und ein negatives Ergebnis ist ein gültiges Forschungsergebnis.

## 5. Zentrale technische Eigenentwicklung (§5)

Der Forschungsgegenstand ist nicht lediglich die Nutzung bestehender LLMs oder NLI-Modelle. Zu entwickeln und experimentell zu untersuchen sind:

- **A. Evidenzrepräsentation** – Evidenzgraph-Struktur über Aussagen, Entitäten, Attribute, Werte, Zeitpunkte/Zeitintervalle, Statuszustände, Dokumentversionen, Provenienz, Dokumente und Fundstellen.
- **B. Temporale und statusbezogene Konsistenz** – Unterscheidung von echtem gleichzeitigem Widerspruch, zulässigem Statuswechsel, zeitlicher Fortschreibung, neuer Dokumentversion, Ergänzung, veralteter Information, fehlendem Kontext, unklarem Fall.
- **C. Hybride Evidenzfusion** – Kombination regelbasierter Evidenz, Embedding-Signalen, NLI-Scores, optionalen LLM-Signalen, Entitätsbeziehungen, temporalen Bedingungen, Statusbedingungen, Graphpfaden, Provenienzinformation; Kalibrierbarkeit probabilistischer und symbolischer Signale.
- **D. Nachvollziehbare Entscheidung** – beteiligte Aussagen, Fundstellen, Dokumente, aufgelöste Entitäten, Zeit-/Statuskontext, Widerspruchstyp, Evidenz, Konfidenzwert, kurze Begründung; keine Chain-of-Thought-Ausgaben als Artefakt.

Details: [RESEARCH_DESIGN.md](RESEARCH_DESIGN.md), Abschnitt 3.

## 6. Widerspruchstaxonomie (§9)

Fünf verbindliche Obertypen: Fakt und Wert; Zeit und Status; Modalität und Norm; Akteur und Verantwortung; Abhängigkeit und Schnittstelle. Zusätzliche Kategorien sind zunächst Untertypen oder Sekundärtags; keine parallele 17-teilige Haupttaxonomie. Operationalisierung beginnt in diesem Repository neu (AP1); kein Obertyp ist abgeschlossen. Siehe [TAXONOMY_V1.md](TAXONOMY_V1.md).

## 7. Arbeitspakete und Planstunden (§25)

| AP | Inhalt (Wortlaut Forschungsantrag) | Planstunden |
|---|---|---:|
| AP1 | Technischen Lösungsraum analysieren; Widerspruchstaxonomie und formale Kriterien für semantische, temporale und Statuskonflikte entwickeln. | 200 |
| AP2 | Benchmarkmethodik und Testdatengenerator entwickeln; positive, negative und schwierige Grenzfälle erzeugen und Ground Truth definieren. | 300 |
| AP3 | Regel-, Embedding-, NLI- und LLM-Baselines implementieren; Evaluationspipeline entwickeln und Verfahren experimentell vergleichen. | 400 |
| AP4 | Entitätsauflösung sowie Extraktion und Normalisierung von Attributen, Zeitintervallen, Statuszuständen und Provenienz entwickeln und testen. | 420 |
| AP5 | Evidenzgraph und Fusionsalgorithmen für semantische, temporale und graphbasierte Evidenz entwickeln und Architekturen experimentell vergleichen. | 460 |
| AP6 | Fusionsverfahren kalibrieren und optimieren; Ablations-, Fehler- und Robustheitsanalysen durchführen und alternative Ansätze experimentell testen. | 520 |
| AP7 | Ausgewählte Architektur auf zurückgehaltenen Testdaten validieren; mit Baselines vergleichen und verbleibende technische Fehlermuster analysieren. | 260 |
| **Gesamt** | | **2.560** |

Jahresscheiben: 2026 = 640 h, 2027 = 1.920 h. Diese Stunden sind Planwerte des Forschungsantrags; daraus werden keine tatsächlich geleisteten Personenstunden, kein Erledigungsgrad und keine Stundenzettel abgeleitet. Die sieben Arbeitspakete definieren den Forschungsrahmen und verpflichten nicht zu einem bestimmten positiven Ergebnis (§26). Zeitliche Lage und Forecast: [planning/PROJECT_PLAN_2026_2027.md](../planning/PROJECT_PLAN_2026_2027.md).

## 8. Meilensteine M1–M7 (§36)

| MS | Beschreibung |
|---|---|
| M1 | Widerspruchstaxonomie und formale Entscheidungskriterien operationalisiert. |
| M2 | Kontrollierter Benchmark und Ground Truth versioniert. |
| M3 | Regel-, Embedding-, NLI- und gegebenenfalls LLM-Baselines reproduzierbar evaluiert. |
| M4 | Entitäts-, Zeit-, Status- und Provenienzrepräsentation implementiert und experimentell untersucht. |
| M5 | Mehrere Evidenzgraph- und Fusionsarchitekturen implementiert und gegen Baselines verglichen. |
| M6 | Kalibrierung, Fehleranalysen, Ablationsstudien und Robustheitstests durchgeführt. |
| M7 | Ausgewählte Architektur auf dem zurückgehaltenen Testset final evaluiert. |

Kein Meilenstein setzt voraus, dass HyConCheck eine Baseline übertrifft. Stand je Meilenstein: [status/CURRENT_STATUS.md](../status/CURRENT_STATUS.md).

## 9. Qualitäts-Gates (§35)

Vor Übergang in ein neues großes Arbeitspaket sind zu prüfen: **Daten** (Ground Truth hinreichend definiert?), **Methodik** (Vergleich fair?), **Baselines** (angemessene Einzelverfahren implementiert?), **Reproduzierbarkeit** (zentrale Experimente wiederholbar?), **Leakage** (Testset weiterhin geschützt?), **Erkenntnis** (hat die Phase tatsächlich technische Erkenntnisse erzeugt?), **Projektbezug** (entspricht die nächste Phase dem verbindlichen Forschungsgegenstand?). Ein nicht erfülltes Gate wird behoben oder dokumentiert, bevor die nächste Phase als abgeschlossen gilt.

## 10. Definition of Done (§37)

Das Projekt ist abgeschlossen, wenn mindestens vorliegen:

- **Forschung:** dokumentierter Stand der Technik; konkretisierte Forschungslücke; beantwortete Forschungsfragen; bewertete Hypothesen; dokumentierte positive und negative Erkenntnisse; dokumentierte Limitationen.
- **Taxonomie und Daten:** versionierte Widerspruchstaxonomie; Annotationsleitfaden; kontrollierter Benchmark; dokumentierte Ground Truth; geschützter Train/Validation/Test-Split.
- **Software:** reproduzierbare Codebasis; Testdatengenerator; Baselines; Entitäts-/Zeit-/Statusverarbeitung; Evidenzgraph; experimentelle Fusionsverfahren; Evaluationsframework.
- **Experimente:** Baselinevergleiche; Architekturvergleiche; Fehleranalysen; Ablationsstudien; Robustheitsstudien; finale Evaluation auf zurückgehaltenen Daten.
- **Dokumentation:** Research Design; Quellenregister; Experimentregister; Entscheidungsprotokoll; Forschungsjournal; Ergebnisdokumentation; Abschlussbericht.

Das Projekt gilt nicht erst dann als erfolgreich, wenn das Hybridverfahren besser als alle Baselines ist. Ein methodisch belastbares negatives Ergebnis erfüllt ebenfalls den Forschungszweck.

## 11. Abschlussfrage (§38)

Am Ende muss auf Grundlage reproduzierbarer Experimente beantwortet werden: Kann eine Evidenzgraph-basierte Fusions- und Entscheidungslogik semantische, temporale, statusbezogene und graphbasierte Evidenz in heterogenen IT-Projektdokumenten so kombinieren, dass Widersprüche gegenüber Regel-, Embedding-, NLI- und LLM-Einzelverfahren zuverlässiger und nachvollziehbarer erkannt werden? Falls nein: Warum nicht? Welche Komponenten scheitern? Unter welchen Bedingungen? Welche technische Grenze wurde identifiziert? Auch diese Antwort ist ein gültiges Forschungsergebnis.

## 12. Technische Risiken (§17) und Terminrisiken

| Risiko | Beschreibung (§17) | Umgang |
|---|---|---|
| Entity Resolution | Falsches Matching kann scheinbare Konflikte erzeugen; zu striktes Matching kann reale Konflikte übersehen. | Untersuchung in AP4; Fehlerklasse „Entity Resolution Failure“; Ablation (§20, §21) |
| Zeitnormalisierung | Relative Zeitangaben, überlappende Gültigkeitsintervalle und fehlende Zeitanker können zulässige Änderungen als Widerspruch erscheinen lassen. | Untersuchung in AP4; Robustheitstests mit relativen Datumsangaben (§22) |
| Fehlerfortpflanzung | Lokale Extraktionsfehler können sich über Graphrelationen fortpflanzen und mehrere falsche Konfliktpfade erzeugen. | Prüfung von H7; Fehlerklasse „Graph Propagation Failure“ |
| Evidenzfusion | Probabilistische NLI-/LLM-Scores und harte Zeit-/Statusbedingungen können möglicherweise nicht stabil auf einer gemeinsamen Entscheidungsskala kalibriert werden. | Prüfung von H6/F6; Kalibrierungsmetriken (§16) in AP6 |
| Hybridverfahren | Das Hybridverfahren kann schlechter sein als einzelne Baselines. | Ursache untersuchen; Zielmetrik, Ground Truth und Testaufteilung nicht nachträglich verändern |

Terminrisiken und konkrete Gegenmaßnahmen werden nach §39.10 im [Projektplan](../planning/PROJECT_PLAN_2026_2027.md) geführt und wöchentlich (Soll-Ist-Abgleich) bzw. monatlich (Abschlussprognose) fortgeschrieben.

## 13. Verbindliche Regeln

Wissenschaftliche Integrität (§23), Reproduzierbarkeit (§24), Testset-Schutz (§11), Ground Truth (§12), Ressourcen (§33), Umgang mit der Arbeitsumgebung und Secrets (§32), Werkzeugneutralität (§0, §39.12), Repository als System of Record (§27), Forschungsjournal (§28), Entscheidungsprotokoll (§29), Tagesarbeitsprozess (§30), Qualitätsprüfungen (§31). Kurzfassung in [AGENTS.md](../AGENTS.md); Wortlaut im Master-Prompt.

## 14. Nicht-Ziele

- Kein Produktivsystem, keine Produktentwicklung.
- Keine Übernahme oder Weiterführung früherer Repositorys, Ergebnisse oder Erledigungsstände.
- Keine stillschweigende Änderung des Forschungsgegenstands oder Kernumfangs (§3, §26); größere Abweichungen nur dokumentiert im Entscheidungsprotokoll.
- Kein vorausgesetzter Hybridvorteil und keine Verpflichtung zu einem positiven Ergebnis (§23, §26, §36, §37).
