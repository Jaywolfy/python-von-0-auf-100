"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 14 · AUFGABEN — Klassen & Objekte                         ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Erste Klasse
# ══════════════════════════════════════════════════════════════════
# Schreib eine Klasse Person mit:
#   - __init__(self, name, alter, stadt)
#   - Methode vorstellen() -> "Ich bin Anna, 30, aus Berlin"
#   - __str__ -> "Person(Anna, 30)"
# Erzeuge 3 Personen und gib sie aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Rechteck
# ══════════════════════════════════════════════════════════════════
# Klasse Rechteck mit breite und hoehe.
# Methoden: flaeche(), umfang(), ist_quadrat()
# __str__ -> "Rechteck 3x4 (Fläche 12)"
# Teste mit 3 verschiedenen Rechtecken.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Zustand verändern
# ══════════════════════════════════════════════════════════════════
# Klasse Zaehler mit:
#   - start-Wert (Standard 0)
#   - hoch(schritt=1), runter(schritt=1), zuruecksetzen()
#   - verlauf: Liste aller Werte, die der Zähler hatte
#   - __str__
# Teste: hoch, hoch, runter, hoch(5), zurücksetzen - und zeig den Verlauf.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Einkaufswagen
# ══════════════════════════════════════════════════════════════════
# Klasse Einkaufswagen mit:
#   - hinzufuegen(artikel, preis, menge=1)
#   - entfernen(artikel)
#   - gesamtpreis()
#   - anzahl_artikel()
#   - rechnung() -> formatierter String
# Teste mit 4 Artikeln.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Die Klassenattribut-Falle
# ══════════════════════════════════════════════════════════════════
# Dieser Code hat einen Bug. Finde ihn, erkläre ihn, repariere ihn.
#
#   class Spieler:
#       inventar = []
#       def __init__(self, name):
#           self.name = name
#       def aufheben(self, gegenstand):
#           self.inventar.append(gegenstand)
#
#   a = Spieler("Anna"); b = Spieler("Bernd")
#   a.aufheben("Schwert")
#   print(b.inventar)     # ???

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🔴 - Bibliothek
# ══════════════════════════════════════════════════════════════════
# Klasse Buch: titel, autor, jahr, ausgeliehen (Standard False)
#   Methoden: ausleihen(), zurueckgeben(), __str__
#   ausleihen() soll einen Fehler werfen, wenn schon ausgeliehen!
#
# Klasse Bibliothek: verwaltet eine Liste von Büchern
#   Methoden: hinzufuegen(buch), suche(stichwort),
#             verfuegbare(), ausgeliehene(), statistik()
#
# Teste mit 5 Büchern: 2 ausleihen, suchen, Statistik ausgeben.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 ⭐ BONUS - Aufgabenverwaltung
# ══════════════════════════════════════════════════════════════════
# Klasse Aufgabe: titel, prioritaet (1-3), erledigt, faellig (Datum-String)
# Klasse AufgabenListe:
#   - hinzufuegen, erledigen(titel), offene(), erledigte()
#   - nach_prioritaet() -> sortiert
#   - fortschritt() -> "3/7 erledigt (43 %)" + Balken
#   - __str__ -> komplette formatierte Übersicht mit ☐/☑
# Teste mit 6 Aufgaben.

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
