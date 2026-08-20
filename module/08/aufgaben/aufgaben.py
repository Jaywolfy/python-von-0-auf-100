"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 08 · AUFGABEN — Funktionen                                ║
║  🟢 Grundlagen  🟡 Anwenden  🔴 Transfer  🥗 Mix  ⭐ Bonus        ║
║                                                                  ║
║  ⚠️ REGEL FÜR DIESES MODUL:                                      ║
║     Jede Funktion gibt ihr Ergebnis mit return zurück.           ║
║     print() nur beim AUFRUF, nicht IN der Funktion!              ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Erste Funktion
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion quadrat(zahl), die das Quadrat zurückgibt.
# Teste sie mit 3, 7 und -4.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Mit Default-Wert
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion begruessung(name, sprache="de"), die
# je nach Sprache zurückgibt:
#   "de" -> "Hallo Anna!"
#   "en" -> "Hello Anna!"
#   "fr" -> "Bonjour Anna!"
#   sonst -> "Hi Anna!"
# Teste alle vier Fälle.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟢 - Rückgabe statt Ausgabe
# ══════════════════════════════════════════════════════════════════
# Diese Funktion ist falsch gebaut. Schreib sie richtig
# (mit return) und zeig, warum das besser ist.
#
#   def verdopple(x):
#       print(x * 2)
#
# Beweise es: berechne verdopple(verdopple(5))  -> soll 20 ergeben

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Mehrere Rückgabewerte
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion analysiere(zahlen), die Minimum, Maximum,
# Summe und Durchschnitt als Tupel zurückgibt.
# Rufe sie auf und entpacke das Ergebnis in vier Variablen.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Funktionen kombinieren
# ══════════════════════════════════════════════════════════════════
# Schreib DREI kleine Funktionen:
#   ist_gerade(zahl)         -> True/False
#   filtere_gerade(liste)    -> neue Liste nur mit geraden Zahlen
#                               (nutzt ist_gerade!)
#   summe_gerade(liste)      -> Summe der geraden Zahlen
#                               (nutzt filtere_gerade!)
# Teste mit [1,2,3,4,5,6,7,8,9,10]

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - Temperatur-Umrechner
# ══════════════════════════════════════════════════════════════════
# Schreib:
#   celsius_zu_fahrenheit(c)
#   fahrenheit_zu_celsius(f)
#   celsius_zu_kelvin(c)
# Alle mit Docstring! Teste alle drei und prüfe:
# fahrenheit_zu_celsius(celsius_zu_fahrenheit(20)) soll wieder 20 sein.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🥗 MIX - Passwortgenerator-Prüfer
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion pruefe_passwort(pw), die ein Dictionary
# zurückgibt:
#   {"laenge_ok": True, "hat_ziffer": True, "hat_gross": False,
#    "hat_klein": True, "punkte": 3, "bewertung": "MITTEL"}
# Schreib eine zweite Funktion zeige_bericht(ergebnis), die das
# Dictionary hübsch mit ✅/❌ ausgibt.
# Teste mit 3 verschiedenen Passwörtern.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 🔴 - Scope verstehen
# ══════════════════════════════════════════════════════════════════
# Sag ZUERST voraus, was ausgegeben wird. Dann testen.
#
#   x = 10
#   def f1():
#       x = 20
#       return x
#   def f2():
#       return x
#   def f3(x):
#       x = x + 5
#       return x
#
#   print(f1(), f2(), f3(x), x)

# 👉 Deine Vorhersage + Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 9 🔴 - Refactoring
# ══════════════════════════════════════════════════════════════════
# Zerlege dieses Skript in mindestens 3 sinnvolle Funktionen
# plus eine main().
#
#   produkte = [["Laptop",899.99,2],["Maus",25.50,5],["Tastatur",79.00,3]]
#   gesamt = 0
#   for p in produkte:
#       zeilensumme = p[1] * p[2]
#       gesamt += zeilensumme
#       print(p[0], p[2], "x", p[1], "=", zeilensumme)
#   mwst = gesamt * 0.19
#   print("Netto:", gesamt)
#   print("MwSt:", mwst)
#   print("Brutto:", gesamt + mwst)

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 10 ⭐ BONUS - Rekursion (Vorgeschmack)
# ══════════════════════════════════════════════════════════════════
# Eine Funktion darf sich selbst aufrufen! Das heißt Rekursion.
# Schreib fakultaet(n):  5! = 5*4*3*2*1 = 120
#   - Wenn n <= 1: gib 1 zurück (Abbruchbedingung!)
#   - Sonst: gib n * fakultaet(n-1) zurück
# Teste mit 1, 5 und 10.
# ⚠️ Ohne Abbruchbedingung -> RecursionError!

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
