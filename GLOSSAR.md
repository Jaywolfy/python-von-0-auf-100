# 📔 Glossar — jeder Fachbegriff auf Deutsch erklärt

> Fachbegriffe sind in der Programmierung fast immer **englisch**. Das ist gut so — sonst findest du keine Hilfe im Netz. Hier steht, was sie bedeuten.
> 💡 Nutz `Strg + F` zum Suchen.

---

## 🔤 A–C

| Begriff | Aussprache/Deutsch | Bedeutung |
|---|---|---|
| **Argument** | Argument | Der konkrete Wert, den du einer Funktion beim Aufruf mitgibst. `len("hallo")` → `"hallo"` ist das Argument. |
| **Attribut** | Attribut | Eine Variable, die zu einem Objekt gehört. `hund.name` |
| **Boolean / bool** | „Buhlien" | Wahrheitswert: nur `True` oder `False`. |
| **Bug** | Fehler, „Wanze" | Ein Fehler im Programm. Kommt angeblich von einer echten Motte in einem Computer 1947. 🦋 |
| **Built-in** | eingebaut | Funktionen, die Python immer mitbringt: `print`, `len`, `sum`, `type`, … |
| **Bytecode** | — | Zwischenform, in die Python deinen Code übersetzt, bevor er läuft. Musst du nicht verstehen. |
| **Call / aufrufen** | aufrufen | Eine Funktion ausführen: `meine_funktion()`. Die Klammern sind der Aufruf! |
| **CLI** | Command Line Interface | Programm, das im Terminal per Texteingabe bedient wird. |
| **Comprehension** | — | Kurzschreibweise, um Listen/Dicts zu bauen: `[x*2 for x in zahlen]` |
| **Concatenation** | Verkettung | Strings aneinanderhängen: `"a" + "b"` → `"ab"` |
| **Constructor** | Konstruktor | Die `__init__`-Methode — läuft, wenn ein Objekt erzeugt wird. |

## 🔤 D–F

| Begriff | Deutsch | Bedeutung |
|---|---|---|
| **Debugger** | Fehlersucher | Werkzeug, mit dem du dein Programm anhältst und Zeile für Zeile durchgehst. 🐞 |
| **Dictionary / dict** | Wörterbuch | Sammlung aus Schlüssel-Wert-Paaren: `{"name": "Anna", "alter": 30}` |
| **Docstring** | — | Text direkt unter `def`, der die Funktion beschreibt. In `"""dreifachen Anführungszeichen"""`. |
| **Dunder** | Double Underscore | Methoden mit doppelten Unterstrichen: `__init__`, `__str__`. Python ruft sie automatisch auf. |
| **Encoding** | Zeichenkodierung | Wie Text als Bytes gespeichert wird. Nimm **immer** `utf-8`. |
| **Exception** | Ausnahme | Ein Fehler zur Laufzeit, den man abfangen kann (`try`/`except`). |
| **Expression** | Ausdruck | Etwas, das einen **Wert ergibt**: `3 + 4`, `len(x)`, `a > b` |
| **f-String** | Format-String | `f"Hallo {name}"` — Variablen direkt in Text einsetzen. Die moderne Art. ⭐ |
| **Float** | Fließkommazahl | Zahl mit Nachkommastellen: `3.14`. Achtung: **Punkt**, kein Komma! |
| **Framework** | Rahmenwerk | Große Bibliothek, die die Struktur deines Programms vorgibt (z. B. Django). |
| **Function** | Funktion | Benannter, wiederverwendbarer Codeblock. Mit `def` definiert. |

## 🔤 G–L

| Begriff | Deutsch | Bedeutung |
|---|---|---|
| **Global** | global | Variable, die im ganzen Modul sichtbar ist (statt nur in einer Funktion). |
| **IDE** | Entwicklungsumgebung | Programm zum Programmieren. Deins: **VS Code**. |
| **Immutable** | unveränderlich | Kann nach dem Erstellen nicht geändert werden: `str`, `int`, `tuple`. |
| **Import** | einbinden | Code aus anderen Dateien/Bibliotheken nutzbar machen: `import math` |
| **Indentation** | Einrückung | Die Leerzeichen am Zeilenanfang. In Python **bestimmen sie die Logik** — nicht nur Optik! ⚠️ |
| **Index** | Index | Positionsnummer in einer Liste/String. **Beginnt bei 0!** |
| **Integer / int** | Ganzzahl | Zahl ohne Nachkomma: `42`, `-7` |
| **Interpreter** | — | Das Programm, das deinen Python-Code ausführt. |
| **Iterable** | iterierbar | Alles, worüber man mit `for` laufen kann: Listen, Strings, Dicts, … |
| **Keyword** | Schlüsselwort | Reserviertes Wort von Python: `if`, `for`, `def`, `class`, `return`, … |
| **Lambda** | — | Winzige namenlose Funktion: `lambda x: x * 2` |
| **Library / Bibliothek** | — | Sammlung von fertigem Code, den du benutzen kannst. |
| **Linter** | — | Werkzeug, das deinen Code auf Fehler & Stil prüft (z. B. Ruff). 🧼 |
| **List** | Liste | Geordnete, veränderbare Sammlung: `[1, 2, 3]` |
| **Loop** | Schleife | Wiederholung: `for` oder `while` |

