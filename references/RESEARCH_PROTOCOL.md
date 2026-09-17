# HyConCheck – Rechercheprotokoll und Suchstrategie für den Stand der Technik

| | |
|---|---|
| Etappe | BL-001 (AP1) |
| Version | 1.0 |
| Stand | 17.09.2026 |
| Status | verbindlich für die nachfolgende Literaturrecherche (BL-002) |
| Grundlage | Master-Prompt §4, §6–§8, §23, §34, §39.5 ([docs/HYCONCHECK_MASTER_PROMPT.md](../docs/HYCONCHECK_MASTER_PROMPT.md)); [docs/RESEARCH_DESIGN.md](../docs/RESEARCH_DESIGN.md) |

**Abgrenzung:** Dieses Dokument definiert *wie* recherchiert wird. Es enthält **keine** Rechercheergebnisse, keine Quellen und keine Bewertung des Stands der Technik. In BL-001 wurde keine Literaturdatenbank abgefragt und keine Webrecherche durchgeführt. Die im Master-Prompt §4 formulierte Wissenslücke bleibt eine **zu überprüfende Annahme**; H1–H7 bleiben **ungeprüft**.

---

## 1. Ziel der Literaturrecherche

Die Recherche (BL-002) und ihre Auswertung (BL-003, BL-004) müssen insbesondere klären:

| Nr. | Klärungsziel | Bezug |
|---|---|---|
| Z1 | Stand der Technik zur automatisierten Widerspruchserkennung (Definitionen, Verfahren, Reifegrad) | F1, §3 |
| Z2 | Stand der Technik zur **dokumentübergreifenden** Widerspruchserkennung | F1, F4, H5 |
| Z3 | In welchem Umfang semantische, temporale, statusbezogene und graphbasierte Evidenz **bereits gemeinsam** verarbeitet wird | zentrale Forschungsfrage, §4, §5 |
| Z4 | Welche Rolle Entity Resolution bei der Widerspruchserkennung spielt und welche Fehlerwirkungen beschrieben sind | F2, F5, H2, H7 |
| Z5 | Welche Ansätze für Zeitnormalisierung und temporales Reasoning bestehen (relative Zeitangaben, Intervalle, Gültigkeit) | F2, F5, H3, H7 |
| Z6 | Welche Ansätze Status- und Zustandsübergänge modellieren und von Widersprüchen unterscheiden | F2, H4, §5B |
| Z7 | Welche Evidenzgraph-/Knowledge-Graph-Verfahren für Repräsentation, Kandidatensuche und Schlussfolgern relevant sind | F2, H5, §5A |
| Z8 | Welche hybriden/neuro-symbolischen Ansätze probabilistische Modellsignale mit symbolischen Bedingungen koppeln | F6, H6, §5C |
| Z9 | Welche Verfahren zur Evidenzfusion und Unsicherheitskalibrierung bestehen und wie sie evaluiert werden | F3, F6, H6, §16 |
| Z10 | Welche Benchmarks und Evaluationsmethoden existieren (Taxonomien, Labels, Splits, Metriken, Leakage-Schutz) | F1, §10–§12, §16 |
| Z11 | Ob die im Master-Prompt §4 formulierte Forschungslücke durch die Literatur **gestützt, präzisiert oder widerlegt** wird | §4, §39.5, BL-004 |

Die Recherche liefert Stand der Technik und methodische Grundlagen. Sie bestätigt oder widerlegt **keine** Hypothese; das geschieht ausschließlich durch eigene reproduzierbare Experimente (§8, §23).

## 2. Verbindung zum HyConCheck-Forschungsdesign

| Element des Forschungsdesigns | Beitrag der Recherche | Themencluster (Abschnitt 3) |
|---|---|---|
| Zentrale Forschungsfrage (§6) | Ob und wie Evidenzgraph-basierte Fusion semantischer, Entitäts-, Zeit-, Status- und Provenienzinformation bereits untersucht wurde; welche Einzelverfahren als Vergleichsbasis gelten | A–P |
| F1 Erkennbarkeit der Widerspruchstypen | Bestehende Widerspruchstaxonomien, Labelschemata, gemeldete Erkennungsgüten je Typ | A, C, D, P |
| F2 Beitrag der Komponenten | Ablationsbefunde und Komponentenstudien in der Literatur | F, G, H, I, K, L, O |
| F3 Hybrid vs. Baselines | Publizierte Vergleiche hybrider Systeme gegen Regel-, Embedding-, NLI-, LLM-Verfahren | A, B, D, M, O |
| F4 Systematische Fehler | Fehleranalysen, bekannte Fehlerklassen, schwierige Fälle | A, C, D, P |
| F5 Fehlerfortpflanzung | Studien zu Fehlerketten in Pipelines und Graphen | F, G, K, L |
| F6 Gemeinsame Entscheidungsskala | Kalibrierung, Score-Fusion, symbolisch-probabilistische Kopplung | M, N, O |
| H1–H7 | Nur **Stand der Technik und methodische Grundlagen** je Hypothese (welche Befunde existieren, unter welchen Bedingungen); keine Bewertung der Hypothesen | je Hypothese: H1 A/D/O; H2 F; H3 G/H; H4 I; H5 K/L; H6 N/O; H7 F/G/K |
| AP1 | Technischer Lösungsraum; Grundlage für Taxonomie-Operationalisierung (BL-010 ff.) und formale Kriterien (BL-013) | alle |
| AP2 (Benchmark, Ground Truth) | Benchmark-Designs, Annotationsschemata, Split-/Leakage-Regeln | P, J, C |
| AP3 (Baselines) | Referenzverfahren B0–B4 und ihre übliche Konfiguration | A, B, C, E |
| AP4 (Extraktion/Normalisierung) | Entity Resolution, Zeitnormalisierung, Statusmodellierung, Provenienz | F, G, H, I |
| AP5 (Evidenzgraph, Fusion) | Graphrepräsentationen, Graph-Reasoning, Fusionsverfahren | K, L, M, O |
| AP6 (Kalibrierung, Ablation, Robustheit) | Kalibrierungsmetriken, Ablationsdesigns, Robustheitstests | N, O, P |

