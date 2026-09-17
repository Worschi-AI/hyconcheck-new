# ADR-0002 – Vollständiger Master-Prompt als maßgebliche Quelle und Angleichung der Projektgrundlage

- **Status:** angenommen
- **Datum:** 2026-09-17
- **Bezug:** BL-000a (Einrichtung); präzisiert ADR-0001

## Problem

Die Projektgrundlage vom 17.09.2026 (Commit „Projektgrundlage für HyConCheck einrichten“) wurde auf Basis eines verkürzten Auftrags erstellt. Der vollständige Forschungsauftrag (`docs/HYCONCHECK_MASTER_PROMPT.md`, §0–§39) liegt seit demselben Tag byte-identisch im Repository vor. Es ist festzulegen, welche Quelle maßgeblich ist und wie die bisherigen Repository-Annahmen zu behandeln sind.

## Evidenz

- Konsistenzprüfung vom 17.09.2026 (Tageslog, Etappe 4): AP-Bezeichnungen und -Inhalte, AP-Zeiträume, Jahresverteilung je AP und Meilensteine MS0–MS8 waren Eigenannahmen; H1–H7 wurden als „offen zu formulieren“ geführt, obwohl der Master-Prompt sie als Ausgangshypothesen vorgibt (§8); zentrale Forschungsfrage (§6), F1–F6 (§7), Eigenentwicklung A–D (§5), Testset-Schutz (§11), Baseline B0 (§13), Stufen A–G (§14), Metriken (§16), Risiken (§17), Experimentregeln (§18–§22), Qualitäts-Gates (§35), M1–M7 (§36), Definition of Done (§37) und Abschlussfrage (§38) fehlten; der Zeitnachweis wurde als „nicht vorhanden“ geführt, obwohl die Forecast-Quelle inzwischen bereitgestellt ist; die Git-Regeln in AGENTS.md wichen von §30/§39 ab.
- Master-Prompt §1: Bei Widersprüchen zwischen älteren Projektunterlagen und dem Auftrag hat der „Verbindliche Projektkern“ (§2) Vorrang. §0: `planning/PROJECT_PLAN_2026_2027.md` ist der verbindliche Gesamtplan.

## Optionen

1. Bisherige Repository-Annahmen beibehalten und nur ergänzen.
2. Master-Prompt als alleinige maßgebliche Quelle festlegen; alle abweichenden Annahmen ersetzen; unbelegte Annahmen entfernen.
3. Repository verwerfen und neu aufsetzen.

## Entscheidung

Option 2. Der vollständige Master-Prompt ist die maßgebliche fachliche Quelle des Repositorys. Alle Repository-Dokumente werden daran angeglichen; keine bisherige Annahme bleibt allein deshalb bestehen, weil sie bereits committet oder gemergt war.

Präzisierung von ADR-0001: Der Neuaufbau „bei null“ betrifft Dateien, Commits, Erledigungsstände und Forschungsergebnisse. **Nicht** bei null beginnen – weil sie durch den Forschungsauftrag vorgegeben sind – der offizielle Projekttitel, der Kernumfang (§3), das Forschungsproblem als zu überprüfende Annahme (§4, §39.5), die zentrale Forschungsfrage (§6), F1–F6 (§7), die Ausgangshypothesen H1–H7 (§8, Status ungeprüft), die fünf Taxonomie-Obertypen (§9), die Baselines B0–B4 (§13) sowie die Arbeitspakete und Planstunden (§25). Neu beginnen deren Überprüfung, Operationalisierung, Implementierung und Evaluation.

Ergänzend zu ADR-0001 (§2): Fachlich zum Vorhaben gehörende Arbeiten, die seit September 2026 außerhalb dieses Repositorys stattgefunden haben, liegen im offiziellen Projektzeitraum. Sie werden weder geleugnet noch als in diesem Repository durchgeführt dargestellt; werden sie erwähnt, wird ihre externe Herkunft mit tatsächlichem Dokumentationsdatum gekennzeichnet.

## Begründung

Der Master-Prompt ist der eingereichte Forschungsauftrag; Eigenannahmen dürfen ihn nicht überlagern (§1, §26). Ein vollständiger Neuaufbau (Option 3) wäre unnötig, da die Struktur nach §27 bereits passt. Option 1 würde die falschen AP-Zuordnungen fortschreiben.

## Auswirkung

- AP1–AP7 in allen Dokumenten nach §25; Meilensteine M1–M7 nach §36; Qualitäts-Gates nach §35; Definition of Done nach §37; Abschlussfrage nach §38.
- H1–H7 mit unverändertem Wortlaut und Status „ungeprüft“; F1–F6 und Forschungsfrage im Forschungsdesign.
- Unbelegte AP-Zeiträume und Jahresverteilung je AP aus dem Projektplan entfernt; sie werden erst mit der Forecast-Integration (BL-090) aus der bereitgestellten Forecast-Quelle abgeleitet. Die Forecast-Quelle wurde bereitgestellt; ihre kontrollierte Prüfung und Integration erfolgt in einer separaten Etappe.
- Taxonomie-Datei enthält nur den Rahmen nach §9; vorläufige Arbeitsdefinitionen entfernt (§39.6).
- Git-Prozess nach §30/§39: jede Etappe endet mit sachlichem Commit und vorbereitetem, nicht automatisch zusammengeführtem Pull Request.
- ADR-Vorlage nach §29. ADR-0001 bleibt inhaltlich unverändert (nur Statusvermerk „präzisiert durch ADR-0002“).
- Bestehende Tageslog-Einträge bleiben unverändert; Präzisierungen als neue Einträge.

## Zugehörige Experimente / Commits

- Keine Experimente.
- Commit „Projektgrundlage an vollständigen Forschungsauftrag angleichen“ auf Branch `work/master-prompt-alignment` (Basis `main` @ `588584e`).
