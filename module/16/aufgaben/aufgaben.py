"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 16 · AUFGABEN — CSV & JSON                                ║
╚══════════════════════════════════════════════════════════════════╝
"""
from pathlib import Path

UEB = Path(__file__).parent / "_uebung16"
UEB.mkdir(exist_ok=True)

# --- Testdaten (nicht ändern) ---------------------------------------
(UEB / "verkaeufe.csv").write_text(
    "datum;produkt;kategorie;menge;einzelpreis\n"
    "2026-01-15;Laptop;Technik;2;899,99\n"
    "2026-01-18;Maus;Technik;10;25,50\n"
    "2026-02-03;Schreibtisch;Möbel;1;349,00\n"
    "2026-02-14;Tastatur;Technik;5;79,00\n"
    "2026-02-28;Bürostuhl;Möbel;3;259,90\n"
    "2026-03-05;Monitor;Technik;4;219,00\n"
    "2026-03-22;Regal;Möbel;2;129,50\n",
    encoding="utf-8")

(UEB / "einstellungen.json").write_text(
    '{\n'
    '  "app": "Lagerverwaltung",\n'
    '  "version": "2.1",\n'
    '  "besitzer": {"name": "Anna", "rolle": "Admin"},\n'
    '  "lager": [\n'
    '    {"ort": "Halle A", "kapazitaet": 5000, "belegt": 3200},\n'
    '    {"ort": "Halle B", "kapazitaet": 3000, "belegt": 2950}\n'
    '  ],\n'
    '  "benachrichtigungen": {"email": true, "sms": false}\n'
    '}\n', encoding="utf-8")


# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - CSV lesen
# ══════════════════════════════════════════════════════════════════
# Lies verkaeufe.csv mit DictReader und gib alle Zeilen aus.
# ⚠️ delimiter=";" und newline="" nicht vergessen!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Typen umwandeln
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion deutsche_zahl(text), die "1.234,56" -> 1234.56
# macht. Teste mit: "899,99", "1.234,56", "25,50", "10"

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Auswertung
# ══════════════════════════════════════════════════════════════════
# Lies die Verkäufe ein (mit korrekten Typen!) und gib aus:
#   a) Gesamtumsatz (menge * einzelpreis)
#   b) Umsatz pro Kategorie
#   c) Bestseller (höchste Stückzahl)
#   d) Teuerstes Produkt
#   e) Anzahl verkaufter Artikel gesamt

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - CSV schreiben
# ══════════════════════════════════════════════════════════════════
# Schreib eine neue Datei "umsatz_pro_kategorie.csv" mit den Spalten:
#   kategorie;anzahl_verkaeufe;stueckzahl;umsatz
# Sortiert nach Umsatz absteigend.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - JSON lesen
# ══════════════════════════════════════════════════════════════════
# Lies einstellungen.json und gib aus:
#   a) Den App-Namen
#   b) Den Namen des Besitzers
#   c) Alle Lagerorte
#   d) Für jedes Lager die Auslastung in Prozent
#   e) Ist E-Mail-Benachrichtigung aktiv?

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - JSON ändern & speichern
# ══════════════════════════════════════════════════════════════════
# a) Füge ein drittes Lager hinzu ("Halle C", 4000, 100)
# b) Setze sms auf true
# c) Erhöhe die Version auf "2.2"
# d) Speichere als "einstellungen_neu.json" (indent=2, ensure_ascii=False)
# e) Lies die neue Datei wieder ein und prüfe die Änderungen

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - CSV nach JSON
# ══════════════════════════════════════════════════════════════════
# Wandle verkaeufe.csv in eine JSON-Datei um, mit dieser Struktur:
#   {
#     "erstellt": "2026-07-26",
#     "anzahl_datensaetze": 7,
#     "gesamtumsatz": 4321.45,
#     "nach_kategorie": {
#        "Technik": [ {...}, {...} ],
#        "Möbel":   [ {...} ]
#     }
#   }

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 ⭐ BONUS - Robuster CSV-Import
# ══════════════════════════════════════════════════════════════════
# Erstelle eine CSV mit ABSICHTLICHEN Fehlern (fehlende Werte,
# kaputte Zahlen, leere Zeilen) und schreib eine Funktion
# lade_verkaeufe(pfad), die:
#   - gültige Zeilen einliest
#   - fehlerhafte Zeilen mit Zeilennummer und Grund sammelt
#   - ein Ergebnis-Dictionary zurückgibt
#   - NIEMALS abstürzt

# 👉 Dein Code:



print(f"\n✅ Deine Dateien liegen in: {UEB}")
