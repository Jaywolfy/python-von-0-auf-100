"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 13 · MUSTERLÖSUNGEN — Exceptions                          ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)


def sichere_zahl(text, standard=0):
    """Wandelt einen Text in eine Zahl um; bei Fehlern den Standardwert."""
    try:
        return int(text)
    except (ValueError, TypeError):
        return standard


for wert in ("42", "3.14", "abc", "", None):
    print(f"  sichere_zahl({wert!r:<8}) = {sichere_zahl(wert)}")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)


def teile_sicher(a, b):
    """Teilt a durch b und behandelt die typischen Fehlerfälle."""
    try:
        return a / b
    except ZeroDivisionError:
        print("    ❌ Division durch Null")
        return None
    except TypeError as fehler:
        print(f"    ❌ Falscher Typ: {fehler}")
        return None


for a, b in ((10, 2), (10, 0), ("10", 2)):
    print(f"  teile_sicher({a!r}, {b!r}) = {teile_sicher(a, b)}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟡\n", "=" * 60)

daten = ["12", "abc", "45", "", "7", "3.5", None, "99"]
summe = 0
verarbeitet = 0
uebersprungen = []

for wert in daten:
    try:
        summe += int(wert)
        verarbeitet += 1
    except (ValueError, TypeError):
        uebersprungen.append(wert)

print(f"  ✅ {verarbeitet} Werte verarbeitet, Summe = {summe}")
print(f"  ⚠️  {len(uebersprungen)} übersprungen: {uebersprungen}")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)


class UngueltigeEmailError(ValueError):
    """Wird ausgelöst, wenn eine E-Mail-Adresse ungültig ist."""


def pruefe_email(text):
    """Prüft eine E-Mail-Adresse grob auf Gültigkeit."""
    if not isinstance(text, str):
        raise UngueltigeEmailError(f"Kein Text: {text!r}")
    if "@" not in text:
        raise UngueltigeEmailError("Kein @ enthalten")
    lokal, _, domain = text.partition("@")
    if not lokal:
        raise UngueltigeEmailError("Kein Name vor dem @")
    if "." not in domain:
        raise UngueltigeEmailError("Kein Punkt in der Domain")
    return True


for adresse in ("max@firma.de", "keinatzeichen.de", "@firma.de",
                "max@firma", "a.b@sub.firma.co.uk"):
    try:
        pruefe_email(adresse)
        print(f"  ✅ {adresse}")
    except UngueltigeEmailError as fehler:
        print(f"  ❌ {adresse:<22} {fehler}")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)


def verarbeite(daten):
    """Summiert Daten und meldet das Ende immer."""
    try:
        ergebnis = sum(daten)
        print(f"    Summe: {ergebnis}")
        return ergebnis
    except TypeError as fehler:
        print(f"    ❌ Fehler: {fehler}")
        return None
    finally:
        print("    → Verarbeitung beendet (finally)")


print("  verarbeite([1,2,3]):")
verarbeite([1, 2, 3])
print("  verarbeite([1,'zwei',3]):")
verarbeite([1, "zwei", 3])


print("\n" + "=" * 60, "\nAUFGABE 6 🔴 - Anti-Muster\n", "=" * 60)

print("""  PROBLEME DER ALTEN VERSION:
   1. 'except:' fängt ALLES ab - auch KeyboardInterrupt und Tippfehler
   2. Rückgabe {} verschleiert den Unterschied zwischen
      "Datei fehlt" und "Datei ist leer"
   3. Kein encoding -> Umlautprobleme
   4. z.split("=") kracht bei Zeilen ohne "=" (z.B. Kommentare)
   5. Der try-Block umfasst viel zu viel Code
   6. Der Nutzer erfährt nie, WAS schiefging
""")

from pathlib import Path

BEISP = Path(__file__).parent / "_konfig13"
BEISP.mkdir(exist_ok=True)
(BEISP / "config.ini").write_text(
    "# Kommentarzeile\nname = Testprojekt\nversion=1.0\nkaputte_zeile\n",
    encoding="utf-8")


def lade_konfiguration(pfad):
    """Lädt eine einfache key=value-Konfiguration.

    Wirft FileNotFoundError, wenn die Datei fehlt.
    Ungültige Zeilen werden übersprungen und gemeldet.
    """
    pfad = Path(pfad)
    konfig = {}
    ignoriert = []

    with open(pfad, encoding="utf-8") as f:       # klein gehaltener Bereich
        for nr, zeile in enumerate(f, start=1):
            zeile = zeile.strip()
            if not zeile or zeile.startswith("#"):
                continue
            if "=" not in zeile:
                ignoriert.append((nr, zeile))
                continue
            schluessel, _, wert = zeile.partition("=")
            konfig[schluessel.strip()] = wert.strip()

    if ignoriert:
        print(f"    ⚠️  {len(ignoriert)} ungültige Zeile(n) übersprungen: {ignoriert}")
    return konfig


print("  Verbesserte Version:")
print(f"    {lade_konfiguration(BEISP / 'config.ini')}")
try:
    lade_konfiguration(BEISP / "gibtsnicht.ini")
except FileNotFoundError as fehler:
    print(f"    Fehlende Datei wird korrekt gemeldet: {fehler.strerror}")


print("\n" + "=" * 60, "\nAUFGABE 7 🔴\n", "=" * 60)

eingaben = ["abc", "-5", "999", "42"]


def frage_zahl(prompt, min_wert, max_wert, simulierte_eingaben=None):
    """Fragt so lange, bis eine gültige Zahl im Bereich eingegeben wurde."""
    index = 0
    while True:
        if simulierte_eingaben is not None:
            if index >= len(simulierte_eingaben):
                return None
            eingabe = simulierte_eingaben[index]
            index += 1
            print(f"  {prompt}{eingabe}")
        else:
            eingabe = input(prompt)

        try:
            zahl = int(eingabe)
        except ValueError:
            print("    → Bitte eine ganze Zahl eingeben")
            continue

        if not (min_wert <= zahl <= max_wert):
            print(f"    → Muss zwischen {min_wert} und {max_wert} liegen")
            continue

        print(f"    → ✅ Akzeptiert: {zahl}")
        return zahl


frage_zahl("Zahl (1-100): ", 1, 100, simulierte_eingaben=eingaben)


print("\n" + "=" * 60, "\nAUFGABE 8 ⭐\n", "=" * 60)


def verarbeite_alle(elemente, funktion):
    """Wendet funktion auf alle Elemente an und sammelt Erfolge und Fehler."""
    erfolge = []
    fehler = []

    for element in elemente:
        try:
            erfolge.append(funktion(element))
        except Exception as f:      # hier bewusst breit: wir kennen die
            fehler.append((element, f"{type(f).__name__}: {f}"))

    gesamt = len(elemente)
    return {
        "erfolge": erfolge,
        "fehler": fehler,
        "quote": len(erfolge) / gesamt if gesamt else 0,
    }


ergebnis = verarbeite_alle(["1", "2", "x", "4"], int)
print(f"  Erfolge: {ergebnis['erfolge']}")
print(f"  Fehler:  {ergebnis['fehler']}")
print(f"  Quote:   {ergebnis['quote']:.0%}")

print("\n🎉 Modul 13 geschafft! Deine Programme überleben jetzt Fehler. 🛡️")
