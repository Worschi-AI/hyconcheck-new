# results/

Rohresultate, Kennzahlen und Auswertungen nach Master-Prompt §16, §18 und §24. Derzeit leer.

## Regeln

- Ablage je Experiment unter `results/EXP-YYYY-NNNN/`: Rohvorhersagen (unverändert), Ground-Truth-Referenz, aggregierte Kennzahlen, Auswertungsprotokoll.
- **Reproduzierbarkeit (§24):** jedes Ergebnis referenziert Git-Commit, Dataset-Version, Konfiguration, Modellversion, Promptversion, Random Seed, Rohresultate und Auswertungscode. Maschinell erzeugte Artefakte werden gegenüber manueller Nacherfassung bevorzugt.
- **Metriken (§16):** primär Precision, Recall, Widerspruchs-F1, False-Positive-Rate; sekundär u. a. Macro-F1 nach Widerspruchstyp, FNR, PR-AUC, ECE/Brier, Recall@K, Laufzeit, Speicher, Tokenverbrauch, Kosten, Prüfaufwand, Evidenzvollständigkeit; getrennt nach Dokumenttyp, Widerspruchstyp, Schwierigkeitsgrad, synthetisch/real, Kontextlänge, Zeit- und Statusbezug.
- Negative Ergebnisse und fehlgeschlagene Läufe werden ebenso abgelegt wie positive (§23).
- Caches (`results/cache/`) werden nicht versioniert.
