"""
Modul 07 - Beispiel 2: Tupel und Sets
"""

# ====================================================================
# TUPEL - unveränderlich
# ====================================================================
punkt = (3, 5)
farbe_orange = (255, 128, 0)

print(f"punkt        = {punkt}")
print(f"punkt[0]     = {punkt[0]}")
print(f"len(punkt)   = {len(punkt)}")
# punkt[0] = 9   ->  TypeError: 'tuple' object does not support item assignment

# ⚠️ Ein-Element-Tupel braucht ein Komma!
kein_tupel = (1)
echtes_tupel = (1,)
print(f"\n(1)  ist ein {type(kein_tupel).__name__}")
print(f"(1,) ist ein {type(echtes_tupel).__name__}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# UNPACKING ⭐
# ====================================================================
x, y = punkt
print(f"x, y = punkt      ->  x={x}, y={y}")

r, g, b = farbe_orange
print(f"r, g, b           ->  {r}, {g}, {b}")

erster, *rest = [1, 2, 3, 4, 5]
print(f"erster, *rest     ->  erster={erster}, rest={rest}")

*anfang, letzter = [1, 2, 3, 4, 5]
print(f"*anfang, letzter  ->  anfang={anfang}, letzter={letzter}")

a, b = "links", "rechts"
a, b = b, a
print(f"Tauschen          ->  a={a}, b={b}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# TUPEL ALS RÜCKGABE MEHRERER WERTE (Vorgeschmack Modul 08)
# ====================================================================
def min_max_summe(zahlen):
    return min(zahlen), max(zahlen), sum(zahlen)     # -> Tupel


kleinste, groesste, gesamt = min_max_summe([4, 9, 2, 7])
print(f"min={kleinste}, max={groesste}, summe={gesamt}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# SETS - Mengen ohne Duplikate
# ====================================================================
zahlen = [1, 3, 3, 5, 1, 7, 5, 9]
einmalig = set(zahlen)

print(f"Liste:          {zahlen}")
print(f"set(Liste):     {einmalig}   ← Duplikate weg!")
print(f"zurück zu Liste:{sorted(einmalig)}")

print()
s = {1, 2, 3}
s.add(4)
s.discard(1)
s.discard(99)          # kein Fehler, auch wenn nicht vorhanden
print(f"Nach add/discard: {s}")
print(f"3 in s:           {3 in s}")

leer = set()           # ⚠️ {} wäre ein leeres DICT
print(f"Leeres Set:       {leer}, Typ: {type(leer).__name__}")
print(f"{{}} ist ein:      {type({}).__name__}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# MENGENOPERATIONEN - sehr praktisch!
# ====================================================================
anna_skills = {"Python", "SQL", "Docker", "Git"}
bernd_skills = {"JavaScript", "Git", "Docker", "React"}

print(f"Anna:  {anna_skills}")
print(f"Bernd: {bernd_skills}")
print()
print(f"Beide können (&):        {anna_skills & bernd_skills}")
print(f"Zusammen (|):            {anna_skills | bernd_skills}")
print(f"Nur Anna (-):            {anna_skills - bernd_skills}")
print(f"Nur einer von beiden(^): {anna_skills ^ bernd_skills}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# 🌍 REALBEISPIEL: Dateien vergleichen
# ====================================================================
ordner_a = {"bericht.pdf", "foto.jpg", "notizen.txt", "daten.csv"}
ordner_b = {"bericht.pdf", "foto.jpg", "backup.zip"}

print("Backup-Vergleich:")
print(f"  Fehlt im Backup:   {ordner_a - ordner_b}")
print(f"  Nur im Backup:     {ordner_b - ordner_a}")
print(f"  In beiden:         {ordner_a & ordner_b}")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Finde die gemeinsamen Buchstaben von "Python" und "Programm".
#   2. Wie viele UNTERSCHIEDLICHE Wörter hat ein langer Satz?
#   3. Was passiert bei {1, 2} & {"a", "b"}?
# ------------------------------------------------------------------
