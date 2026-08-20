# 🎁 Modul 26 — Skripte alltagstauglich machen

> ⏱️ ~5 Stunden · ⬅️ [Modul 25](../25/README.md) · ➡️ 🎓 [Capstone](../../projekte/capstone/README.md)

---

## 🎯 Lernziele

- [ ] Skripte mit `argparse` konfigurierbar machen
- [ ] `logging` statt `print` einsetzen
- [ ] Konfigurationsdateien nutzen
- [ ] Skripte zeitgesteuert ausführen ⏰
- [ ] ein Projekt so übergeben, dass andere es benutzen können

---

## 🌍 Warum das wichtig ist

Der Unterschied zwischen einem **Skript** und einem **Werkzeug**:

```text
❌ Skript                          ✅ Werkzeug
   Pfad steht im Code fest            Pfad als Argument
   print() überall                    saubere Logdatei
   nur du kannst es starten           README + requirements
   du musst es manuell starten        läuft automatisch jeden Morgen
```

Das ist das letzte Modul — und es macht aus allem, was du gebaut hast, etwas, das **wirklich benutzt** wird. 🎉

---

## 📖 Die Lektion

### 1. ⭐ `argparse` — Skripte konfigurierbar machen

```python
import argparse
from pathlib import Path

def parse_argumente():
    parser = argparse.ArgumentParser(
        description="Sortiert Dateien nach Typ in Unterordner.",
        epilog="Beispiel: python aufraeumer.py ~/Downloads --ausfuehren",
    )
    parser.add_argument("ordner", type=Path,
                        help="Der aufzuräumende Ordner")
    parser.add_argument("-a", "--ausfuehren", action="store_true",
                        help="Änderungen wirklich durchführen (sonst Trockenlauf)")
    parser.add_argument("-b", "--backup", action="store_true",
                        help="Vorher ein ZIP-Backup anlegen")
    parser.add_argument("--log", type=Path, default=None,
                        help="Pfad zur Logdatei")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Ausführliche Ausgabe")
    return parser.parse_args()

args = parse_argumente()
print(args.ordner, args.ausfuehren)
```

```bash
python aufraeumer.py ~/Downloads
python aufraeumer.py ~/Downloads --ausfuehren --backup
python aufraeumer.py --help          # 🎁 Hilfe gibt's geschenkt!
```

💡 `--help` erzeugt argparse **automatisch** aus deinen Beschreibungen. Deshalb: gute `help=`-Texte schreiben.

> 🛡️ **Sicherheits-Muster:** Mach den **Trockenlauf zum Standard** und das Ausführen zur Option (`--ausfuehren`). Dann kann ein vergessenes Flag nie Schaden anrichten.

### 2. 📝 `logging` statt `print`

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)-8s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler(),        # zusätzlich auf den Bildschirm
    ],
)

log = logging.getLogger(__name__)

log.debug("Details für die Fehlersuche")
log.info("Normale Statusmeldung")
log.warning("Achtung, aber es geht weiter")
log.error("Etwas ist schiefgegangen")
log.critical("Schwerer Fehler")
```

| Warum besser als `print`? |
|---|
| ⏱️ Zeitstempel automatisch |
| 🎚️ Level filterbar (`--verbose` → DEBUG, sonst INFO) |
| 📄 gleichzeitig in Datei **und** auf den Bildschirm |
| 🔇 abschaltbar, ohne den Code zu ändern |
| 🔍 nachvollziehbar, was um 3 Uhr nachts passiert ist |

```python
try:
    ...
except Exception:
    log.exception("Fehler beim Verarbeiten")   # ⭐ inkl. Traceback in die Logdatei!
```

### 3. ⚙️ Konfigurationsdateien

```python
import json
from pathlib import Path

STANDARD = {"quellordner": "~/Downloads", "backup": True, "log_level": "INFO"}

def lade_konfig(pfad=Path("konfig.json")):
    """Lädt die Konfiguration, ergänzt fehlende Werte durch Standardwerte."""
    konfig = STANDARD.copy()
    if pfad.exists():
        konfig.update(json.loads(pfad.read_text(encoding="utf-8")))
    return konfig
```

**Reihenfolge der Priorität** (so machen es Profis):

```text
1. Kommandozeilen-Argumente    (höchste Priorität)
2. Umgebungsvariablen (.env)
3. Konfigurationsdatei
4. Eingebaute Standardwerte    (niedrigste)
```

### 4. ⏰ Automatisch ausführen lassen

<details>
<summary>🪟 <b>Windows — Aufgabenplanung</b></summary>

1. `Win` → *„Aufgabenplanung"* öffnen
2. *Einfache Aufgabe erstellen…*
3. Trigger: z. B. täglich 08:00
4. Aktion: *Programm starten*
   - Programm: `C:\Pfad\zum\projekt\.venv\Scripts\python.exe`
   - Argumente: `C:\Pfad\zum\projekt\src\haupt.py --ausfuehren`
   - Starten in: `C:\Pfad\zum\projekt`

⚠️ **Immer absolute Pfade!** Und den Python aus der **venv**, nicht den System-Python.
</details>

<details>
<summary>🍎🐧 <b>macOS / Linux — cron</b></summary>

```bash
crontab -e
```

```cron
# Minute Stunde Tag Monat Wochentag  Befehl
0 8 * * *   /pfad/projekt/.venv/bin/python /pfad/projekt/haupt.py >> /pfad/cron.log 2>&1
0 8 * * 1   ...    # jeden Montag 8 Uhr
*/30 * * * * ...   # alle 30 Minuten
```
</details>

### 5. 📊 Fortschritt anzeigen

```python
def fortschritt(aktuell, gesamt, breite=30):
    """Gibt einen Fortschrittsbalken zurück."""
    anteil = aktuell / gesamt
    gefuellt = int(anteil * breite)
    return f"[{'█' * gefuellt}{'░' * (breite - gefuellt)}] {anteil:>4.0%}"

