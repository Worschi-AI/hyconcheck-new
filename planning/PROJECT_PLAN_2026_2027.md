# HyConCheck – Projektplan 2026/2027

Stand: 17.09.2026 – verbindlicher Gesamtplan (Master-Prompt §0), angeglichen an [docs/HYCONCHECK_MASTER_PROMPT.md](../docs/HYCONCHECK_MASTER_PROMPT.md) §25, §35, §36, §39.

Projektzeitraum: **01.09.2026 bis 31.12.2027**. Das Projekt hat am 01.09.2026 begonnen.

## 1. Planungsgrundlagen

- Alle Stundenangaben sind **Planwerte des Forschungsantrags** (§25). Daraus werden keine tatsächlich geleisteten Personenstunden, kein Erledigungsgrad und keine Stundenzettel abgeleitet.
- Automatische Laufzeit von Arbeitswerkzeugen, Modellen, Experimenten oder Rechnern ist keine menschliche Arbeitszeit. Technische Aktivitätsprotokolle und menschliche Zeitaufzeichnungen bleiben getrennt.
- Die sieben Arbeitspakete definieren den Forschungsrahmen und verpflichten nicht zu einem bestimmten positiven Ergebnis (§26). Methoden, Architekturen, Varianten, Hypothesen, Experimente und Unteransätze dürfen aufgrund tatsächlicher Ergebnisse geändert werden; größere Änderungen des Forschungsgegenstands werden im Entscheidungsprotokoll dokumentiert.
- **Forecast:** Die bereitgestellte Planungsquelle (`HyConCheck_Zeitnachweis.xlsx`, Quellstand 16.09.2026, SHA-256 `b647994cde8ab4c992865dd8b1c2a8872801646786ff19fafc15952273acf48f`) wurde am 17.09.2026 kontrolliert geprüft und als Forecast integriert (BL-090, siehe [forecast/README.md](forecast/README.md)). Alle Zeitangaben in Abschnitt 2a sind **Forecast gemäß bereitgestellter Planungsquelle, keine Ist-Aussage**. Es liegen keine Ist-Stunden vor; aus dem Forecast werden keine Erledigungsgrade abgeleitet; vergangene Plantermine bedeuten keine Erledigung. Frühere zeitliche Eigenannahmen waren zuvor entfernt worden ([ADR-0002](../docs/decisions/ADR-0002-master-prompt-als-massgebliche-quelle.md)).

## 2. Arbeitspakete und Planstunden (§25)

| AP | Kurzbezeichnung | Inhalt (Wortlaut Forschungsantrag) | Planstunden |
|---|---|---|---:|
| AP1 | Lösungsraum, Taxonomie, formale Kriterien | Technischen Lösungsraum analysieren; Widerspruchstaxonomie und formale Kriterien für semantische, temporale und Statuskonflikte entwickeln. | 200 |
| AP2 | Benchmark, Testdatengenerator, Ground Truth | Benchmarkmethodik und Testdatengenerator entwickeln; positive, negative und schwierige Grenzfälle erzeugen und Ground Truth definieren. | 300 |
| AP3 | Baselines und Evaluationspipeline | Regel-, Embedding-, NLI- und LLM-Baselines implementieren; Evaluationspipeline entwickeln und Verfahren experimentell vergleichen. | 400 |
| AP4 | Entitäts-, Attribut-, Zeit-, Status-, Provenienzverarbeitung | Entitätsauflösung sowie Extraktion und Normalisierung von Attributen, Zeitintervallen, Statuszuständen und Provenienz entwickeln und testen. | 420 |
| AP5 | Evidenzgraph und Fusionsalgorithmen | Evidenzgraph und Fusionsalgorithmen für semantische, temporale und graphbasierte Evidenz entwickeln und Architekturen experimentell vergleichen. | 460 |
| AP6 | Kalibrierung, Ablation, Fehler- und Robustheitsanalysen | Fusionsverfahren kalibrieren und optimieren; Ablations-, Fehler- und Robustheitsanalysen durchführen und alternative Ansätze experimentell testen. | 520 |
| AP7 | Validierung auf zurückgehaltenen Testdaten | Ausgewählte Architektur auf zurückgehaltenen Testdaten validieren; mit Baselines vergleichen und verbleibende technische Fehlermuster analysieren. | 260 |
| **Summe** | | | **2.560** |

Die Kurzbezeichnungen sind aus dem Wortlaut abgeleitete Arbeitsbezeichnungen; maßgeblich ist die Spalte „Inhalt“.

### Jahresscheiben (Planwerte des Forschungsantrags)

| Jahr | Planstunden |
|---|---:|
| 2026 | 640 |
| 2027 | 1.920 |
| Gesamt | 2.560 |

Eine Verteilung der AP-Planstunden auf die Jahre ist im Forschungsantrag nicht auf AP-Ebene vorgegeben; sie stammt ausschließlich aus der Forecast-Quelle (Abschnitt 2a).

## 2a. Forecast: geplante AP-Zeiträume und Jahresverteilung

