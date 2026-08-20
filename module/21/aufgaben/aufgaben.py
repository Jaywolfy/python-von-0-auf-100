"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 21 · AUFGABEN — Regex                                     ║
║  💡 Teste deine Muster live auf https://regex101.com (Python)    ║
╚══════════════════════════════════════════════════════════════════╝
"""
import re

TEXT = """
Bestellung BE-2026-4711 vom 15.03.2026
Kunde: Anna Müller, anna.mueller@beispiel.de, Tel. 0151-98765432
Lieferadresse: Bahnhofstr. 7a, 80331 München
Artikel: 3x Laptop (899,99 €), 2x Maus (25,50 €)
Gesamtbetrag: 2.750,97 €
Zahlung per IBAN DE12500105170648489890
Tracking: https://versand.example.com/track/XY123456789DE
Rückfragen an service@beispiel.de oder 089/1234567
Zweite Bestellung BE-2026-4712 vom 02.04.2026, Betrag 149,00 €
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Erste Muster
# ══════════════════════════════════════════════════════════════════
# Finde mit re.findall:
#   a) alle Zahlenfolgen
#   b) alle Wörter, die mit einem Großbuchstaben beginnen
#   c) alle Postleitzahlen (genau 5 Ziffern, mit Wortgrenzen!)
#   d) alle Wörter mit genau 4 Buchstaben

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - E-Mails und URLs
# ══════════════════════════════════════════════════════════════════
# Finde alle E-Mail-Adressen und alle URLs.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Beträge
# ══════════════════════════════════════════════════════════════════
# a) Finde alle Eurobeträge (Format: 1.234,56 € oder 25,50 €)
# b) Wandle sie in floats um und berechne die Summe
# 💡 Tipp: Gruppen + replace für das deutsche Format

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Gruppen
# ══════════════════════════════════════════════════════════════════
# Extrahiere aus allen Bestellnummern (BE-JAHR-NUMMER) mit
# BENANNTEN Gruppen: praefix, jahr, nummer.
# Gib für jede Bestellung aus:
#   Bestellung 4711 aus dem Jahr 2026

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Datumsformat umwandeln
# ══════════════════════════════════════════════════════════════════
# Wandle alle Daten von TT.MM.JJJJ in JJJJ-MM-TT um (re.sub).
# Gib den umgewandelten Text aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - Anonymisieren
# ══════════════════════════════════════════════════════════════════
# Ersetze im Text:
#   - alle E-Mails durch "[E-MAIL]"
#   - alle Telefonnummern durch "[TELEFON]"
#   - die IBAN durch "[IBAN]"
# Gib den anonymisierten Text aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - Artikelpositionen parsen
# ══════════════════════════════════════════════════════════════════
# Aus "3x Laptop (899,99 €), 2x Maus (25,50 €)" soll werden:
#   [{"menge": 3, "artikel": "Laptop", "preis": 899.99, "summe": 2699.97},
#    {"menge": 2, "artikel": "Maus",   "preis": 25.50,  "summe": 51.0}]
# Gib eine formatierte Tabelle mit Gesamtsumme aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 🔴 - Validierung
# ══════════════════════════════════════════════════════════════════
# Schreib Funktionen, die True/False zurückgeben:
#   ist_gueltige_email(text)
#   ist_gueltige_plz(text)      (5 Ziffern, nicht mit 0 beginnend)
#   ist_gueltiges_datum(text)   (TT.MM.JJJJ, Tag 01-31, Monat 01-12)
#   ist_starkes_passwort(text)  (min. 8 Zeichen, Groß, Klein, Ziffer, Sonderzeichen)
# Teste jede mit 3 guten und 3 schlechten Beispielen.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 9 ⭐ BONUS - Universeller Extraktor
# ══════════════════════════════════════════════════════════════════
# Schreib extrahiere_alles(text), die ein Dictionary zurückgibt:
#   {"emails": [...], "telefone": [...], "daten": [...],
#    "betraege": [...], "plz": [...], "urls": [...], "ibans": [...]}
# und zeige_bericht(daten), die es hübsch mit Emojis ausgibt.

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
