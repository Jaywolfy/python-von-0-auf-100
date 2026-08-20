"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 15 · MUSTERLÖSUNGEN                                       ║
╚══════════════════════════════════════════════════════════════════╝
"""
import math
from dataclasses import dataclass, field

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)


class Fahrzeug:
    """Basisklasse für alle Fahrzeuge."""

    def __init__(self, marke, baujahr):
        self.marke = marke
        self.baujahr = baujahr

    def beschreibung(self):
        return f"{self.marke} ({self.baujahr})"

    def __str__(self):
        return self.beschreibung()


class Auto(Fahrzeug):
    def __init__(self, marke, baujahr, tueren):
        super().__init__(marke, baujahr)
        self.tueren = tueren

    def beschreibung(self):
        return f"🚗 {super().beschreibung()}, {self.tueren} Türen"


class Motorrad(Fahrzeug):
    def __init__(self, marke, baujahr, hubraum):
        super().__init__(marke, baujahr)
        self.hubraum = hubraum

    def beschreibung(self):
        return f"🏍️  {super().beschreibung()}, {self.hubraum} ccm"


for f in (Auto("VW", 2020, 5), Auto("Fiat", 2018, 3),
          Motorrad("Honda", 2022, 650), Motorrad("BMW", 2019, 1200)):
    print(f"  {f}")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

print("""  VORHERSAGE: AttributeError: 'Kind' object has no attribute 'a'
  Weil Kind.__init__ die Elternversion nie aufruft, wird self.a
  nie gesetzt.""")


class Basis:
    def __init__(self, a):
        self.a = a


class Kind(Basis):
    def __init__(self, a, b):
        super().__init__(a)       # ✅ FIX
        self.b = b


k = Kind(1, 2)
print(f"  Repariert: k.a = {k.a}, k.b = {k.b} ✅")


print("\n" + "=" * 60, "\nAUFGABE 3 🟡\n", "=" * 60)


class Temperatur:
    """Eine Temperatur in Grad Celsius."""

    def __init__(self, celsius):
        self.celsius = round(celsius, 1)

    def in_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def __str__(self):
        return f"{self.celsius} °C"

    def __repr__(self):
        return f"Temperatur({self.celsius})"

    def __add__(self, andere):
        return Temperatur(self.celsius + andere.celsius)

    def __eq__(self, andere):
        return self.celsius == andere.celsius

    def __lt__(self, andere):
        return self.celsius < andere.celsius


t1, t2 = Temperatur(23.5), Temperatur(-4.2)
print(f"  t1              -> {t1}")
print(f"  repr(t1)        -> {t1!r}")
print(f"  t1 in °F        -> {t1.in_fahrenheit():.1f} °F")
print(f"  t1 + t2         -> {t1 + t2}")
print(f"  t1 > t2         -> {t1 > t2}")
temps = [Temperatur(x) for x in (18, -5, 31.2, 0, 7.7)]
print(f"  sortiert        -> {sorted(temps)}")
print(f"  wärmste         -> {max(temps)}")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)


@dataclass
class Mitarbeiter:
    """Ein Mitarbeiter im Unternehmen."""
    name: str
    abteilung: str
    gehalt: float
    skills: list = field(default_factory=list)

    def gehalt_erhoehen(self, prozent):
        self.gehalt = round(self.gehalt * (1 + prozent / 100), 2)
        return self.gehalt


team = [
    Mitarbeiter("Anna", "IT", 4800, ["Python", "SQL"]),
    Mitarbeiter("Bernd", "Marketing", 3900, ["SEO", "Texten"]),
    Mitarbeiter("Clara", "IT", 5600, ["Python", "Docker", "AWS"]),
    Mitarbeiter("David", "Vertrieb", 4200, ["CRM", "Texten"]),
]

print(f"  {'Name':<10}{'Abteilung':<14}{'Gehalt':>10}  Skills")
print("  " + "-" * 60)
for m in team:
    print(f"  {m.name:<10}{m.abteilung:<14}{m.gehalt:>10.2f}  {', '.join(m.skills)}")

gehaelter = [m.gehalt for m in team]
top = max(team, key=lambda m: m.gehalt)
alle_skills = sorted({s for m in team for s in m.skills})

pro_abteilung = {}
for m in team:
    pro_abteilung.setdefault(m.abteilung, []).append(m.name)

print("  " + "-" * 60)
print(f"  Ø Gehalt:        {sum(gehaelter) / len(gehaelter):,.2f} €")
print(f"  Spitzenverdiener:{top.name} ({top.gehalt:,.2f} €)")
print(f"  Alle Skills:     {alle_skills}")
print(f"  Pro Abteilung:   {pro_abteilung}")

team[1].gehalt_erhoehen(5)
print(f"  Bernd nach +5 %: {team[1].gehalt:,.2f} €")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)


@dataclass
class Song:
    titel: str
    kuenstler: str
    dauer_s: int


class Playlist:
    """Eine Playlist, die sich wie eine Sammlung verhält."""

    def __init__(self, name):
        self.name = name
        self.songs = []

    def hinzufuegen(self, song):
        self.songs.append(song)
        return self

    def gesamtdauer(self):
        return sum(s.dauer_s for s in self.songs) / 60

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, titel):
        return any(s.titel == titel for s in self.songs)

    def __str__(self):
        return f"{self.name} ({len(self)} Songs, {self.gesamtdauer():.1f} Min)"


pl = Playlist("Zum Programmieren")
pl.hinzufuegen(Song("Focus", "Lo-Fi Beats", 195))
pl.hinzufuegen(Song("Deep Work", "Ambient Co", 320))
pl.hinzufuegen(Song("Night Coding", "Synthwave", 248))

print(f"  {pl}")
print(f"  len(pl)              -> {len(pl)}")
print(f"  pl[0].titel          -> {pl[0].titel}")
print(f"  'Focus' in pl        -> {'Focus' in pl}")
print(f"  'Metal' in pl        -> {'Metal' in pl}")
print("  Alle Songs:")
for s in pl:
    print(f"    {s.titel:<16} {s.kuenstler:<16} {s.dauer_s // 60}:{s.dauer_s % 60:02d}")


print("\n" + "=" * 60, "\nAUFGABE 6 🔴\n", "=" * 60)

print("""  a) Quadrat <-> Rechteck        VERERBUNG    "Ein Quadrat IST ein Rechteck"
     (Vorsicht: klassisches Beispiel für Vererbungs-Fallstricke,
      wenn man breite/hoehe unabhängig ändern kann!)
  b) Haus <-> Zimmer             KOMPOSITION  "Ein Haus HAT Zimmer"
  c) Manager <-> Mitarbeiter     VERERBUNG    "Ein Manager IST ein Mitarbeiter"
  d) Buch <-> Seite              KOMPOSITION  "Ein Buch HAT Seiten"
  e) Elektroauto <-> Auto        VERERBUNG    "Ein E-Auto IST ein Auto"
  f) Playlist <-> Song           KOMPOSITION  "Eine Playlist HAT Songs"