**Forecast gemäß bereitgestellter Planungsquelle, keine Ist-Aussage.** Quelle: `HyConCheck_Zeitnachweis.xlsx` (Stand 16.09.2026), integriert am 17.09.2026 (BL-090). Maschinenlesbar in [forecast/forecast_daily.csv](forecast/forecast_daily.csv), [forecast/forecast_subactivities.csv](forecast/forecast_subactivities.csv), [forecast/forecast_summary.csv](forecast/forecast_summary.csv).

| AP | Geplanter Zeitraum (Forecast) | Forecast 2026 | Forecast 2027 | Gesamt |
|---|---|---:|---:|---:|
| AP1 | 01.09.2026 – 07.10.2026 | 200 | 0 | 200 |
| AP2 | 08.10.2026 – 03.12.2026 | 300 | 0 | 300 |
| AP3 | 03.12.2026 – 17.02.2027 | 140 | 260 | 400 |
| AP4 | 17.02.2027 – 10.05.2027 | 0 | 420 | 420 |
| AP5 | 11.05.2027 – 04.08.2027 | 0 | 460 | 460 |
| AP6 | 04.08.2027 – 10.11.2027 | 0 | 520 | 520 |
| AP7 | 10.11.2027 – 30.12.2027 | 0 | 260 | 260 |
| **Forecast-Summe** | | **640** | **1.920** | **2.560** |

- Die Überschneidungen an den AP-Wechseltagen 03.12.2026, 17.02.2027, 04.08.2027 und 10.11.2027 sind Halbtagswechsel (4 h + 4 h) und kein Planungsfehler.
- Die Forecast-Summen reproduzieren die Planwerte des Forschungsantrags (§25) exakt.
- Vergangene Plantermine (z. B. AP1-Tage vor dem 17.09.2026) bedeuten keine Erledigung; der fachliche Stand wird ausschließlich nach vorliegenden Artefakten geführt ([status/CURRENT_STATUS.md](../status/CURRENT_STATUS.md)).
- Puffer- und Feiertagszeilen der Quelle (29 Tage) sind Kapazitätsplatzhalter mit 0 Stunden und nicht enthalten.

## 3. Fachliche Abhängigkeiten (abgeleitet aus §25, §11, §14, §35)

| Abhängigkeit | Begründung |
|---|---|
| AP2 setzt die operationalisierte Taxonomie und formale Kriterien aus AP1 voraus. | Ground-Truth-Labels und Widerspruchstypen benötigen Definitionen und Entscheidungstests (§9, §10, §12). |
| AP3 setzt Benchmark, Ground Truth und eingefrorenen Split aus AP2 voraus. | Baselines werden auf Entwicklungs-/Validationsdaten evaluiert; Testset geschützt (§11, §13). |
| AP4 kann nach AP1 beginnen und parallel zu AP3 laufen. | Entitäts-, Zeit-, Status- und Provenienzverarbeitung benötigt Taxonomie und Benchmarkdaten, aber keine Baseline-Ergebnisse. |
| AP5 setzt AP3 (Vergleichsbasis) und AP4 (Graphinhalte) voraus. | Evidenzgraph und Fusion bauen auf extrahierten Entitäten, Zeit-, Status- und Provenienzinformation auf und werden gegen Baselines verglichen (§5, §14 Stufen D–F). |
| AP6 setzt AP5 voraus. | Kalibrierung, Ablationen, Fehler- und Robustheitsanalysen beziehen sich auf die Hybridarchitekturen (§20–§22). |
| AP7 setzt AP6 und das seit AP2 eingefrorene Testset voraus. | Finale Evaluation erst nach Festlegung der Architektur; vorregistrierte Hauptevaluation (§11, §14 Stufe G). |

Die Entwicklungsstufen A–G (§14) sind keine verpflichtende Reihenfolge; die finale Architektur wird nicht vor den Experimenten festgelegt.

## 4. Meilensteine M1–M7 (§36)

| MS | Beschreibung (Wortlaut) | korrespondierendes AP | Status |
|---|---|---|---|
| M1 | Widerspruchstaxonomie und formale Entscheidungskriterien operationalisiert. | AP1 | offen |
| M2 | Kontrollierter Benchmark und Ground Truth versioniert. | AP2 | offen |
| M3 | Regel-, Embedding-, NLI- und gegebenenfalls LLM-Baselines reproduzierbar evaluiert. | AP3 | offen |
| M4 | Entitäts-, Zeit-, Status- und Provenienzrepräsentation implementiert und experimentell untersucht. | AP4 | offen |
| M5 | Mehrere Evidenzgraph- und Fusionsarchitekturen implementiert und gegen Baselines verglichen. | AP5 | offen |
| M6 | Kalibrierung, Fehleranalysen, Ablationsstudien und Robustheitstests durchgeführt. | AP6 | offen |
| M7 | Ausgewählte Architektur auf dem zurückgehaltenen Testset final evaluiert. | AP7 | offen |

