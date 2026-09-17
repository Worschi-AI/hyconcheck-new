# AGENTS.md – Einstieg für alle Mitwirkenden und Werkzeuge

Maßgebliche fachliche Quelle ist der vollständige Forschungsauftrag [docs/HYCONCHECK_MASTER_PROMPT.md](docs/HYCONCHECK_MASTER_PROMPT.md) (§0–§39). Bei Widersprüchen zwischen älteren Projektunterlagen und dem Master-Prompt hat dessen Abschnitt „Verbindlicher Projektkern“ (§2) Vorrang. Dieses Dokument bleibt bewusst kurz und verweist auf die verbindlichen Detaildokumente.

## Vor jeder Etappe lesen (Master-Prompt §1, §30)

1. `AGENTS.md`
2. [docs/PROJECT_CHARTER.md](docs/PROJECT_CHARTER.md)
3. [docs/RESEARCH_DESIGN.md](docs/RESEARCH_DESIGN.md)
4. [status/CURRENT_STATUS.md](status/CURRENT_STATUS.md)
5. [planning/BACKLOG.md](planning/BACKLOG.md)
6. relevante aktuelle Artefakte

Verbindlicher Gesamtplan: [planning/PROJECT_PLAN_2026_2027.md](planning/PROJECT_PLAN_2026_2027.md) (§0).

## Kernregeln (Kurzfassung, Details im Master-Prompt)

- **Neuaufbau (§0, §2, §39):** keine Übernahme von Dateien, Commits, Erledigungsständen oder Ergebnissen aus früheren Repositorys; keine Git-Historie umschreiben, keine Rückdatierung, keine Vermischung von Historien; Arbeiten außerhalb dieses Repositorys weder leugnen noch als hier durchgeführt darstellen. Siehe [ADR-0001](docs/decisions/ADR-0001-neuaufbau-ohne-uebernahme.md), [ADR-0002](docs/decisions/ADR-0002-master-prompt-als-massgebliche-quelle.md).
- **Projektzeitraum:** 01.09.2026 – 31.12.2027 (§2).
- **Werkzeugneutralität (§0, §39.12):** keine Attribution von Entwicklungswerkzeugen oder Anbietern in Dateien, Branch-Namen, Commit-Messages, Commit-Trailern, PR-Titeln oder PR-Beschreibungen. Fachbegriffe wie KI, Machine Learning, LLM, NLI, Embeddings bleiben zulässig.
- **Planstunden (§25):** ausschließlich Planwerte; keine Ist-Stunden ableiten, keine Stundenzettel erzeugen; Werkzeug-/Modell-/Rechnerlaufzeit ist keine menschliche Arbeitszeit; technische Aktivitätsprotokolle und Zeitaufzeichnungen bleiben getrennt.
- **Wissenschaftliche Integrität (§23):** keine erfundenen Ergebnisse, Quellen, Messwerte oder Tätigkeiten; kein Cherry Picking; Testdaten nie zur Optimierung; negative Ergebnisse werden dokumentiert.
- **Testset-Schutz (§11):** gruppierter 60/20/20-Split, eingefrorenes Testset, Testlabels nicht für Entwicklung, Promptoptimierung, Schwellenwertwahl, Modellauswahl oder Fehlerkorrektur.
- **Reproduzierbarkeit (§24):** Commit, Dataset-Version, Konfiguration, Modell-/Promptversion, Seed, Rohresultate, Auswertungscode, Kennzahlen.
- **Ressourcen (§33):** keine kostenpflichtigen APIs oder Dienste ohne ausdrückliche Freigabe; Open-Source-Modelle, kleine Entwicklungsdatensätze, Caching, gestufte Experimente bevorzugen.
- **Secrets (§32):** keine Secrets in Quellcode, Logs, Prompts, Commits oder Datensätzen; keine eigenmächtige Erzeugung von Zugangsdaten oder Authentifizierung.
- **Status (§28, §39.11):** PLANUNG strikt von TATSÄCHLICH DURCHGEFÜHRTER ARBEIT trennen; nichts ohne geprüftes Artefakt als abgeschlossen führen; kein Taxonomie-Obertyp ist derzeit abgeschlossen.

## Arbeitsprozess je Etappe (§30)

Genau eine abgegrenzte Etappe auswählen und tatsächlich durchführen → Tests ausführen → Ergebnisse und Fehlschläge dokumentieren → [status/CURRENT_STATUS.md](status/CURRENT_STATUS.md), [planning/BACKLOG.md](planning/BACKLOG.md) und [status/DAILY_LOG.md](status/DAILY_LOG.md) aktualisieren → sachlich benannten Commit erstellen → Pull Request vorbereiten (nicht automatisch zusammenführen) → nächsten Schritt festhalten. Nicht die leichteste Aufgabe wählen, sondern nach Abhängigkeiten, Erkenntnisgewinn und aktuellem Arbeitspaket priorisieren.

Git-Identität: die lokal konfigurierte (`git config --local user.name` / `user.email`); keine Commit-Trailer.

## Qualitätsprüfungen (§31, §39.15)

```bash
py tests/check_repo_conventions.py
```

```bash
git diff --check
```

Bei Codeänderungen zusätzlich `python -m pytest` und `ruff check .` sowie geeignete fachliche Validierungen. Solange kein ausführbarer Projektcode vorliegt, wird deren Nichtanwendbarkeit in [tests/README.md](tests/README.md) dokumentiert. Fehlgeschlagene Prüfungen werden nicht verschwiegen; keine Scheintests.

## Entscheidungen und Experimente

- Wesentliche Entscheidungen als ADR in [docs/decisions/](docs/decisions/) nach dem Schema in §29 (Vorlage: [ADR-0000-vorlage.md](docs/decisions/ADR-0000-vorlage.md)).
- Experimente nur mit Protokoll `EXP-YYYY-NNNN` in [experiments/](experiments/) nach §18/§19; derzeit werden keine Experimente durchgeführt (§39).
- Daten nach §10–§12 in [data/](data/); Quellen nach §34 in [references/](references/); Ergebnisse nach §24 in [results/](results/).

## Berichtsformat nach einer Etappe (§39)

erstellte/geänderte Dateien · eingerichtete oder geänderte Grundlagen · Prüfungen und Testergebnisse · offene Planungsgrundlagen · offene methodische Punkte · Terminrisiken und Gegenmaßnahmen · Commit · vorbereiteter Pull Request · nächste fachlich sinnvolle Etappe.
