"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 10 · AUFGABEN — Comprehensions & Builtins                 ║
║  🟢 Grundlagen  🟡 Anwenden  🔴 Transfer  🥗 Mix  ⭐ Bonus        ║
╚══════════════════════════════════════════════════════════════════╝
"""

zahlen = [12, -5, 33, 0, -18, 7, 45, -2, 8]
woerter = ["Programmierung", "Code", "Python", "Bug", "Debugger", "IDE"]
personen = [
    {"name": "Anna",  "alter": 30, "stadt": "Berlin",  "gehalt": 4200},
    {"name": "Bernd", "alter": 25, "stadt": "Hamburg", "gehalt": 3800},
    {"name": "Clara", "alter": 41, "stadt": "Berlin",  "gehalt": 5500},
    {"name": "David", "alter": 35, "stadt": "München", "gehalt": 4900},
]

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Erste Comprehensions
# ══════════════════════════════════════════════════════════════════
# Erzeuge mit je EINER Comprehension:
#   a) alle Zahlen verdreifacht
#   b) nur die positiven Zahlen
#   c) alle Zahlen als String
#   d) die Quadrate aller Zahlen zwischen 1 und 10

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Schleife -> Comprehension
# ══════════════════════════════════════════════════════════════════
# Schreib diese Schleife als Comprehension:
#
#   ergebnis = []
#   for w in woerter:
#       if len(w) > 4:
#           ergebnis.append(w.lower())

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟢 - if/else in der Comprehension
# ══════════════════════════════════════════════════════════════════
# Erzeuge aus zahlen eine Liste, in der jede Zahl durch
# "positiv", "negativ" oder "null" ersetzt ist.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - enumerate & zip
# ══════════════════════════════════════════════════════════════════
namen = ["Anna", "Bernd", "Clara"]
punkte = [85, 92, 78]
# a) Gib eine nummerierte Rangliste aus (ab 1)
# b) Baue ein Dictionary {name: punkte}
# c) Gib für jeden aus: "Anna hat 85 Punkte"
# d) Wer hat die meisten Punkte? (max mit key)

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - sorted mit key
# ══════════════════════════════════════════════════════════════════
# Sortiere die personen-Liste:
#   a) nach Alter (aufsteigend)
#   b) nach Gehalt (absteigend)
#   c) nach Namenslänge
#   d) alphabetisch nach Stadt, dann nach Name
#      💡 Tipp: key=lambda p: (p["stadt"], p["name"])
# Gib jeweils nur die Namen aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - any & all
# ══════════════════════════════════════════════════════════════════
# Prüfe und gib jeweils True/False aus:
#   a) Verdient jemand mehr als 5000?
#   b) Sind alle älter als 20?
#   c) Wohnt jemand in Köln?
#   d) Enthalten alle Wörter mindestens einen Vokal?

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🥗 MIX - Dict-Comprehensions
# ══════════════════════════════════════════════════════════════════
# a) {name: alter} aus personen
# b) {name: gehalt} nur für Leute über 30
# c) Alle Gehälter um 5 % erhöhen -> {name: neues_gehalt}
# d) {wort: laenge} für alle Wörter, sortiert nach Länge ausgeben

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 🔴 - Datenauswertung
# ══════════════════════════════════════════════════════════════════
# Berechne und gib formatiert aus:
#   a) Durchschnittsalter
#   b) Gesamtgehalt
#   c) Höchstes und niedrigstes Gehalt (mit Namen!)
#   d) Alle Städte ohne Duplikate
#   e) Wie viele Personen pro Stadt? (Dictionary)
#   f) Namen aller Berliner

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 9 🔴 - Verschachtelt
# ══════════════════════════════════════════════════════════════════
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Mit Comprehensions:
#   a) Alle Zahlen in EINER flachen Liste
#   b) Alle Zahlen verdoppelt (als Matrix, also Liste von Listen)
#   c) Nur die geraden Zahlen (flach)
#   d) Die Diagonale (1, 5, 9)
#   e) Die Zeilensummen

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 10 ⭐ BONUS - Refactoring-Urteil
# ══════════════════════════════════════════════════════════════════
# Dieser Code funktioniert. Entscheide bei JEDEM Block:
# Comprehension oder Schleife lassen? Begründe kurz als Kommentar!
#
#   # Block A
#   grosse = []
#   for z in zahlen:
#       if z > 10:
#           grosse.append(z)
#
#   # Block B
#   ergebnis = []
#   for p in personen:
#       if p["alter"] > 25:
#           if p["stadt"] == "Berlin":
#               bonus = p["gehalt"] * 0.1
#               if bonus > 400:
#                   ergebnis.append((p["name"], round(bonus)))
#
#   # Block C
#   namen_gross = []
#   for p in personen:
#       namen_gross.append(p["name"].upper())

# 👉 Dein Code + Begründungen:



print("\n✅ Fertig? Ab zu den Lösungen!")