Die Zuordnung dient der Vollständigkeitskontrolle: Jedes Element muss nach BL-002/BL-003 mindestens einen dokumentierten Literaturbezug **oder** die dokumentierte Feststellung „keine relevante Literatur gefunden“ erhalten.

## 3. Verbindliche Themencluster

| ID | Themencluster | Kernbegriffe (englisch) | Bezug |
|---|---|---|---|
| A | Contradiction Detection | contradiction detection, contradiction identification, conflicting statements | Z1, F1, H1 |
| B | Natural Language Inference | natural language inference, textual entailment, NLI | Z1, B3 |
| C | Document-level NLI | document-level NLI, long-document inference, multi-sentence entailment | Z1, Z2 |
| D | Cross-document Contradiction Detection | cross-document contradiction, inter-document inconsistency, multi-document conflict | Z2, H5 |
| E | Semantic Consistency Checking | semantic consistency checking, consistency verification, inconsistency detection in documents/requirements | Z1, B1 |
| F | Entity Resolution | entity resolution, entity linking, coreference, record linkage | Z4, H2, H7 |
| G | Temporal Reasoning | temporal reasoning, temporal normalization, temporal expression, temporal relation extraction | Z5, H3 |
| H | Temporal Knowledge Graphs | temporal knowledge graph, time-aware knowledge graph, temporal fact validity | Z5, Z7 |
| I | Status / State Transition Modeling | state transition, status transition, lifecycle modeling, state tracking | Z6, H4 |
| J | Fact Verification | fact verification, fact checking, claim verification, evidence retrieval | Z1, Z10 |
| K | Evidence Graphs | evidence graph, evidence representation, provenance graph, argument/claim graph | Z7, H5 |
| L | Knowledge Graph Reasoning | knowledge graph reasoning, graph-based inference, graph neural network reasoning, path reasoning | Z7, H5 |
| M | Neuro-symbolic AI | neuro-symbolic, neural-symbolic, hybrid symbolic and neural reasoning | Z8, H6 |
| N | Uncertainty Calibration | uncertainty calibration, confidence calibration, expected calibration error, selective prediction | Z9, F6, H6 |
| O | Evidence Fusion | evidence fusion, score fusion, decision fusion, multi-signal combination | Z9, H6 |
| P | Contradiction Benchmarks | contradiction benchmark, NLI benchmark, consistency benchmark, evaluation dataset | Z10 |

Ergänzende Begriffe sind zulässig, wenn sie nachvollziehbar aus einem Cluster abgeleitet und im Suchprotokoll (Abschnitt 19) mit Clusterbezug dokumentiert werden. Neue Cluster werden nur per ADR eingeführt.

## 4. Quellenpriorität und Umgang mit nicht peer-reviewten Quellen

Verbindliche Priorisierung (Master-Prompt §34):

1. peer-reviewed Literatur (Journal- und Konferenzbeiträge mit Begutachtung)
2. etablierte Benchmarks (mit publizierter Beschreibung, öffentlich verfügbaren Daten und dokumentierten Ergebnissen)
3. hochwertige Preprints
4. offizielle technische Dokumentation
5. nachvollziehbare Open-Source-Implementierungen

Regeln für nicht peer-reviewte Quellen (Stufen 3–5):

- Sie werden im Register mit `peer_review_status = nein` geführt und in der Auswertung **getrennt** ausgewiesen.
- Ein Preprint gilt als „hochwertig“, wenn er (a) eine nachvollziehbare Methodik und Evaluation enthält, (b) Code oder Daten verfügbar sind **oder** (c) er von mindestens einer aufgenommenen peer-reviewten Arbeit zitiert wird. Andernfalls: Aufnahme nur als „Hinweis“, nicht als Evidenz.
- Liegt zu einem Preprint eine spätere peer-reviewte Version vor, wird diese bevorzugt (Abschnitt 11).
- Technische Dokumentation und Open-Source-Implementierungen dienen als Belege für Verfügbarkeit, Konfiguration und Reproduzierbarkeit von Verfahren, nicht als Belege für Wirksamkeitsaussagen.
- Aussagen zum Stand der Technik und zur Forschungslücke (BL-003, BL-004) stützen sich primär auf Stufen 1–2; Stufen 3–5 dürfen ergänzen, aber keine Kernaussage allein tragen.

## 5. Recherchequellen / Suchsysteme (geplant; in BL-001 nicht durchsucht)

