"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 11 · AUFGABEN — Dateien & Pfade                           ║
║  🟢 Grundlagen  🟡 Anwenden  🔴 Transfer  🥗 Mix  ⭐ Bonus        ║
║                                                                  ║
║  ⚠️ WICHTIG: Arbeite NUR im Ordner _uebung (wird angelegt).      ║
║     Nie mit "w" an echten Dateien üben!                          ║
╚══════════════════════════════════════════════════════════════════╝
"""
from pathlib import Path

UEB = Path(__file__).parent / "_uebung"
UEB.mkdir(exist_ok=True)

# Testdaten anlegen (nicht ändern)
(UEB / "einkaufsliste.txt").write_text(
    "Milch\nBrot\nEier\nKäse\nButter\nApfel\n", encoding="utf-8")
(UEB / "noten.csv").write_text(
    "Anna;2.3\nBernd;1.7\nClara;3.0\nDavid;1.3\nEmil;4.0\n", encoding="utf-8")
(UEB / "text.txt").write_text(
    "Python ist eine großartige Sprache.\n"
    "Mit Python kann man Dateien lesen.\n"
    "Python macht Automatisierung einfach.\n", encoding="utf-8")


# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Lesen
# ══════════════════════════════════════════════════════════════════
# Lies UEB/"einkaufsliste.txt" und gib jede Zeile nummeriert aus:
#   1. Milch
#   2. Brot
#   ...
# ⚠️ Ohne die \n am Ende!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Schreiben
# ══════════════════════════════════════════════════════════════════
# Schreib eine neue Datei UEB/"meine_ziele.txt" mit 5 Zeilen:
# deinen 5 Zielen für diesen Python-Kurs.
# Lies sie danach wieder ein und gib sie aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟢 - Anhängen
# ══════════════════════════════════════════════════════════════════
# Hänge drei weitere Artikel an die einkaufsliste.txt an
# (Modus "a"!) und gib die Datei danach komplett aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Zeilen zählen & filtern
# ══════════════════════════════════════════════════════════════════
# Lies UEB/"text.txt" und gib aus:
#   a) Anzahl Zeilen
#   b) Anzahl Wörter
#   c) Anzahl Zeichen (ohne Zeilenumbrüche)
#   d) Alle Zeilen, die "Python" enthalten
#   e) Das längste Wort

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - CSV-artige Datei verarbeiten
# ══════════════════════════════════════════════════════════════════
# Lies UEB/"noten.csv" (Format: Name;Note) und gib aus:
#   - eine formatierte Tabelle
#   - den Durchschnitt
#   - den besten und schlechtesten Schüler
#   - wie viele bestanden haben (Note <= 4.0)

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - Bericht schreiben
# ══════════════════════════════════════════════════════════════════
# Erzeuge aus den Noten eine Datei UEB/"zeugnis.txt" mit:
#   ZEUGNIS
#   =======
#   Anna       2.3  bestanden
#   ...
#   -------
#   Durchschnitt: 2.46

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - Ordner durchsuchen
# ══════════════════════════════════════════════════════════════════
# Erstelle in UEB einen Unterordner "sortiert" mit den Unterordnern
# "Text", "Daten", "Sonstiges".
# Liste dann ALLE Dateien in UEB (auch in Unterordnern) auf und gib
# für jede an, in welchen Zielordner sie gehören würde:
#   .txt        -> Text
#   .csv        -> Daten
#   alles andere-> Sonstiges
# ⚠️ Nur ANZEIGEN, noch nichts verschieben! (Das kommt in Modul 25)

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 🥗 MIX - Wortstatistik in Datei
# ══════════════════════════════════════════════════════════════════
# Lies text.txt, zähle jedes Wort (klein, ohne Satzzeichen)
# und schreibe eine Datei "wortstatistik.txt" mit den Wörtern
# absteigend nach Häufigkeit sortiert:
#   python : 3
#   ist    : 1
#   ...

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 9 🔴 - Datei sicher lesen
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion lies_sicher(pfad), die:
#   - den Inhalt zurückgibt, wenn die Datei existiert
#   - sonst None zurückgibt und eine hilfreiche Meldung ausgibt
#     (inkl. absolutem Pfad und aktuellem Arbeitsverzeichnis)
# Teste mit einer vorhandenen und einer fehlenden Datei.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 10 ⭐ BONUS - Backup-Funktion
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion backup(pfad), die eine Kopie der Datei
# anlegt - mit Zeitstempel im Namen:
#   noten.csv  ->  noten_20260726_143052.csv
# 💡 Tipp: from datetime import datetime
#          datetime.now().strftime("%Y%m%d_%H%M%S")
# 💡 Neuer Name: pfad.with_name(f"{pfad.stem}_{stempel}{pfad.suffix}")

# 👉 Dein Code:



print(f"\n✅ Fertig? Deine Dateien liegen in: {UEB}")
