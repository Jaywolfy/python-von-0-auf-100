"""
Modul 14 - Beispiel: Klassen und Objekte
"""

# ====================================================================
# 1. DIE EINFACHSTE KLASSE
# ====================================================================
print("=" * 60, "\n1. EINFACHE KLASSE\n", "=" * 60)


class Hund:
    """Ein Hund mit Name und Rasse."""

    def __init__(self, name, rasse):
        # __init__ läuft AUTOMATISCH beim Erzeugen eines Objekts
        self.name = name            # Instanzattribut
        self.rasse = rasse

    def bellen(self):
        # self = "dieses konkrete Objekt"
        return f"{self.name} sagt Wuff!"

    def __str__(self):
        return f"{self.name} ({self.rasse})"


bello = Hund("Bello", "Dackel")
rex = Hund("Rex", "Schäferhund")

print(f"  bello.name  = {bello.name}")
print(f"  rex.rasse   = {rex.rasse}")
print(f"  bello.bellen() -> {bello.bellen()}")
print(f"  rex.bellen()   -> {rex.bellen()}")
print(f"  print(bello)   -> {bello}")
print("\n  💡 Zwei Objekte, eine Klasse - völlig unabhängig voneinander.")


# ====================================================================
# 2. WAS self WIRKLICH IST
# ====================================================================
print("\n" + "=" * 60, "\n2. self entzaubert\n", "=" * 60)

print(f"  bello.bellen()      -> {bello.bellen()}")
print(f"  Hund.bellen(bello)  -> {Hund.bellen(bello)}")
print("""
  💡 Beides ist DASSELBE. Python schreibt bello.bellen() intern in
     Hund.bellen(bello) um. Deshalb ist self immer der erste Parameter -
     und deshalb gibst du ihn beim Aufruf NICHT an.
""")


# ====================================================================
# 3. EINE KLASSE MIT ZUSTAND
# ====================================================================
print("=" * 60, "\n3. Klasse mit Zustand: Konto\n", "=" * 60)


class Konto:
    """Ein Bankkonto mit Buchungshistorie."""

    zinssatz = 0.02          # KLASSENATTRIBUT - für alle Konten gleich

    def __init__(self, inhaber, stand=0.0):
        self.inhaber = inhaber
        self.stand = stand
        self.buchungen = []          # jedes Objekt bekommt seine EIGENE Liste

    def einzahlen(self, betrag):
        """Zahlt einen Betrag ein."""
        if betrag <= 0:
            raise ValueError("Betrag muss positiv sein")
        self.stand += betrag
        self.buchungen.append(("Einzahlung", betrag))
        return self.stand

    def abheben(self, betrag):
        """Hebt einen Betrag ab, wenn genug Guthaben da ist."""
        if betrag > self.stand:
            raise ValueError(f"Nur {self.stand:.2f} € verfügbar")
        self.stand -= betrag
        self.buchungen.append(("Abhebung", -betrag))
        return self.stand

    def zinsen_gutschreiben(self):
        """Schreibt Zinsen nach dem aktuellen Zinssatz gut."""
        zinsen = self.stand * Konto.zinssatz
        self.stand += zinsen
        self.buchungen.append(("Zinsen", zinsen))
        return zinsen

    def kontoauszug(self):
        """Gibt einen formatierten Kontoauszug als String zurück."""
        zeilen = [f"  Kontoauszug: {self.inhaber}", "  " + "-" * 34]
        for art, betrag in self.buchungen:
            zeilen.append(f"  {art:<16}{betrag:>16.2f} €")
        zeilen.append("  " + "-" * 34)
        zeilen.append(f"  {'STAND':<16}{self.stand:>16.2f} €")
        return "\n".join(zeilen)

    def __str__(self):
        return f"Konto({self.inhaber}: {self.stand:.2f} €)"


konto_anna = Konto("Anna", 1000)
konto_bernd = Konto("Bernd")

konto_anna.einzahlen(500)
konto_anna.abheben(200)
konto_anna.zinsen_gutschreiben()

konto_bernd.einzahlen(50)

print(konto_anna.kontoauszug())
print()
print(f"  {konto_anna}")
print(f"  {konto_bernd}")
print(f"\n  Bernds Buchungen: {konto_bernd.buchungen}")
print("  💡 Getrennte Listen! Weil sie in __init__ angelegt werden.")

# Fehlerbehandlung greift auch hier
try:
    konto_bernd.abheben(1000)
except ValueError as fehler:
    print(f"\n  Abhebung abgelehnt: {fehler}")


# ====================================================================
# 4. ⚠️ DIE KLASSENATTRIBUT-FALLE
# ====================================================================
print("\n" + "=" * 60, "\n4. ⚠️ Klassenattribut-Falle\n", "=" * 60)


class KursFalsch:
    teilnehmer = []              # ❌ ALLE Kurse teilen sich diese Liste!

    def __init__(self, name):
        self.name = name

    def anmelden(self, person):
        self.teilnehmer.append(person)


class KursRichtig:
    def __init__(self, name):
        self.name = name
        self.teilnehmer = []     # ✅ eigene Liste pro Objekt

    def anmelden(self, person):
        self.teilnehmer.append(person)


a = KursFalsch("Python")
b = KursFalsch("Java")
a.anmelden("Anna")
print(f"  ❌ KursFalsch:  Java-Kurs hat plötzlich {b.teilnehmer} 😱")

c = KursRichtig("Python")
d = KursRichtig("Java")
c.anmelden("Anna")
print(f"  ✅ KursRichtig: Java-Kurs hat {d.teilnehmer}")


# ====================================================================
# 5. MEHRERE OBJEKTE VERWALTEN
# ====================================================================
print("\n" + "=" * 60, "\n5. Viele Objekte verwalten\n", "=" * 60)

konten = [
    Konto("Anna", 1500),
    Konto("Bernd", 320),
    Konto("Clara", 8900),
    Konto("David", 75),
]

print(f"  {'Inhaber':<10}{'Stand':>12}")
print("  " + "-" * 22)
for k in sorted(konten, key=lambda k: k.stand, reverse=True):
    print(f"  {k.inhaber:<10}{k.stand:>10.2f} €")

gesamt = sum(k.stand for k in konten)
reichste = max(konten, key=lambda k: k.stand)
print("  " + "-" * 22)
print(f"  {'SUMME':<10}{gesamt:>10.2f} €")
print(f"  Höchster Stand: {reichste.inhaber}")
print(f"  Über 1000 €:    {[k.inhaber for k in konten if k.stand > 1000]}")

print("""
  💡 Objekte lassen sich genau wie alle anderen Werte in Listen
     packen, sortieren, filtern und auswerten.
""")
