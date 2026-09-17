# planning/forecast/ – Forecast aus der bereitgestellten Planungsquelle

Ergebnis der Etappe BL-090 (kontrollierte Forecast-Integration) nach Master-Prompt §25 und §39.7.

## Quelle

| | |
|---|---|
| Quelldateiname | `HyConCheck_Zeitnachweis.xlsx` |
| SHA-256 der unveränderten Quelldatei | `b647994cde8ab4c992865dd8b1c2a8872801646786ff19fafc15952273acf48f` |
| Quellstand | 16.09.2026 |
| Integrationsdatum | 17.09.2026 |
| Geprüfte Tabellenblätter | `Tagesplanung` (386 Datenzeilen), `Subaktivitäten` (66 Datenzeilen) |
| Aufbewahrung | Die Quelldatei bleibt **außerhalb des Repositorys unverändert erhalten**; sie wurde nicht kopiert und nicht verändert. Der SHA-256 wurde vor und nach der Integration geprüft. |
| Technische Eigenschaften der Quelle | keine Formeln, keine externen Verknüpfungen, keine Makros, keine Ist-Spalten; zwei strukturierte Tabellen |

## Verbindliche Einordnung

- **Reine Forecast-Quelle.** Alle Werte sind Planwerte des Forschungsantrags (Master-Prompt §25) auf Tages- und Subaktivitätsebene.
- **Keine Ist-Stunden.** Die Quelle enthält keine Ist-Stunden, und aus ihr werden keine abgeleitet. Es werden keine Stundenzettel erzeugt.
- **Vergangene Termine bedeuten keine Erledigung.** Plantermine, die vor dem jeweiligen Betrachtungsdatum liegen, sind keine Aussage über durchgeführte Arbeit. Ob eine Tätigkeit durchgeführt wurde, ergibt sich ausschließlich aus geprüften Artefakten im Repository (Forschungsjournal, Backlog, Status).
- **Keine AP-Erledigungsgrade aus dem Forecast.** Der fachliche Stand von AP1–AP7, Hypothesen, Forschungsfragen und Taxonomie wird unabhängig vom Forecast nach dem tatsächlichen Forschungsstand geführt.
- Automatische Laufzeiten von Werkzeugen, Modellen oder Rechnern sind keine menschliche Arbeitszeit; technische Aktivitätsprotokolle und menschliche Zeitaufzeichnungen bleiben getrennt.

## Summen (Forecast)

| AP | Planstunden | 2026 | 2027 |
|---|---:|---:|---:|
| AP1 | 200 | 200 | 0 |
| AP2 | 300 | 300 | 0 |
| AP3 | 400 | 140 | 260 |
| AP4 | 420 | 0 | 420 |
| AP5 | 460 | 0 | 460 |
| AP6 | 520 | 0 | 520 |
| AP7 | 260 | 0 | 260 |
| **Gesamt** | **2.560** | **640** | **1.920** |

Die AP-Summen sind in `Tagesplanung` und `Subaktivitäten` identisch und stimmen exakt mit Master-Prompt §25 überein (AP1 200, AP2 300, AP3 400, AP4 420, AP5 460, AP6 520, AP7 260; 2026 = 640, 2027 = 1.920, Gesamt = 2.560).

## Behandlung von Puffer und Feiertagen

- 21 Zeilen `Puffer / kein FuE` und 8 Zeilen `Feiertag` sind reine **Kapazitätsplatzhalter mit 0 Stunden**. Sie tragen keine AP-Zuordnung, kein Artefakt und gehen in keine Summe ein.
- In den Artefakten erhalten sie `category = BUFFER` bzw. `HOLIDAY`; die ursprüngliche Bezeichnung steht in `source_label`.

## Darstellungshinweise

- **37 Kalendertage mit zwei Halbtagszeilen** (je 4 h): Übergänge zwischen Subaktivitäten, an vier Tagen auch zwischen Arbeitspaketen (03.12.2026, 17.02.2027, 04.08.2027, 10.11.2027). Jeder Kalendertag summiert auf 8 h (Arbeitstag) oder 0 h (Puffer/Feiertag). Überschneidungen an AP-Wechseltagen sind Halbtagswechsel und kein Planungsfehler.
- **„(geplante Etappe n/m)“** in `planned_activity_raw` ist reine Darstellungsinformation der Quelle. Bei Halbtagen wird dieselbe Etappennummer mehrfach vergeben; die Kennung wird **nicht** als Fortschritts- oder Zeilenzähler verwendet. Maßgeblich sind die Stundensummen.
- Die AP-Kurztitel der Quelle (`ap_title`) sind Arbeitsbezeichnungen; für die Inhalte der Arbeitspakete ist der Wortlaut in Master-Prompt §25 maßgeblich.

## Personenbezogene Daten

Die Spalte `Name` der Quelle wurde **nicht** übernommen. Die Artefakte enthalten keine Personennamen und keine lokalen Dateipfade.

## Artefakte

| Datei | Inhalt |
|---|---|
| `forecast_daily.csv` | 386 Zeilen aus `Tagesplanung`: `date` (ISO), `weekday`, `iso_week`, `year`, `month`, `work_package` (AP1–AP7, leer bei Puffer/Feiertag), `ap_title`, `planned_activity_raw` (mit Etappenkennung), `subactivity` (ohne Etappenkennung), `planned_artifact`, `planned_hours` (0/4/8), `category` (`AP`/`BUFFER`/`HOLIDAY`), `source_label` |
| `forecast_subactivities.csv` | 66 Zeilen aus `Subaktivitäten`: `work_package`, `ap_title`, `subactivity`, `planned_hours`, `planned_artifact` |
| `forecast_summary.csv` | Aggregationen: `scope` ∈ {`work_package`, `year`, `work_package_year`, `category`, `total`}, `work_package`, `year` (`ALL`, wenn nicht anwendbar), `planned_hours` |
| `build_forecast_csv.py` | Erzeugt die drei CSV-Dateien reproduzierbar aus der Quelldatei (Standardbibliothek, lesend; Pfad nur als Aufrufargument) |

Erzeugung: `py planning/forecast/build_forecast_csv.py <pfad-zur-quelldatei.xlsx>`. Prüfung: `py tests/check_repo_conventions.py` (Zeilenzahlen, Summen, Tagessummen, Konsistenz, keine Namensspalte).

## Geplante AP-Zeiträume (Forecast gemäß bereitgestellter Planungsquelle, keine Ist-Aussage)

| AP | Zeitraum |
|---|---|
| AP1 | 01.09.2026 – 07.10.2026 |
| AP2 | 08.10.2026 – 03.12.2026 |
| AP3 | 03.12.2026 – 17.02.2027 |
| AP4 | 17.02.2027 – 10.05.2027 |
| AP5 | 11.05.2027 – 04.08.2027 |
| AP6 | 04.08.2027 – 10.11.2027 |
| AP7 | 10.11.2027 – 30.12.2027 |

Verbindlicher Gesamtplan: [../PROJECT_PLAN_2026_2027.md](../PROJECT_PLAN_2026_2027.md).
