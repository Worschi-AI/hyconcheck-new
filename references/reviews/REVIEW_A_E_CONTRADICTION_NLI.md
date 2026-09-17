# Zwischenauswertung BL-002.1 – Cluster A–E: Contradiction Detection, NLI, Document-level NLI, Cross-document Contradiction Detection, Semantic Consistency Checking

| | |
|---|---|
| Etappe | BL-002.1 (AP1), Recherchetranche 1 von 5 |
| Datum | 17.09.2026 |
| Grundlage | [RESEARCH_PROTOCOL.md](../RESEARCH_PROTOCOL.md); [LITERATURE_SEARCH_LOG.md](../LITERATURE_SEARCH_LOG.md) (RUN-0001–RUN-0041); [SOURCES.md](../SOURCES.md) (SRC-0001–SRC-0052); [LITERATURE_MATRIX.csv](../LITERATURE_MATRIX.csv) |
| Status | **vorläufig** – nur Cluster A–E; Cluster F–P folgen in BL-002.2–BL-002.4; Snowballing/Sättigung in BL-002.5 |

**Verbindliche Lesart:** Diese Auswertung verwendet ausschließlich die 47 aufgenommenen Quellen. Sie formuliert **keine** abschließende Forschungslücke und bewertet **keine** Hypothese. Alle Aussagen gelten „in den bislang geprüften Arbeiten dieser Recherchetranche“. Für 12 Quellen liegt nur der verifizierte Abstract vor (im Register mit `screening_status = abstract-only` und „Abstract-Basis“ gekennzeichnet); Aussagen zu ihnen sind entsprechend eingeschränkt, und der Volltext ist für BL-002.5 nachzubeschaffen. Diese Fassung berücksichtigt die Korrekturen des unabhängigen Qualitäts-Audits vom 17.09.2026.

## 1. Umfang und Stand dieser Recherchetranche

- Suchsysteme tatsächlich genutzt: Google Scholar (S1), Semantic Scholar API (S2), ACL Anthology (S4), arXiv API (S5). Nicht abgefragt: IEEE Xplore, ACM DL, SpringerLink, ScienceDirect (für spätere Tranchen); DBLP-API beim Test nicht erreichbar (HTTP 500), Verifikation über andere Wege.
- 28 API-Läufe, 9 Browser-Läufe, 3 Snowballing-Läufe; ca. 1.080 Titel-Screenings (mit Dubletten); 52 Quellen ab Stufe 2 im Register; 47 aufgenommen (42 peer-reviewed, 5 Preprints), 5 ausgeschlossen (SRC-0003, SRC-0048, SRC-0049, SRC-0051, SRC-0052).
- Volltext gelesen: 35 Quellen; `abstract-only`: 12 (paywalled bzw. Download gesperrt; bibliografisch verifiziert, Abstract geprüft, Volltext nicht geprüft).
- Primärcluster der Aufnahmen: A 20, B 8, C 5, D 5, E 9 (Mehrfachzuordnungen siehe Register; 15 Quellen zusätzlich P, 13 D).
- Suchstring-Befunde: ES-03, ES-04 und ES-24 waren in der Semantic-Scholar-Bulk-Suche zu unspezifisch (fachfremde Fenster); Ableitungen `-v3` wurden dokumentiert. Die Phrase „cross-document contradiction detection“ ist in der Literatur selten (S2: 5 Treffer; arXiv: 2); dokumentübergreifende Arbeiten firmieren unter „evidence conflicts“, „inter-context conflicts“, „knowledge conflicts“, „cross-document NLI“, „multi-document consistency“ – dies ist eine Konsequenz für die Suchstrings (Abschnitt 13).

## 2. Contradiction Detection (Cluster A)

