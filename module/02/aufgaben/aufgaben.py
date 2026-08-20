"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 02 · AUFGABEN — Strings                                   ║
║  🟢 Grundlagen  🟡 Anwenden  🔴 Transfer  ⭐ Bonus                ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Begrüßung
# ══════════════════════════════════════════════════════════════════
# Lege vorname, nachname und alter an.
# Gib mit EINEM f-String aus:
#   Hallo Anna Schmidt, du bist 25 Jahre alt!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Erstes, letztes, Länge
# ══════════════════════════════════════════════════════════════════
wort = "Programmieren"
# Gib aus:
#   Erstes Zeichen: P
#   Letztes Zeichen: n
#   Länge: 13
#   Die ersten 4 Zeichen: Prog
#   Die letzten 4 Zeichen: eren

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟢 - Umdrehen
# ══════════════════════════════════════════════════════════════════
# Dreh das Wort "Fledermaus" um und gib es aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Preisliste
# ══════════════════════════════════════════════════════════════════
# Gib diese drei Artikel als saubere Tabelle aus.
# Artikelname linksbündig (20 Zeichen), Preis rechtsbündig mit
# genau 2 Nachkommastellen (10 Zeichen).
#
# Kaffee        12.5
# Tee            3.99
# Kakao         7.125
#
# Erwartet ungefähr so:
# Kaffee                    12.50
# Tee                        3.99
# Kakao                      7.13

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Datenzeile zerlegen
# ══════════════════════════════════════════════════════════════════
zeile = "Müller;Anna;1995;Hamburg"
# Zerlege die Zeile und gib aus:
#   Anna Müller, geboren 1995, wohnhaft in Hamburg

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - Initialen
# ══════════════════════════════════════════════════════════════════
voller_name = "anna maria schmidt"
# Erzeuge daraus die Initialen in Großbuchstaben mit Punkten:
#   A.M.S.
# 💡 Tipp: split() + Index [0] + upper() + join()

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - Palindrom
# ══════════════════════════════════════════════════════════════════
# Ein Palindrom liest sich vorwärts wie rückwärts.
# Prüfe für diese drei Wörter, ob sie Palindrome sind,
# und gib jeweils "JA" oder "NEIN" aus.
#
# ⚠️ Groß-/Kleinschreibung und Leerzeichen sollen egal sein!
wort_a = "Otto"
wort_b = "Ein Esel lese nie"   # klassisches deutsches Palindrom
wort_c = "Python"
# 💡 Tipp: .lower(), .replace(" ", ""), [::-1], ==
# 💡 Du darfst if benutzen - oder einfach den Vergleich (True/False) ausgeben.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 🔴 - Tabelle mit Rahmen
# ══════════════════════════════════════════════════════════════════
# Gib diese Daten als Tabelle MIT Rahmen aus (| und -).
# Spalten: Name (12), Stadt (12), Alter (5, rechtsbündig)
#
#   Anna    Berlin    30
#   Bernd   Hamburg   25
#   Clara   München   41

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 9 ⭐ BONUS - E-Mail zerlegen
# ══════════════════════════════════════════════════════════════════
email = "max.mustermann@beispiel-firma.de"
# Gib aus:
#   Benutzername: max.mustermann
#   Domain:       beispiel-firma.de
#   Vorname:      Max
#   Nachname:     Mustermann
#   Anzeigename:  Max Mustermann
#   Kürzel:       mmustermann     (erster Buchstabe Vorname + Nachname)

# 👉 Dein Code:



print("\n✅ Fertig? Vergleiche mit den Lösungen!")
