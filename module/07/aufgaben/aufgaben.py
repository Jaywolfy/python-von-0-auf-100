"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 07 · AUFGABEN — Dicts, Tupel & Sets                       ║
║  🟢 Grundlagen  🟡 Anwenden  🔴 Transfer  🥗 Mix  ⭐ Bonus        ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Dein Dictionary
# ══════════════════════════════════════════════════════════════════
# Erstelle ein Dictionary "auto" mit: marke, modell, baujahr, ps, elektrisch
# a) Gib alle Schlüssel-Wert-Paare zeilenweise aus
# b) Ändere das Baujahr
# c) Füge "farbe" hinzu
# d) Greife sicher auf "kilometerstand" zu (Standard: "unbekannt")

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Telefonbuch
# ══════════════════════════════════════════════════════════════════
telefonbuch = {"Anna": "0151-111", "Bernd": "0160-222", "Clara": "0170-333"}
# a) Gib Bernds Nummer aus
# b) Füge "David" hinzu
# c) Lösche "Anna"
# d) Gib alle Namen alphabetisch sortiert mit Nummer aus
# e) Prüfe, ob "Emil" enthalten ist

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟢 - Unpacking
# ══════════════════════════════════════════════════════════════════
koordinate = (52.52, 13.40)
datensatz = ["Anna", 30, "Berlin", "anna@mail.de"]
# a) Entpacke koordinate in breite und laenge
# b) Entpacke datensatz in name, alter, stadt, email
# c) Entpacke [1,2,3,4,5] in erster und rest

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Zählen
# ══════════════════════════════════════════════════════════════════
farben = ["rot","blau","rot","grün","blau","rot","gelb","blau","rot"]
# Zähle mit einem Dictionary, wie oft jede Farbe vorkommt.
# Gib das Ergebnis absteigend sortiert aus, mit Balken:
#   rot   4  ████
#   blau  3  ███
#   ...

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Sets
# ══════════════════════════════════════════════════════════════════
kurs_a = {"Anna", "Bernd", "Clara", "David"}
kurs_b = {"Clara", "David", "Emil", "Frida"}
# Gib aus:
#   a) alle Teilnehmer insgesamt (ohne Duplikate)
#   b) wer in BEIDEN Kursen ist
#   c) wer NUR in Kurs A ist
#   d) wer in genau einem der beiden Kurse ist
#   e) die Gesamtzahl unterschiedlicher Personen

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - Verschachtelt lesen
# ══════════════════════════════════════════════════════════════════
laender = {
    "Deutschland": {"hauptstadt": "Berlin", "einwohner": 84.4, "sprachen": ["Deutsch"]},
    "Schweiz":     {"hauptstadt": "Bern",   "einwohner": 8.8,  "sprachen": ["Deutsch","Französisch","Italienisch"]},
    "Kanada":      {"hauptstadt": "Ottawa", "einwohner": 40.1, "sprachen": ["Englisch","Französisch"]},
}
# a) Gib die Hauptstadt der Schweiz aus
# b) Gib die zweite Sprache Kanadas aus
# c) Gib für jedes Land eine Zeile aus:
#    Deutschland  | Berlin  | 84.4 Mio | 1 Sprache(n)
# d) Welches Land hat die meisten Einwohner?
# e) Welche Sprachen kommen insgesamt vor (ohne Duplikate)?

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🥗 MIX - Textstatistik
# ══════════════════════════════════════════════════════════════════
text = """Python ist eine Programmiersprache. Python ist einfach zu lernen.
Viele Menschen lernen Python weil Python vielseitig ist."""
# a) Zerlege in Wörter (Punkte entfernen, klein schreiben)
# b) Zähle jedes Wort mit einem Dictionary
# c) Gib die 5 häufigsten Wörter aus
# d) Wie viele UNTERSCHIEDLICHE Wörter gibt es? (Set!)
# e) Welche Wörter kommen nur einmal vor?

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 🔴 - Warenkorb
# ══════════════════════════════════════════════════════════════════
preise = {"Apfel": 0.50, "Brot": 2.30, "Milch": 1.10, "Käse": 4.80}
warenkorb = {"Apfel": 6, "Brot": 2, "Käse": 1}
# Gib eine Rechnung aus:
#   Apfel    6 x  0.50 =   3.00
#   Brot     2 x  2.30 =   4.60
#   Käse     1 x  4.80 =   4.80
#   ----------------------------
#   SUMME                 12.40
# Sauber ausgerichtet mit f-Strings!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 9 🔴 - Dict umdrehen
# ══════════════════════════════════════════════════════════════════
laenderkuerzel = {"DE": "Deutschland", "FR": "Frankreich", "IT": "Italien"}
# Erstelle ein neues Dictionary, bei dem Schlüssel und Werte
# vertauscht sind:  {"Deutschland": "DE", ...}

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 10 ⭐ BONUS - Notenverwaltung
# ══════════════════════════════════════════════════════════════════
noten = {
    "Anna":  [2.3, 1.7, 2.0],
    "Bernd": [3.0, 3.3, 2.7],
    "Clara": [1.0, 1.3, 1.7],
    "David": [4.0, 3.7, 2.3],
}
# Gib eine Übersicht aus mit:
#   - Name, alle Noten, Durchschnitt (2 Nachkommastellen)
#   - Klassendurchschnitt
#   - bester und schlechtester Schüler
#   - alle, die besser als der Klassendurchschnitt sind

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
