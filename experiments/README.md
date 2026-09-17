# experiments/

Experimentregister und -protokolle nach Master-Prompt §18–§19. Derzeit leer; in der Grundlagenphase werden keine Experimente durchgeführt (§39).

## Regeln

- Jedes relevante Experiment erhält eine eindeutige ID `EXP-YYYY-NNNN` und ein Protokoll `experiments/EXP-YYYY-NNNN.md`; das Register `experiments/REGISTER.md` listet alle Experimente.
- **Pflichtfelder (§18):** Forschungsfrage, Hypothese, Code-Commit, Dataset-Version, Taxonomie-Version, Konfiguration, Modell und Modellversion, Promptversion (falls relevant), Seed, Rohvorhersagen, Ground Truth, Kennzahlen, Laufzeit, Fehler, Interpretation, Entscheidung, nächster Schritt.
- Jedes Experiment beantwortet eine konkrete Erkenntnisfrage; Experimente ohne Erkenntnisziel werden vermieden.
- **Zyklus (§19):** offene Frage → Hypothese → Experimentdefinition → Implementierung → Tests → Ausführung → Rohresultate unverändert speichern → Kennzahlen → Fehleranalyse (§20) → Schlussfolgerung → Folgeentscheidung → nächster Versuch.
- Ablationen (§21) und Robustheitstests (§22) sind eigene Experimente.
- Testset-Schutz (§11): kein Experiment greift vor der vorregistrierten Hauptevaluation auf Testlabels zu.
- Ressourcen (§33): keine kostenpflichtigen APIs/Dienste ohne Freigabe; kleine Entwicklungsdatensätze, Caching, gestufte Experimente.
- Rohresultate und Kennzahlen: `results/`; Konfigurationen: `configs/`.
