# HyConCheck – Projektplan 2026/2027

Stand: 17.09.2026 – Erstfassung zur Projekteinrichtung.

Projektzeitraum: **01.09.2026 – 31.12.2027** (16 Monate).

## 1. Planungsgrundlagen

- Alle Stundenangaben sind **Planwerte**. Sie sind keine Aussage über tatsächlich geleistete Personenstunden und werden nicht als solche fortgeschrieben.
- Vorgegeben sind die Planstunden je Arbeitspaket (AP1–AP7) sowie die Jahresscheiben 2026 = 640 h und 2027 = 1.920 h (Gesamt 2.560 h).
- Die Verteilung der AP-Planstunden auf die Jahre und die zeitliche Lage der Arbeitspakete (Abschnitte 2 und 3) sind **Planungsannahmen** dieses Dokuments und können durch ADR angepasst werden.
- **Offene Planungsgrundlage:** Die Datei `HyConCheck_Zeitnachweis.xlsx` liegt im Repository nicht vor (geprüft am 17.09.2026). Ein Abgleich von Plan- und Ist-Stunden ist daher nicht möglich; Ist-Stunden werden in diesem Repository nicht geschätzt oder konstruiert. Sobald ein Zeitnachweis vorliegt, wird seine Ablage und Auswertung als ADR festgelegt.

## 2. Arbeitspakete und Planstunden

| AP | Bezeichnung | Geplanter Zeitraum | Plan 2026 | Plan 2027 | Gesamt |
|---|---|---|---:|---:|---:|
| AP1 | Stand der Technik und Forschungsdesign | 09/2026 – 10/2026 | 200 | 0 | 200 |
| AP2 | Taxonomie und Annotationsrichtlinie | 10/2026 – 12/2026 | 300 | 0 | 300 |
| AP3 | Benchmark und Ground Truth | 12/2026 – 03/2027 | 140 | 260 | 400 |
| AP4 | Baselines und Einzelverfahren | 02/2027 – 05/2027 | 0 | 420 | 420 |
| AP5 | Evidenzgraph und Fusion | 04/2027 – 08/2027 | 0 | 460 | 460 |
| AP6 | Integrierte Architektur und Evaluation | 07/2027 – 11/2027 | 0 | 520 | 520 |
| AP7 | Dissemination, Dokumentation und Abschluss | 10/2027 – 12/2027 (Dokumentation laufend) | 0 | 260 | 260 |
| **Summe** | | | **640** | **1.920** | **2.560** |

Kontrollsummen: 2026 = 640 h, 2027 = 1.920 h, Gesamt = 2.560 h.

## 3. Arbeitspakete im Einzelnen

### AP1 – Stand der Technik und Forschungsdesign (200 h)

- Rechercheprotokoll und Suchstrategie (BL-001)
- Systematische Erhebung und Bewertung des Stands der Technik
- Formulierung der Forschungslücke
- Formulierung der Hypothesen H1–H7 mit Metriken und Kriterien
- Ergebnis: D1

### AP2 – Taxonomie und Annotationsrichtlinie (300 h)

- Operationalisierung der fünf Obertypen (Definitionen, Abgrenzungen, Untertypen)
- Annotationsrichtlinie mit Entscheidungsregeln und Beispielen
- Pilotannotation und Übereinstimmungsmessung
- Ergebnis: D2

### AP3 – Benchmark und Ground Truth (400 h)

- Datenquellen, Lizenz, Aufbereitung
- Annotation, Adjudikation, Qualitätskennzahlen
- Versionierter Benchmark mit Aufteilung
- Ergebnis: D3

### AP4 – Baselines und Einzelverfahren (420 h)

- Einheitliche Schnittstelle für Verfahren
- Baselines je Verfahrensfamilie (regelbasiert, Embedding, NLI, LLM)
- Auswertung je Obertyp
- Ergebnis: D4

### AP5 – Evidenzgraph und Fusion (460 h)

- Modell des Evidenzgraphen (Schema, Herkunft, Konfidenzen)
- Fusionsverfahren und Kalibrierung
- Vergleich gegen Baselines
- Ergebnis: D5

### AP6 – Integrierte Architektur und Evaluation (520 h)

- Integration der Bausteine zur Prototyp-Architektur
- Gesamtevaluation und Fehleranalyse
- Prüfung von H1–H7
- Ergebnis: D6

### AP7 – Dissemination, Dokumentation und Abschluss (260 h)

- Abschlussdokumentation und Reproduzierbarkeitspaket
- Publikationen/Vorträge
- Projektabschluss
- Ergebnis: D7

## 4. Meilensteine (Planungsannahmen)

| MS | Beschreibung | Geplant | Status |
|---|---|---|---|
| MS0 | Projektgrundlage im Repository eingerichtet | 09/2026 | erreicht (17.09.2026) |
| MS1 | Rechercheprotokoll liegt vor (BL-001) | 09/2026 | offen |
| MS2 | Forschungslücke und H1–H7 formuliert (AP1 abgeschlossen) | 10/2026 | offen |
| MS3 | Taxonomie V1 operationalisiert, Annotationsrichtlinie pilotiert (AP2 abgeschlossen) | 12/2026 | offen |
| MS4 | Benchmark V1 mit Ground Truth (AP3 abgeschlossen) | 03/2027 | offen |
| MS5 | Baselines ausgewertet (AP4 abgeschlossen) | 05/2027 | offen |
| MS6 | Evidenzgraph und Fusion evaluiert (AP5 abgeschlossen) | 08/2027 | offen |
| MS7 | Integrierte Architektur evaluiert, Hypothesen geprüft (AP6 abgeschlossen) | 11/2027 | offen |
| MS8 | Projektabschluss (AP7 abgeschlossen) | 12/2027 | offen |

## 5. Abhängigkeiten

- AP2 baut auf der Forschungslücke aus AP1 auf; die Obertypen sind bereits gesetzt, sodass AP2 parallel zu AP1 beginnen kann.
- AP3 setzt eine pilotierte Annotationsrichtlinie (AP2) voraus.
- AP4 setzt eine erste Benchmark-Version (AP3) voraus.
- AP5 setzt Baselines (AP4) als Vergleichsbasis voraus.
- AP6 setzt AP3–AP5 voraus.
- AP7 läuft für Dokumentation begleitend; Abschlussarbeiten nach AP6.

## 6. Änderungshistorie

| Datum | Änderung |
|---|---|
| 17.09.2026 | Erstfassung: Planstunden, Jahresscheiben, zeitliche Lage, Meilensteine, Hinweis auf fehlenden Zeitnachweis |
