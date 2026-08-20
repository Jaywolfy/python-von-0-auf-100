"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 14 · MUSTERLÖSUNGEN — Klassen & Objekte                   ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)


class Person:
    """Eine Person mit Name, Alter und Wohnort."""

    def __init__(self, name, alter, stadt):
        self.name = name
        self.alter = alter
        self.stadt = stadt

    def vorstellen(self):
        """Gibt einen Vorstellungssatz zurück."""
        return f"Ich bin {self.name}, {self.alter}, aus {self.stadt}"

    def __str__(self):
        return f"Person({self.name}, {self.alter})"


personen = [Person("Anna", 30, "Berlin"),
            Person("Bernd", 25, "Hamburg"),
            Person("Clara", 41, "München")]

for p in personen:
    print(f"  {p}  ->  {p.vorstellen()}")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)


class Rechteck:
    """Ein Rechteck mit Breite und Höhe."""

    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

    def flaeche(self):
        return self.breite * self.hoehe

    def umfang(self):
        return 2 * (self.breite + self.hoehe)

    def ist_quadrat(self):
        return self.breite == self.hoehe

    def __str__(self):
        return f"Rechteck {self.breite}x{self.hoehe} (Fläche {self.flaeche()})"


for r in (Rechteck(3, 4), Rechteck(5, 5), Rechteck(2, 10)):
    print(f"  {r}  Umfang {r.umfang()}  Quadrat: {r.ist_quadrat()}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟡\n", "=" * 60)


class Zaehler:
    """Ein Zähler, der seinen kompletten Verlauf mitschreibt."""

    def __init__(self, start=0):
        self.start = start
        self.wert = start
        self.verlauf = [start]

    def hoch(self, schritt=1):
        self.wert += schritt
        self.verlauf.append(self.wert)
        return self.wert

    def runter(self, schritt=1):
        self.wert -= schritt
        self.verlauf.append(self.wert)
        return self.wert

    def zuruecksetzen(self):
        self.wert = self.start
        self.verlauf.append(self.wert)
        return self.wert

    def __str__(self):
        return f"Zähler: {self.wert} (nach {len(self.verlauf) - 1} Schritten)"


z = Zaehler()
z.hoch()
z.hoch()
z.runter()
z.hoch(5)
print(f"  {z}")
print(f"  Verlauf: {z.verlauf}")
z.zuruecksetzen()
print(f"  Nach Reset: {z}  Verlauf: {z.verlauf}")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)


class Einkaufswagen:
    """Ein Einkaufswagen mit Artikeln, Preisen und Mengen."""

    def __init__(self):
        self.artikel = {}      # {name: (preis, menge)}

    def hinzufuegen(self, name, preis, menge=1):
        if name in self.artikel:
            alter_preis, alte_menge = self.artikel[name]
            self.artikel[name] = (alter_preis, alte_menge + menge)
        else:
            self.artikel[name] = (preis, menge)

    def entfernen(self, name):
        if name not in self.artikel:
            raise KeyError(f"'{name}' ist nicht im Wagen")
        del self.artikel[name]

    def gesamtpreis(self):
        return sum(preis * menge for preis, menge in self.artikel.values())

    def anzahl_artikel(self):
        return sum(menge for _, menge in self.artikel.values())

    def rechnung(self):
        zeilen = ["  RECHNUNG", "  " + "-" * 38]
        for name, (preis, menge) in self.artikel.items():
            zeilen.append(f"  {name:<16}{menge:>3} x {preis:>6.2f} = {preis * menge:>8.2f}")
        zeilen.append("  " + "-" * 38)
        zeilen.append(f"  {'SUMME':<16}{'':>12}{self.gesamtpreis():>10.2f}")
        return "\n".join(zeilen)

    def __str__(self):
        return f"Einkaufswagen({self.anzahl_artikel()} Artikel, {self.gesamtpreis():.2f} €)"


wagen = Einkaufswagen()
wagen.hinzufuegen("Kaffee", 8.99, 2)
wagen.hinzufuegen("Milch", 1.19, 6)
wagen.hinzufuegen("Brot", 2.49)
wagen.hinzufuegen("Käse", 4.80, 1)
print(wagen.rechnung())
print(f"\n  {wagen}")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

print("""  BUG: 'inventar = []' ist ein KLASSENATTRIBUT.
       Alle Spieler teilen sich DIESELBE Liste.
       Hebt Anna ein Schwert auf, hat Bernd es auch.
  FIX: Die Liste in __init__ anlegen -> self.inventar = []
""")


class Spieler:
    """Ein Spieler mit eigenem Inventar."""

    def __init__(self, name):
        self.name = name
        self.inventar = []      # ✅ eigene Liste pro Spieler

    def aufheben(self, gegenstand):
        self.inventar.append(gegenstand)
        return self.inventar

    def __str__(self):
        return f"{self.name}: {self.inventar}"


a = Spieler("Anna")
b = Spieler("Bernd")
a.aufheben("Schwert")
a.aufheben("Trank")
print(f"  {a}")
print(f"  {b}   ← korrekt leer ✅")


print("\n" + "=" * 60, "\nAUFGABE 6 🔴\n", "=" * 60)


class BuchNichtVerfuegbarError(Exception):
    """Das Buch ist bereits ausgeliehen."""


