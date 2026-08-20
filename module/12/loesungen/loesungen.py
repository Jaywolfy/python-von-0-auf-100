"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 12 · MUSTERLÖSUNGEN — Module & Standardbibliothek         ║
╚══════════════════════════════════════════════════════════════════╝
"""
import random
import string
from datetime import date, datetime, timedelta
from collections import Counter

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

heute = date.today()
print(f"  a) Heute:          {heute.strftime('%d.%m.%Y')}")
print(f"  b) Wochentag:      {heute.strftime('%A')}")
print(f"  c) In 100 Tagen:   {(heute + timedelta(days=100)).strftime('%d.%m.%Y')}")
silvester = date(heute.year, 12, 31)
print(f"  d) Bis Silvester:  {(silvester - heute).days} Tage")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

random.seed(1)

wuerfe = [random.randint(1, 6) for _ in range(1000)]
zaehler = Counter(wuerfe)
print("  a) 1000 Würfe:")
for augen in sorted(zaehler):
    anzahl = zaehler[augen]
    print(f"     {augen}: {anzahl:>4}  {'█' * (anzahl // 8)}")

print(f"\n  b) Lottozahlen: {sorted(random.sample(range(1, 50), 6))}")

farben = ["Herz", "Karo", "Pik", "Kreuz"]
werte = ["7", "8", "9", "10", "B", "D", "K", "A"]
deck = [f"{f} {w}" for f in farben for w in werte]
random.shuffle(deck)
print(f"  c) Erste 5 Karten: {deck[:5]}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟡\n", "=" * 60)

text = """Der schnelle braune Fuchs springt über den faulen Hund
Der Hund schläft weiter Der Fuchs rennt weiter"""

woerter = text.lower().split()
wort_zaehler = Counter(woerter)

print("  a) Top 5 Wörter:")
for wort, anzahl in wort_zaehler.most_common(5):
    print(f"     {wort:<12} {anzahl}x")

buchstaben = Counter(z for z in text.lower() if z.isalpha())
print("\n  b) Top 5 Buchstaben:")
for z, anzahl in buchstaben.most_common(5):
    print(f"     '{z}' {anzahl}x")

print(f"\n  c) Unterschiedliche Wörter: {len(wort_zaehler)}")
einmalig = [w for w, n in wort_zaehler.items() if n == 1]
print(f"  d) Nur einmal ({len(einmalig)}): {sorted(einmalig)}")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)
print("""  Beispiel für meine_werkzeuge.py:

    \"\"\"Meine persönliche Werkzeugkiste.\"\"\"

    def prozent(teil, ganzes):
        \"\"\"Berechnet den Prozentanteil.\"\"\"
        return teil / ganzes * 100 if ganzes else 0

    def kuerze(text, laenge=30):
        \"\"\"Kürzt Text und hängt ... an.\"\"\"
        return text if len(text) <= laenge else text[:laenge - 3] + "..."

    def titel(text, breite=50):
        \"\"\"Gibt eine Überschrift mit Rahmen zurück.\"\"\"
        return f"{'=' * breite}\\n{text.center(breite)}\\n{'=' * breite}"

    def ja_nein(wert):
        \"\"\"Wandelt True/False in 'Ja'/'Nein'.\"\"\"
        return "Ja" if wert else "Nein"

    if __name__ == "__main__":
        print(titel("SELBSTTEST"))
        print(prozent(25, 200))
        print(kuerze("Ein sehr langer Text der gekürzt wird"))
        print(ja_nein(True))

  Danach im Hauptprogramm:  from meine_werkzeuge import titel, prozent
""")


print("=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)


def alter_infos(geburtsdatum_text):
    """Berechnet verschiedene Altersangaben aus einem Geburtsdatum."""
    geburt = datetime.strptime(geburtsdatum_text, "%d.%m.%Y").date()
    heute = date.today()

    jahre = heute.year - geburt.year
    if (heute.month, heute.day) < (geburt.month, geburt.day):
        jahre -= 1

    naechster = date(heute.year, geburt.month, geburt.day)
    if naechster < heute:
        naechster = date(heute.year + 1, geburt.month, geburt.day)

    return {
        "alter_jahre": jahre,
        "alter_tage": (heute - geburt).days,
        "wochentag_der_geburt": geburt.strftime("%A"),
        "tage_bis_naechster_geburtstag": (naechster - heute).days,
    }


for schluessel, wert in alter_infos("15.03.1998").items():
    print(f"  {schluessel:<32} {wert}")


print("\n" + "=" * 60, "\nAUFGABE 6 🔴\n", "=" * 60)


def erzeuge_passwort(laenge=12, sonderzeichen=True):
    """Erzeugt ein zufälliges Passwort mit garantierter Zeichenvielfalt."""
    if laenge < 4:
        raise ValueError("Passwort muss mindestens 4 Zeichen haben")

    sonder = "!@#$%&*?"
    pool = string.ascii_letters + string.digits
    pflicht = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
    ]
    if sonderzeichen:
        pflicht.append(random.choice(sonder))
        pool += sonder

    rest = [random.choice(pool) for _ in range(laenge - len(pflicht))]
    zeichen = pflicht + rest
    random.shuffle(zeichen)
    return "".join(zeichen)


for _ in range(3):
    print(f"  {erzeuge_passwort()}")
print(f"  Ohne Sonderzeichen: {erzeuge_passwort(16, sonderzeichen=False)}")


print("\n" + "=" * 60, "\nAUFGABE 7 ⭐\n", "=" * 60)

termine = [
    ("Zahnarzt", "05.08.2026"),
    ("Geburtstag", "12.09.2026"),
    ("Urlaub", "01.08.2026"),
    ("Steuererklärung", "31.07.2026"),
]

heute = date.today()
aufbereitet = []
for name, datum_text in termine:
    datum = datetime.strptime(datum_text, "%d.%m.%Y").date()
    aufbereitet.append((datum, name))

aufbereitet.sort()

print(f"  Heute ist der {heute.strftime('%d.%m.%Y')}\n")
for datum, name in aufbereitet:
    tage = (datum - heute).days
    warnung = " ⚠️" if 0 <= tage < 7 else ""
    vergangen = " (vorbei)" if tage < 0 else ""
    print(f"  In {tage:>4} Tagen | {datum.strftime('%d.%m.%Y')} ({datum.strftime('%a')}) "
          f"| {name}{warnung}{vergangen}")

print("\n🎉 Modul 12 geschafft!")
