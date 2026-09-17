# data/

Benchmark, Ground Truth und Splits nach Master-Prompt §10–§12. Derzeit leer; Aufbau in AP2 (BL-020 ff.).

## Regeln

- **Pflichtfelder je Fall (§10):** eindeutige ID, Szenario-ID, Dokument-ID, Dokumenttyp, Version, Zeitkontext, Text/Aussage, Fundstelle, beteiligte Entitäten, Ground-Truth-Label, Widerspruchstyp, Begründung, Schwierigkeitsgrad, Provenienz des Beispiels.
- **Fallarten (§10):** positive Widerspruchsfälle, negative Fälle, schwierige Gegenbeispiele, Versionsfortschreibungen, Statusänderungen, temporale Grenzfälle, Entitätsmehrdeutigkeiten, dokumentübergreifende Konflikte, unklare Fälle.
- **Synthetisch vs. real:** Synthetische Daten sind eindeutig als synthetisch gekennzeichnet. Anonymisierte reale Beispiele nur, wenn zulässig, hinreichend anonymisiert und getrennt dokumentiert. Beide Klassen bleiben in Auswertungen getrennt ausweisbar.
- **Split (§11):** gruppierter Train/Validation/Test-Split 60/20/20; Varianten desselben Szenarios nie über Splits verteilt; Testsplit eingefroren; Testlabels nicht für Methodenentwicklung, Promptoptimierung, Schwellenwertwahl, Modellauswahl oder Fehlerkorrektur.
- **Ground Truth (§12):** keine Anpassung nach Kenntnis von Modellresultaten; Annotationsregeln, Leitfadenänderungen, schwierige/unklare Fälle, Begründungen und Taxonomie-Version dokumentieren; zeitlich getrennte Blind-Reannotation für einen festgelegten Anteil.
- **Labels (§9):** Widerspruch / kein Widerspruch / unklar; Fortschreibung, fehlender Kontext, Versionswechsel, Mehrdeutigkeit als Sekundärtags.
- Rohdaten und Caches (`data/raw/`, `data/cache/`) werden nicht versioniert; Schemata, Annotationen, Splits und Versionsstände werden versioniert.
- Keine Übernahme von Daten oder Annotationen aus früheren Repositorys (ADR-0001). Keine Secrets, keine personenbezogenen Daten ohne Anonymisierung.