for i, datei in enumerate(dateien, start=1):
    print(f"\r{fortschritt(i, len(dateien))} {datei.name[:30]:<30}", end="")
print()
```

Oder mit `tqdm` (`pip install tqdm`):

```python
from tqdm import tqdm
for datei in tqdm(dateien, desc="Verarbeite"):
    ...
```

### 6. 📦 Das fertige Projekt

```text
mein-werkzeug/
├── README.md               ← Was, Installation, Nutzung, Beispiele
├── requirements.txt
├── .gitignore
├── .env.beispiel           ← Vorlage ohne echte Geheimnisse
├── konfig.beispiel.json
├── src/
│   └── mein_werkzeug/
│       ├── __init__.py
│       ├── haupt.py        ← argparse + main()
│       ├── kern.py         ← die eigentliche Logik
│       └── werkzeuge.py
└── tests/
    └── test_kern.py
```

### 7. ✅ Übergabe-Checkliste

```text
□ README erklärt Zweck in einem Satz
□ Installation in ≤ 3 Befehlen
□ Mindestens ein Nutzungsbeispiel
□ --help funktioniert und ist verständlich
□ requirements.txt vollständig
□ .env.beispiel vorhanden (ohne echte Keys!)
□ Fehler werden abgefangen und geloggt
□ Trockenlauf ist der Standard 🛡️
□ Tests laufen grün
□ Auf einem frischen Rechner/venv getestet
```

> 🧠 **Der ehrlichste Test:** Lösch deine venv, klone das Repo in einen neuen Ordner und folge deiner eigenen README. Wenn es funktioniert, ohne dass du etwas „aus dem Kopf" ergänzen musst — dann ist es fertig. ✅

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

---

## 🛠️ Mini-Projekt: Ein altes Projekt „produktionsreif" machen

Nimm dein bestes bisheriges Projekt und rüste es komplett aus:

- [ ] `argparse` mit mindestens 4 Optionen
- [ ] `logging` in Datei + Konsole, Level per `--verbose` steuerbar
- [ ] Konfigurationsdatei mit Standardwerten
- [ ] Fortschrittsanzeige
- [ ] Vollständige Fehlerbehandlung
- [ ] README, die jemand anderes versteht
- [ ] Zeitgesteuerte Ausführung eingerichtet ⏰

---

## 🧠 Selbsttest

1. Wofür `argparse`?
2. Was macht `action="store_true"`?
3. Warum `logging` statt `print`?
4. Welche fünf Log-Level gibt es?
5. Was macht `log.exception()` besonders?
6. Wie ist die Prioritätsreihenfolge der Konfiguration?
7. Wie startest du ein Skript zeitgesteuert?
8. Warum sollte der Trockenlauf der Standard sein?
9. Was gehört in eine `.env.beispiel`?
10. ✍️ Was ist dein ehrlichster Test dafür, ob ein Projekt fertig ist?

<details>
<summary>💡 Antworten</summary>

1. Um Skripte über Kommandozeilen-Argumente konfigurierbar zu machen — inkl. automatischer `--help`.
2. Macht aus der Option einen Schalter: vorhanden = `True`, sonst `False`.
3. Zeitstempel, Level, gleichzeitig Datei + Konsole, filterbar, abschaltbar.
4. DEBUG, INFO, WARNING, ERROR, CRITICAL.
5. Es schreibt zusätzlich den kompletten Traceback in die Logdatei.
6. Argumente → Umgebungsvariablen → Konfigdatei → Standardwerte.
7. Windows: Aufgabenplanung. macOS/Linux: cron.
8. Weil ein vergessenes Flag dann keinen Schaden anrichten kann. 🛡️
9. Die **Namen** aller benötigten Variablen — aber keine echten Werte.
10. Frische venv, Repo neu klonen, nur der eigenen README folgen — läuft es?
</details>

---

## 🔄 Wiederholung (Modul 23–25)

1. Warum `time.sleep()` beim Scrapen?
2. Wozu `data_only=True`?
3. Was macht ein Trockenlauf?
4. Warum Duplikate per Hash suchen?

---

## 🔗 Vertiefung

- 📖 [argparse-Tutorial](https://docs.python.org/3/howto/argparse.html)
- 📖 [logging-HOWTO](https://docs.python.org/3/howto/logging.html)
- 📖 [Real Python — Command Line Interfaces](https://realpython.com/command-line-interfaces-python-argparse/)

---

<div align="center">

## 🎓 Das war das letzte Modul!

Du hast **27 Module, 6 Projekte und über 200 Aufgaben** hinter dir.

**➡️ [Weiter zum Capstone-Projekt](../../projekte/capstone/README.md)** 🏆

</div>