| ID | Suchsystem | Vorgesehen für | Rolle |
|---|---|---|---|
| S1 | Google Scholar | breite Erstsuche über alle Cluster; Forward Snowballing („cited by“) | Primärsystem (Breite) |
| S2 | Semantic Scholar | Erstsuche mit Zitationsdaten, Forward/Backward Snowballing, Dublettenabgleich über Identifier | Primärsystem (Zitationsnetz) |
| S3 | DBLP | Verifikation bibliografischer Angaben (Venue, Jahr, Peer-Review-Status) für Informatik-Publikationen | Verifikation |
| S4 | ACL Anthology | Cluster A–E, J, P (NLP-Kernvenues); Volltexte | Primärsystem (NLP) |
| S5 | arXiv | Preprints (Stufe 3) aller Cluster; Abgleich mit späteren peer-reviewten Versionen | Ergänzung (Preprints) |
| S6 | IEEE Xplore | Cluster E, F, I, K, L, M (Software-/Systems-Engineering, Requirements, Knowledge Engineering) | Primärsystem (Engineering) |
| S7 | ACM Digital Library | Cluster E, F, K, L, M, N, O (Datenmanagement, Information Retrieval, KI) | Primärsystem (Informatik) |
| S8 | SpringerLink | Cluster H, K, L, M (Knowledge Graphs, Semantic Web, KI-Konferenzen mit Springer-Proceedings) | Ergänzung |
| S9 | ScienceDirect | Cluster E, F, G, I, N, O (Journals zu Information Systems, Expert Systems, Data & Knowledge Engineering) | Ergänzung |

Regeln:

- Jeder Primärstring (Abschnitt 6.1) wird mindestens in S1, S2 und S4 ausgeführt sowie in den dem Cluster zugeordneten Systemen S6–S9.
- Ergänzende Strings (6.2) werden mindestens in S1 und S2 ausgeführt.
- S3 wird für jede aufgenommene Quelle zur Verifikation der bibliografischen Angaben genutzt.
- Je Suchlauf (System × String × Filter) werden die ersten **50 Treffer** in der Standard-Relevanzsortierung des Systems gescreent (Trefferfenster); bei weniger Treffern alle. Weitere Treffer nur, wenn unter den ersten 50 mindestens 10 Aufnahmen auf Stufe 2 liegen (dann nächste 50). Trefferanzahl und gescreente Anzahl werden protokolliert (Abschnitt 19).
- Syntaxunterschiede der Systeme werden im Suchprotokoll dokumentiert (exakt eingegebener String je System).

## 6. Suchstrings

Konventionen: Anführungszeichen = Phrasensuche; `AND` / `OR` in Großbuchstaben; Klammern zur Gruppierung; Trunkierung wird **nicht** verwendet (nicht in allen Systemen gleich); systemabhängige Anpassungen (z. B. fehlende Klammerunterstützung) werden als Varianten mit gleicher ID und Suffix `-v2` protokolliert.

### 6.1 Primärstrings (je Themencluster)

| ID | Cluster | Primärstring |
|---|---|---|
| PS-A | A | `"contradiction detection" AND (document OR "natural language" OR NLP)` |
| PS-B | B | `"natural language inference" AND (contradiction OR inconsistency) AND (document OR "natural language")` |
| PS-C | C | `"document-level natural language inference" OR ("document-level NLI" AND contradiction)` |
| PS-D | D | `"cross-document contradiction detection" OR ("cross-document" AND contradiction AND detection)` |
| PS-E | E | `"semantic consistency checking" AND (document OR requirements OR "natural language")` |
| PS-F | F | `"entity resolution" AND (contradiction OR inconsistency OR "consistency checking") AND (document OR "information extraction")` |
| PS-G | G | `"temporal reasoning" AND ("natural language" OR "information extraction") AND (contradiction OR consistency OR temporal)` |
| PS-H | H | `"temporal knowledge graph" AND (consistency OR contradiction OR validity OR reasoning)` |
| PS-I | I | `"state transition modeling" OR ("state transition" AND (status OR lifecycle) AND ("natural language" OR document OR "information extraction"))` |
| PS-J | J | `"fact verification" AND (evidence OR "knowledge graph") AND (contradiction OR refute)` |
| PS-K | K | `"evidence graph" AND ("natural language" OR document OR provenance OR verification)` |
| PS-L | L | `"knowledge graph reasoning" AND (contradiction OR inconsistency OR consistency OR temporal)` |
| PS-M | M | `"neuro-symbolic" AND ("natural language" OR "knowledge graph" OR reasoning) AND (consistency OR contradiction OR verification)` |
| PS-N | N | `"uncertainty calibration" AND ("natural language inference" OR NLP OR "natural language" OR classifier)` |
| PS-O | O | `"evidence fusion" AND (NLP OR "natural language" OR "knowledge graph" OR "decision fusion")` |
| PS-P | P | `"contradiction benchmark" OR (contradiction AND benchmark AND (NLP OR "natural language" OR evaluation))` |

### 6.2 Ergänzende Suchstrings

