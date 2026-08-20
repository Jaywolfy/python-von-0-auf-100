"""
Modul 15 - Beispiel: Vererbung, Dunder-Methoden, dataclasses
"""
from dataclasses import dataclass, field

# ====================================================================
# 1. VERERBUNG
# ====================================================================
print("=" * 60, "\n1. VERERBUNG\n", "=" * 60)


class Tier:
    """Basisklasse für alle Tiere."""

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def schlafen(self):
        return f"{self.name} schläft 😴"

    def laut(self):
        return "..."

    def steckbrief(self):
        return f"{self.name}, {self.alter} Jahre, sagt '{self.laut()}'"

    def __str__(self):
        return f"{type(self).__name__}({self.name})"


class Hund(Tier):
    """Ein Hund - ist ein Tier."""

    def __init__(self, name, alter, rasse):
        super().__init__(name, alter)     # ⭐ Elternteil macht name + alter
        self.rasse = rasse

    def laut(self):
        return "Wuff!"

    def steckbrief(self):
        return f"{super().steckbrief()} | Rasse: {self.rasse}"


class Katze(Tier):
    """Eine Katze - ist auch ein Tier."""

    def laut(self):
        return "Miau!"


class Fisch(Tier):
    """Ein Fisch - macht keinen Laut."""

    def schlafen(self):
        return f"{self.name} döst mit offenen Augen 🐟"


tiere = [Hund("Bello", 3, "Dackel"), Katze("Minka", 5), Fisch("Nemo", 1)]

for t in tiere:
    print(f"  {t}")
    print(f"    {t.steckbrief()}")
    print(f"    {t.schlafen()}")

print(f"\n  isinstance(tiere[0], Hund)  -> {isinstance(tiere[0], Hund)}")
print(f"  isinstance(tiere[0], Tier)  -> {isinstance(tiere[0], Tier)}  ← ein Hund IST ein Tier")
print(f"  isinstance(tiere[1], Hund)  -> {isinstance(tiere[1], Hund)}")


# ====================================================================
# 2. DUNDER-METHODEN
# ====================================================================
print("\n" + "=" * 60, "\n2. DUNDER-METHODEN\n", "=" * 60)


class Geld:
    """Ein Geldbetrag mit Währung."""

    def __init__(self, betrag, waehrung="EUR"):
        self.betrag = round(betrag, 2)
        self.waehrung = waehrung

    def __str__(self):
        return f"{self.betrag:.2f} {self.waehrung}"

    def __repr__(self):
        return f"Geld({self.betrag}, {self.waehrung!r})"

    def __add__(self, andere):
        if self.waehrung != andere.waehrung:
            raise ValueError("Verschiedene Währungen")
        return Geld(self.betrag + andere.betrag, self.waehrung)

    def __sub__(self, andere):
        return Geld(self.betrag - andere.betrag, self.waehrung)

    def __mul__(self, faktor):
        return Geld(self.betrag * faktor, self.waehrung)

    def __eq__(self, andere):
        return (self.betrag, self.waehrung) == (andere.betrag, andere.waehrung)

    def __lt__(self, andere):
        return self.betrag < andere.betrag


a = Geld(10.50)
b = Geld(5.25)

print(f"  str(a)      -> {a}")
print(f"  repr(a)     -> {a!r}")
print(f"  a + b       -> {a + b}")
print(f"  a - b       -> {a - b}")
print(f"  a * 3       -> {a * 3}")
print(f"  a == b      -> {a == b}")
print(f"  a > b       -> {a > b}")
print(f"  sorted      -> {sorted([a, b, Geld(99), Geld(0.5)])}")


class Warenkorb:
    """Ein Warenkorb, der sich wie eine Sammlung verhält."""

    def __init__(self):
        self.artikel = []

    def hinzufuegen(self, name, preis):
        self.artikel.append((name, Geld(preis)))
        return self

    def __len__(self):
        return len(self.artikel)

    def __getitem__(self, index):
        return self.artikel[index]

    def __contains__(self, name):
        return any(a == name for a, _ in self.artikel)

    def __str__(self):
        gesamt = sum(g.betrag for _, g in self.artikel)
        return f"Warenkorb({len(self)} Artikel, {gesamt:.2f} EUR)"


