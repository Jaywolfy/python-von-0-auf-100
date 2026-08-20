# 📦 Modul 17 — venv, pip & Projektstruktur

> ⏱️ ~4 Stunden · ⬅️ [Modul 16](../16/README.md) · ➡️ [Modul 18](../18/README.md)

---

## 🎯 Lernziele

- [ ] verstehen, **warum** virtuelle Umgebungen existieren
- [ ] eine venv anlegen, aktivieren, benutzen
- [ ] Pakete mit `pip` installieren und dokumentieren
- [ ] ein Projekt sauber strukturieren
- [ ] `.gitignore` und `requirements.txt`

---

## 🌍 Warum das wichtig ist

🏠 **Alltagsbild:** Stell dir vor, du hast **eine einzige Werkzeugkiste** für alle Projekte. Projekt A braucht Schraubenzieher Version 1, Projekt B Version 2. Du kannst nur eine haben → eines der Projekte geht kaputt.

Genau das passiert ohne venv:

```text
❌ Ohne venv                        ✅ Mit venv
                                    
System-Python                       Projekt A/.venv → requests 2.28
  ├─ requests 2.31  ← Projekt A     Projekt B/.venv → requests 2.31
  └─ Projekt B braucht 2.28 💥      Beide funktionieren 🎉
```

Ab hier arbeitest du **immer** mit venv. Das ist kein Extra für Profis — das ist Standard ab dem ersten Projekt mit Fremdpaketen.

---

## 📖 Die Lektion

### 1. venv anlegen und aktivieren

```bash
# Im Projektordner:
python -m venv .venv
```

**Aktivieren:**

| System | Befehl |
|---|---|
| 🪟 Windows (PowerShell) | `.venv\Scripts\activate` |
| 🍎🐧 macOS / Linux | `source .venv/bin/activate` |

✅ Erfolgreich, wenn vorne in der Zeile `(.venv)` steht:

```text
(.venv) C:\projekte\mein-tool>
```

**Verlassen:** `deactivate`

💡 **In VS Code viel einfacher:** `Strg+Shift+P` → *„Python: Create Environment"* → *venv* → fertig. VS Code aktiviert sie danach automatisch in jedem neuen Terminal. 🎉

<details>
<summary>🪟 <b>Windows: „Skriptausführung ist deaktiviert"</b></summary>

PowerShell **als Administrator** öffnen und einmalig ausführen:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
</details>

### 2. pip — Pakete installieren

```bash
pip install requests                 # neueste Version
pip install requests==2.31.0         # exakte Version
pip install -r requirements.txt      # alles aus Datei ⭐

pip list                             # was ist installiert?
pip show requests                    # Details
pip uninstall requests
```

### 3. ⭐ `requirements.txt`

```bash
pip freeze > requirements.txt        # aktuellen Stand einfrieren
```

```text
requests==2.31.0
beautifulsoup4==4.12.2
openpyxl==3.1.2
```

**Warum das zählt:** Damit kann jemand anderes (oder du in einem Jahr, auf einem anderen Rechner) dein Projekt mit **einem Befehl** lauffähig machen:

```bash
pip install -r requirements.txt
```

### 4. 🗂️ Projektstruktur

```text
mein-tool/
├── .venv/                  ← virtuelle Umgebung (NICHT in Git!)
├── .gitignore
├── README.md               ← was ist das, wie startet man es
├── requirements.txt
├── src/
│   └── mein_tool/
│       ├── __init__.py
│       ├── haupt.py
│       └── werkzeuge.py
├── tests/
│   └── test_werkzeuge.py
└── daten/
    ├── eingabe/
    └── ausgabe/
```

📌 Für kleine Skripte reicht auch flach — aber ab ~3 Dateien lohnt sich Struktur.

### 5. `.gitignore`

```gitignore
# Python
__pycache__/
*.pyc
.venv/
venv/

# Umgebung & Geheimnisse
.env
*.key

# Editor
.vscode/
.idea/
.DS_Store

# Ausgaben
*.log
daten/ausgabe/
```