| ID | Cluster | Ergänzender Suchstring | Zweck |
|---|---|---|---|
| ES-01 | A, D | `("contradiction detection" OR "inconsistency detection") AND "cross-document"` | dokumentübergreifende Verfahren |
| ES-02 | A, E | `("inconsistency detection" OR "conflict detection") AND (requirements OR specification OR "software documentation")` | technische Dokumente / Requirements |
| ES-03 | A, I | `(contradiction OR inconsistency) AND (status OR "state change" OR "state transition") AND (document OR ticket OR report)` | Statusbezug |
| ES-04 | A, G | `(contradiction OR inconsistency) AND temporal AND ("natural language" OR document)` | temporaler Bezug |
| ES-05 | B, C | `("natural language inference" OR entailment) AND ("long document" OR "document-level" OR "multi-sentence")` | lange Kontexte |
| ES-06 | B, N | `"natural language inference" AND (calibration OR "confidence" OR uncertainty)` | NLI-Konfidenz |
| ES-07 | E, K | `("consistency checking" OR "consistency verification") AND ("knowledge graph" OR graph OR provenance)` | graphbasierte Konsistenz |
| ES-08 | F | `("entity resolution" OR "entity linking" OR coreference) AND ("error propagation" OR "downstream" OR pipeline)` | Fehlerfortpflanzung (H7) |
| ES-09 | F | `("entity resolution" OR "record linkage") AND (documents OR "heterogeneous sources" OR "information extraction")` | heterogene Quellen |
| ES-10 | G | `("temporal normalization" OR "temporal expression" OR "time expression") AND ("information extraction" OR "natural language")` | Zeitnormalisierung |
| ES-11 | G, H | `("temporal relation" OR "temporal interval" OR "validity interval") AND ("knowledge graph" OR extraction OR reasoning)` | Zeitintervalle/Gültigkeit |
| ES-12 | H, L | `("temporal knowledge graph" OR "dynamic knowledge graph") AND (completion OR reasoning OR "fact validity")` | zeitbezogenes Graph-Reasoning |
| ES-13 | I | `("state tracking" OR "status tracking" OR "lifecycle") AND ("natural language" OR "issue tracking" OR "project documents")` | Status in Projektdokumenten |
| ES-14 | J, P | `("fact verification" OR "claim verification") AND (benchmark OR dataset) AND (contradiction OR refuted)` | Verifikations-Benchmarks |
| ES-15 | K, L | `("evidence graph" OR "provenance graph" OR "claim graph") AND (reasoning OR fusion OR verification)` | Evidenzgraph-Reasoning |
| ES-16 | L | `("graph neural network" OR "graph-based") AND (contradiction OR inconsistency OR "consistency checking") AND ("natural language" OR document)` | GNN-basierte Konsistenz |
| ES-17 | M, O | `("neuro-symbolic" OR "neural-symbolic" OR hybrid) AND (rules OR constraints OR "symbolic") AND ("natural language inference" OR "consistency" OR "knowledge graph")` | hybride Kopplung |
| ES-18 | N, O | `(calibration OR "uncertainty") AND ("score fusion" OR "evidence fusion" OR "late fusion" OR "decision fusion")` | kalibrierte Fusion |
| ES-19 | N | `("expected calibration error" OR "Brier score" OR "selective prediction") AND ("natural language" OR NLP OR classifier)` | Kalibrierungsmetriken |
| ES-20 | O, K | `("evidence fusion" OR "multi-source fusion") AND (provenance OR "knowledge graph" OR document)` | Fusion mit Provenienz |
| ES-21 | P | `(NLI OR "natural language inference" OR contradiction) AND (benchmark OR dataset) AND (evaluation OR "test set" OR leakage)` | Benchmarks/Evaluation |
| ES-22 | P, E | `("consistency" OR contradiction) AND benchmark AND (documents OR "software" OR requirements OR "project")` | dokumentbezogene Benchmarks |
| ES-23 | alle | `("large language model" OR LLM) AND (contradiction OR inconsistency) AND (detection OR "consistency checking") AND (document OR "cross-document")` | LLM-basierte Verfahren (B4) |
| ES-24 | alle | `(hybrid OR "combined") AND (contradiction OR inconsistency) AND ("knowledge graph" OR temporal OR status OR provenance) AND ("natural language" OR document)` | Vorwegnahme-Suche (Abschnitt 16) |

Gesamt: 16 Primärstrings, 24 ergänzende Strings. Änderungen an Strings werden versioniert (ID + Suffix) und im Suchprotokoll begründet.

## 7. Veröffentlichungszeitraum

Regel R-Zeit (reproduzierbar anwendbar):

1. **Primärfenster:** Alle Primär- und Ergänzungsstrings werden **ohne unteren Datumsfilter** ausgeführt. Ein oberer Filter existiert nicht (Stand: Recherchedatum).
2. **Gewichtung aktueller Forschung:** Beim Screening werden Treffer ab **2018** (Beginn der breiten Verwendung vortrainierter Transformer-Modelle in NLI und Retrieval) als „aktuell“ markiert (`recency = aktuell`); ältere Treffer als `grundlegend`. Innerhalb des Trefferfensters (Abschnitt 5) werden aktuelle Treffer vollständig gescreent.
3. **Ältere Arbeiten** (vor 2018) werden **nicht** ausgeschlossen. Sie werden aufgenommen, wenn mindestens eines gilt: (a) sie definieren eine Aufgabe, einen Benchmark oder eine Taxonomie, auf die aufgenommene aktuelle Arbeiten Bezug nehmen; (b) sie werden von mindestens zwei aufgenommenen Arbeiten zitiert (Backward Snowballing); (c) sie sind die primäre Quelle eines Verfahrens, das in HyConCheck als Baseline (B0–B4) oder Komponente (AP4/AP5) in Frage kommt.
4. Ein Cutoff, der Grundlagenarbeiten nach 3(a)–(c) entfernen würde, ist unzulässig.
5. Das Recherchedatum jedes Suchlaufs wird protokolliert; spätere Aktualisierungsläufe (z. B. vor AP3, AP5, AP7) verwenden dieselben Strings mit dokumentiertem neuen Datum.

## 8. Sprache

- **Englisch** ist die primäre Wissenschaftssprache; alle Suchstrings sind englisch.
- **Deutschsprachige** Quellen werden nur ergänzend aufgenommen, wenn sie fachlich relevant sind (z. B. Normen, Fachberichte, deutschsprachige Benchmarks zu Projektdokumenten) und keine englischsprachige Entsprechung existiert. Sie werden mit `language = de` geführt; eine deutschsprachige Zusatzsuche ist nur mit dokumentierten Strings (Suffix `-de`) zulässig.
- Andere Sprachen werden nicht systematisch durchsucht; zufällige Treffer werden mit Sprache protokolliert und nur bei englischem Volltext oder verfügbarer Übersetzung geprüft.

