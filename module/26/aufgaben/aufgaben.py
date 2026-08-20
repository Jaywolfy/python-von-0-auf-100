"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 26 · AUFGABEN — Skripte alltagstauglich machen            ║
║                                                                  ║
║  ⚠️ Die meisten Aufgaben ergeben eigene .py-Dateien, die du im   ║
║     Terminal aufrufst. Diese Datei ist deine Anleitung.          ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Erstes argparse-Skript
# ══════════════════════════════════════════════════════════════════
# Erstelle "gruss.py":
#   - Pflichtargument: name
#   - Optional: --gross (macht die Ausgabe groß)
#   - Optional: --anzahl N (Standard 1, wie oft gegrüßt wird)
#   - Optional: --sprache de/en/fr (Standard de)
#
# Teste:
#   python gruss.py Anna
#   python gruss.py Anna --gross --anzahl 3
#   python gruss.py Anna --sprache en
#   python gruss.py --help

# 👉 Dein Code (in gruss.py):



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Typen und Auswahlmöglichkeiten
# ══════════════════════════════════════════════════════════════════
# Erstelle "rechner.py":
#   - zwei Zahlen als Argumente (type=float!)
#   - --operation mit choices=["add","sub","mul","div"]
#   - --nachkomma N (Standard 2)
#   - Division durch 0 sauber abfangen und Exit-Code 1 zurückgeben
#
# 💡 parser.add_argument("--operation", choices=[...], default="add")

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Logging einrichten
# ══════════════════════════════════════════════════════════════════
# Erstelle "logging_demo.py", das:
#   - eine Logdatei UND die Konsole beschreibt
#   - alle 5 Level demonstriert
#   - mit --verbose auf DEBUG umschaltet
#   - einen Fehler mit log.exception() protokolliert (inkl. Traceback)
# Schau dir danach die Logdatei an!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Fortschrittsbalken
# ══════════════════════════════════════════════════════════════════
# Schreib fortschritt(aktuell, gesamt, breite=30), die zurückgibt:
#   [████████████░░░░░░░░░░░░░░░░░░]  40%  (12/30)
# Baue eine Demo mit time.sleep(0.05) über 50 Schritte,
# die den Balken in EINER Zeile aktualisiert (\r und end="").

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Konfigurationsdatei
# ══════════════════════════════════════════════════════════════════
# Schreib lade_konfig(pfad) mit dieser Priorität:
#   1. Kommandozeilenargumente
#   2. Konfigurationsdatei (JSON)
#   3. Eingebaute Standardwerte
# Demonstriere alle drei Fälle. Fehlerhafte JSON-Datei darf
# NICHT zum Absturz führen.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🔴 - Trockenlauf als Standard
# ══════════════════════════════════════════════════════════════════
# Erstelle "umbenenner.py":
#   - Ordner als Pflichtargument
#   - --praefix TEXT  (wird allen Dateien vorangestellt)
#   - --ausfuehren    (ohne dieses Flag: nur Trockenlauf!)
#   - --nur-endung .txt (nur bestimmte Dateien)
#   - Logging + Fortschrittsbalken
#   - Sauberer Exit-Code (0 = ok, 1 = Ordner fehlt, 2 = Fehler)
# ⚠️ Teste NUR in einem Testordner!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - README schreiben
# ══════════════════════════════════════════════════════════════════
# Schreib eine vollständige README.md für dein umbenenner.py:
#   - Was macht es? (ein Satz)
#   - Installation (max. 3 Befehle)
#   - Nutzung mit mindestens 3 Beispielen
#   - Alle Optionen als Tabelle
#   - Sicherheitshinweis zum Trockenlauf
#   - Bekannte Einschränkungen
#
# ✅ Test: Gib sie jemandem, der das Tool nicht kennt.
#    Kann er es in 5 Minuten benutzen?

# 👉 Deine README:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 ⭐ BONUS - Zeitsteuerung einrichten
# ══════════════════════════════════════════════════════════════════
# Richte ein, dass eines deiner Skripte automatisch läuft:
#   🪟 Windows: Aufgabenplanung
#   🍎🐧 macOS/Linux: crontab -e
#
# Empfehlung fürs Üben: ein Skript, das nur eine Zeile in eine
# Logdatei schreibt - alle 5 Minuten. Nach einer Stunde
# nachschauen, ob 12 Einträge da sind. ⏰
#
# ⚠️ Wichtig: ABSOLUTE Pfade + Python aus der venv!
#
# 👉 Notiere hier deine Konfiguration:



print("""
✅ Modul 26 ist Praxis, kein Lesen.

Deine Aufgabe ist nicht, diese Datei auszuführen -
sondern eigene Skripte zu bauen und im TERMINAL aufzurufen.

Schau dir als Vorlage an:
    module/26/beispiele/01_werkzeug.py

Und probier aus:
    python module/26/beispiele/01_werkzeug.py --help
""")