- **Grundlagen (vor 2018):** SRC-0001 definiert Widerspruch für NLP (zwei Aussagen können äußerst unwahrscheinlich gleichzeitig wahr sein), setzt Ereignis-Koreferenz voraus und liefert eine Typologie (Antonymie, Negation, numerisch, faktiv, Struktur, lexikalisch, Weltwissen) mit Präzision/Recall je Typ; auf RTE-Daten bleibt die Erkennung schwach (z. B. RTE3 dev P 61,9 %/R 31,7 %). SRC-0002 zeigt an Webtext, dass ca. 99 % scheinbarer Widersprüche über funktionale Relationen tatsächlich konsistent sind (Meronyme, Synonyme, Mehrdeutigkeit) – Hintergrundwissen und Referenzauflösung sind entscheidend. SRC-0004 modelliert Antonymie über spezifische Embeddings (Abstract-Basis).
- **Lern- und Fehleranalysen:** SRC-0006 findet, dass Transformer-basierte CD-Modelle bei Präpositionen, Verben, kontextabhängigen Antonymen/Homonymen, unvollständigen Sätzen und langen Absätzen scheitern. SRC-0005 (Deutsch, übersetztes SNLI) und SRC-0007 (Finanzberichte, F1 89,55 % auf proprietären Daten) zeigen Domänen-/Sprachtransfer auf Satzpaaren (beide Abstract-Basis).
- **Domänen:** Klinische Widersprüche mit Ontologie-Distant-Supervision (SRC-0008; explizit auf Einzelsätze beschränkt), biomedizinische Dokumentpaare mit erklärenden Kontextvariablen (SRC-0016), Dialoge (SRC-0012), Tweets (SRC-0013).
- **Dokumentebene mit LLMs (2024–2026):** SRC-0009 (ContraDoc, 449 Dokumente, Typen/Scope/Evidenz), SRC-0010 (SFT+RL verbessert Llama-3.1-8B von 38,5 % auf 51,1 % Accuracy), SRC-0011 (FIND: expertengesetzte Inkonsistenzen in Finanz- und wissenschaftlichen Dokumenten; bestes Modell findet 64 %, Precision ≈ 52,5 %), SRC-0015 (Evidenzextraktionsmetriken). Befund: selbst die stärksten LLMs verfehlen fast die Hälfte der Inkonsistenzen in langen technischen Dokumenten (SRC-0011) und sind bei nuancierten Selbstwidersprüchen unzuverlässig (SRC-0009).
- **Generierte Benchmarks:** SRC-0014 (RAG-Kontexte, drei Typen self/pair/conditional), SRC-0036 (Legal, sechs Typen, self/pairwise), SRC-0037 (Enterprise, Abstract-Basis) erzeugen Widersprüche synthetisch mit Human-in-the-loop.

## 3. Natural Language Inference (Cluster B)

- Benchmarks SNLI (SRC-0017) und MultiNLI (SRC-0018) definieren die 3-Klassen-Formulierung, die den B3-Baselines zugrunde liegt.
- Bekannte Schwächen: Annotationsartefakte erlauben Hypothesis-only-Vorhersagen (67 % SNLI, 53 % MultiNLI; Negation korreliert mit „contradiction“) (SRC-0019); menschliche Uneinigkeit ist systematisch und wird von Modellunsicherheit nicht abgebildet (SRC-0020); die Referenzdeterminiertheits-Annahme führt zu > 80 % falschen Widerspruchsvorhersagen, wenn Prämisse und Hypothese sich auf verschiedene Kontexte beziehen (SRC-0021).
- Kalibrierung: vortrainierte Transformer sind in-domain kalibriert, out-of-domain helfen Temperature Scaling/Label Smoothing (SRC-0022); SCALE berichtet taskabhängige Kalibrierung (SRC-0029).
- Deutschsprachige NLI für Anforderungen: SRC-0043 (> 21.000 semisynthetische Paare; GPT-4o über feinabgestimmten Transformern; Abstract-Basis).

## 4. Document-level NLI (Cluster C)

