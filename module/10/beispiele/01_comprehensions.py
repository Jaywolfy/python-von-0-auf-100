"""
Modul 10 - Beispiel 1: Comprehensions und Builtins
"""

zahlen = [4, -2, 7, 0, -9, 15, 3]
woerter = ["Banane", "Kiwi", "apfel", "Zitrone", "erdbeere"]

# ====================================================================
# LIST-COMPREHENSIONS
# ====================================================================
print("=" * 60)
print("LIST-COMPREHENSIONS")
print("=" * 60)

# Vorher / Nachher
quadrate_lang = []
for x in range(6):
    quadrate_lang.append(x ** 2)

quadrate_kurz = [x ** 2 for x in range(6)]

print(f"Mit Schleife:      {quadrate_lang}")
print(f"Mit Comprehension: {quadrate_kurz}")

print()
print(f"Ausgangsliste:     {zahlen}")
print(f"Verdoppelt:        {[x * 2 for x in zahlen]}")
print(f"Nur positive:      {[x for x in zahlen if x > 0]}")
print(f"Quadrate gerader:  {[x**2 for x in zahlen if x % 2 == 0]}")
print(f"Negative -> 0:     {[x if x > 0 else 0 for x in zahlen]}")
print(f"Beträge:           {[abs(x) for x in zahlen]}")

print()
print(f"Wörter:            {woerter}")
print(f"Großgeschrieben:   {[w.upper() for w in woerter]}")
print(f"Längen:            {[len(w) for w in woerter]}")
print(f"Länger als 5:      {[w for w in woerter if len(w) > 5]}")
print(f"Erste Buchstaben:  {[w[0] for w in woerter]}")

print("""
💡 MERKE:
   Filter (nur if):   [ausdruck  for x in daten  if bedingung]
   if/else:           [a if bedingung else b  for x in daten]
   Der Unterschied: beim Filtern steht if HINTEN, beim Umformen VORNE.
""")

# ====================================================================
# DICT- UND SET-COMPREHENSIONS
# ====================================================================
print("=" * 60)
print("DICT- UND SET-COMPREHENSIONS")
print("=" * 60)

laengen = {w: len(w) for w in woerter}
print(f"Wort -> Länge:     {laengen}")

kuerzel = {"DE": "Deutschland", "FR": "Frankreich"}
umgedreht = {v: k for k, v in kuerzel.items()}
print(f"Dict umgedreht:    {umgedreht}")

nur_lange = {w: len(w) for w in woerter if len(w) > 5}
print(f"Nur lange Wörter:  {nur_lange}")

einmalige_laengen = {len(w) for w in woerter}
print(f"Set der Längen:    {einmalige_laengen}")

# ====================================================================
# ENUMERATE & ZIP
# ====================================================================
print("\n" + "=" * 60)
print("ENUMERATE & ZIP")
print("=" * 60)

namen = ["Anna", "Bernd", "Clara"]
alter = [30, 25, 41]
staedte = ["Berlin", "Hamburg", "München"]

print("enumerate:")
for nr, name in enumerate(namen, start=1):
    print(f"  {nr}. {name}")

print("\nzip (zwei Listen parallel):")
for name, a in zip(namen, alter):
    print(f"  {name:<8} {a} Jahre")

print("\nzip (drei Listen):")
for name, a, stadt in zip(namen, alter, staedte):
    print(f"  {name:<8} {a:>3}  {stadt}")

print(f"\ndict(zip(...)):  {dict(zip(namen, alter))}")

# ====================================================================
# SORTED MIT KEY
# ====================================================================
print("\n" + "=" * 60)
print("SORTED MIT KEY")
print("=" * 60)

print(f"Original:            {woerter}")
print(f"Standard:            {sorted(woerter)}   ← Großbuchstaben zuerst!")
print(f"key=str.lower:       {sorted(woerter, key=str.lower)}")
print(f"key=len:             {sorted(woerter, key=len)}")
print(f"key=len, reverse:    {sorted(woerter, key=len, reverse=True)}")

personen = [
    {"name": "Anna", "alter": 30},
    {"name": "Bernd", "alter": 25},
    {"name": "Clara", "alter": 41},
]
nach_alter = sorted(personen, key=lambda p: p["alter"])
print(f"\nNach Alter sortiert: {[p['name'] for p in nach_alter]}")
print(f"Älteste Person:      {max(personen, key=lambda p: p['alter'])['name']}")

# ====================================================================
# ANY & ALL
# ====================================================================
print("\n" + "=" * 60)
print("ANY & ALL")
print("=" * 60)

passwort = "Sonne2026"
noten = [2.3, 1.7, 3.0, 4.0]
dateien = ["bericht.pdf", "foto.jpg", "notiz.txt"]

print(f'any(z.isdigit() for z in "{passwort}")     -> {any(z.isdigit() for z in passwort)}')
print(f'any(z.isupper() for z in "{passwort}")     -> {any(z.isupper() for z in passwort)}')
print(f"all(n <= 4.0 for n in {noten})  -> {all(n <= 4.0 for n in noten)}")
print(f"any(d.endswith('.pdf') for d in dateien)  -> {any(d.endswith('.pdf') for d in dateien)}")
print(f"all(d.endswith('.pdf') for d in dateien)  -> {all(d.endswith('.pdf') for d in dateien)}")

# ====================================================================
# ⚠️ WANN NICHT
# ====================================================================
print("\n" + "=" * 60)
print("⚠️  WANN KEINE COMPREHENSION")
print("=" * 60)
print("""
❌ Unlesbar:
   erg = [y*2 for x in daten if x for y in x if y > 0 and y < 100]

✅ Lesbar:
   erg = []
   for x in daten:
       if not x:
           continue
       for y in x:
           if 0 < y < 100:
               erg.append(y * 2)

👉 Regel: Passt es in EINE Zeile und du verstehst es beim ersten Lesen?
          Dann Comprehension. Sonst Schleife.
          Lesbarkeit schlägt Kürze. IMMER.
""")
