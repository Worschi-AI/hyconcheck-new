# references/

Quellenregister und Rechercheartefakte für den Stand der Technik nach Master-Prompt §34.

| Datei | Inhalt | Stand 17.09.2026 |
|---|---|---|
| [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md) | Verbindliches Rechercheprotokoll und Suchstrategie (BL-001): Ziele, Themencluster A–P, Suchsysteme, Suchstrings, Zeitraum, Sprache, Ein-/Ausschluss, Screening, Dubletten, Provenienz, Extraktion, Qualitätsbewertung, Bias-Schutz, Stopkriterium, Snowballing | vorhanden (Version 1.0) |
| [LITERATURE_SEARCH_LOG.md](LITERATURE_SEARCH_LOG.md) | Suchprotokoll je Suchlauf (Protokoll Abschnitt 19) | leere Vorlage – keine Suchläufe |
| [SOURCES.md](SOURCES.md) | Quellenregister mit Provenienz (Protokoll Abschnitt 12) | leere Vorlage – keine Quellen |
| [LITERATURE_MATRIX.csv](LITERATURE_MATRIX.csv) | Extraktions- und Bewertungsmatrix aufgenommener Quellen (Protokoll Abschnitte 13, 14) | nur Kopfzeile – keine Daten |

## Regeln

- **Themen (§34):** contradiction detection, Natural Language Inference, document-level NLI, cross-document contradiction detection, semantic consistency checking, entity resolution, temporal reasoning, temporal knowledge graphs, status/state transition modeling, fact verification, evidence graphs, knowledge graph reasoning, neuro-symbolic AI, uncertainty calibration, evidence fusion, contradiction benchmarks – als Cluster A–P im Protokoll verankert.
- **Priorität (§34):** 1. peer-reviewed Literatur, 2. etablierte Benchmarks, 3. hochwertige Preprints, 4. offizielle technische Dokumentation, 5. nachvollziehbare Open-Source-Implementierungen.
- Quellen werden mit vollständiger Provenienz gespeichert (Protokoll Abschnitt 12). Nur tatsächlich geprüfte Quellen werden erfasst; keine Quelle wird behauptet, die nicht geprüft wurde (§23, §34).
- Volltexte werden nicht im Repository abgelegt; keine personenbezogenen oder vertraulichen Projektdaten in Suchanfragen (Protokoll Abschnitt 21).
- Frühere Arbeiten zu HyConCheck außerhalb dieses Repositorys werden hier – falls erwähnt – ausschließlich als externe Quellen mit Herkunftskennzeichnung behandelt (ADR-0001, ADR-0002).

## Nächste Etappe

BL-002 – Recherche gemäß Protokoll durchführen (erst dann werden Suchsysteme tatsächlich abgefragt).