## 9. Ein- und Ausschlusskriterien

### 9.1 Einschlusskriterien (alle müssen erfüllt sein, sofern nicht als „oder“ gekennzeichnet)

| ID | Kriterium |
|---|---|
| IN-1 | Fachliche Relevanz für HyConCheck: Beitrag zu mindestens einem Klärungsziel Z1–Z11 |
| IN-2 | Methodische Relevanz: beschreibt ein Verfahren, eine Repräsentation, einen Benchmark, eine Evaluationsmethode oder eine Fehleranalyse |
| IN-3 | Nachvollziehbare Methodik: Vorgehen ist so beschrieben, dass es grundsätzlich reproduzierbar oder zumindest überprüfbar ist |
| IN-4 | Ausreichende technische Beschreibung: Eingaben, Verarbeitung, Ausgaben und – falls empirisch – Daten und Metriken sind angegeben |
| IN-5 | Bezug zu mindestens einem Themencluster A–P |
| IN-6 | Sprache Englisch **oder** Deutsch nach Abschnitt 8 |
| IN-7 | Quellentyp nach Abschnitt 4 (Stufe 1–5) mit ausreichender Provenienz (Abschnitt 12) |

### 9.2 Ausschlusskriterien (eines genügt)

| ID | Kriterium |
|---|---|
| EX-1 | Reiner Meinungsbeitrag ohne Methode oder Daten |
| EX-2 | Marketingtext oder Produktbeschreibung ohne technische Substanz |
| EX-3 | Nicht nachvollziehbare Sekundärdarstellung (z. B. Blogzusammenfassung ohne Primärquelle) |
| EX-4 | Reiner Anwendungsbericht ohne methodische Relevanz |
| EX-5 | Dublette einer bereits erfassten Quelle (Abschnitt 11) |
| EX-6 | Quelle ohne ausreichende Provenienz (kein Titel/Autor/Jahr/Ort nachweisbar) |
| EX-7 | Kein Volltext zugänglich und Abstract reicht für die Beurteilung nach IN-3/IN-4 nicht aus (mit Vermerk `volltext_nicht_verfuegbar`) |
| EX-8 | Thema ohne Bezug zu natürlicher Sprache, Dokumenten, Wissensgraphen oder Evidenzverarbeitung (z. B. rein physikalische Zustandsmodelle) |

Ausschlüsse mit EX-7 werden gesondert gelistet, damit sie bei späterer Verfügbarkeit erneut geprüft werden können.

## 10. Screening-Prozess

| Stufe | Bezeichnung | Grundlage | Entscheidung | Dokumentation |
|---|---|---|---|---|
| 1 | Titel-Screening | Titel (+ Venue, Jahr) | `weiter` / `ausschluss` (nur EX-2, EX-5, EX-8 oder offensichtlich fehlender Clusterbezug) | Zähler je Suchlauf im Suchprotokoll; Ausschlüsse ohne Einzelbegründung zulässig |
| 2 | Abstract-Screening | Abstract, Schlüsselwörter | `weiter` / `ausschluss` mit Kriterium-ID | Eintrag im Quellenregister mit `screening_status = abstract` und Kriterium |
| 3 | Volltextprüfung | Volltext | `aufnahme` / `ausschluss` mit Kriterium-ID **und** Begründung in einem Satz | Eintrag im Quellenregister; Begründung Pflicht |
| 4 | Aufnahme in Literaturbasis | Volltext, Extraktionsschema | Extraktion nach Abschnitt 13; Qualitätsbewertung nach Abschnitt 14; Clusterzuordnung; Bezug zu Z, F, H | Zeile in `LITERATURE_MATRIX.csv`; Eintrag in `SOURCES.md` |

Regeln: Eine Stufe darf nicht übersprungen werden. Bei Unsicherheit wird `weiter` gewählt (konservatives Screening). Alle Entscheidungen der Stufen 2–4 werden mit Datum protokolliert. Ausschlüsse auf Volltextebene (Stufe 3) werden immer mit Kriterium und Begründung dokumentiert.

## 11. Dublettenbehandlung

- **Bevorzugter Identifikator:** DOI. Ohne DOI: normalisierter Titel (Kleinschreibung, ohne Satzzeichen) + Nachname des Erstautors + Jahr; zusätzlich arXiv-ID oder ACL-Anthology-ID, falls vorhanden.
- Dubletten über mehrere Suchsysteme erhalten **eine** Source-ID; alle Suchläufe, in denen die Quelle gefunden wurde, werden im Register unter `search_system` und `search_string` als Liste geführt.
- **Preprint und spätere peer-reviewte Version:** beide Fundstellen werden erfasst, aber unter einer Source-ID zusammengeführt; die **peer-reviewte Version** ist die bevorzugte Version (Zitation, Extraktion). Der Preprint bleibt als `alternate_version` referenziert. Weichen Inhalte wesentlich ab (z. B. andere Ergebnisse), wird dies im Extraktionsfeld „wichtigste Ergebnisse“ vermerkt und die peer-reviewte Fassung als maßgeblich verwendet.
- Erweiterte Journalfassungen einer Konferenzarbeit werden als eigene Quelle geführt, wenn sie substanziell neue Inhalte enthalten; sonst als `alternate_version`.

## 12. Provenienzschema (Quellenregister)

Jede tatsächlich geprüfte Quelle (ab Screening-Stufe 2) erhält im Register mindestens:

