# tests/

Tests und Qualitätsprüfungen nach Master-Prompt §31 und §39.15.

| Prüfung | Zweck | Aufruf | Stand 17.09.2026 |
|---|---|---|---|
| `check_repo_conventions.py` | Konventionsprüfung (kein Unit-Test): Pflichtdateien, Werkzeugneutralität, interne Links, Vollständigkeit des Master-Prompts, Wortlaut von H1–H7/F1–F6/AP-Inhalten, Planstunden, Taxonomie-Status, Forecast-Artefakte (`planning/forecast/`: Zeilenzahlen 386/66, keine Namensspalte, keine lokalen Pfade, AP-/Jahres-/Gesamtsummen, Tagessummen 0/8, Nicht-AP-Zeilen 0 h, AP-Titel-Konsistenz, SHA-256 und „keine Ist-Aussage“ im README, BL-090-Status) | `py tests/check_repo_conventions.py` | anwendbar |
| `git diff --check` | Whitespace-Fehler | `git diff --check` | anwendbar |
| `python -m pytest` | Unit-/Integrationstests des Projektcodes | `python -m pytest` | **noch nicht anwendbar**: `src/` enthält keinen ausführbaren Projektcode, es existieren keine Testmodule, und `pytest` ist in der Umgebung nicht installiert (erneut geprüft 17.09.2026, BL-090); `planning/forecast/build_forecast_csv.py` ist ein Hilfsskript zur Artefakterzeugung, dessen Ergebnis durch die Konventionsprüfung abgedeckt ist; es werden keine Scheintests für Planungsdokumente erzeugt |
| `ruff check .` | Lint des Python-Codes | `ruff check .` | **noch nicht anwendbar** als Pflichtprüfung: kein Projektcode in `src/`, `ruff` in der Umgebung nicht installiert (erneut geprüft 17.09.2026, BL-090); wird mit dem ersten Code (BL-021/BL-030) eingeführt und konfiguriert |

Mit dem ersten Projektcode werden `pytest`- und `ruff`-Konfiguration (z. B. `pyproject.toml`) und Testmodule ergänzt; fehlgeschlagene Prüfungen werden nicht verschwiegen (§31).