- Datensätze: DocNLI (SRC-0023; binär entailment/not), ContractNLI (SRC-0024; entailed/contradicted/not mentioned + Evidenzspannen; „Negation durch Ausnahmen“ als Schwierigkeit), CaseHoldNLI (SRC-0025).
- Verfahren: hierarchischer Dokumentgraph mit topischen/entitäts-/konzeptbasierten Kanten und Evidenzauswahl (SRC-0025, 8–12 % über SOTA; Autoren nennen temporales Wissen als Future Work); Retrieval–Reading–Fusion (SRC-0026); Segmentierung + Aggregation satzweiser NLI-Scores (SRC-0027: Granularitäts-Mismatch als Kernursache früherer Fehlschläge; SRC-0028: Aggregation über Dokumente und Cluster; SRC-0029: Chunking).
- Befund: Dokument-NLI wird in den geprüften Arbeiten überwiegend durch Zerlegung in Satz-/Chunk-Entscheidungen plus Aggregation/Fusion gelöst; explizite Zeit-, Status- oder Versionsinformation ist in keiner der geprüften C-Arbeiten Teil des Modells.

## 5. Cross-document Contradiction Detection (Cluster D)

- **Konzeptuelle Grundlage:** Cross-Document Structure Theory (SRC-0030, SRC-0031) unterscheidet bereits 2000/2004 dokumentübergreifende Relationen wie Widerspruch, Fortschreibung/Follow-up, Attribution, Modalität und berücksichtigt Provenienz und Chronologie – als Taxonomie, nicht als automatisches Verfahren.
- **Aktuelle Verfahren/Benchmarks:** CDCL-NLI (SRC-0032) modelliert Dokumentpaare über einen heterogenen RST-Graphen mit Graph-Fusion (Macro-F1 ≈ 69–71 %; nur Paare). ECON (SRC-0033) vergleicht NLI-, Factual-Consistency- und LLM-Detektoren auf generierten Evidenzkonflikten (hohe Precision, schwache Recall kleiner Modelle; −18,2 % F1 bei längeren Kontexten; LLMs lösen Konflikte oft unbegründet auf). MAGIC (SRC-0034) erzeugt Inter-Kontext-Konflikte aus Knowledge-Graph-Subgraphen (Single-/Multi-Hop) und zeigt, dass LLMs Multi-Hop-Konflikte und deren Lokalisierung schlecht beherrschen. SRC-0028 findet mit reiner NLI-Aggregation reale Inkonsistenzen zwischen Wikipedia-Sprachversionen. SRC-0014, SRC-0036, SRC-0037 modellieren paarweise/dokumentübergreifende Widersprüche in RAG-Kontexten; SRC-0036 berichtet, dass dokumentübergreifende Fälle deutlich schwerer bleiben als Selbstwidersprüche (LLM-only F1 46,9 %). SRC-0038 zeigt für regulatorische Paare, dass reine Entailment-Formulierungen den Fall „eine Seite schweigt“ (SILENT) nicht erfassen und ein Obligation-Graph lexikalische Verfahren übertrifft, aber hinter einem LLM-Judge bleibt (Pilot, n = 101). SRC-0044 berichtet industrielle dokumentübergreifende Konsistenzprüfung mit einem LLM-Agenten (Coverage 47 % → 74 % durch Domänenwissen; Abstract-Basis).
- **Befund:** Dokumentübergreifende Widerspruchserkennung existiert in den geprüften Arbeiten vor allem als (a) Paar-NLI über Dokumente, (b) Konfliktdetektion in abgerufenen Kontextmengen (RAG) und (c) synthetische Benchmarks. Zeitliche Gültigkeit, Status und Versionen werden dabei – mit Ausnahme der konzeptuellen CST-Relationen – nicht als eigene Dimension modelliert.

## 6. Semantic Consistency Checking (Cluster E)

