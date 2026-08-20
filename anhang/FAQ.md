# ❓ FAQ — Häufige Fragen

---

## 🎓 Zum Kurs

<details>
<summary><b>Ich habe eine Woche verpasst. Muss ich aufholen?</b></summary>

Nein. Mach genau da weiter, wo du aufgehört hast. Der Plan ist ein Vorschlag, kein Vertrag.

**Einzige Empfehlung:** Vor dem Weitermachen einen Wiederholtag einlegen — Selbsttests der letzten zwei Module aus dem Kopf beantworten. Dann geht es leichter weiter.
</details>

<details>
<summary><b>Kann ich Module überspringen?</b></summary>

Kurz: nein.

Die Module bauen strikt aufeinander auf. Wer Modul 08 (Funktionen) überspringt, versteht Modul 14 (Klassen) garantiert nicht — und wer Modul 05 (Schleifen) überspringt, kommt bei Listen nicht weiter.

**Ausnahme:** Wenn du **alle** Selbsttestfragen eines Moduls ohne Nachschauen beantworten kannst, darfst du die Übungen kürzen.
</details>

<details>
<summary><b>Ich verstehe ein Modul einfach nicht. Was tun?</b></summary>

In dieser Reihenfolge:

1. **Beispiele nochmal abtippen** — nicht lesen, tippen
2. Code auf [pythontutor.com](https://pythontutor.com/visualize.html) Schritt für Schritt ansehen
3. Ein **anderes** Erklärvideo suchen (Corey Schafer, Real Python)
4. Dem Thema **einen Tag Pause** geben — oft klickt es dann von selbst
5. Ganz kleines eigenes Beispiel bauen: 3 Zeilen, die genau dieses eine Konzept nutzen
6. Jemanden fragen (r/learnpython, Python Discord)

**Wenn es nach all dem immer noch nicht sitzt:** weitermachen. Manche Konzepte versteht man erst, wenn man sie später gebraucht hat.
</details>

<details>
<summary><b>Wie viel Zeit brauche ich wirklich?</b></summary>

Der Plan rechnet mit **1 Stunde an 6 Tagen pro Woche** = ~160 Stunden in 26 Wochen.

Realistisch:
- 30 Min/Tag → ca. 52 Wochen
- 1 h/Tag → ca. 26 Wochen
- 2 h/Tag → ca. 15 Wochen (aber Tag 6 nie streichen!)

**Wichtiger als die Menge ist die Regelmäßigkeit.** 25 Minuten täglich schlagen 3 Stunden am Sonntag. Jedes Mal.
</details>

<details>
<summary><b>Soll ich nebenbei noch andere Kurse machen?</b></summary>

**Maximal einen.** Und erst, wenn du Teil 1 durch hast.

Zwischen mehreren Kursen zu springen ist die beliebteste Art, sechs Monate zu verlieren, ohne etwas zu können. Was du brauchst, ist nicht mehr Material — es ist mehr Übung.
</details>

---

## 🐍 Zu Python

<details>
<summary><b>Python 3.12, 3.13 oder 3.14 — welche Version?</b></summary>

Jede 3.12 oder neuer ist völlig in Ordnung. Nimm einfach die aktuellste von [python.org](https://www.python.org/downloads/).

Nur eines ist wichtig: **kein Python 2**. Wenn du irgendwo `print "hallo"` ohne Klammern siehst — veraltet, ignorieren. ⚰️
</details>

<details>
<summary><b>Brauche ich Mathe?</b></summary>

Grundrechenarten. Wirklich.

Programmieren ist viel näher an Kochrezepten und Logikrätseln als an Analysis. Für Data Science oder Machine Learning wird später Statistik nützlich — für alles in diesem Kurs nicht.
</details>

<details>
<summary><b>Muss ich Englisch können?</b></summary>

Grundkenntnisse helfen sehr — Fehlermeldungen, Dokumentation und Stack Overflow sind englisch.

**Aber:** Die 30 wichtigsten Wörter lernst du in den ersten Wochen nebenbei (`error`, `expected`, `not defined`, `invalid`, `missing`, `list`, `string`, …). Und im Zweifel: Fehlermeldung in den Übersetzer werfen. Kein Grund aufzuhören.
</details>

<details>
<summary><b>Was ist der Unterschied zwischen Python und Anaconda?</b></summary>

Anaconda ist eine Python-Distribution mit vielen vorinstallierten Data-Science-Paketen. Für diesen Kurs **nicht nötig** und eher verwirrend (eigener Paketmanager, große Installation).

Nimm das normale Python von python.org + venv. Sauberer und du verstehst besser, was passiert.
</details>

---

## 🛠️ Technische Probleme

<details>
<summary><b>"python wird nicht als Befehl erkannt"</b></summary>

1. Terminal **komplett schließen und neu öffnen** (löst es in 60 % der Fälle)
2. `python3` statt `python` probieren
3. Du hast beim Installieren den Haken *„Add python.exe to PATH"* vergessen → Installer erneut starten → *Modify* → PATH aktivieren
</details>

<details>
<summary><b>"ModuleNotFoundError: No module named 'xyz'"</b></summary>

Drei mögliche Ursachen:

1. Paket nicht installiert → `pip install xyz`
2. **venv nicht aktiviert** → steht `(.venv)` vorne in der Zeile?
3. VS Code nutzt einen anderen Interpreter → `Strg+Shift+P` → *„Python: Select Interpreter"* → den aus `.venv` wählen
</details>

<details>
<summary><b>Mein Code ändert sich nicht, egal was ich mache</b></summary>

**Hast du gespeichert?** `Strg + S` 😄

Kein Witz — das ist der häufigste Grund. Stell in VS Code Auto-Speichern ein:
`"files.autoSave": "afterDelay"` (steht schon in der SETUP.md-Konfiguration).
</details>

<details>
<summary><b>Mein Programm hängt und reagiert nicht mehr</b></summary>

`Strg + C` im Terminal. Das bricht das laufende Programm ab.

Meist ist es eine Endlosschleife: eine `while`-Bedingung, die nie `False` wird. Prüf, ob der Zähler in der Schleife wirklich verändert wird.
</details>

<details>
<summary><b>Umlaute werden als ï¿½ oder Kästchen angezeigt</b></summary>

Encoding-Problem. Beim Öffnen von Dateien **immer** angeben:

```python
open("datei.txt", encoding="utf-8")
```

Bei Excel-Exporten hilft manchmal `encoding="utf-8-sig"` oder `encoding="cp1252"`.
</details>

<details>
<summary><b>IndentationError, obwohl alles richtig aussieht</b></summary>

Du hast Tabs und Leerzeichen gemischt — sieht identisch aus, ist es aber nicht.

Fix: `Strg+Shift+P` → *„Convert Indentation to Spaces"*.
Und installier **indent-rainbow** — dann siehst du solche Probleme sofort. 🌈
</details>

---

## 🧠 Motivation & Lernen

<details>
<summary><b>Ich habe keine Lust mehr. Woche 6 ist zäh.</b></summary>

Das ist **vorhergesagt**, nicht ungewöhnlich. Woche 4–8 ist bei fast allen das Tief: Der Anfangsreiz ist weg, aber du kannst noch nichts Beeindruckendes bauen.

Was hilft:
- 🎯 Ziel drastisch runterschrauben: **10 Minuten** statt einer Stunde. Aber täglich.
- 🛠️ Etwas Dummes bauen, das Spaß macht (ein Programm, das dich beleidigt, wenn du falsch rätst 😄)
- 📓 Journal von Woche 1 lesen — *„Was, DAS war mal schwer für mich?"*
- 👥 Jemandem davon erzählen. Öffentliche Zusagen halten besser.
- 🧱 Denk dran: Du legst gerade das Fundament. Fundamente sehen nie beeindruckend aus.
</details>

<details>
<summary><b>Ich vergesse alles wieder. Bin ich zu dumm?</b></summary>

Nein — dein Gehirn arbeitet völlig normal. **Vergessen ist ein Feature, kein Bug.**

Was du brauchst, ist nicht mehr Intelligenz, sondern **Wiederholung**:
👉 [`anhang/SPACED_REPETITION.md`](SPACED_REPETITION.md)

Und: Der Wiederholtag (Tag 6) existiert genau dafür. Wer ihn streicht, vergisst. Wer ihn macht, behält.
</details>

<details>
<summary><b>Darf ich ChatGPT/Claude benutzen?</b></summary>

Als **Tutor** ja, als **Ghostwriter** nein.

| ✅ Erlaubt | ❌ Macht dich abhängig |
|---|---|
| „Warum kommt hier ein TypeError?" | „Schreib mir Aufgabe 5" |
| „Erklär mir Zeile 4 wie einem Anfänger" | Antwort kopieren, weiter |
| „Gib mir einen Hinweis, nicht die Lösung" | „Löse das für mich" |

**Eiserne Regel:** In den ersten 11 Modulen **keinen Code kopieren**. Erklärungen: gern. Code: selbst tippen.
</details>

<details>
<summary><b>Wie lange, bis ich einen Job finden könnte?</b></summary>

Ehrliche Antwort: Dieser Kurs allein reicht nicht. Er bringt dich auf solide Mittelstufe — das ist der Punkt, ab dem echtes Lernen erst anfängt.

Danach brauchst du:
- 🏗️ Mehrere echte Projekte (nicht Tutorials)
- 🎯 Eine Spezialisierung (Web, Data, Automatisierung, …)
- 🌳 Ein sichtbares GitHub-Profil
- ⏱️ Realistisch: weitere 6–18 Monate ernsthafte Praxis

**Aber:** Um deinen eigenen Alltag zu automatisieren, reicht dieser Kurs vollkommen. Und das ist ein sehr konkreter, sofort spürbarer Gewinn. 🎉
</details>

---

## 🤷 Noch eine Frage?

- 💬 [r/learnpython](https://www.reddit.com/r/learnpython/) — anfängerfreundlich, sehr aktiv
- 🇩🇪 [Python-Forum.de](https://www.python-forum.de/) — deutschsprachig
- 💬 [Python Discord](https://discord.gg/python) — Hilfe oft in Minuten
