"""
Modul 01 - Beispiel 2: Datentypen und Umwandlungen
"""

# ====================================================================
# DIE VIER GRUNDTYPEN
# ====================================================================
text    = "Hallo"     # str   - Zeichenkette
ganz    = 42          # int   - Ganzzahl
komma   = 3.14        # float - Fließkommazahl (PUNKT, kein Komma!)
wahr    = True        # bool  - True oder False
nichts  = None        # NoneType - "absichtlich leer"

print("text   :", text,   "→", type(text))
print("ganz   :", ganz,   "→", type(ganz))
print("komma  :", komma,  "→", type(komma))
print("wahr   :", wahr,   "→", type(wahr))
print("nichts :", nichts, "→", type(nichts))

print("\n" + "-" * 60 + "\n")

# ====================================================================
# WARUM DER TYP WICHTIG IST
# ====================================================================
# Derselbe Operator "+" macht je nach Typ etwas völlig anderes:

print("3 + 4      =", 3 + 4)          # 7      → Addition
print('"3" + "4"  =', "3" + "4")      # 34     → Verkettung!
print('"ab" * 3   =', "ab" * 3)       # ababab → Wiederholung
print("2 * 3      =", 2 * 3)          # 6      → Multiplikation

# Das hier geht NICHT:
# print("3" + 4)   →  TypeError: can only concatenate str to str

print("\n" + "-" * 60 + "\n")

# ====================================================================
# TYPEN UMWANDELN (casting)
# ====================================================================
print('int("42")          =', int("42"))
print("int(3.99)          =", int(3.99), "  ← schneidet AB, rundet nicht!")
print("round(3.99)        =", round(3.99), "  ← so rundet man richtig")
print('float("3.14")      =', float("3.14"))
print("float(5)           =", float(5))
print("str(42)            =", str(42), "  (jetzt ein String:", type(str(42)), ")")

print()
print("bool(0)     =", bool(0))
print("bool(1)     =", bool(1))
print('bool("")    =', bool(""))
print('bool("hi")  =', bool("hi"))
print("bool(None)  =", bool(None))

print("\n" + "-" * 60 + "\n")

# ====================================================================
# DER KLASSIKER: STRING + ZAHL
# ====================================================================
alter_als_text = "25"          # z.B. aus einer Eingabe oder Datei
print("alter_als_text hat Typ:", type(alter_als_text))

# alter_als_text + 1     →  TypeError!

alter_als_zahl = int(alter_als_text)      # umwandeln!
print("Nächstes Jahr:", alter_als_zahl + 1)

print("\n💡 Merke: Bei jedem seltsamen Ergebnis zuerst type() prüfen!")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Was ergibt int("42.5")? Warum? Wie löst du es?
#   2. Was ergibt bool([])? Und bool([1])?
#   3. Was ist type(3 / 1)? Überrascht?
# ------------------------------------------------------------------