| Feld | Bedeutung |
|---|---|
| `source_id` | interne ID `SRC-NNNN`, fortlaufend, nie wiederverwendet |
| `title` | Titel |
| `authors` | Autoren (Nachname, Initialen; vollständige Liste) |
| `year` | Erscheinungsjahr der bevorzugten Version |
| `venue` | Publikation/Venue (Zeitschrift, Konferenz, Repository) |
| `doi` | DOI, falls vorhanden |
| `url` | URL der bevorzugten Version |
| `source_type` | Stufe nach Abschnitt 4: `peer-reviewed` / `benchmark` / `preprint` / `technical-documentation` / `open-source` |
| `peer_review_status` | `ja` / `nein` / `unklar` |
| `search_system` | Suchsystem(e) S1–S9 oder `snowballing-backward` / `snowballing-forward` mit Ausgangs-Source-ID |
| `search_string` | ID(s) der verwendeten Suchstrings |
| `retrieved_on` | Recherche-/Abrufdatum (ISO) |
| `screening_status` | `title` / `abstract` / `fulltext` / `included` |
| `decision` | `aufnahme` / `ausschluss` |
| `decision_criteria` | IN-/EX-Kriterien-IDs |
| `justification` | Begründung (Pflicht ab Stufe 3) |
| `clusters` | zugeordnete Themencluster A–P |
| `language` | `en` / `de` / andere |
| `alternate_version` | DOI/URL der anderen Version (Preprint ↔ peer-reviewed) |
| `recency` | `aktuell` (ab 2018) / `grundlegend` (vor 2018) nach Abschnitt 7 |
| `gap_evidence` | `stuetzend` / `einschraenkend` / `widerlegend` / `neutral` in Bezug auf die Lückenannahme (Abschnitt 16) |

Keine Quelle darf im Register stehen, die nicht tatsächlich geöffnet und auf der angegebenen Stufe geprüft wurde. Vermutete, aus Erinnerung zitierte oder nur in anderen Arbeiten erwähnte Quellen werden nicht eingetragen.

## 13. Extraktionsschema für aufgenommene Literatur

Jede aufgenommene Quelle (Stufe 4) erhält eine Zeile in `LITERATURE_MATRIX.csv` mit folgenden Feldern (Freitext knapp; `n/a`, wenn nicht behandelt; `unklar`, wenn nicht ermittelbar):

| Feld | Inhalt |
|---|---|
| `source_id` | Verweis auf Quellenregister |
| `research_problem` | Forschungsproblem der Arbeit |
| `method` | Verfahren / Methode |
| `dataset_benchmark` | Datensatz / Benchmark (Name, Größe, Verfügbarkeit) |
| `document_type` | Dokumenttyp(en) der Daten |
| `contradiction_definition` | verwendete Widerspruchsdefinition |
| `contradiction_types` | unterstützte Widerspruchstypen (Mapping auf die fünf HyConCheck-Obertypen, sofern möglich; sonst Originalbezeichnung) |
| `entity_resolution` | Rolle/Verfahren der Entity Resolution |
| `temporal_modeling` | temporale Modellierung |
| `status_modeling` | Statusmodellierung |
| `provenance` | Provenienzbehandlung |
| `graph_representation` | Graphrepräsentation |
| `semantic_model` | semantisches Modell (z. B. NLI-Modell, Embeddings, LLM) |
| `fusion_method` | Fusionsverfahren |
| `uncertainty_handling` | Unsicherheits-/Konfidenzbehandlung, Kalibrierung |
| `baselines` | verwendete Baselines |
| `evaluation_metrics` | Evaluationsmetriken |
| `key_results` | wichtigste Ergebnisse (mit Zahlen nur, wenn im Volltext angegeben) |
| `limitations` | Limitationen (von den Autoren genannt oder bei der Prüfung erkannt, gekennzeichnet) |
| `relevance_hyconcheck` | Relevanz für HyConCheck (hoch/mittel/niedrig + Satz) |
| `relation_F` | Bezug zu F1–F6 |
| `relation_H` | Bezug zu H1–H7 (nur Stand-der-Technik-Bezug, keine Bewertung) |
| `open_gap` | offene technische Lücke, die die Arbeit benennt oder erkennbar lässt |
| `quality_transparency`, `quality_reproducibility`, `quality_evaluation`, `quality_relevance`, `quality_evidence` | Qualitätsbewertung nach Abschnitt 14 |
| `anticipates_hyconcheck` | `nein` / `teilweise` / `weitgehend` – Grad, in dem die Arbeit den HyConCheck-Ansatz vorwegnimmt (Abschnitt 16) |

## 14. Qualitätsbewertung

Qualitative Stufen `hoch` / `mittel` / `niedrig` je Kriterium; keine Summenbildung, keine Punktzahl.

| Kriterium | hoch | mittel | niedrig |
|---|---|---|---|
| Methodische Transparenz | Verfahren vollständig beschrieben (Architektur, Parameter, Vorverarbeitung) | wesentliche Schritte beschrieben, Details fehlen | Verfahren nur skizziert |
| Reproduzierbarkeit | Code und Daten verfügbar oder Daten öffentlich und Verfahren vollständig spezifiziert | Daten oder Code verfügbar, nicht beides; oder nur mit Aufwand rekonstruierbar | weder Code noch Daten, Spezifikation unvollständig |
| Evaluationsqualität | klar definierte Metriken, Baselines, Aufteilung, Fehleranalyse oder Signifikanz/Varianz berichtet | Metriken und Baselines vorhanden, ohne Fehleranalyse/Varianz | keine Baselines oder unklare Aufteilung/Metriken |
| Relevanz für HyConCheck | adressiert direkt mindestens zwei Klärungsziele oder ein Ziel dokumentübergreifend/temporal/statusbezogen | adressiert ein Klärungsziel oder ist methodische Grundlage | nur randständiger Bezug |
| Qualität der Evidenz | peer-reviewed und empirisch mit nachvollziehbarer Evaluation | peer-reviewed ohne empirische Evaluation oder hochwertiger Preprint mit Evaluation | nicht peer-reviewed und ohne belastbare Evaluation |