- **Requirements Engineering:** Taxonomie von Widerspruchsuntertypen auf logischer Basis (SRC-0039, Abstract-Basis) und deren Operationalisierung als formale Logik + LLM (ALICE, SRC-0040: Accuracy 72 % / Recall 75 % / Precision 83 % vs. LLM-only 47 % / 32 % / 80 % auf Dataset 1). LLM-Vorstudie (SRC-0041) und hybride Kombination Clustering + LLM (SRC-0042) berichten Verbesserungen gegenüber LLM-only (Abstract-Basis). Regelbasierte Konfliktdetektion über ein Acht-Tupel-Semantikmodell mit sieben Konflikttypen (SRC-0045: Recall ≈ 100 %, Precision Ø 83,9 %). Semisynthetische deutschsprachige NLI-Paare (SRC-0043).
- **Heterogene Artefakte/Spezifikationen:** Ontologiegetriebene Observables mit RAG+LLM-Extraktion und SMT-Prüfung (SRC-0047, ohne Standardmetriken); LLM-generierte Knowledge Graphs aus RFC-Spezifikationen mit intra-/inter-entitätsbezogener Widerspruchsdetektion (SRC-0046, Abstract-Basis); LLM-basierter Agent mit explizit eingebundenem Domänenwissen für interne und dokumentübergreifende Konsistenzprüfung in der Industrie (SRC-0044, Abstract-Basis; keine symbolische Komponente belegt).
- **Befund:** In RE-Arbeiten sind hybride Verfahren (symbolisch + LLM) verbreitet und werden in den geprüften Fällen als besser als LLM-only berichtet – auf paarweisen Anforderungen und ohne Zeit-/Statusdimension.

## 7. Relevante Benchmarks / Datensätze (verifiziert in dieser Tranche)

| Benchmark | Quelle | Ebene | Labels/Typen | Öffentlich (laut Quelle) |
|---|---|---|---|---|
| RTE1–3 (Widerspruchsannotation), Negationskorpus | SRC-0001 | Satzpaar | Typologie 7 Klassen | teilweise |
| AuContraire Web-Widerspruchspaare | SRC-0002 | Satzpaar | echt/scheinbar | ja |
| SNLI / MultiNLI | SRC-0017 / SRC-0018 | Satzpaar | E/C/N | ja |
| RefNLI | SRC-0021 | Satz–Passage | Referenzambiguität | ja |
| DECODE | SRC-0012 | Dialog | Widerspruch ja/nein | ja |
| SummaC-Benchmark (6 Datensätze), TRUE (11), ScreenEval | SRC-0027, SRC-0029 | Dokument–Zusammenfassung | konsistent/inkonsistent | ja |
| DocNLI, ContractNLI, CaseHoldNLI, ConTRoL | SRC-0023, SRC-0024, SRC-0025 | Dokument | E/(C)/N (+Evidenz) | ja |
| ContraDoc, ContraDocPaired | SRC-0009, SRC-0015 | Einzeldokument | Selbstwiderspruch, Typ, Scope, Evidenz | ja |
| FIND | SRC-0011 | Einzeldokument (Finanz, arXiv) | Inkonsistenztypen, Evidenz, Modalität Text/Tabelle | ja (Repository genannt) |
| BioConflict | SRC-0016 | Dokumentpaar | Konflikt + Kontextvariablen | unklar |
| CST Bank | SRC-0031 | Satzpaare über Dokumente | CST-Relationen | historisch |
| CDCL-NLI | SRC-0032 | Dokumentpaar, 26 Sprachen | E/C/N + EDU-Evidenz | ja |
| ECON | SRC-0033 | Evidenzpaare | Answer-/Factoid-Konflikte | ja |
| MAGIC | SRC-0034 | Kontextpaare (KG) | 1/N × Single/Multi-Hop | ja |
| RegDivergence-101 | SRC-0038 | Regulierungspaare | AGREE/DIVERGE/SILENT | ja (Pilot) |
| RAG-Widerspruchsgenerator (SRC-0014), LegalWiz (SRC-0036), ContraGen (SRC-0037) | – | Dokumentmengen | self/pair/(conditional); 6 Typen | Framework |
| Semisynthetische Automotive-Anforderungspaare | SRC-0043 | Anforderungspaar (Deutsch) | E/C/N | unklar |
| ALICE-Datensätze (Dataset 1–3) | SRC-0040 | Anforderungspaare | Widerspruchstypen | laut Papier zugänglich |