class Buch:
    """Ein Buch in der Bibliothek."""

    def __init__(self, titel, autor, jahr):
        self.titel = titel
        self.autor = autor
        self.jahr = jahr
        self.ausgeliehen = False

    def ausleihen(self):
        if self.ausgeliehen:
            raise BuchNichtVerfuegbarError(f"'{self.titel}' ist bereits ausgeliehen")
        self.ausgeliehen = True
        return True

    def zurueckgeben(self):
        self.ausgeliehen = False
        return True

    def __str__(self):
        status = "📕 ausgeliehen" if self.ausgeliehen else "📗 verfügbar"
        return f"{self.titel:<28} {self.autor:<18} {self.jahr}  {status}"


class Bibliothek:
    """Verwaltet eine Sammlung von Büchern."""

    def __init__(self, name):
        self.name = name
        self.buecher = []

    def hinzufuegen(self, buch):
        self.buecher.append(buch)

    def suche(self, stichwort):
        s = stichwort.lower()
        return [b for b in self.buecher
                if s in b.titel.lower() or s in b.autor.lower()]

    def verfuegbare(self):
        return [b for b in self.buecher if not b.ausgeliehen]

    def ausgeliehene(self):
        return [b for b in self.buecher if b.ausgeliehen]

    def statistik(self):
        gesamt = len(self.buecher)
        aus = len(self.ausgeliehene())
        quote = aus / gesamt if gesamt else 0
        return (f"  {self.name}: {gesamt} Bücher | "
                f"{gesamt - aus} verfügbar | {aus} ausgeliehen ({quote:.0%})")


bib = Bibliothek("Stadtbibliothek")
for titel, autor, jahr in [
    ("Der Prozess", "Kafka", 1925),
    ("Die Verwandlung", "Kafka", 1915),
    ("Faust", "Goethe", 1808),
    ("Der Steppenwolf", "Hesse", 1927),
    ("Siddhartha", "Hesse", 1922),
]:
    bib.hinzufuegen(Buch(titel, autor, jahr))

bib.buecher[0].ausleihen()
bib.buecher[3].ausleihen()

print("  BESTAND:")
for b in bib.buecher:
    print(f"    {b}")

print(f"\n  Suche 'Kafka': {[b.titel for b in bib.suche('Kafka')]}")
print(f"  Verfügbar:     {len(bib.verfuegbare())}")
print()
print(bib.statistik())

try:
    bib.buecher[0].ausleihen()
except BuchNichtVerfuegbarError as fehler:
    print(f"\n  ❌ {fehler}")


print("\n" + "=" * 60, "\nAUFGABE 7 ⭐\n", "=" * 60)


class Aufgabe:
    """Eine einzelne To-do-Aufgabe."""

    PRIO_SYMBOLE = {1: "🔴", 2: "🟡", 3: "🟢"}

    def __init__(self, titel, prioritaet=2, faellig=""):
        if prioritaet not in (1, 2, 3):
            raise ValueError("Priorität muss 1, 2 oder 3 sein")
        self.titel = titel
        self.prioritaet = prioritaet
        self.faellig = faellig
        self.erledigt = False

    def abhaken(self):
        self.erledigt = True

    def __str__(self):
        kaestchen = "☑" if self.erledigt else "☐"
        symbol = self.PRIO_SYMBOLE[self.prioritaet]
        return f"{kaestchen} {symbol} {self.titel:<32} {self.faellig}"


class AufgabenListe:
    """Verwaltet mehrere Aufgaben."""

    def __init__(self, name):
        self.name = name
        self.aufgaben = []

    def hinzufuegen(self, aufgabe):
        self.aufgaben.append(aufgabe)

    def erledigen(self, titel):
        for a in self.aufgaben:
            if a.titel == titel:
                a.abhaken()
                return True
        raise KeyError(f"Aufgabe '{titel}' nicht gefunden")

    def offene(self):
        return [a for a in self.aufgaben if not a.erledigt]

    def erledigte(self):
        return [a for a in self.aufgaben if a.erledigt]

    def nach_prioritaet(self):
        return sorted(self.aufgaben, key=lambda a: (a.erledigt, a.prioritaet))

    def fortschritt(self):
        gesamt = len(self.aufgaben)
        fertig = len(self.erledigte())
        anteil = fertig / gesamt if gesamt else 0
        balken = "█" * int(anteil * 20) + "░" * (20 - int(anteil * 20))
        return f"{balken} {fertig}/{gesamt} erledigt ({anteil:.0%})"

    def __str__(self):
        zeilen = [f"  ╔{'═' * 52}╗",
                  f"  ║ {self.name:<50} ║",
                  f"  ╚{'═' * 52}╝"]
        for a in self.nach_prioritaet():
            zeilen.append(f"    {a}")
        zeilen.append(f"\n    {self.fortschritt()}")
        return "\n".join(zeilen)


liste = AufgabenListe("MEINE AUFGABEN")
for titel, prio, faellig in [
    ("Modul 14 durcharbeiten", 1, "27.07."),
    ("Einkaufen gehen", 3, "26.07."),
    ("Steuererklärung", 1, "31.07."),
    ("Zahnarzttermin machen", 2, "02.08."),
    ("Repo aufräumen", 3, ""),
    ("Journal schreiben", 2, "heute"),
]:
    liste.hinzufuegen(Aufgabe(titel, prio, faellig))

liste.erledigen("Einkaufen gehen")
liste.erledigen("Journal schreiben")
liste.erledigen("Modul 14 durcharbeiten")

print(liste)

print("\n🎉 Modul 14 geschafft!")