Die Bewertung wird je Quelle mit Datum und – bei `niedrig` in Relevanz oder Evidenz – mit einem Satz Begründung im Register vermerkt. Quellen mit `niedrig` in „Qualität der Evidenz“ tragen keine Kernaussage der Auswertung allein.

## 15. Umgang mit widersprüchlicher Literatur

Widersprüchliche Ergebnisse verschiedener Quellen werden **nicht geglättet** und nicht durch Auswahl einer „passenden“ Quelle aufgelöst. Bei der Auswertung (BL-003) werden für jede festgestellte Diskrepanz dokumentiert:

- die beteiligten Quellen (Source-IDs),
- unterschiedliche Methoden,
- Datensätze,
- Populationen/Korpora (Dokumenttypen, Domänen, Sprachen),
- Metriken und ihre Definitionen,
- Modellversionen,
- experimentelle Bedingungen (Splits, Seeds, Rechenbudget, Kontextlänge).

Diskrepanzen werden als solche in `STATE_OF_THE_ART.md` ausgewiesen; sie sind selbst ein Befund zum Stand der Technik.

## 16. Research-Gap-Regel (Bias-Schutz)

Die HyConCheck-Forschungslücke (§4) darf **erst nach** systematischer Literaturauswertung (BL-003) in BL-004 konkretisiert werden. Um zu verhindern, dass nur nach bestätigender Literatur gesucht wird, gilt verbindlich:

1. **Bestätigende und widerlegende Evidenz:** Für jedes Klärungsziel Z1–Z11 wird sowohl nach Arbeiten gesucht, die die Lückenannahme stützen, als auch nach Arbeiten, die sie einschränken oder widerlegen. Beide Kategorien werden im Register mit `gap_evidence = stuetzend` / `einschraenkend` / `widerlegend` / `neutral` gekennzeichnet.
2. **Vorwegnahme-Suche:** ES-23 und ES-24 sowie die Forward-Snowballing-Läufe zielen ausdrücklich auf Ansätze, die HyConCheck **teilweise oder vollständig vorwegnehmen** könnten (gemeinsame Verarbeitung semantischer, temporaler, statusbezogener und graphbasierter Evidenz mit Fusion). Jede aufgenommene Quelle erhält das Feld `anticipates_hyconcheck`.
3. **Negative Evidenz:** Arbeiten, die zeigen, dass Komponenten (z. B. Entity Resolution, temporale Modellierung, Fusion) keinen oder negativen Effekt hatten, werden aufgenommen und in der Auswertung gesondert berichtet.
4. **Keine selektive Aufnahme:** Die Aufnahmeentscheidung folgt ausschließlich den Kriterien in Abschnitt 9; „passt nicht zur Lückenannahme“ ist kein Ausschlussgrund. Screening-Zähler (gefunden/gescreent/aufgenommen/ausgeschlossen je Lauf) machen Auslassungen sichtbar.
5. **Ergebnisoffenheit:** BL-004 endet mit genau einer der Feststellungen `gestützt`, `präzisiert` (mit neuer Formulierung) oder `widerlegt` – jeweils mit Belegen über Source-IDs. Eine Feststellung `widerlegt` oder `präzisiert` ist ein gültiges Ergebnis und führt zu einem ADR über die Anpassung des Forschungsdesigns (§26).

## 17. Stop-/Sättigungskriterium

Die initiale Stand-der-Technik-Recherche (BL-002) gilt als hinreichend breit, wenn **alle** folgenden Bedingungen erfüllt und im Suchprotokoll belegt sind:

1. **Clusterabdeckung:** Alle 16 Primärstrings wurden in den zugeordneten Systemen (Abschnitt 5) ausgeführt; jedes Cluster A–P hat mindestens eine aufgenommene Quelle **oder** eine dokumentierte Feststellung „keine geeignete Quelle im Trefferfenster“ mit Zählern.
2. **Aktualität:** Für jedes Cluster wurden die Treffer der letzten drei Jahre vor dem Recherchedatum im Trefferfenster vollständig gescreent.
3. **Snowballing-Sättigung:** Backward- und Forward-Snowballing (Abschnitt 18) der Kernarbeiten liefert in der letzten Runde keine neue **Methodenkategorie** mehr (Kategorie = neuer Eintrag in den Extraktionsfeldern `method`, `graph_representation` oder `fusion_method`, der bisher nicht vertreten war).
4. **Dublettenanteil:** Die letzten zwei zusätzlichen Suchläufe (neue ergänzende Strings oder neues System) erzeugen im Trefferfenster überwiegend (> 80 %) Dubletten oder bereits abgedeckte Ansätze.
5. **Klärungsziele:** Jedes Klärungsziel Z1–Z11 kann mit den aufgenommenen Quellen adressiert werden **oder** ist ausdrücklich als „Literatur nicht auffindbar“ markiert – letzteres ist selbst ein Befund für BL-004.