Unter den in dieser Recherchetranche **im Volltext geprüften** Benchmarks wurde bislang keiner identifiziert, der gleichzeitig mehrere Dokumente, Zeit-/Gültigkeitsangaben, Statuszustände, Versionen und Provenienz als annotierte Felder abbildet (Vergleich mit Master-Prompt §10). Für die nur auf Abstract-Basis geprüften Benchmark-Quellen (SRC-0031, SRC-0037, SRC-0043) ist das Annotationsschema noch nicht abschließend verifiziert; die Aussage ist eine vorläufige Beobachtung dieser Tranche und wird nach Volltext-Nachbeschaffung (BL-002.5) und in den Clustern F–P erneut geprüft.

## 8. Methodische Muster (in den geprüften Arbeiten)

1. **Satzpaar-NLI als Kern** (B1–B3-Familie), erweitert durch Segmentierung/Chunking und Aggregation für Dokumente (SRC-0027, SRC-0028, SRC-0029, SRC-0026).
2. **Evidenzauswahl vor Klassifikation** (Retrieval, Graph-Pooling, RL-Selektion) zur Überwindung von Kontextlimits (SRC-0025, SRC-0026, SRC-0029).
3. **LLM-Prompting als Detektor** mit bekannten Instabilitäten (Antwortinkonsistenz, Yes-Bias, Multi-Hop-Schwäche) (SRC-0009, SRC-0010, SRC-0014, SRC-0033, SRC-0034).
4. **Hybride symbolisch-neuronale Verfahren** in RE/Spezifikationen: formale Logik + LLM, Clustering + LLM, Ontologie + SMT + LLM, KG + Regeln (SRC-0040, SRC-0042, SRC-0046, SRC-0047).
5. **Graphrepräsentationen** als Dokument-/Diskursgraph (SRC-0025, SRC-0032), Knowledge-Graph (SRC-0034, SRC-0046) oder Obligation-Graph (SRC-0038) – jeweils ohne explizite Zeit-/Statuskanten.
6. **Synthetische Widerspruchsinjektion mit Human-in-the-loop** als dominantes Benchmark-Muster (SRC-0009, SRC-0011, SRC-0014, SRC-0036, SRC-0037, SRC-0043).
7. **Zeitbewusste Faktverfolgung** als Einzelfall: FactTrack (SRC-0035) führt Gültigkeitsintervalle je atomarem Fakt und unterscheidet legitime Zustandsänderungen von Widersprüchen – in der Erzähldomäne.

## 9. Erkennbare Limitationen der bisherigen Ansätze (aus den Quellen)

- Referenz-/Entitätsambiguität erzeugt massiv falsche Widersprüche (SRC-0002, SRC-0021); Koreferenz ist Voraussetzung (SRC-0001).
- Granularitäts-Mismatch Satz vs. Dokument (SRC-0027); Leistungsabfall bei längeren Kontexten (SRC-0033, SRC-0014, SRC-0011 mit Truncation).
- Annotationsartefakte und Labeluneinigkeit gefährden Benchmarks (SRC-0019, SRC-0020, SRC-0021).
- LLM-Detektoren: Inkonsistenz wiederholter Antworten, Bias zu „Ja“, schlechte Lokalisierung, unbegründete Konfliktauflösung (SRC-0009, SRC-0010, SRC-0033, SRC-0034).
- Fehlende Dimensionen: temporale/numerische Konflikte (SRC-0014, SRC-0025 als Future Work), strukturierte Evidenz (SRC-0033), Mehr-als-zwei-Dokumente (SRC-0032), Stille/Abwesenheit einer Regelung statt Widerspruch (SRC-0038).
- Synthetische Widersprüche wirken nicht immer natürlich; Kosten der Generierung (SRC-0009, SRC-0036).
- Abstract-Basis-Quellen (12) erlauben keine Aussage über Reproduzierbarkeit.

