# ✅ Modul 17 · Lösungen & Erklärungen

## Aufgabe 1
Eine frische venv enthält je nach Python-Version **0–2 Pakete** (`pip`, oft `setuptools`).
Das ist der Punkt: Du startest **sauber**, ohne den Ballast des Systems.

## Aufgabe 2
`pip install requests` installiert zusätzlich:
`urllib3`, `certifi`, `charset-normalizer`, `idna`.

**Warum?** Das sind **Abhängigkeiten** (dependencies). `requests` benutzt sie intern.
pip löst den kompletten Abhängigkeitsbaum automatisch auf — deshalb schreibt man
in Python selten alles selbst.

## Aufgabe 3
`requirements.txt` enthält **alle** Pakete inklusive Abhängigkeiten — meist 10–15 Zeilen,
obwohl du nur 3 installiert hast.

> 💡 Für größere Projekte nutzt man Werkzeuge wie `pip-tools` oder `uv`, die zwischen
> „direkt gewollt" und „nur mitgezogen" unterscheiden. Für dich reicht `pip freeze` völlig.

## Aufgabe 4
```text
projekt-a: requests 2.28.0
projekt-b: requests 2.32.x
```
Zwei Versionen desselben Pakets, gleichzeitig, ohne Konflikt.
**Ohne venv wäre das unmöglich** — es kann nur eine Version im System geben.

## Aufgabe 5 — Beispiel `.gitignore`

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
env/
.env
.vscode/
.idea/
.DS_Store
*.log
daten/ausgabe/
```

## Beispiel `README.md`

```markdown
# Mein Werkzeug

Kleines Tool, das X automatisiert.

## Installation

    python -m venv .venv
    .venv\Scripts\activate       # Windows
    pip install -r requirements.txt

## Nutzung

    python src/haupt.py --eingabe daten/eingabe

## Anforderungen
Python 3.12+
```

**Faustregel für eine gute README:** Jemand, der das Projekt zum ersten Mal sieht,
muss es in **unter 5 Minuten** zum Laufen bringen. Ohne dich zu fragen.

## Aufgabe 6
`os.environ["KEY"]` wirft einen `KeyError`, wenn die Variable fehlt — das Programm
stürzt ab. `os.environ.get("KEY", "standard")` gibt einen Standardwert zurück.

**Faustregel:**
- Ohne den Wert läuft nichts (z. B. Datenbank-Passwort) → `[]`, damit es früh und laut kracht
- Es gibt einen sinnvollen Standardwert → `.get()`

## Aufgabe 7
Häufige Stolpersteine beim Wiederherstellungs-Test:

| Problem | Ursache |
|---|---|
| `ModuleNotFoundError` | Paket manuell installiert, aber nie eingefroren |
| `FileNotFoundError` | Ordner wie `daten/ausgabe/` existiert nicht (ist in `.gitignore`!) |
| `KeyError: 'API_KEY'` | `.env` fehlt → lege eine `.env.beispiel` an! |

> 💡 **Profi-Tipp:** Lege eine `.env.beispiel` mit leeren Werten an und committe **die**.
> So weiß jeder, welche Variablen gebraucht werden — ohne dass Geheimnisse im Repo landen.

```text
# .env.beispiel
API_KEY=
UMGEBUNG=entwicklung
```

🎉 **Modul 17 geschafft!** Deine Projekte sind jetzt weitergabefähig.