Es wird **kein** fester Quellenumfang vorgegeben. Wird das Kriterium nicht erreicht, wird die Recherche mit dokumentierten zusätzlichen Strings/Systemen fortgesetzt; ein Abbruch aus Zeitgründen wird als solcher mit den unerfüllten Bedingungen dokumentiert und nicht als Sättigung ausgegeben.

## 18. Snowballing (erst in BL-002)

- **Kernarbeiten:** aufgenommene Quellen mit `relevance_hyconcheck = hoch` sowie alle Quellen mit `anticipates_hyconcheck ≠ nein`.
- **Backward Snowballing:** Referenzlisten der Kernarbeiten werden vollständig auf Titel-Ebene gescreent (Stufe 1); Kandidaten durchlaufen Stufen 2–4. Fundstelle: `search_system = snowballing-backward`, Ausgangs-ID vermerkt.
- **Forward Snowballing:** zitierende Arbeiten der Kernarbeiten über S1/S2 („cited by“), Trefferfenster 50 nach Relevanz/Zitationen; Fundstelle `snowballing-forward`.
- **Runden:** Snowballing wird in Runden geführt; neue Kernarbeiten einer Runde werden in der nächsten Runde geschneeballt. Abbruch nach Abschnitt 17.3.

## 19. Reproduzierbarkeit der Suchläufe

Für jeden Suchlauf wird in `LITERATURE_SEARCH_LOG.md` festgehalten:

| Feld | Inhalt |
|---|---|
| `run_id` | `RUN-NNNN` |
| `date` | Datum des Laufs (ISO) |
| `search_system` | S1–S9 oder Snowballing-Art |
| `string_id` | PS-/ES-ID (ggf. mit Varianten-Suffix) |
| `exact_string` | exakt eingegebener String (systemspezifische Syntax) |
| `filters` | Filter (Datum, Dokumenttyp, Sprache, Sortierung) |
| `result_count` | Trefferanzahl laut System |
| `screened_count` | gescreente Treffer (Trefferfenster) |
| `included_ids` | aufgenommene Source-IDs (Stufe 2 „weiter“ → Register) |
| `excluded_count` | ausgeschlossene Treffer auf Stufe 1 |
| `notes` | Begründungen, Abweichungen, Syntaxanpassungen |

Ein Suchlauf ohne vollständigen Eintrag gilt als nicht durchgeführt.

## 20. Geplante Folgeartefakte

| Datei | Inhalt | Status in BL-001 |
|---|---|---|
| [`references/LITERATURE_SEARCH_LOG.md`](LITERATURE_SEARCH_LOG.md) | Suchprotokoll aller Läufe (Abschnitt 19) | leere Vorlage, keine Läufe |
| [`references/SOURCES.md`](SOURCES.md) | Quellenregister mit Provenienz (Abschnitt 12) | leere Vorlage, keine Quellen |
| [`references/LITERATURE_MATRIX.csv`](LITERATURE_MATRIX.csv) | Extraktionsmatrix aufgenommener Quellen (Abschnitte 13, 14) | nur Kopfzeile, keine Daten |
| `docs/STATE_OF_THE_ART.md` | Auswertung (BL-003) inkl. Diskrepanzen (Abschnitt 15) | noch nicht angelegt |
| Abschnitt in `docs/RESEARCH_DESIGN.md` + ADR | Ergebnis der Lückenprüfung (BL-004) | noch nicht angelegt |

Die Vorlagen enthalten keine erfundenen Literaturdaten.

## 21. Datenschutz und Quellenintegrität

- Keine personenbezogenen Projektdaten (Namen, Zeitnachweise, interne Dokumente) in Suchanfragen.
- Keine vertraulichen Projektinformationen (interne Dokumente, Datenbestände, unveröffentlichte Ergebnisse) an externe Suchsysteme übermitteln; Suchstrings bestehen ausschließlich aus den in Abschnitt 6 definierten Fachbegriffen.
- Nur öffentlich zitierfähige wissenschaftliche/technische Informationen werden verwendet und erfasst.
- Keine kostenpflichtigen Dienste ohne ausdrückliche Freigabe (§33); bei Paywalls gilt EX-7 mit Vermerk.
- Volltexte werden nicht im Repository abgelegt (Urheberrecht); erfasst werden bibliografische Daten, Extraktion und Bewertung.

## 22. Ergebnis und Abschlusskriterium von BL-001

BL-001 ist abgeschlossen, wenn dieses Protokoll die folgenden Punkte reproduzierbar festlegt – alle sind in dieser Version enthalten:

| Kriterium | Abschnitt |
|---|---|
| Rechercheprotokoll reproduzierbar dokumentiert | 1–22 |
| Suchsysteme definiert | 5 |
| Suchstrings definiert | 6 |
| Ein-/Ausschlusskriterien festgelegt | 9 |
| Screeningprozess definiert | 10 |
| Provenienzschema festgelegt | 12 |
| Extraktionsschema festgelegt | 13 |
| Research-Gap-Bias-Schutz festgelegt | 16 |
| Sättigungs-/Stopkriterium definiert | 17 |
| Folgeartefakte spezifiziert | 20 |

BL-001 bedeutet **nicht**: Literaturrecherche abgeschlossen · Stand der Technik bewertet · Forschungslücke bestätigt · Hypothesen bewertet · AP1 abgeschlossen. Nächste Etappe: **BL-002 – Recherche gemäß Protokoll durchführen** (erst dann werden Suchsysteme tatsächlich abgefragt).

## Änderungshistorie

| Datum | Version | Änderung |
|---|---|---|
| 17.09.2026 | 1.0 | Erstfassung (BL-001) |