> 🔐 **Wichtigste Regel:** `.venv/` und `.env` **niemals** ins Repo. Die venv ist groß und reproduzierbar, `.env` enthält Passwörter. Einmal gepusht = für immer in der Git-History.

### 6. 🔑 Geheimnisse: `.env`

```python
# .env  (NICHT committen!)
API_KEY=abc123geheim
```

```python
# im Code
import os
schluessel = os.environ.get("API_KEY")
```

Mit `python-dotenv` (`pip install python-dotenv`):

```python
from dotenv import load_dotenv
load_dotenv()
schluessel = os.environ["API_KEY"]
```

🚨 **Niemals** API-Keys direkt in den Code schreiben. Das ist der häufigste Sicherheitsfehler auf GitHub überhaupt.

### 7. 📋 Der Standard-Workflow für jedes neue Projekt

```bash
mkdir mein-projekt && cd mein-projekt
python -m venv .venv
.venv\Scripts\activate            # oder source .venv/bin/activate
pip install <was du brauchst>
pip freeze > requirements.txt
git init                          # Modul 20
```

Präg dir diese fünf Zeilen ein. Du wirst sie hunderte Male tippen. 💪

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| venv nicht aktiviert | `ModuleNotFoundError` | `(.venv)` in der Zeile prüfen |
| `.venv/` committet | Repo wird riesig | `.gitignore` |
| `requirements.txt` vergessen | niemand kann es starten | `pip freeze >` |
| API-Key im Code | 🚨 Sicherheitsleck | `.env` |
| VS Code nutzt falschen Interpreter | Pakete „fehlen" | `Python: Select Interpreter` |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.md`](aufgaben/aufgaben.md) — dieses Modul übst du im **Terminal**, nicht in einer `.py`-Datei.

---

## 🛠️ Mini-Projekt: Projekt sauber aufsetzen

Nimm eines deiner bisherigen Projekte und bring es in Form:

- [ ] eigener Ordner + `.venv`
- [ ] `README.md` (Was? Wie starten? Was wird gebraucht?)
- [ ] `requirements.txt`
- [ ] `.gitignore`
- [ ] Code in `src/`, Daten in `daten/`
- [ ] Test: venv löschen, neu anlegen, `pip install -r requirements.txt` — läuft es noch? ✅

---

## 🧠 Selbsttest

1. Wozu eine virtuelle Umgebung?
2. Wie legst du eine venv an?
3. Woran erkennst du, dass sie aktiv ist?
4. Was macht `pip freeze > requirements.txt`?
5. Wie installierst du alles aus einer requirements.txt?
6. Warum `.venv/` nicht in Git?
7. Wo gehören API-Keys hin?
8. Was gehört in eine `.gitignore`?
9. Wie wechselst du den Interpreter in VS Code?
10. ✍️ Erkläre venv mit einem eigenen Bild.

<details>
<summary>💡 Antworten</summary>

1. Um Paketversionen pro Projekt zu isolieren und Konflikte zu vermeiden.
2. `python -m venv .venv`
3. `(.venv)` steht vorne in der Terminal-Zeile.
4. Schreibt alle installierten Pakete mit Version in eine Datei.
5. `pip install -r requirements.txt`
6. Sie ist groß, plattformabhängig und jederzeit reproduzierbar.
7. In eine `.env`-Datei, die nicht ins Repo kommt.
8. `__pycache__/`, `.venv/`, `.env`, Editor-Ordner, Logs, generierte Ausgaben.
9. `Strg+Shift+P` → „Python: Select Interpreter".
10. Z. B.: „Eine venv ist eine eigene Werkzeugkiste pro Projekt statt einer gemeinsamen für alles."
</details>

---

## 🔄 Wiederholung (Modul 14–16)

1. Was ist `self`?
2. Wozu `ensure_ascii=False`?
3. Merksatz Vererbung vs. Komposition?
4. Warum `newline=""` bei CSV?

---

## 🔗 Vertiefung

- 📖 [Python venv Doku](https://docs.python.org/3/library/venv.html)
- 📖 [Real Python — Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

**➡️ [Modul 18 — Tests mit pytest](../18/README.md)** ✅