## 10. Mögliche Überschneidungen mit HyConCheck (Vorwegnahme, Feld `anticipates_hyconcheck`)

- **weitgehend (1):** SRC-0035 FactTrack – zeitliche Gültigkeitsintervalle und World-State-Update zur Unterscheidung von Fortschreibung und Widerspruch (§5B, Bezug H3/H4) – jedoch für Story-Outlines, ohne Entity Resolution über Quellen, ohne Evidenzgraph, ohne Provenienz.
- **teilweise (17):** Graphbasierte Dokument-/Cross-Document-Inferenz (SRC-0025, SRC-0032, SRC-0034, SRC-0046, SRC-0038); Fusion satzweiser Evidenz (SRC-0026, SRC-0028); hybride symbolisch-neuronale RE-Verfahren (SRC-0040, SRC-0042, SRC-0047); LLM-basierter Ansatz mit explizit eingebundenem Domänenwissen für dokumentübergreifende Konsistenzprüfung (SRC-0044); dokumentübergreifende Widerspruchsbenchmarks/-generatoren (SRC-0009, SRC-0011, SRC-0014, SRC-0036, SRC-0037); CST als konzeptuelle Relationstaxonomie mit Fortschreibung/Provenienz (SRC-0030).
- In keiner geprüften Arbeit dieser Tranche werden semantische, entitäts-, zeit-, status- und provenienzbezogene Evidenz **gemeinsam** in einer Repräsentation mit kalibrierter Fusion verarbeitet – dies ist eine **vorläufige Beobachtung**, die in den Clustern F–P (insbesondere G, H, I, K, M, O) geprüft werden muss.

## 11. Evidenz, die die bisherige Forschungslückenannahme einschränkt (`gap_evidence = einschraenkend`, 14 Quellen)

- Teile der Lückenannahme (§4) sind bereits adressiert: Graphrepräsentationen für Dokument-NLI (SRC-0025, SRC-0032), Fusion von Einzelbefunden (SRC-0026, SRC-0028), KG-basierte Widerspruchsdetektion in Spezifikationen (SRC-0046), zeitbewusste Faktverfolgung (SRC-0035), hybride Verfahren in RE (SRC-0040, SRC-0042, SRC-0047), LLM mit explizit eingebundenem Domänenwissen für dokumentübergreifende Konsistenzprüfung (SRC-0044), dokumentübergreifende Benchmarks (SRC-0034, SRC-0038), konzeptuelle Cross-Document-Relationen inkl. Fortschreibung und Provenienz (SRC-0030, SRC-0031).
- Für die Baseline-Frage (F3/H1) liegen Hinweise in beide Richtungen vor: hybrid > LLM-only in RE-Settings (SRC-0040, SRC-0036), aber LLM-Judge > Graph-RAG > NLI in einem regulatorischen Pilot (SRC-0038). Dies ist Stand der Technik anderer Settings und **keine** Bewertung von H1.
- `gap_evidence = stuetzend` (10 Quellen) betrifft vor allem: fehlende Zeit-/Status-/Versionsdimension in den im Volltext geprüften Benchmarks und Modellen, Referenzambiguität als Fehlerquelle, Schwäche bei dokumentübergreifenden und Multi-Hop-Fällen.

## 12. Vorläufig offene Fragen

