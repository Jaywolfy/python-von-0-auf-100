# 🔤 Spickzettel · Strings

## Erstellen
```python
a = "doppelte"
b = 'einfache'
c = """mehrere
Zeilen"""
d = "Er sagte \"Hallo\""     # Escape
e = r"C:\neuer\ordner"       # raw string: \n bleibt \n
```

## f-Strings ⭐ (die moderne Art)
```python
name, alter = "Anna", 30
f"{name} ist {alter}"          # Anna ist 30
f"{3.14159:.2f}"               # 3.14   (2 Nachkommastellen)
f"{1234567:,}"                 # 1,234,567
f"{0.856:.1%}"                 # 85.6%
f"{name:>10}"                  # rechtsbündig, Breite 10
f"{name:<10}"                  # linksbündig
f"{name:^10}"                  # zentriert
f"{name:*^10}"                 # ***Anna***
f"{alter=}"                    # alter=30   (super zum Debuggen!)
```

## Index & Slicing
```python
t = "Programmieren"
#    0123456789...        von hinten: -1 ist das letzte

t[0]        # 'P'
t[-1]       # 'n'
t[0:7]      # 'Program'   (bis 7 AUSSCHLIESSLICH)
t[:7]       # 'Program'
t[7:]       # 'mieren'
t[::2]      # 'Pormire'   jedes 2. Zeichen
t[::-1]     # 'nereimmargorP'   umdrehen!
len(t)      # 13
```

## Wichtigste Methoden
```python
s = "  Hallo Welt  "

s.strip()              # "Hallo Welt"   Leerzeichen weg
s.lstrip() / rstrip()  # nur links/rechts
s.upper()              # "  HALLO WELT  "
s.lower()              # "  hallo welt  "
s.title()              # "  Hallo Welt  "
s.capitalize()         # nur 1. Buchstabe groß
s.replace("Welt","Du") # ersetzen
s.split()              # ['Hallo','Welt']  (an Leerzeichen)
"a,b,c".split(",")     # ['a','b','c']
"-".join(["a","b"])    # "a-b"
s.find("Welt")         # Index oder -1
s.count("l")           # Anzahl
s.startswith("  H")    # True
s.endswith("t  ")      # False
s.center(20, "*")
s.zfill(5)             # "00042" bei "42"
```

## Prüfungen
```python
"abc".isalpha()      # nur Buchstaben?
"123".isdigit()      # nur Ziffern?
"a1".isalnum()       # Buchstaben oder Ziffern?
"  ".isspace()       # nur Leerraum?
"Abc".islower()      # alles klein?
```

## Wichtig: Strings sind unveränderlich!
```python
s = "hallo"
s[0] = "H"        # ❌ TypeError!
s = "H" + s[1:]   # ✅ so geht's
s = s.upper()     # ✅ Methoden geben NEUEN String zurück
```

## Mehrfach & Vergleich
```python
"-" * 30              # "------------------------------"
"a" in "hallo"        # False
"al" in "hallo"       # True
"apfel" < "birne"     # True (alphabetisch)
```