korb = Warenkorb()
korb.hinzufuegen("Kaffee", 8.99).hinzufuegen("Milch", 1.19).hinzufuegen("Brot", 2.49)

print(f"\n  len(korb)          -> {len(korb)}      ← dank __len__")
print(f"  korb[0]            -> {korb[0]}   ← dank __getitem__")
print(f"  'Milch' in korb    -> {'Milch' in korb}   ← dank __contains__")
print(f"  print(korb)        -> {korb}")
print("\n  for-Schleife funktioniert auch (dank __getitem__):")
for name, preis in korb:
    print(f"    {name:<10} {preis}")


# ====================================================================
# 3. DATACLASSES
# ====================================================================
print("\n" + "=" * 60, "\n3. @dataclass\n", "=" * 60)


@dataclass
class Punkt:
    """Ein Punkt im 2D-Raum."""
    x: float
    y: float = 0.0

    def abstand_zum_ursprung(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


p1 = Punkt(3, 4)
p2 = Punkt(3, 4)

print(f"  p1              -> {p1}          ← __repr__ geschenkt")
print(f"  p1 == p2        -> {p1 == p2}          ← __eq__ geschenkt")
print(f"  Abstand         -> {p1.abstand_zum_ursprung()}")


@dataclass
class Artikel:
    """Ein Artikel im Sortiment."""
    name: str
    preis: float
    bestand: int = 0
    tags: list = field(default_factory=list)      # ⚠️ NICHT tags: list = []

    def gesamtwert(self):
        return self.preis * self.bestand


artikel = [
    Artikel("Laptop", 899.99, 5, ["technik", "büro"]),
    Artikel("Maus", 25.50, 42, ["technik"]),
    Artikel("Notizbuch", 4.99, 120, ["büro"]),
]

print(f"\n  {'Artikel':<14}{'Preis':>10}{'Bestand':>10}{'Wert':>12}")
print("  " + "-" * 46)
for a in artikel:
    print(f"  {a.name:<14}{a.preis:>10.2f}{a.bestand:>10}{a.gesamtwert():>12.2f}")
print("  " + "-" * 46)
print(f"  {'GESAMT':<14}{'':>20}{sum(a.gesamtwert() for a in artikel):>12.2f}")
print(f"\n  Technik-Artikel: {[a.name for a in artikel if 'technik' in a.tags]}")


# ====================================================================
# 4. KOMPOSITION STATT VERERBUNG
# ====================================================================
print("\n" + "=" * 60, "\n4. KOMPOSITION vs. VERERBUNG\n", "=" * 60)


@dataclass
class Motor:
    """Ein Motor."""
    ps: int
    kraftstoff: str

    def starten(self):
        return f"Motor ({self.ps} PS, {self.kraftstoff}) startet 🔥"


class Auto:
    """Ein Auto HAT einen Motor (Komposition, nicht Vererbung!)."""

    def __init__(self, marke, modell, motor):
        self.marke = marke
        self.modell = modell
        self.motor = motor         # ← Komposition

    def starten(self):
        return f"{self.marke} {self.modell}: {self.motor.starten()}"

    def __str__(self):
        return f"{self.marke} {self.modell} ({self.motor.ps} PS)"


auto = Auto("VW", "Golf", Motor(150, "Benzin"))
e_auto = Auto("Tesla", "Model 3", Motor(283, "Strom"))

print(f"  {auto}")
print(f"    {auto.starten()}")
print(f"  {e_auto}")
print(f"    {e_auto.starten()}")

print("""
  💡 MERKSATZ:
     "Ein Hund IST EIN Tier"      -> Vererbung   ✅
     "Ein Auto IST EIN Motor"     -> Unsinn      ❌
     "Ein Auto HAT EINEN Motor"   -> Komposition ✅

     Im Zweifel: Komposition. Sie ist flexibler und führt
     seltener in Sackgassen.
""")