Kein Meilenstein setzt voraus, dass HyConCheck eine Baseline übertrifft. Geplante Termine je Meilenstein ergeben sich aus dem Forecast-Ende des korrespondierenden AP (Abschnitt 2a; Forecast, keine Ist-Aussage): M1 07.10.2026, M2 03.12.2026, M3 17.02.2027, M4 10.05.2027, M5 04.08.2027, M6 10.11.2027, M7 30.12.2027.

Repository-Ereignis (kein Meilenstein des Forschungsantrags): Projektgrundlage im Repository eingerichtet am 17.09.2026 (BL-000) und an den vollständigen Master-Prompt angeglichen am 17.09.2026 (BL-000a).

## 5. Qualitäts-Gates vor AP-Übergang (§35)

Vor Übergang in ein neues großes Arbeitspaket sind zu prüfen und im Statusdokument zu dokumentieren:

| Gate | Prüffrage |
|---|---|
| Daten | Ist die Ground Truth hinreichend definiert? |
| Methodik | Ist der Vergleich fair? |
| Baselines | Sind angemessene Einzelverfahren implementiert? |
| Reproduzierbarkeit | Sind zentrale Experimente wiederholbar? |
| Leakage | Ist das Testset weiterhin geschützt? |
| Erkenntnis | Hat die bisherige Phase tatsächlich technische Erkenntnisse erzeugt? |
| Projektbezug | Entspricht die nächste Phase weiterhin dem verbindlichen HyConCheck-Forschungsgegenstand? |

Wenn ein Gate nicht erfüllt ist, wird das Problem behoben oder dokumentiert, bevor die nächste Phase als abgeschlossen gilt.

## 6. Forecast- und Fortschrittskontrolle (§39.10)

- **Wöchentlich:** Soll-Ist-Abgleich der geplanten Artefakte und Arbeitspakettermine (Backlog BL-091). Der Abgleich bezieht sich auf Artefakte und Termine, nicht auf Personenstunden.
- **Monatlich:** Aktualisierung der Abschlussprognose (Backlog BL-092).
- **Terminrisiken und Gegenmaßnahmen:** werden im Abschnitt 7 geführt und bei jedem Abgleich fortgeschrieben.
- Referenz für den Soll-Ist-Abgleich sind die Forecast-Zeiträume und geplanten Artefakte aus Abschnitt 2a bzw. `forecast/`; „Ist“ bezeichnet dabei ausschließlich im Repository vorliegende, geprüfte Artefakte – nie Stunden. Erster Abgleich: noch nicht erfolgt.

## 7. Terminrisiken und Gegenmaßnahmen

| Risiko | Auswirkung | Gegenmaßnahme | Status |
|---|---|---|---|
| Forecast-Start AP1 (01.09.2026) liegt vor der Einrichtung dieses Repositorys (17.09.2026); für die Forecast-Tage 01.–16.09.2026 (88 Planstunden AP1) liegt hier kein Artefakt vor | Rechercheprotokoll (BL-001) und Literaturmatrizen später als im Forecast; Folgetermine AP1/AP2 gefährdet | BL-001 unmittelbar beginnen; beim ersten wöchentlichen Soll-Ist-Abgleich (BL-091) Abweichung gegen Forecast dokumentieren; keine Umdeutung vergangener Plantermine als erledigt | offen |
| AP1 (200 h) umfasst Stand der Technik, Überprüfung der Wissenslücke und Taxonomie-Operationalisierung | Verzögerter Start von AP2 | Rechercheprotokoll mit klaren Ein-/Ausschlusskriterien (BL-001); Taxonomie-Operationalisierung parallel zur Recherche beginnen | offen |
| Ground-Truth-Erstellung durch Einzelperson (§12) | Verzögerung AP2/AP3, begrenzte Annotationsmenge | Testdatengenerator priorisieren; Blind-Reannotation auf festgelegten Anteil begrenzen; Umfang gestuft festlegen | offen |
| B4 (LLM-Baseline) und LLM-Signale abhängig von kostenfreier Verfügbarkeit (§13, §33) | B4 ggf. nicht durchführbar | Open-Source-Modelle bevorzugen; Nichtdurchführbarkeit dokumentieren statt kostenpflichtige Dienste ohne Freigabe zu nutzen | offen |

## 8. Änderungshistorie

| Datum | Änderung |
|---|---|
| 17.09.2026 | Erstfassung (mit angenommenen AP-Bezeichnungen, AP-Zeiträumen, Jahresverteilung je AP und Meilensteinen MS0–MS8) |
| 17.09.2026 | Angleichung an Master-Prompt: AP-Inhalte nach §25, M1–M7 nach §36, Qualitäts-Gates nach §35, Abhängigkeiten korrigiert, unbelegte AP-Zeiträume und Jahresverteilung je AP entfernt, Forecast-Integration als separate Etappe, Fortschrittskontrolle und Terminrisiken nach §39.10 ergänzt (ADR-0002) |
| 17.09.2026 | BL-090: Forecast aus der bereitgestellten Planungsquelle kontrolliert integriert (Abschnitt 2a, `forecast/`); AP-Zeiträume und Jahresverteilung als Forecast, keine Ist-Aussage; Meilensteintermine als Forecast; Terminrisiko zu vergangenen Forecast-Tagen ergänzt |
