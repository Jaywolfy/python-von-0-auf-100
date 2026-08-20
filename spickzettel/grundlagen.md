# 🐍 Spickzettel · Grundlagen

## Ausgabe & Eingabe
```python
print("Hallo")                 # Text ausgeben
print("a", "b", sep="-")       # a-b
print("kein Umbruch", end="")  # ohne Zeilenumbruch
name = input("Dein Name: ")    # Eingabe (IMMER ein String!)
alter = int(input("Alter: "))  # Eingabe als Zahl
```

## Variablen & Typen
```python
name  = "Anna"     # str    Text
alter = 25          # int    Ganzzahl
groesse = 1.83      # float  Kommazahl (PUNKT!)
aktiv = True        # bool   True / False
nichts = None       # NoneType  "kein Wert"

type(alter)         # <class 'int'>
```

## Rechnen
```python
7 + 3      # 10   Addition
7 - 3      # 4    Subtraktion
7 * 3      # 21   Multiplikation
7 / 3      # 2.333…  Division -> IMMER float
7 // 3     # 2    Ganzzahldivision (abrunden)
7 % 3      # 1    Rest (Modulo)
7 ** 3     # 343  Potenz

x += 1     # x = x + 1     (auch -= *= /= //= %=)
round(3.567, 2)   # 3.57
abs(-5)           # 5
```

## Typumwandlung
```python
int("42")      # 42
float("3.14")  # 3.14
str(42)        # "42"
bool(0)        # False
list("abc")    # ['a','b','c']
```

## Vergleiche & Logik
```python
==  gleich          !=  ungleich
<   kleiner         >   größer
<=  kleiner-gleich  >=  größer-gleich

and   beide wahr       or   mindestens eins wahr
not   umkehren         in   enthalten?

3 < x < 10          # Verkettung erlaubt!
"a" in "hallo"      # False
```

## Bedingungen
```python
if temperatur > 30:
    print("heiß")
elif temperatur > 20:
    print("angenehm")
else:
    print("kalt")

# Kurzform (Ternary)
status = "warm" if temp > 20 else "kalt"
```

## Schleifen
```python
for i in range(5):          # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):   # 2,4,6,8  (start, stop, schritt)
    print(i)

for frucht in ["Apfel", "Birne"]:
    print(frucht)

for i, wert in enumerate(liste):     # Index + Wert
    print(i, wert)

while bedingung:
    ...
    break      # Schleife sofort verlassen
    continue   # zum nächsten Durchlauf springen

for x in liste:
    ...
else:          # läuft NUR, wenn kein break kam
    ...
```

## Funktionen
```python
def begruesse(name, gruss="Hallo"):
    """Gibt eine Begrüßung zurück."""
    return f"{gruss}, {name}!"

begruesse("Anna")                  # "Hallo, Anna!"
begruesse("Anna", gruss="Moin")    # "Moin, Anna!"

def mehrere():
    return 1, 2          # gibt ein Tupel zurück
a, b = mehrere()
```

## Wahrheitsgehalt (Truthiness)
```python
# Diese Werte gelten als FALSE:
False, None, 0, 0.0, "", [], {}, (), set()
# Alles andere ist TRUE

if liste:            # statt: if len(liste) > 0
    print("nicht leer")
```

## Kommentare
```python
# einzeiliger Kommentar

"""
Mehrzeiliger Text.
Als erste Zeile in Funktion/Klasse = Docstring.
"""
```

## Programmstart
```python
def main():
    ...

if __name__ == "__main__":
    main()
```

## Einrückung ⚠️
```python
# IMMER 4 Leerzeichen. NIE Tabs mischen.
if True:
    print("drin")     # gehört zum if
print("draußen")      # gehört nicht mehr dazu
```