## 🔤 M–R

| Begriff | Deutsch | Bedeutung |
|---|---|---|
| **Method** | Methode | Funktion, die zu einem Objekt gehört: `"text".upper()` |
| **Module** | Modul | Eine `.py`-Datei mit Code, den man importieren kann. |
| **Mutable** | veränderlich | Kann nachträglich geändert werden: `list`, `dict`, `set` |
| **Object** | Objekt | Eine konkrete „Sache" im Programm. In Python ist **alles** ein Objekt. |
| **OOP** | Objektorientierte Programmierung | Code um Objekte herum organisieren (Modul 14/15). |
| **Package** | Paket | Ordner mit mehreren Modulen. Oder: etwas, das man mit `pip` installiert. |
| **Parameter** | Parameter | Der Platzhalter in der Funktionsdefinition. `def gruss(name)` → `name` ist Parameter. |
| **PATH** | — | Systemvariable, die sagt, wo Programme liegen. Grund für „python nicht gefunden". |
| **PEP 8** | — | Der offizielle Python-Stilguide. Wie man Code formatiert. |
| **pip** | — | Pythons Paketmanager: `pip install requests` |
| **Parsen** | zerlegen/auswerten | Rohdaten (Text) in eine nutzbare Struktur umwandeln. |
| **REPL** | — | Die interaktive Python-Konsole (tippe `python` im Terminal). Zum Ausprobieren. 🧪 |
| **Refactoring** | Umbau | Code verbessern, **ohne** sein Verhalten zu ändern. ♻️ |
| **Regex** | Regulärer Ausdruck | Suchmuster für Text: `\d{5}` findet Postleitzahlen. |
| **Return** | Rückgabe | Was eine Funktion als Ergebnis zurückliefert. Ohne `return` → `None`. |

## 🔤 S–Z

| Begriff | Deutsch | Bedeutung |
|---|---|---|
| **Scope** | Gültigkeitsbereich | Wo eine Variable sichtbar ist. Innerhalb einer Funktion ≠ außerhalb. |
| **Set** | Menge | Sammlung ohne Duplikate, ungeordnet: `{1, 2, 3}` |
| **Slicing** | Ausschneiden | Teilbereich holen: `liste[2:5]`, `text[:3]` |
| **Snake_case** | — | Pythons Namensstil: `mein_langer_name` (Kleinbuchstaben + Unterstriche). |
| **Stack Trace / Traceback** | Fehlerprotokoll | Die Fehlerausgabe. **Lies sie von unten nach oben!** 🔍 |
| **Standard Library** | Standardbibliothek | Alles, was Python ohne Installation mitbringt (`os`, `json`, `datetime`, …). |
| **String / str** | Zeichenkette | Text: `"Hallo"` |
| **Syntax** | — | Die Grammatikregeln der Sprache. `SyntaxError` = Tippfehler. |
| **Terminal / Shell** | Konsole | Das schwarze Fenster für Textbefehle. 🖥️ |
| **Truthiness** | Wahrheitsgehalt | Was Python als „wahr" wertet: alles außer `0`, `""`, `[]`, `{}`, `None`, `False`. |
| **Tuple** | Tupel | Unveränderliche Liste: `(1, 2, 3)` |
| **Type Hint** | Typangabe | Optionale Notiz zum Typ: `def f(x: int) -> str:` (Modul 19). |
| **Unpacking** | Entpacken | `a, b = (1, 2)` — mehrere Werte auf einmal zuweisen. |
| **venv** | virtuelle Umgebung | Isolierter Python-Bereich pro Projekt (Modul 17). 📦 |
| **Whitespace** | Leerraum | Leerzeichen, Tabs, Zeilenumbrüche. In Python **bedeutungstragend**! |
| **Wrapper** | Hülle | Code, der anderen Code umschließt und ergänzt. |

---

## 🎯 Die 12 Begriffe, die du zuerst brauchst

Wenn dir das alles zu viel ist — merk dir zuerst nur diese:

```text
1.  Variable      → beschrifteter Karton für einen Wert
2.  String        → Text
3.  Integer       → ganze Zahl
4.  Liste         → nummerierte Sammlung
5.  Dictionary    → Sammlung mit Namensschildern
6.  Funktion      → wiederverwendbarer Baustein
7.  Argument      → was du einer Funktion mitgibst
8.  Return        → was eine Funktion zurückgibt
9.  Schleife      → Wiederholung
10. Bedingung     → Entscheidung (if)
11. Einrückung    → bestimmt, was zusammengehört
12. Traceback     → die Fehlermeldung (dein Freund! 🔍)
```

Alles andere kommt von selbst. 😊
