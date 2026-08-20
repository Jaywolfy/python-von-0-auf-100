# 📋 Spickzettel · Listen, Dicts, Tupel, Sets

## Welche Struktur wann? 🤔
| Ich brauche… | Nimm |
|---|---|
| Reihenfolge, änderbar | **Liste** `[]` |
| Reihenfolge, fix (z. B. Koordinaten) | **Tupel** `()` |
| Nachschlagen per Name/Schlüssel | **Dict** `{}` |
| Duplikate entfernen, schnelles „ist drin?" | **Set** `{}` |

---

## Listen
```python
l = [3, 1, 2]

l[0]            # 3
l[-1]           # 2
l[0:2]          # [3, 1]
len(l)          # 3

l.append(4)         # ans Ende
l.insert(0, 9)      # an Position
l.extend([5,6])     # mehrere anhängen
l.remove(1)         # ERSTES Vorkommen von Wert 1 löschen
x = l.pop()         # letztes Element entfernen UND zurückgeben
x = l.pop(0)        # erstes
del l[0]            # nach Index löschen
l.clear()           # alles weg

l.sort()                    # ändert die Liste
l.sort(reverse=True)
l.sort(key=len)             # nach Kriterium
sorted(l)                   # gibt NEUE Liste zurück
l.reverse()
l.count(3)
l.index(3)          # Position von Wert 3
3 in l              # True/False
sum(l), min(l), max(l)

kopie = l.copy()    # ⚠️ kopie = l wäre nur ein zweiter Name!
```

### Comprehensions ✨
```python
[x * 2 for x in range(5)]                  # [0,2,4,6,8]
[x for x in zahlen if x > 0]               # filtern
[x if x > 0 else 0 for x in zahlen]        # umformen
[(x, y) for x in "ab" for y in [1, 2]]     # verschachtelt
```

---

## Dictionaries
```python
d = {"name": "Anna", "alter": 30}

d["name"]                # "Anna"  → KeyError wenn nicht da
d.get("stadt")           # None    → sicher!
d.get("stadt", "unbek.") # Standardwert

d["stadt"] = "Berlin"    # hinzufügen/ändern
d.update({"a": 1, "b": 2})
del d["alter"]
wert = d.pop("alter", None)

d.keys()      # dict_keys(['name','stadt'])
d.values()
d.items()     # Paare

for k, v in d.items():
    print(k, "=", v)

"name" in d              # prüft SCHLÜSSEL
len(d)

{k: v * 2 for k, v in d.items()}      # Dict-Comprehension
```

### Verschachtelt
```python
personen = {
    "anna": {"alter": 30, "hobbys": ["lesen", "laufen"]},
    "ben":  {"alter": 25, "hobbys": ["kochen"]},
}
personen["anna"]["hobbys"][0]     # "lesen"
```

---

## Tupel (unveränderlich)
```python
t = (1, 2, 3)
t = 1, 2, 3          # Klammern optional
einzel = (1,)        # ⚠️ Komma nötig!

a, b, c = t          # Unpacking
erste, *rest = [1,2,3,4]     # erste=1, rest=[2,3,4]

t[0]                 # lesen ok
t[0] = 9             # ❌ TypeError
```

---

## Sets (Mengen)
```python
s = {1, 2, 3}
s = set([1,1,2,2])   # {1, 2}  → Duplikate weg!
leer = set()         # ⚠️ {} wäre ein Dict!

s.add(4)
s.discard(1)         # kein Fehler wenn nicht da
s.remove(1)          # KeyError wenn nicht da

a | b    # Vereinigung
a & b    # Schnittmenge
a - b    # Differenz
a ^ b    # nur in einem von beiden

3 in s   # sehr schnell! ⚡
```

---

## ⚠️ Die drei häufigsten Fallen

```python
# 1) Zuweisung kopiert NICHT
a = [1,2,3]
b = a          # b ist DIESELBE Liste
b.append(4)
print(a)       # [1,2,3,4]  😱
b = a.copy()   # ✅ so

# 2) Während des Iterierens verändern
for x in liste:
    liste.remove(x)        # ❌ überspringt Elemente
liste = [x for x in liste if bedingung]   # ✅

# 3) Veränderbarer Default-Parameter
def f(items=[]):     # ❌ wird zwischen Aufrufen geteilt!
def f(items=None):   # ✅
    if items is None:
        items = []
```
