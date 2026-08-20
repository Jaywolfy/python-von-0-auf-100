"""
Modul 13 - Beispiel: Exceptions
"""
from pathlib import Path

# ====================================================================
# 1. GRUNDFORM
# ====================================================================
print("=" * 60, "\n1. GRUNDFORM\n", "=" * 60)

for eingabe in ("10", "abc", "0"):
    try:
        zahl = int(eingabe)
        ergebnis = 100 / zahl
        print(f"  '{eingabe}' -> 100/{zahl} = {ergebnis}")
    except ValueError:
        print(f"  '{eingabe}' -> ❌ keine gültige Zahl")
    except ZeroDivisionError:
        print(f"  '{eingabe}' -> ❌ durch 0 kann man nicht teilen")

# ====================================================================
# 2. else UND finally
# ====================================================================
print("\n" + "=" * 60, "\n2. else / finally\n", "=" * 60)


def teste(wert):
    print(f"  Eingabe: {wert!r}")
    try:
        zahl = int(wert)
    except ValueError as fehler:
        print(f"    except: {fehler}")
    else:
        print(f"    else:   Umwandlung erfolgreich -> {zahl}")
    finally:
        print("    finally: läuft IMMER (aufräumen)")


teste("42")
teste("vier")

# ====================================================================
# 3. DIE FEHLERMELDUNG NUTZEN
# ====================================================================
print("\n" + "=" * 60, "\n3. Fehlermeldung auswerten\n", "=" * 60)

beispiele = [lambda: int("abc"),
             lambda: [1, 2, 3][10],
             lambda: {"a": 1}["b"],
             lambda: 1 / 0,
             lambda: "text" + 5]

for funktion in beispiele:
    try:
        funktion()
    except Exception as fehler:          # nur zu Demozwecken so pauschal!
        print(f"  {type(fehler).__name__:<20} {fehler}")

# ====================================================================
# 4. raise - selbst Fehler auslösen
# ====================================================================
print("\n" + "=" * 60, "\n4. raise\n", "=" * 60)


def setze_alter(alter):
    """Prüft und setzt ein Alter."""
    if not isinstance(alter, int):
        raise TypeError(f"Alter muss int sein, war aber {type(alter).__name__}")
    if alter < 0:
        raise ValueError(f"Alter kann nicht negativ sein: {alter}")
    if alter > 130:
        raise ValueError(f"Unrealistisches Alter: {alter}")
    return alter


for wert in (30, -5, "dreißig", 200):
    try:
        print(f"  setze_alter({wert!r}) = {setze_alter(wert)}")
    except (TypeError, ValueError) as fehler:
        print(f"  setze_alter({wert!r}) -> {type(fehler).__name__}: {fehler}")

# ====================================================================
# 5. EIGENE EXCEPTIONS
# ====================================================================
print("\n" + "=" * 60, "\n5. Eigene Exceptions\n", "=" * 60)


class KontoFehler(Exception):
    """Basisklasse für alle Kontofehler."""


class ZuWenigGuthabenError(KontoFehler):
    """Guthaben reicht nicht aus."""


class LimitUeberschrittenError(KontoFehler):
    """Tageslimit überschritten."""


def abheben(guthaben, betrag, tageslimit=500):
    """Hebt Geld ab - oder wirft einen aussagekräftigen Fehler."""
    if betrag > tageslimit:
        raise LimitUeberschrittenError(f"{betrag} € > Tageslimit {tageslimit} €")
    if betrag > guthaben:
        raise ZuWenigGuthabenError(f"Nur {guthaben} € verfügbar, {betrag} € gefordert")
    return guthaben - betrag


for betrag in (100, 800, 2000):
    try:
        rest = abheben(1000, betrag)
        print(f"  {betrag:>5} € abgehoben ✅  Rest: {rest} €")
    except KontoFehler as fehler:      # fängt BEIDE Unterklassen!
        print(f"  {betrag:>5} € ❌ {type(fehler).__name__}: {fehler}")

# ====================================================================
# 6. 🌍 REALBEISPIEL: robuste Dateiverarbeitung
# ====================================================================
print("\n" + "=" * 60, "\n6. 🌍 Robuste Verarbeitung\n", "=" * 60)

ORDNER = Path(__file__).parent / "_testdaten13"
ORDNER.mkdir(exist_ok=True)
(ORDNER / "gut1.txt").write_text("42\n", encoding="utf-8")
(ORDNER / "gut2.txt").write_text("17\n", encoding="utf-8")
(ORDNER / "kaputt.txt").write_text("keine zahl\n", encoding="utf-8")
(ORDNER / "leer.txt").write_text("", encoding="utf-8")

summe = 0
erfolge = 0
probleme = []

for datei in sorted(ORDNER.glob("*.txt")):
    try:
        inhalt = datei.read_text(encoding="utf-8").strip()
        summe += int(inhalt)
        erfolge += 1
    except ValueError:
        probleme.append((datei.name, "kein gültiger Zahlenwert"))
    except FileNotFoundError:
        probleme.append((datei.name, "Datei verschwunden"))

print(f"  ✅ {erfolge} Dateien verarbeitet, Summe = {summe}")
print(f"  ⚠️  {len(probleme)} übersprungen:")
for name, grund in probleme:
    print(f"      {name:<14} {grund}")

print("""
  💡 GENAU DAS ist der Unterschied zwischen einem Skript und einem
     Werkzeug: Es bricht nicht bei der ersten kaputten Datei ab,
     sondern macht weiter und BERICHTET, was schiefging.
""")

# ====================================================================
# 7. ❌ WAS MAN NICHT TUN SOLL
# ====================================================================
print("=" * 60, "\n7. ❌ Anti-Muster\n", "=" * 60)
print("""
  ❌ except: pass
       Verschluckt ALLES - auch deine eigenen Tippfehler.
       Du suchst danach stundenlang, warum "nichts passiert".

  ❌ try: <50 Zeilen Code> except Exception: print("Fehler")
       Welche der 50 Zeilen ist fehlgeschlagen? Keine Ahnung.

  ✅ try-Blöcke so KLEIN wie möglich, Exceptions so SPEZIFISCH
     wie möglich, Fehlermeldung immer mit  as fehler  ausgeben.
""")