1. Gibt es in Cluster G/H/I Verfahren, die Zeitnormalisierung und Statusübergänge explizit in Widerspruchsentscheidungen einbeziehen (über SRC-0035 hinaus)?
2. Existieren Evidenzgraph-/Provenienzgraph-Ansätze (Cluster K/L) mit Konsistenz- oder Widerspruchsprüfung über Dokumente?
3. Wie werden probabilistische NLI-/LLM-Scores mit harten Bedingungen kalibriert (Cluster M/N/O) – SRC-0022 und SRC-0029 behandeln nur Einzelmodelle?
4. Welche Benchmarks (Cluster P) enthalten Versions-/Zeit-/Statusfelder – oder fehlt dies durchgängig?
5. Nicht zugängliche Volltexte: SRC-0003, SRC-0051 sowie 12 `abstract-only`-Quellen – ist eine Beschaffung über IEEE/Elsevier/MDPI möglich? (Publisher-Seiten von SRC-0041 und SRC-0043 waren am 17.09.2026 im Browser lesbar, ScienceDirect für SRC-0046 nicht.)
6. Vorgemerkte, nicht geprüfte Treffer (siehe Suchprotokoll RUN-0034, RUN-0036, RUN-0037): CLAUSE, AraREQ, French Contradiction Datasets, SEC-FinTables, MMIR, Query-Conditioned NLI, Transitive Self-Consistency.

## 13. Konsequenzen für die späteren Cluster F–P

- **Suchstrings:** Für D/K/O zusätzliche Begriffe aufnehmen: „evidence conflict“, „inter-context conflict“, „knowledge conflict“, „multi-document consistency“, „cross-document NLI“; für I: „state tracking“, „world state“, „validity interval“; ES-03/ES-04/ES-24 mit NLP-Anker neu fassen (bereits als `-v3` begonnen).
- **Systeme:** IEEE Xplore, ACM DL, SpringerLink, ScienceDirect für E/F/I/K/M im Browser abfragen; DBLP-Verifikation erneut testen.
- **Snowballing (BL-002.5):** Kernarbeiten mit `relevance = hoch` und `anticipates ≠ nein` (u. a. SRC-0001, SRC-0021, SRC-0025, SRC-0026, SRC-0030, SRC-0032, SRC-0033, SRC-0034, SRC-0035, SRC-0040) rückwärts/vorwärts schneeballen; Harabagiu 2006 (SRC-0003) beschaffen.
- **Taxonomie (BL-010 ff.):** Typologien aus SRC-0001, SRC-0009, SRC-0011, SRC-0036, SRC-0039/0040, SRC-0045, SRC-0030 als Input für die Abgrenzung der fünf Obertypen; CST-Relationen Fortschreibung/Attribution/Modalität als Kandidaten für Sekundärtags.
- **Benchmark (BL-020 ff.):** Generatormuster (SRC-0009, SRC-0014, SRC-0036, SRC-0043) und Artefaktrisiken (SRC-0019, SRC-0021) berücksichtigen; Felder Zeitkontext/Version/Status/Provenienz wurden in den im Volltext geprüften Benchmarks dieser Tranche nicht gemeinsam vorgefunden (für `abstract-only`-Benchmarks nicht abschließend verifiziert).
- **Baselines (AP3):** B1 nach SRC-0045/SRC-0040-Mustern, B2/B3 nach SRC-0027/SRC-0028/SRC-0029, B4 nach SRC-0009/SRC-0011/SRC-0014-Protokollen; Kalibrierung nach SRC-0022.

## Änderungshistorie

| Datum | Änderung |
|---|---|
| 17.09.2026 | Erstfassung nach BL-002.1 (Cluster A–E) |
| 17.09.2026 | Präzisierung nach unabhängigem Qualitäts-Audit: Benchmark-Aussage auf Volltext-geprüfte Benchmarks begrenzt; SRC-0044 nicht mehr als symbolisch-neuronales Hybridverfahren geführt; `abstract-only`-Status; Nachverifikation SRC-0028/0034 (Findings of EMNLP 2022/2025, ACL-IDs) und SRC-0041/0043 (IEEE Xplore) |
