# 🖥️ Spickzettel · Terminal

> Das Terminal ist kein Hacker-Werkzeug — es ist nur eine schnellere Art, dem Computer Befehle zu geben.

## Terminal öffnen
| System | Wie |
|---|---|
| 🪟 Windows | `Win` → „PowerShell" · oder in VS Code: `Strg + ö` |
| 🍎 macOS | `Cmd + Leertaste` → „Terminal" |
| 🐧 Linux | `Strg + Alt + T` |

## Navigation
| Aktion | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Wo bin ich? | `pwd` | `pwd` |
| Inhalt anzeigen | `ls` (oder `dir`) | `ls` |
| Ordner wechseln | `cd ordner` | `cd ordner` |
| Eine Ebene hoch | `cd ..` | `cd ..` |
| Nach Hause | `cd ~` | `cd ~` |
| Ordner erstellen | `mkdir neu` | `mkdir neu` |
| Datei erstellen | `ni datei.py` | `touch datei.py` |
| Löschen | `rm datei.py` | `rm datei.py` |
| Bildschirm leeren | `cls` | `clear` |

> 💡 **Tab-Taste = dein bester Freund.** Anfang tippen, `Tab` drücken → wird vervollständigt.
> 💡 **Pfeil ↑** holt den letzten Befehl zurück.

## Python im Terminal
```bash
python --version           # Version prüfen  (evtl. python3)
python skript.py           # Skript ausführen
python skript.py arg1      # mit Argumenten (Modul 26)
python                     # interaktive Konsole (REPL) starten
exit()                     # REPL verlassen
```

## pip (Pakete)
```bash
pip install requests        # installieren
pip install -r requirements.txt   # alle aus Datei
pip list                    # was ist installiert?
pip uninstall requests
pip freeze > requirements.txt     # aktuelle Pakete speichern
```

## Virtuelle Umgebungen (Modul 17)
```bash
python -m venv .venv                 # anlegen

# aktivieren:
.venv\Scripts\activate         # 🪟 Windows PowerShell
source .venv/bin/activate      # 🍎🐧 macOS/Linux

deactivate                     # verlassen
```
> Ist die venv aktiv, steht `(.venv)` vorne in der Zeile. ✅

## Notfall
| Situation | Lösung |
|---|---|
| 🛑 Programm hängt / Endlosschleife | `Strg + C` |
| 🚪 Aus REPL rauskommen | `exit()` oder `Strg + Z` + Enter (Win) / `Strg + D` (Mac) |
| 😵 Terminal reagiert komisch | Schließen und neu öffnen |
| 🔴 Windows: „Skriptausführung deaktiviert" | PowerShell als Admin: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
