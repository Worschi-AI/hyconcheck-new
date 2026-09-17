# HyConCheck

**Hybrides Verfahren zur Erkennung semantischer, temporaler und statusbezogener Widersprüche in heterogenen IT-Dokumenten**

Technischer Neuaufbau der Projektgrundlage. Maßgebliche fachliche Quelle ist der vollständige Forschungsauftrag in [docs/HYCONCHECK_MASTER_PROMPT.md](docs/HYCONCHECK_MASTER_PROMPT.md).

| Eckdaten | |
|---|---|
| Projektzeitraum | 01.09.2026 – 31.12.2027 |
| Planungsvolumen | 2.560 Planstunden (2026: 640 h, 2027: 1.920 h) – Planwerte des Forschungsantrags |
| Arbeitspakete | AP1 – AP7 nach Master-Prompt §25, siehe [Projektplan](planning/PROJECT_PLAN_2026_2027.md) |
| Aktueller Stand | [status/CURRENT_STATUS.md](status/CURRENT_STATUS.md) |
| Nächste fachliche Etappe | BL-001 – Definition des Rechercheprotokolls und der Suchstrategie für den Stand der Technik (AP1) |

## Forschungsziel und Kernumfang

Ziel ist die Entwicklung und experimentelle Validierung eines hybriden Verfahrens zur automatisierten Erkennung semantischer, temporaler und statusbezogener Widersprüche über heterogene IT-Projektdokumente hinweg (Master-Prompt §3).

Der Kernumfang umfasst insbesondere:

- Anforderungen und Spezifikationen
- Besprechungsprotokolle
- Statusberichte
- Projektpläne und Meilensteinübersichten
- Tickets einschließlich Statusinformationen

Andere Dokumenttypen dürfen später ausschließlich als klar gekennzeichnete explorative Robustheitsfälle untersucht werden; sie verändern den Kernumfang nicht.

## Zentrale Forschungsfrage

Kann eine Evidenzgraph-basierte hybride Fusions- und Entscheidungslogik semantische Modellsignale mit Entitäts-, Zeit-, Status- und Provenienzinformation so koppeln, dass dokumentübergreifende Widersprüche zuverlässiger erkannt werden als mit Regel-, Embedding-, NLI- und LLM-Einzelverfahren? (Master-Prompt §6)

Teilforschungsfragen F1–F6, Ausgangshypothesen H1–H7 (Status: ungeprüft), Benchmark, Testset-Schutz, Baselines B0–B4, Entwicklungsstufen A–G, Metriken, Risiken und Experimentregeln: [docs/RESEARCH_DESIGN.md](docs/RESEARCH_DESIGN.md).

Die im Master-Prompt §4 formulierte Wissenslücke wird in diesem Repository als **durch Literaturrecherche zu überprüfende Annahme** behandelt.

## Taxonomie – fünf verbindliche Obertypen

1. Fakt und Wert
2. Zeit und Status
3. Modalität und Norm
4. Akteur und Verantwortung
5. Abhängigkeit und Schnittstelle

Die Operationalisierung beginnt in diesem Repository neu (AP1); kein Obertyp ist abgeschlossen. Siehe [docs/TAXONOMY_V1.md](docs/TAXONOMY_V1.md).

## Neuaufbau ohne Übernahme

Dieses Repository übernimmt keine Dateien, Commits, Erledigungsstände oder Forschungsergebnisse aus früheren Repositorys. Fachlich zum Vorhaben gehörende Arbeiten, die seit September 2026 außerhalb dieses Repositorys stattgefunden haben, liegen innerhalb des offiziellen Projektzeitraums, gelten hier aber nicht als durchgeführt oder abgeschlossen. Siehe [ADR-0001](docs/decisions/ADR-0001-neuaufbau-ohne-uebernahme.md) und [ADR-0002](docs/decisions/ADR-0002-master-prompt-als-massgebliche-quelle.md).

## Repository-Struktur

```
AGENTS.md                      Kurzer Einstieg mit Verweisen auf die verbindlichen Dokumente
README.md                      Diese Übersicht
configs/                       Konfigurationen für Pipelines, Baselines, Experimente
data/                          Benchmark, Ground Truth, Splits – noch leer
docs/                          Fachliche Grundlagendokumente
  HYCONCHECK_MASTER_PROMPT.md  Vollständiger verbindlicher Forschungsauftrag (§0–§39)
  PROJECT_CHARTER.md           Projektauftrag
  RESEARCH_DESIGN.md           Forschungsdesign (Forschungsproblem, Forschungsfragen, H1–H7, Benchmark, Baselines, Metriken, Experimentregeln)
  TAXONOMY_V1.md               Widerspruchstaxonomie V1 (Rahmen; Operationalisierung offen)
  decisions/                   Entscheidungsprotokoll (ADR)
experiments/                   Experimentregister und -protokolle (EXP-YYYY-NNNN) – noch leer
planning/                      Projektplan, Backlog, forecast/ (Forecast-Artefakte aus der Planungsquelle)
references/                    Quellenregister – noch leer
results/                       Rohresultate und Kennzahlen – noch leer
src/                           Quellcode – noch leer
status/                        Aktueller Stand, Forschungsjournal (Tageslog)
tests/                         Tests und Qualitätsprüfungen
```

## Qualitätsprüfungen

```bash
py tests/check_repo_conventions.py
```

```bash
git diff --check
```

`python -m pytest` und `ruff check .` sind nach Master-Prompt §31 bei Codeänderungen verbindlich. Derzeit enthält das Repository keinen ausführbaren Projektcode in `src/`; beide Prüfungen sind daher noch nicht anwendbar (siehe [tests/README.md](tests/README.md)). Es werden keine Scheintests für Planungsdokumente erzeugt.

## Planstunden und Forecast

Alle Stundenangaben sind Planwerte des Forschungsantrags. Daraus werden keine tatsächlich geleisteten Personenstunden abgeleitet; es werden keine Stundenzettel erzeugt. Die bereitgestellte Planungsquelle ist als Forecast integriert ([planning/forecast/](planning/forecast/README.md); Projektplan Abschnitt 2a): Forecast gemäß bereitgestellter Planungsquelle, keine Ist-Aussage – keine Ist-Stunden, keine Erledigungsgrade, vergangene Plantermine bedeuten keine Erledigung.
