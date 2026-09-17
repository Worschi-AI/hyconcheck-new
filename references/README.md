# references/

Quellenregister und Rechercheartefakte für den Stand der Technik nach Master-Prompt §34.

| Datei | Inhalt | Stand 17.09.2026 |
|---|---|---|
| [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md) | Verbindliches Rechercheprotokoll und Suchstrategie (BL-001): Ziele, Themencluster A–P, Suchsysteme, Suchstrings, Zeitraum, Sprache, Ein-/Ausschluss, Screening, Dubletten, Provenienz, Extraktion, Qualitätsbewertung, Bias-Schutz, Stopkriterium, Snowballing | Version 1.1 (Statuswert `abstract-only` ergänzt) |
| [LITERATURE_SEARCH_LOG.md](LITERATURE_SEARCH_LOG.md) | Suchprotokoll je Suchlauf (Protokoll Abschnitt 19) | 41 Einträge (RUN-0001–RUN-0041) aus BL-002.1 |
| [SOURCES.md](SOURCES.md) | Quellenregister mit Provenienz (Protokoll Abschnitt 12) | 52 Einträge (47 aufgenommen: 35 nach Volltextprüfung, 12 `abstract-only`; 5 ausgeschlossen) aus BL-002.1 |
| [LITERATURE_MATRIX.csv](LITERATURE_MATRIX.csv) | Extraktions- und Bewertungsmatrix aufgenommener Quellen (Protokoll Abschnitte 13, 14) | 47 Zeilen |
| [reviews/REVIEW_A_E_CONTRADICTION_NLI.md](reviews/REVIEW_A_E_CONTRADICTION_NLI.md) | Zwischenauswertung Cluster A–E (BL-002.1) – vorläufig | Erstfassung |

## Stand der Recherche (BL-002)

| Tranche | Cluster | Status |
|---|---|---|
| BL-002.1 | A Contradiction Detection, B NLI, C Document-level NLI, D Cross-document Contradiction Detection, E Semantic Consistency Checking | abgeschlossen (17.09.2026) |
| BL-002.2 | F Entity Resolution, G Temporal Reasoning, H Temporal Knowledge Graphs, I Status / State Transition Modeling | offen – nächste Recherchetranche |
| BL-002.3 | J Fact Verification, K Evidence Graphs, L Knowledge Graph Reasoning, M Neuro-symbolic AI | offen |
| BL-002.4 | N Uncertainty Calibration, O Evidence Fusion, P Contradiction Benchmarks | offen |
| BL-002.5 | Snowballing (backward/forward) und Sättigungsprüfung nach Protokoll Abschnitt 17 | offen |

BL-002 insgesamt ist **nicht** abgeschlossen; der Stand der Technik ist **nicht** bewertet (BL-003); die Forschungslücke bleibt eine zu überprüfende Annahme (BL-004); H1–H7 bleiben ungeprüft.

## Regeln

- **Themen (§34):** contradiction detection, Natural Language Inference, document-level NLI, cross-document contradiction detection, semantic consistency checking, entity resolution, temporal reasoning, temporal knowledge graphs, status/state transition modeling, fact verification, evidence graphs, knowledge graph reasoning, neuro-symbolic AI, uncertainty calibration, evidence fusion, contradiction benchmarks – als Cluster A–P im Protokoll verankert.
- **Priorität (§34):** 1. peer-reviewed Literatur, 2. etablierte Benchmarks, 3. hochwertige Preprints, 4. offizielle technische Dokumentation, 5. nachvollziehbare Open-Source-Implementierungen.
- Quellen werden mit vollständiger Provenienz gespeichert (Protokoll Abschnitt 12). Nur tatsächlich geprüfte Quellen werden erfasst; keine Quelle wird behauptet, die nicht geprüft wurde (§23, §34). Quellen ohne zugänglichen Volltext tragen `screening_status = abstract-only`: bibliografisch verifiziert, Abstract geprüft, Volltext nicht geprüft, Aufnahme entsprechend eingeschränkt, Nachbeschaffung in BL-002.5 (Protokoll Abschnitt 10).
- Volltexte werden nicht im Repository abgelegt; keine personenbezogenen oder vertraulichen Projektdaten in Suchanfragen (Protokoll Abschnitt 21).
- Frühere Arbeiten zu HyConCheck außerhalb dieses Repositorys werden hier – falls erwähnt – ausschließlich als externe Quellen mit Herkunftskennzeichnung behandelt (ADR-0001, ADR-0002).
