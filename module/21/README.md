# 🔍 Modul 21 — Reguläre Ausdrücke (Regex)

> ⏱️ ~5 Stunden · ⬅️ [Modul 20](../20/README.md) · ➡️ [Modul 22](../22/README.md)

---

## 🎯 Lernziele

- [ ] Suchmuster lesen und schreiben
- [ ] `re.search`, `findall`, `sub`, `split` benutzen
- [ ] Gruppen einsetzen, um Teile herauszuziehen
- [ ] wissen, **wann Regex die falsche Wahl** ist

---

## 🌍 Warum das wichtig ist

Regex ist eine **Mustersprache für Text**. Alles, was du sonst mit 30 Zeilen `if` und `split` bauen würdest, wird zu einer Zeile:

```python
re.findall(r"\d{5}", text)                 # alle Postleitzahlen
re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", t)  # alle E-Mail-Adressen
re.sub(r"\s+", " ", text)                  # mehrfache Leerzeichen normalisieren
```

Rechnungen, Logdateien, Exporte, Webseiten — überall, wo Text ein Muster hat, ist Regex das schnellste Werkzeug. 🔍

> ⚠️ **Aber:** Regex ist berüchtigt schwer lesbar. Es gibt den Klassiker: *„Du hattest ein Problem, jetzt hast du zwei."* Nutze es gezielt — nicht für alles.

---

## 📖 Die Lektion

