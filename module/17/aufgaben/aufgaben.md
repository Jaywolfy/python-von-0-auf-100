# ⌨️ Modul 17 · Aufgaben (Terminal-Übungen)

> Dieses Modul übst du im **Terminal**. Hak jeden Schritt ab. ✅

---

## Aufgabe 1 🟢 — Erste venv

- [ ] Lege einen Ordner `uebung-venv` an
- [ ] Wechsle hinein
- [ ] Erstelle eine venv: `python -m venv .venv`
- [ ] Aktiviere sie
- [ ] Prüfe: Steht `(.venv)` vorne in der Zeile?
- [ ] `pip list` → wie viele Pakete sind installiert?
- [ ] `deactivate` → ist `(.venv)` weg?

**Notiere:** Wie viele Pakete waren in der frischen venv?

---

## Aufgabe 2 🟢 — Pakete installieren

- [ ] venv wieder aktivieren
- [ ] `pip install requests`
- [ ] `pip list` → was kam alles dazu? (mehr als nur requests!)
- [ ] `pip show requests` → welche Version? Welche Abhängigkeiten?
- [ ] Teste im Python-REPL:
  ```python
  import requests
  print(requests.__version__)
  ```

**Frage:** Warum wurden mehr Pakete installiert als nur `requests`?

---

## Aufgabe 3 🟡 — requirements.txt

- [ ] `pip install beautifulsoup4 openpyxl`
- [ ] `pip freeze > requirements.txt`
- [ ] Öffne die Datei — wie viele Zeilen?
- [ ] `deactivate`, dann `.venv`-Ordner **löschen**
- [ ] Neue venv anlegen und aktivieren
- [ ] `pip install -r requirements.txt`
- [ ] `pip list` → alles wieder da? 🎉

**Das ist der wichtigste Moment dieses Moduls.** Genau so gibst du später Projekte weiter.

---

## Aufgabe 4 🟡 — Isolation beweisen

- [ ] Lege ZWEI Ordner an: `projekt-a` und `projekt-b`
- [ ] In jedem eine eigene venv
- [ ] In A: `pip install requests==2.28.0`
- [ ] In B: `pip install requests` (neueste)
- [ ] Prüfe in beiden: `pip show requests` → Version
- [ ] Unterschiedlich? ✅ **Das ist der ganze Punkt von venv.**

---

## Aufgabe 5 🟡 — Projektstruktur

Baue diese Struktur auf:

```text
mein-werkzeug/
├── .venv/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   └── werkzeuge.py
├── tests/
└── daten/
    ├── eingabe/
    └── ausgabe/
```

- [ ] `.gitignore` mit den Standardeinträgen füllen
- [ ] `README.md` mit: Projektname, Zweck, Installation, Nutzung
- [ ] In `werkzeuge.py` drei Funktionen aus Modul 12 kopieren

---

## Aufgabe 6 🔴 — .env und Geheimnisse

- [ ] `pip install python-dotenv`
- [ ] Datei `.env` anlegen:
  ```text
  API_KEY=mein_geheimer_test_schluessel
  UMGEBUNG=entwicklung
  ```
- [ ] `.env` in die `.gitignore` eintragen
- [ ] Schreib `konfig_test.py`:
  ```python
  import os
  from dotenv import load_dotenv

  load_dotenv()
  print("Key:", os.environ.get("API_KEY"))
  print("Umgebung:", os.environ.get("UMGEBUNG"))
  print("Fehlt:", os.environ.get("GIBTSNICHT", "Standardwert"))
  ```
- [ ] Ausführen

**Frage:** Warum ist `os.environ.get()` besser als `os.environ[]`?

---

## Aufgabe 7 ⭐ Bonus — Der Wiederherstellungs-Test

Der ultimative Test, ob dein Projekt wirklich weitergabefähig ist:

- [ ] `.venv`-Ordner komplett löschen
- [ ] Alle `__pycache__`-Ordner löschen
- [ ] Neue venv anlegen
- [ ] `pip install -r requirements.txt`
- [ ] Projekt starten

**Läuft es ohne einen einzigen manuellen Handgriff?** Dann ist es fertig. ✅
Falls nicht: Was fehlte? Ergänze es in der README.

---

## 💡 Merkzettel

```bash
python -m venv .venv                 # anlegen
.venv\Scripts\activate               # 🪟 aktivieren
source .venv/bin/activate            # 🍎🐧 aktivieren
pip install <paket>                  # installieren
pip freeze > requirements.txt        # einfrieren
pip install -r requirements.txt      # wiederherstellen
deactivate                           # verlassen
```
