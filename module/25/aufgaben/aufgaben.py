"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 25 · AUFGABEN — Dateien & Ordner automatisieren           ║
╠══════════════════════════════════════════════════════════════════╣
║  🛡️ SICHERHEIT: Alle Aufgaben arbeiten NUR im Ordner _uebung25,  ║
║     der automatisch angelegt wird. Deine echten Dateien sind     ║
║     nicht in Gefahr.                                             ║
║                                                                  ║
║  ⚠️ REGEL: Jede Funktion, die Dateien verändert, MUSS einen      ║
║     trockenlauf-Parameter haben (Standard: True)!                ║
╚══════════════════════════════════════════════════════════════════╝
"""
import shutil
from pathlib import Path

UEB = Path(__file__).parent / "_uebung25"

# --- Testumgebung aufbauen ------------------------------------------
if UEB.exists():
    shutil.rmtree(UEB)
UEB.mkdir()

DATEIEN = [
    "IMG_0001.jpg", "IMG_0002.jpg", "IMG_0003.JPG", "screenshot.png",
    "Rechnung Müller 2026-01.pdf", "Rechnung Schmidt 2026-02.pdf",
    "vertrag final v2.pdf", "Präsentation Q1.pptx",
    "notizen 2026.txt", "TODO.txt", "alte notiz.txt",
    "Budget 2026.xlsx", "kunden export.csv", "umsatz.xlsx",
    "song.mp3", "podcast folge 12.mp3", "urlaubsvideo.mp4",
    "backup.zip", "readme", "daten.json", "skript.py",
]
for name in DATEIEN:
    (UEB / name).write_text(f"Inhalt: {name}\n", encoding="utf-8")

# Duplikate
(UEB / "bericht.txt").write_text("Gleicher Inhalt hier.\n", encoding="utf-8")
(UEB / "bericht_kopie.txt").write_text("Gleicher Inhalt hier.\n", encoding="utf-8")
(UEB / "Bericht (1).txt").write_text("Gleicher Inhalt hier.\n", encoding="utf-8")

# Unterordner
(UEB / "Downloads alt").mkdir()
for name in ("altes_bild.jpg", "altes_dokument.pdf", "altes_lied.mp3"):
    (UEB / "Downloads alt" / name).write_text("alt\n", encoding="utf-8")

print(f"🧪 Testumgebung: {UEB}")
print(f"   {len(list(UEB.rglob('*')))} Einträge angelegt\n")


# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Überblick verschaffen
# ══════════════════════════════════════════════════════════════════
# Gib aus:
#   a) Anzahl aller Dateien (auch in Unterordnern)
#   b) Anzahl der Ordner
#   c) Alle Dateiendungen mit Anzahl, sortiert
#   d) Gesamtgröße in Bytes

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Filtern
# ══════════════════════════════════════════════════════════════════
# Finde und gib aus:
#   a) Alle Bilder (.jpg/.jpeg/.png), Groß-/Kleinschreibung egal
#   b) Alle Dateien, die "Rechnung" im Namen haben
#   c) Alle Dateien OHNE Endung
#   d) Alle Dateien mit Leerzeichen im Namen

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Namen bereinigen (mit Trockenlauf!)
# ══════════════════════════════════════════════════════════════════
# Schreib bereinige_namen(ordner, trockenlauf=True), die Dateinamen
# aufräumt:
#   - Leerzeichen  -> Unterstrich
#   - alles klein
#   - Umlaute ersetzen (ä->ae, ö->oe, ü->ue, ß->ss)
#   - Klammern und Sonderzeichen entfernen
# "Rechnung Müller 2026-01.pdf" -> "rechnung_mueller_2026-01.pdf"
# ⚠️ Erst Trockenlauf zeigen, dann echt ausführen!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Ordner sortieren
# ══════════════════════════════════════════════════════════════════
# Schreib sortiere_nach_typ(ordner, trockenlauf=True), die Dateien
# in Unterordner einsortiert (Bilder, Dokumente, Tabellen, Musik,
# Videos, Archive, Code, Sonstiges).
# Gib eine Statistik zurück. Erst Trockenlauf, dann echt!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Duplikate finden
# ══════════════════════════════════════════════════════════════════
# a) Schreib datei_hash(pfad) mit hashlib.sha256
# b) Schreib finde_duplikate(ordner) -> {hash: [pfade]}
# c) Gib alle Duplikatgruppen aus
# d) Berechne, wie viel Speicherplatz durch Löschen frei würde
# ⚠️ NUR ANZEIGEN, nichts löschen!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🔴 - Sicherer "Papierkorb"
# ══════════════════════════════════════════════════════════════════
# Schreib in_papierkorb(datei, papierkorb_ordner), die eine Datei
# NICHT löscht, sondern in einen Papierkorb-Ordner verschiebt -
# mit Zeitstempel im Namen, falls dort schon eine gleichnamige liegt.
# Schreib zusätzlich papierkorb_leeren(ordner, aelter_als_tage=30).
# 💡 Das ist die sichere Alternative zu os.remove()!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - Backup mit Zeitstempel
# ══════════════════════════════════════════════════════════════════
# Schreib erstelle_backup(quelle, ziel_ordner), die:
#   - ein ZIP mit Zeitstempel im Namen erstellt
#   - die Größe zurückgibt
#   - alte Backups (mehr als 5) automatisch entfernt
# 💡 shutil.make_archive

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 ⭐ BONUS - Der komplette Aufräumer
# ══════════════════════════════════════════════════════════════════
# Baue alles zusammen zu einem Skript, das:
#   1. Backup erstellt
#   2. Namen bereinigt
#   3. Nach Typ sortiert
#   4. Duplikate meldet (nicht löscht!)
#   5. Einen Bericht als Textdatei schreibt
#   6. IMMER mit Trockenlauf beginnt und den Nutzer fragt
# Das ist im Kern schon Projekt 3! 🗂️

# 👉 Dein Code:



print(f"\n✅ Fertig? Schau dir {UEB} an - und dann in die Lösungen!")