> 💡 **Übe alles hier live mit:** 👉 **[regex101.com](https://regex101.com/)** (Flavor: Python). Die Seite erklärt jedes Zeichen deines Musters. Ohne sie ist Regex doppelt so schwer.

### 1. Der Einstieg

```python
import re

text = "Meine Nummer ist 0151-12345678"

treffer = re.search(r"\d+", text)      # r"" = raw string, IMMER benutzen!
if treffer:
    print(treffer.group())             # 0151
```

### 2. 🔤 Zeichenklassen

| Muster | Bedeutung |
|:---:|---|
| `\d` | eine Ziffer (0-9) |
| `\D` | keine Ziffer |
| `\w` | Buchstabe, Ziffer oder `_` |
| `\W` | keins davon |
| `\s` | Leerzeichen, Tab, Umbruch |
| `\S` | kein Leerraum |
| `.` | **jedes** Zeichen (außer `\n`) |
| `[abc]` | a, b **oder** c |
| `[a-z]` | ein Kleinbuchstabe |
| `[^abc]` | **nicht** a, b, c |

### 3. 🔢 Quantoren — wie oft?

| Muster | Bedeutung |
|:---:|---|
| `*` | 0 oder mehr |
| `+` | 1 oder mehr |
| `?` | 0 oder 1 (optional) |
| `{3}` | genau 3 |
| `{2,4}` | 2 bis 4 |
| `{2,}` | mindestens 2 |

```python
r"\d{5}"          # genau 5 Ziffern → Postleitzahl
r"\d{2,4}"        # 2 bis 4 Ziffern
r"colou?r"        # color oder colour
```

### 4. ⚓ Anker

| Muster | Bedeutung |
|:---:|---|
| `^` | Anfang der Zeichenkette |
| `$` | Ende |
| `\b` | Wortgrenze ⭐ |

```python
r"^Hallo"         # muss am Anfang stehen
r"\.txt$"         # muss auf .txt enden
r"\bKatze\b"      # das Wort Katze, nicht "Katzenfutter"
```

### 5. ⭐ Gruppen — Teile herausziehen

```python
datum = "26.07.2026"
treffer = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", datum)

treffer.group(0)       # '26.07.2026'   ganzer Treffer
treffer.group(1)       # '26'
treffer.group(3)       # '2026'
treffer.groups()       # ('26', '07', '2026')
```

**Benannte Gruppen** — deutlich lesbarer:

```python
muster = r"(?P<tag>\d{2})\.(?P<monat>\d{2})\.(?P<jahr>\d{4})"
t = re.search(muster, datum)
t.group("jahr")        # '2026'
t.groupdict()          # {'tag': '26', 'monat': '07', 'jahr': '2026'}
```

### 6. 🧰 Die vier Funktionen

```python
re.search(muster, text)     # ERSTER Treffer → Match-Objekt oder None
re.findall(muster, text)    # ALLE Treffer → Liste  ⭐ am häufigsten
re.finditer(muster, text)   # ALLE als Match-Objekte (mit Position)
re.sub(muster, ersatz, t)   # ersetzen
re.split(muster, text)      # an Muster zerlegen
re.match(muster, text)      # nur am ANFANG (selten gebraucht)
```

⚠️ `search` sucht überall, `match` nur ganz am Anfang. Klassische Verwechslung.

### 7. 🎛️ Nützliche Flags

```python
re.findall(muster, text, re.IGNORECASE)   # Groß/Klein egal
re.findall(muster, text, re.MULTILINE)    # ^ und $ je Zeile
re.findall(muster, text, re.DOTALL)       # . matcht auch \n
```

### 8. 😋 Gierig vs. genügsam

```python
text = "<b>fett</b> und <i>kursiv</i>"

re.findall(r"<.+>", text)     # ['<b>fett</b> und <i>kursiv</i>']  😱 gierig
re.findall(r"<.+?>", text)    # ['<b>', '</b>', '<i>', '</i>']     ✅ genügsam
```

Ein `?` nach dem Quantor macht ihn **genügsam** (nimmt so wenig wie möglich).

### 9. 🌍 Praktische Muster

```python
E_MAIL   = r"[\w.+-]+@[\w-]+\.[\w.]+"
PLZ_DE   = r"\b\d{5}\b"
DATUM_DE = r"\b\d{1,2}\.\d{1,2}\.\d{4}\b"
IBAN_DE  = r"\bDE\d{20}\b"
URL      = r"https?://[^\s]+"
TELEFON  = r"\+?\d[\d\s/-]{6,}\d"
EURO     = r"\d{1,3}(?:\.\d{3})*,\d{2}\s*€"
```

### 10. 🚫 Wann Regex NICHT

| Aufgabe | Besser mit |
|---|---|
| HTML parsen | BeautifulSoup (Modul 23) |
| JSON parsen | `json` (Modul 16) |
| CSV parsen | `csv` (Modul 16) |
| Einfache Prüfung | `.startswith()`, `in`, `.split()` |

```python
# ❌ Regex-Overkill
re.match(r"^bild\.png$", name)
# ✅
name == "bild.png"
```

> 🧠 **Faustregel:** Wenn eine String-Methode es kann → nimm die String-Methode. Regex erst, wenn es ein **variables Muster** gibt.

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `"\d"` statt `r"\d"` | Escape-Chaos | **immer** `r"..."` |
| `.` ohne Escape | matcht jedes Zeichen | `\.` für einen echten Punkt |
| gierige Quantoren | zu viel Treffer | `+?`, `*?` |
| `match` statt `search` | findet nichts | `search` nutzen |
| `treffer.group()` ohne Prüfung | `AttributeError` bei `None` | `if treffer:` |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

---

## 🛠️ Mini-Projekt: Datenextraktor 🔍

`extraktor.py` bekommt einen unstrukturierten Text (Rechnung, E-Mail, Notiz) und zieht heraus:

```text
════════════════════════════════════════
   EXTRAHIERTE DATEN
════════════════════════════════════════
📧 E-Mails:     2  →  buchhaltung@firma.de, ...
📞 Telefon:     1  →  +49 151 12345678
📅 Daten:       3  →  26.07.2026, ...
💶 Beträge:     4  →  1.234,56 €, ...
🏠 PLZ:         1  →  10115
🔗 URLs:        1  →  https://firma.de/rechnung
🏦 IBAN:        1  →  DE89370400440532013000
════════════════════════════════════════
```

**Bonus 🎁:** Ergebnis als JSON speichern (Modul 16).

---

## 🧠 Selbsttest

1. Warum immer `r"..."`?
2. Was matcht `\d{5}`?
3. Unterschied `search` / `findall` / `match`?
4. Wozu Gruppen?
5. Was macht `\b`?
6. Unterschied `+` und `+?`?
7. Wie ignorierst du Groß-/Kleinschreibung?
8. Wann ist Regex die falsche Wahl?
9. Wie matchst du einen echten Punkt?
10. ✍️ Schreib ein Muster für eine deutsche Postleitzahl mit Wortgrenzen.

<details>
<summary>💡 Antworten</summary>

1. Damit `\` nicht von Python selbst als Escape interpretiert wird.
2. Genau fünf Ziffern hintereinander.
3. `search` = erster Treffer irgendwo · `findall` = alle Treffer als Liste · `match` = nur am Anfang.
4. Um Teile aus einem Treffer gezielt herauszuziehen.
5. Eine Wortgrenze — verhindert Treffer mitten in längeren Wörtern.
6. `+` ist gierig (so viel wie möglich), `+?` genügsam (so wenig wie möglich).
7. Mit `re.IGNORECASE`.
8. Bei HTML, JSON, CSV oder wenn eine einfache String-Methode reicht.
9. Mit `\.`
10. `r"\b\d{5}\b"`
</details>

---

## 🔄 Wiederholung (Modul 18–20)

1. Was macht `@parametrize`?
2. Was ist eine magische Zahl?
3. Was macht `git restore --staged`?
4. Was gehört in `.gitignore`?

---

## 🔗 Vertiefung

- 🔍 [regex101.com](https://regex101.com/) ⭐ **unverzichtbar**
- 📖 [Python re-Doku](https://docs.python.org/3/library/re.html)
- 🎮 [RegexOne](https://regexone.com/) — interaktives Tutorial

**➡️ [Modul 22 — APIs & requests](../22/README.md)** 🌐
