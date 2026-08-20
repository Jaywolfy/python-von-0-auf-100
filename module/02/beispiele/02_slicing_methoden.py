"""
Modul 02 - Beispiel 2: Slicing und String-Methoden
"""

# ====================================================================
# INDEX
# ====================================================================
#     P  y  t  h  o  n
#     0  1  2  3  4  5
#    -6 -5 -4 -3 -2 -1
t = "Python"

print("t         =", t)
print("t[0]      =", t[0])       # P
print("t[3]      =", t[3])       # h
print("t[-1]     =", t[-1])      # n   letztes Zeichen
print("t[-2]     =", t[-2])      # o
print("len(t)    =", len(t))     # 6

print("\n" + "-" * 55 + "\n")

# ====================================================================
# SLICING  [start:stop:schritt]   -  stop ist NICHT enthalten
# ====================================================================
print("t[0:3]    =", t[0:3])     # Pyt
print("t[:3]     =", t[:3])      # Pyt
print("t[3:]     =", t[3:])      # hon
print("t[:]      =", t[:])       # Python  (Kopie)
print("t[-3:]    =", t[-3:])     # hon     letzte 3
print("t[:-3]    =", t[:-3])     # Pyt     alles außer den letzten 3
print("t[::2]    =", t[::2])     # Pto     jedes 2. Zeichen
print("t[::-1]   =", t[::-1])    # nohtyP  UMGEDREHT ⭐

print("\n" + "-" * 55 + "\n")

# ====================================================================
# METHODEN
# ====================================================================
s = "   Hallo Welt   "
print(f"Original:      '{s}'")
print(f"strip():       '{s.strip()}'")
print(f"lstrip():      '{s.lstrip()}'")
print(f"rstrip():      '{s.rstrip()}'")
print(f"upper():       '{s.upper()}'")
print(f"lower():       '{s.lower()}'")
print(f"title():       '{s.title()}'")
print(f"replace():     '{s.replace('Welt', 'Python')}'")
print(f"count('l'):     {s.count('l')}")
print(f"find('Welt'):   {s.find('Welt')}")
print(f"find('xyz'):    {s.find('xyz')}   ← -1 heißt: nicht gefunden")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# WICHTIG: STRINGS SIND UNVERÄNDERLICH
# ====================================================================
wort = "hallo"
wort.upper()                 # Ergebnis wird weggeworfen!
print("Nach wort.upper():        ", wort)      # immer noch 'hallo'

wort = wort.upper()          # so ist es richtig
print("Nach wort = wort.upper(): ", wort)      # 'HALLO'

print("\n💡 String-Methoden GEBEN ZURÜCK, sie VERÄNDERN NICHT.")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# PRÜFUNGEN
# ====================================================================
print('"123".isdigit()          ->', "123".isdigit())
print('"12a".isdigit()          ->', "12a".isdigit())
print('"abc".isalpha()          ->', "abc".isalpha())
print('"bild.png".endswith(".png") ->', "bild.png".endswith(".png"))
print('"Herr Meier".startswith("Herr") ->', "Herr Meier".startswith("Herr"))
print('"lo" in "hallo"          ->', "lo" in "hallo")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# SPLIT & JOIN - das Power-Duo ⭐
# ====================================================================
zeile = "Anna,30,Berlin,Entwicklerin"
felder = zeile.split(",")
print("Zeile:  ", zeile)
print("split():", felder)
print("Name:   ", felder[0])
print("Stadt:  ", felder[2])

print()
satz = "Der schnelle braune Fuchs springt"
woerter = satz.split()
print("Wörter:", woerter)
print("Anzahl:", len(woerter))

print()
datum_teile = ["2026", "07", "26"]
print('"-".join(...)  ->', "-".join(datum_teile))
print('".".join(...)  ->', ".".join(reversed(datum_teile)))
print('", ".join(...) ->', ", ".join(["Äpfel", "Birnen", "Kirschen"]))

print()
# Kombination: Wörter umdrehen
print("Original:  ", satz)
print("Umgedreht: ", " ".join(satz.split()[::-1]))

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Hol aus "max.mustermann@firma.de" den Namen vor dem @.
#   2. Wandle "2026-07-26" in "26.07.2026" um.
#   3. Zähle, wie oft "a" in einem langen Satz vorkommt.
# ------------------------------------------------------------------
