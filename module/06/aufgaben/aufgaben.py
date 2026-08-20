"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 06 · AUFGABEN — Listen                                    ║
║  🟢 Grundlagen  🟡 Anwenden  🔴 Transfer  🥗 Mix  ⭐ Bonus        ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Grundlagen
# ══════════════════════════════════════════════════════════════════
einkaufsliste = ["Milch", "Brot", "Eier"]
# a) Füge "Käse" hinzu
# b) Füge "Butter" an Position 0 ein
# c) Entferne "Brot"
# d) Gib die Liste und ihre Länge aus

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Statistik
# ══════════════════════════════════════════════════════════════════
temperaturen = [18, 22, 25, 19, 31, 28, 17]
# Gib aus: Anzahl, Summe, Durchschnitt (1 Nachkommastelle),
#          Minimum, Maximum, sortierte Liste

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟢 - Suchen
# ══════════════════════════════════════════════════════════════════
tiere = ["Hund", "Katze", "Maus", "Katze", "Vogel"]
# a) Ist "Maus" in der Liste?
# b) Wie oft kommt "Katze" vor?
# c) An welcher Position steht "Vogel"?

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Filtern
# ══════════════════════════════════════════════════════════════════
zahlen = [12, -5, 33, 0, -18, 7, 45, -2]
# Erstelle DREI neue Listen: positive, negative, null
# Gib alle drei aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Duplikate entfernen
# ══════════════════════════════════════════════════════════════════
mit_duplikaten = [1, 3, 3, 5, 1, 7, 5, 9, 3]
# Erstelle eine neue Liste OHNE Duplikate, Reihenfolge beibehalten.
# ⚠️ Ohne set() - das ist die Übung! (Tipp: "in" prüfen)

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - Sortieren mit key
# ══════════════════════════════════════════════════════════════════
woerter = ["Banane", "kiwi", "Apfel", "Zitrone", "erdbeere"]
# Gib aus:
#   a) alphabetisch sortiert (Groß/Klein egal!)
#   b) nach Länge sortiert
#   c) nach Länge absteigend
# 💡 Tipp: key=str.lower  und  key=len

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🥗 MIX - Wörter analysieren  (Strings + Schleifen + Listen)
# ══════════════════════════════════════════════════════════════════
satz = "Python ist eine wunderbare und sehr vielseitige Programmiersprache"
# a) Zerlege den Satz in eine Liste von Wörtern
# b) Gib das längste Wort aus
# c) Gib alle Wörter mit mehr als 5 Buchstaben aus
# d) Gib alle Wörter in Großbuchstaben aus, alphabetisch sortiert
# e) Berechne die durchschnittliche Wortlänge

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 🔴 - Die Kopier-Falle
# ══════════════════════════════════════════════════════════════════
# Sag ZUERST voraus (als Kommentar), was ausgegeben wird.
# Dann ausführen und vergleichen.
#
#   a = [1, 2, 3]
#   b = a
#   c = a.copy()
#   b.append(4)
#   c.append(5)
#   print(a)
#   print(b)
#   print(c)

# 👉 Deine Vorhersage + Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 9 🔴 - Matrix
# ══════════════════════════════════════════════════════════════════
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# a) Gib die Matrix zeilenweise sauber formatiert aus
# b) Berechne die Summe ALLER Zahlen
# c) Berechne die Summe jeder Zeile
# d) Gib die Diagonale aus (1, 5, 9)

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 10 ⭐ BONUS - Notenverwaltung
# ══════════════════════════════════════════════════════════════════
schueler = ["Anna", "Bernd", "Clara", "David"]
noten =    [2.3,    1.7,     3.0,     1.3]
# Gib eine Rangliste aus, sortiert nach Note (beste zuerst):
#
#   🥇 1. David    1.3
#   🥈 2. Bernd    1.7
#   🥉 3. Anna     2.3
#      4. Clara    3.0
#
#   Durchschnitt: 2.08
#
# 💡 Tipp: Baue eine Liste von Paaren, z.B. [[1.3,"David"], ...],
#    dann sort()

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
