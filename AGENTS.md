# AGENTS.md – Arbeitsregeln für dieses Repository

Dieses Dokument gilt für alle Mitwirkenden und für alle automatisierten Werkzeuge, die in diesem Repository arbeiten. Es ist zusammen mit [docs/HYCONCHECK_MASTER_PROMPT.md](docs/HYCONCHECK_MASTER_PROMPT.md) vor jeder Arbeitssitzung zu lesen.

## 1. Geltungsbereich und Grundsatz

- Das Repository ist ein **vollständiger technischer Neuaufbau** von HyConCheck. Es werden keine Dateien, Commits, Erledigungsstände oder Forschungsergebnisse aus früheren Repositorys übernommen (siehe [ADR-0001](docs/decisions/ADR-0001-neuaufbau-ohne-uebernahme.md)).
- Es wird ausschließlich in **diesem lokalen Repository** gearbeitet.
- Projektzeitraum: **01.09.2026 – 31.12.2027**.
- Arbeitssprache in Repository-Dateien ist Deutsch; Fachbegriffe, Bezeichner und Code dürfen englisch sein.

## 2. Git-Regeln

- Standard-Arbeitsbranch für die Grundlagenphase: `work/project-foundation`. Neue Branches werden nur auf ausdrückliche Anweisung angelegt.
- Commits werden lokal erstellt. Ein Push oder das Anlegen eines Pull Requests erfolgt **nur auf ausdrückliche Anweisung**.
- Es wird die bereits konfigurierte lokale Git-Identität verwendet (`git config --local user.name` / `user.email`). Sie wird nicht überschrieben.
- Commit-Messages sind knapp, deutsch, im Infinitiv („… einrichten“, „… ergänzen“).
- **Keine Commit-Trailer** wie `Co-authored-by`, `Generated-by`, `Signed-off-by` oder sonstige Werkzeug-/Anbieterattribution.
- Vor jedem Commit: die anwendbaren Qualitätsprüfungen ausführen (Abschnitt 6).

## 3. Unzulässige Inhalte in Repository-Dateien

- Keine operativen Hinweise auf konkrete Entwicklungsassistenten, KI-Werkzeuge oder deren Anbieter (weder im Text noch in Kommentaren, Metadaten oder Commit-Messages).
- Fachlich notwendige Begriffe bleiben zulässig: KI, Machine Learning, LLM, NLI, Embeddings, Transformer usw. – sofern sie den Forschungsgegenstand betreffen.
- Keine fiktiven Stundenzettel, keine erfundenen Ist-Stunden, keine erfundenen Messwerte, Zitate oder Quellen.

## 4. Planstunden

- Alle Stundenangaben sind **Planwerte** (AP1–AP7, Jahresscheiben 2026/2027). Sie werden nicht als geleistete Personenstunden interpretiert oder fortgeschrieben.
- Ist-Stunden werden ausschließlich aus einem tatsächlich vorliegenden Zeitnachweis übernommen. Liegt `HyConCheck_Zeitnachweis.xlsx` nicht vor, bleibt dies als offene Planungsgrundlage dokumentiert.

## 5. Statusführung

- [status/CURRENT_STATUS.md](status/CURRENT_STATUS.md) beschreibt den aktuellen Gesamtstand und die nächste Etappe. Es wird bei jeder inhaltlichen Änderung aktualisiert.
- [status/DAILY_LOG.md](status/DAILY_LOG.md) erhält je Arbeitstag einen Eintrag (Datum, erledigt, offen, Entscheidungen, nächste Schritte). Einträge werden nicht rückwirkend verändert, nur ergänzt.
- [planning/BACKLOG.md](planning/BACKLOG.md) führt alle Arbeitseinheiten (`BL-nnn`) mit Status `offen`, `in Arbeit`, `blockiert` oder `abgeschlossen`.
- Ein Backlog-Eintrag, ein Arbeitspaket oder ein Taxonomie-Obertyp gilt nur dann als `abgeschlossen`, wenn das Ergebnis im Repository vorliegt und geprüft wurde. Abschlussbehauptungen ohne Artefakt sind unzulässig.
- Kein Taxonomie-Obertyp ist zum jetzigen Zeitpunkt abgeschlossen.

## 6. Qualitätsprüfungen

Vor jedem Commit werden die aktuell anwendbaren Prüfungen ausgeführt; in der Grundlagenphase sind das mindestens:

```bash
py tests/check_repo_conventions.py
```

```bash
git diff --check
```

Kommen Code, Daten oder Experimente hinzu, werden die zugehörigen Tests, Schemaprüfungen und Reproduzierbarkeitsprüfungen ergänzt und in [tests/](tests/) abgelegt.

## 7. Entscheidungen

- Projekt- und Architekturentscheidungen werden als ADR in [docs/decisions/](docs/decisions/) festgehalten (Vorlage: [ADR-0000-vorlage.md](docs/decisions/ADR-0000-vorlage.md)).
- Offene Fragen werden als offen markiert, nicht stillschweigend entschieden.

## 8. Experimente und Daten

- Experimente werden erst durchgeführt, wenn ein Experimentprotokoll in [experiments/](experiments/) vorliegt (Ziel, Hypothesenbezug, Daten, Konfiguration, Metriken, Abbruchkriterien).
- Daten werden nur mit dokumentierter Herkunft und Lizenz abgelegt (siehe [data/README.md](data/README.md)).
- Ergebnisse werden reproduzierbar mit Konfiguration und Versionsstand in [results/](results/) dokumentiert.

## 9. Berichtsformat nach einer Arbeitssitzung

1. geänderte/erstellte Dateien
2. durchgeführte Prüfungen und Ergebnisse
3. Commit-SHA und vollständige Commit-Message (sofern committet)
4. offene Punkte und nächste Etappe
