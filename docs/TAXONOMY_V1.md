# HyConCheck – Widerspruchstaxonomie V1

Stand: 17.09.2026 – Rahmenfassung nach Master-Prompt §9 ([HYCONCHECK_MASTER_PROMPT.md](HYCONCHECK_MASTER_PROMPT.md)). Taxonomie-Version: **V1.0-Rahmen** (noch keine operationalisierte Fassung). Die fachliche Operationalisierung hat in diesem Repository **noch nicht begonnen** (§39.6); sie ist Gegenstand von AP1 (BL-010 ff.). Kein Obertyp ist abgeschlossen.

## 1. Verbindliche oberste Ebene

Die fünf Obertypen sind verbindlich festgelegt:

1. Fakt und Wert
2. Zeit und Status
3. Modalität und Norm
4. Akteur und Verantwortung
5. Abhängigkeit und Schnittstelle

Zusätzliche Kategorien sind zunächst Untertypen oder Sekundärtags. Es wird **nicht** parallel eine neue 17-teilige Haupttaxonomie eingeführt.

## 2. Pflichtbestandteile je Obertyp (§9)

Für jeden Obertyp sind in der Operationalisierung mindestens festzulegen:

- Definition
- Entscheidungstest
- Einschlusskriterien
- Ausschlusskriterien
- Grenzfälle
- Abgrenzung zu anderen Obertypen
- synthetische Positivbeispiele
- synthetische Negativbeispiele
- unklare Beispiele

## 3. Entscheidungslabels und Sonderkennzeichnungen (§9)

Zulässige Entscheidungslabels: **Widerspruch**, **kein Widerspruch**, **unklar**.

Fortschreibung, fehlender Kontext, Versionswechsel und Mehrdeutigkeit sind gesondert zu kennzeichnen und dürfen nicht automatisch als Widerspruch gelten. Die Kennzeichnung erfolgt als Sekundärtag; ihre genaue Form wird in der Operationalisierung festgelegt.

## 4. Stand je Obertyp

Statuswerte (Repository-Konvention): `offen` → `in Operationalisierung` → `operationalisiert` (alle Pflichtbestandteile aus Abschnitt 2 liegen vor und sind geprüft). Ein Status „abgeschlossen“ wird für Obertypen nicht vergeben.

| Nr. | Obertyp | Definition | Entscheidungstest | Ein-/Ausschluss | Grenzfälle | Abgrenzung | Beispiele (pos./neg./unklar) | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Fakt und Wert | offen | offen | offen | offen | offen | offen | offen |
| 2 | Zeit und Status | offen | offen | offen | offen | offen | offen | offen |
| 3 | Modalität und Norm | offen | offen | offen | offen | offen | offen | offen |
| 4 | Akteur und Verantwortung | offen | offen | offen | offen | offen | offen | offen |
| 5 | Abhängigkeit und Schnittstelle | offen | offen | offen | offen | offen | offen | offen |

## 5. Verwendung

- Zielschema für Annotation und Ground Truth (§10, §12; AP2).
- Berichtsdimension der Evaluation (Macro-F1 nach Widerspruchstyp, §16).
- Taxonomie-Version ist Pflichtfeld jedes Experiments (§18) und jeder Ground-Truth-Dokumentation (§12).

## 6. Vorgehen zur Operationalisierung (AP1)

Die Operationalisierung erfolgt nach dem Stand der Technik (BL-001 bis BL-003) und wird je Obertyp mit allen Pflichtbestandteilen aus Abschnitt 2 in diesem Dokument versioniert (Backlog BL-010 bis BL-013). Änderungen an Definitionen oder Entscheidungstests nach Beginn der Annotation werden mit Datum, Begründung und Auswirkung auf bestehende Labels dokumentiert (§12).

## 7. Änderungshistorie

| Datum | Version | Änderung |
|---|---|---|
| 17.09.2026 | V1.0-Rahmen | Erstfassung: Obertypen, Pflichtbestandteile, Entscheidungslabels, Sonderkennzeichnungen, Statusdefinition |
| 17.09.2026 | V1.0-Rahmen | Angleichung an Master-Prompt §9: Pflichtbestandteile und Labels nach §9; frühere vorläufige Arbeitsdefinitionen entfernt, da die Operationalisierung erst in AP1 beginnt (§39.6) |
