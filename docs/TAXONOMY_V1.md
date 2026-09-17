# HyConCheck – Taxonomie V1

Stand: 17.09.2026 – Rahmenfassung. Die fünf Obertypen sind verbindlich vorgegeben. Ihre **Operationalisierung beginnt in diesem Repository neu**; kein Obertyp ist abgeschlossen. Die Arbeitsdefinitionen unten sind vorläufige Ausgangspunkte für AP2 und keine finalen Festlegungen.

## 1. Zweck und Geltung

Die Taxonomie ordnet Inkonsistenzen in technischen Dokumentenbeständen nach der Art der betroffenen Aussage. Sie dient

- als Zielschema für Annotation und Ground Truth (AP3),
- als Gliederung für Baselines, Evidenzgraph und Fusion (AP4–AP5),
- als Berichtsdimension der Evaluation (AP6).

## 2. Statusdefinition je Obertyp

Ein Obertyp gilt erst dann als **operationalisiert**, wenn alle folgenden Bestandteile im Repository vorliegen und geprüft sind:

1. Definition und Abgrenzung zu den übrigen Obertypen
2. Untertypen (mindestens eine Ebene) mit Definition
3. Annotationsregeln inkl. Entscheidungsregeln für Grenzfälle
4. Mindestens je ein positives und ein negatives Beispiel je Untertyp (mit Quellenangabe oder als eindeutig gekennzeichnetes Konstrukt)
5. Pilotannotation mit dokumentierter Übereinstimmung

Statuswerte: `offen` → `in Operationalisierung` → `pilotiert` → `operationalisiert`. Der Status `abgeschlossen` wird für Obertypen nicht vergeben.

## 3. Übersicht

| Nr. | Obertyp | Arbeitsdefinition (vorläufig) | Status |
|---|---|---|---|
| 1 | Fakt und Wert | Unvereinbare Sachaussagen oder Werte (Zahlen, Einheiten, Bezeichner, Eigenschaften) zum selben Gegenstand | offen |
| 2 | Zeit und Status | Unvereinbare Zeitangaben, Fristen, Versionen, Gültigkeiten oder Zustandsangaben | offen |
| 3 | Modalität und Norm | Unvereinbare Verbindlichkeitsgrade, Erlaubnisse/Verbote oder Normbezüge | offen |
| 4 | Akteur und Verantwortung | Unvereinbare Angaben zu Rollen, Zuständigkeiten, Ausführenden oder Freigebenden | offen |
| 5 | Abhängigkeit und Schnittstelle | Unvereinbare Angaben zu Voraussetzungen, Verweisen, Schnittstellen oder Kopplungen | offen |

## 4. Obertypen im Einzelnen

### 4.1 Fakt und Wert

- **Arbeitsdefinition:** Zwei oder mehr Aussagen schreiben demselben Gegenstand unvereinbare Fakten oder Werte zu (z. B. Zahlenwert, Einheit, Toleranz, Materialangabe, Bezeichner).
- **Offene Fragen:** Umgang mit Einheitenumrechnung und Rundung; Toleranzbereiche; identische Werte unter verschiedenen Bezeichnern; implizite Werte.
- **Untertypen:** offen.
- **Annotationsregeln:** offen.
- **Beispiele:** offen.
- **Status:** offen.

### 4.2 Zeit und Status

- **Arbeitsdefinition:** Aussagen zu Zeitpunkten, Zeiträumen, Fristen, Versionen, Gültigkeiten oder Bearbeitungszuständen desselben Gegenstands sind unvereinbar (z. B. „freigegeben“ vs. „in Prüfung“; zwei verschiedene Liefertermine).
- **Offene Fragen:** relative vs. absolute Zeitangaben; Versionsketten; zulässige Statusübergänge; zeitliche Gültigkeit von Aussagen (was war wann korrekt?).
- **Untertypen:** offen.
- **Annotationsregeln:** offen.
- **Beispiele:** offen.
- **Status:** offen.

### 4.3 Modalität und Norm

- **Arbeitsdefinition:** Aussagen unterscheiden sich im Verbindlichkeitsgrad oder im normativen Bezug in unvereinbarer Weise (z. B. „muss“ vs. „kann“ zum selben Sachverhalt; Verbot vs. Erlaubnis; widersprüchliche Normverweise).
- **Offene Fragen:** Skala der Modalitäten (muss/soll/kann/darf nicht); Priorität von Normquellen; Ausnahmen und Bedingungen; sprachliche Varianz.
- **Untertypen:** offen.
- **Annotationsregeln:** offen.
- **Beispiele:** offen.
- **Status:** offen.

### 4.4 Akteur und Verantwortung

- **Arbeitsdefinition:** Aussagen zu Rollen, Zuständigkeiten, Ausführenden, Prüfenden oder Freigebenden desselben Vorgangs sind unvereinbar (z. B. zwei verschiedene Verantwortliche; Rolle ohne Zuordnung; widersprüchliche Freigabeinstanz).
- **Offene Fragen:** Rollen vs. Personen vs. Organisationseinheiten; Delegation und Vertretung; Mehrfachverantwortung; Anonymisierung in Benchmarkdaten.
- **Untertypen:** offen.
- **Annotationsregeln:** offen.
- **Beispiele:** offen.
- **Status:** offen.

### 4.5 Abhängigkeit und Schnittstelle

- **Arbeitsdefinition:** Aussagen zu Voraussetzungen, Verweisen, Schnittstellen, Datenformaten oder Kopplungen zwischen Komponenten, Dokumenten oder Prozessen sind unvereinbar (z. B. Verweis auf nicht existierendes Kapitel; unterschiedliche Schnittstellenparameter auf beiden Seiten; zirkuläre Voraussetzungen).
- **Offene Fragen:** Granularität (Dokument, Abschnitt, Aussage, Element); gerichtete vs. ungerichtete Abhängigkeiten; Versionsbezug von Schnittstellen; Abgrenzung zu „Zeit und Status“ bei Versionskonflikten.
- **Untertypen:** offen.
- **Annotationsregeln:** offen.
- **Beispiele:** offen.
- **Status:** offen.

## 5. Querschnittsfragen (offen)

- Mehrfachzuordnung: Kann eine Inkonsistenz mehreren Obertypen angehören? Regel für Primärtyp?
- Schweregrad und Sicherheit: Werden Schwere und Annotationskonfidenz mitgeführt?
- Bezugseinheit: Aussagepaar, Aussagegruppe, Dokumentpaar?
- Nicht-Inkonsistenzen: Wie werden Scheinwidersprüche (Kontext, Bedingungen, Zeitbezug) als Negativbeispiele erfasst?
- Sprache: Deutsch, Englisch, gemischt?

## 6. Änderungshistorie

| Datum | Änderung |
|---|---|
| 17.09.2026 | Erstfassung: Obertypen, Statusdefinition, vorläufige Arbeitsdefinitionen, offene Fragen |
