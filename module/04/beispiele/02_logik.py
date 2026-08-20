"""
Modul 04 - Beispiel 2: and, or, not und Truthiness
"""

# ====================================================================
# AND / OR / NOT
# ====================================================================
alter = 25
hat_fuehrerschein = True
hat_auto = False

if alter >= 18 and hat_fuehrerschein:
    print("Darf Auto fahren 🚗")

if hat_fuehrerschein and not hat_auto:
    print("Braucht ein Mietauto 🚙")

if alter < 6 or alter > 65:
    print("Ermäßigter Eintritt 🎫")
else:
    print("Voller Eintrittspreis 💶")

print()


# ====================================================================
# WAHRHEITSTABELLE
# ====================================================================
print(f"{'A':<7}{'B':<7}{'A and B':<10}{'A or B':<10}{'not A':<7}")
print("-" * 41)
for a in (True, False):
    for b in (True, False):
        print(f"{str(a):<7}{str(b):<7}{str(a and b):<10}{str(a or b):<10}{str(not a):<7}")

print()


# ====================================================================
# DER KLASSISCHE DENKFEHLER
# ====================================================================
name = "Clara"

# ❌ FALSCH - sieht richtig aus, ist es aber nicht:
if name == "Anna" or "Bernd":
    print("FALSCH: Clara wurde als Anna/Bernd erkannt! 😱")

# Warum? "Bernd" allein ist ein nicht-leerer String -> immer True.
print(f'  bool("Bernd") = {bool("Bernd")}   <- deshalb immer wahr')

# ✅ RICHTIG:
if name == "Anna" or name == "Bernd":
    print("Anna oder Bernd")
else:
    print("RICHTIG: Clara ist weder Anna noch Bernd ✅")

# ✅✅ NOCH BESSER:
if name in ("Anna", "Bernd"):
    print("Anna oder Bernd")
else:
    print("BESSER lesbar: Clara ist nicht dabei ✅")

print()


# ====================================================================
# TRUTHINESS - was gilt als wahr?
# ====================================================================
werte = [0, 1, -1, 0.0, "", "text", " ", [], [1], {}, {"a": 1}, None, True, False]

print(f"{'Wert':<15}{'bool()':<10}")
print("-" * 25)
for w in werte:
    print(f"{repr(w):<15}{str(bool(w)):<10}")

print()

# In der Praxis:
eingabe = ""
if eingabe:
    print("Eingabe vorhanden")
else:
    print("Keine Eingabe erhalten (leerer String ist falsy)")

liste = []
if not liste:
    print("Liste ist leer")

print()


# ====================================================================
# GUARD CLAUSES statt tiefer Verschachtelung
# ====================================================================
angemeldet = True
guthaben = 50
artikel_verfuegbar = True
preis = 30

print("--- Verschachtelt (schwer lesbar) ---")
if angemeldet:
    if guthaben >= preis:
        if artikel_verfuegbar:
            print("  Kauf möglich ✅")
        else:
            print("  Artikel nicht verfügbar")
    else:
        print("  Zu wenig Guthaben")
else:
    print("  Bitte anmelden")

print("--- Flach mit Guard Clauses (besser lesbar) ---")
if not angemeldet:
    print("  Bitte anmelden")
elif guthaben < preis:
    print("  Zu wenig Guthaben")
elif not artikel_verfuegbar:
    print("  Artikel nicht verfügbar")
else:
    print("  Kauf möglich ✅")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Setz guthaben auf 10. Welcher Zweig läuft jetzt?
#   2. Was ergibt bool("False")? Warum?
#   3. Baue eine Bedingung: "wenn Wochenende ODER Feiertag, und
#      nicht krank -> Ausflug".
# ------------------------------------------------------------------