""")


class MitarbeiterBasis:
    def __init__(self, name, gehalt):
        self.name = name
        self.gehalt = gehalt

    def rolle(self):
        return "Mitarbeiter"

    def __str__(self):
        return f"{self.name} ({self.rolle()}, {self.gehalt:,.0f} €)"


class Manager(MitarbeiterBasis):
    def __init__(self, name, gehalt, team_groesse):
        super().__init__(name, gehalt)
        self.team_groesse = team_groesse

    def rolle(self):
        return f"Manager von {self.team_groesse}"


@dataclass
class Zimmer:
    name: str
    qm: float


class Haus:
    """Ein Haus HAT Zimmer (Komposition)."""

    def __init__(self, adresse):
        self.adresse = adresse
        self.zimmer = []

    def zimmer_hinzufuegen(self, z):
        self.zimmer.append(z)
        return self

    def wohnflaeche(self):
        return sum(z.qm for z in self.zimmer)

    def __str__(self):
        return f"{self.adresse}: {len(self.zimmer)} Zimmer, {self.wohnflaeche():.1f} m²"


print("  Vererbung (c):")
print(f"    {MitarbeiterBasis('Anna', 4800)}")
print(f"    {Manager('Clara', 7200, 8)}")
print("  Komposition (b):")
haus = Haus("Hauptstraße 5")
haus.zimmer_hinzufuegen(Zimmer("Wohnzimmer", 28.5))
haus.zimmer_hinzufuegen(Zimmer("Küche", 12.0))
haus.zimmer_hinzufuegen(Zimmer("Schlafzimmer", 16.5))
print(f"    {haus}")


print("\n" + "=" * 60, "\nAUFGABE 7 ⭐\n", "=" * 60)


class Form:
    """Basisklasse für geometrische Formen."""

    def flaeche(self):
        raise NotImplementedError("Unterklasse muss flaeche() definieren")

    def umfang(self):
        raise NotImplementedError("Unterklasse muss umfang() definieren")

    def __str__(self):
        return (f"{type(self).__name__:<12} Fläche {self.flaeche():>8.2f}  "
                f"Umfang {self.umfang():>8.2f}")


class Rechteck(Form):
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

    def flaeche(self):
        return self.breite * self.hoehe

    def umfang(self):
        return 2 * (self.breite + self.hoehe)


class Quadrat(Rechteck):
    def __init__(self, seite):
        super().__init__(seite, seite)      # ein Quadrat IST ein Rechteck


class Kreis(Form):
    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        return math.pi * self.radius ** 2

    def umfang(self):
        return 2 * math.pi * self.radius


class Dreieck(Form):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def flaeche(self):
        s = self.umfang() / 2                 # Heron-Formel
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def umfang(self):
        return self.a + self.b + self.c


formen = [Rechteck(4, 6), Quadrat(5), Kreis(3), Dreieck(3, 4, 5), Kreis(1.5)]

print("  Nach Fläche sortiert:")
for f in sorted(formen, key=lambda f: f.flaeche()):
    print(f"    {f}")
print("  " + "-" * 50)
print(f"    {'GESAMT':<12} Fläche {sum(f.flaeche() for f in formen):>8.2f}")

try:
    Form().flaeche()
except NotImplementedError as fehler:
    print(f"\n  Form().flaeche() -> NotImplementedError: {fehler}")

print("\n🎉 Modul 15 geschafft! OOP sitzt. 🏛️")
