"""
Modul 06 - Beispiel 1: Listen im Überblick
"""

# ====================================================================
# ERSTELLEN & ZUGREIFEN
# ====================================================================
namen = ["Anna", "Bernd", "Clara", "David"]

print(f"Liste:      {namen}")
print(f"namen[0]:   {namen[0]}")
print(f"namen[-1]:  {namen[-1]}      ← letztes Element")
print(f"namen[1:3]: {namen[1:3]}")
print(f"namen[:2]:  {namen[:2]}")
print(f"namen[::-1]:{namen[::-1]}")
print(f"len():      {len(namen)}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# LISTEN SIND VERÄNDERBAR (mutable)
# ====================================================================
namen[0] = "Anni"
print(f"Nach namen[0] = 'Anni': {namen}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# METHODEN
# ====================================================================
zahlen = [3, 1, 4]
print(f"Start:              {zahlen}")

zahlen.append(5)
print(f"append(5):          {zahlen}")

zahlen.insert(0, 9)
print(f"insert(0, 9):       {zahlen}")

zahlen.extend([6, 7])
print(f"extend([6,7]):      {zahlen}")

zahlen.remove(1)
print(f"remove(1) [WERT]:   {zahlen}")

letztes = zahlen.pop()
print(f"pop() -> {letztes}:        {zahlen}")

erstes = zahlen.pop(0)
print(f"pop(0) -> {erstes}:        {zahlen}")

print()
print(f"count(4):           {zahlen.count(4)}")
print(f"index(4):           {zahlen.index(4)}")
print(f"4 in zahlen:        {4 in zahlen}")
print(f"sum/min/max:        {sum(zahlen)} / {min(zahlen)} / {max(zahlen)}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# SORTIEREN - sort() vs. sorted()
# ====================================================================
original = [5, 2, 8, 1, 9]

kopie_sortiert = sorted(original)
print(f"Original:               {original}")
print(f"sorted(original):       {kopie_sortiert}   ← neue Liste")

original.sort()
print(f"nach original.sort():   {original}   ← Original verändert")

original.sort(reverse=True)
print(f"sort(reverse=True):     {original}")

woerter = ["Banane", "Apfel", "Kiwi", "Erdbeere"]
print()
print(f"Wörter:                 {woerter}")
print(f"sorted() alphabetisch:  {sorted(woerter)}")
print(f"sorted(key=len):        {sorted(woerter, key=len)}")

print("\n⚠️  liste = liste.sort()  ist ein KLASSISCHER FEHLER:")
test = [3, 1, 2]
ergebnis = test.sort()
print(f"   ergebnis = test.sort()  ->  ergebnis ist {ergebnis}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# ⚠️ DIE KOPIER-FALLE
# ====================================================================
a = [1, 2, 3]
b = a                 # KEINE Kopie - nur ein zweiter Name!
b.append(4)

print("a = [1,2,3]; b = a; b.append(4)")
print(f"   a = {a}   ← hat sich auch geändert! 😱")
print(f"   b = {b}")

print()
c = [1, 2, 3]
d = c.copy()          # echte Kopie
d.append(4)
print("c = [1,2,3]; d = c.copy(); d.append(4)")
print(f"   c = {c}      ← unverändert ✅")
print(f"   d = {d}")

print("\n💡 Drei Wege zum Kopieren: a.copy() | list(a) | a[:]")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Sortiere ["Zebra","apfel","Banane"] - was fällt auf?
#      (Tipp: key=str.lower)
#   2. Entferne alle Duplikate aus [1,2,2,3,3,3].
#   3. Was passiert bei liste.index(99), wenn 99 nicht drin ist?
# ------------------------------------------------------------------
