"""
🎲 Zahlenraten - Musterlösung Projekt 1

Benutzt nur Konzepte aus den Modulen 00-05:
Variablen, Strings, Zahlen, Bedingungen, Schleifen.

AUFRUF:
    python zahlenraten.py
"""
import random

# ====================================================================
# EINSTELLUNGEN
# ====================================================================
SCHWIERIGKEITSGRADE = {
    "1": {"name": "Leicht", "min": 1, "max": 50, "versuche": 10},
    "2": {"name": "Mittel", "min": 1, "max": 100, "versuche": 7},
    "3": {"name": "Schwer", "min": 1, "max": 1000, "versuche": 10},
}

BREITE = 44
DEMO_MODUS = True        # 👈 auf False setzen für echtes Spielen

# Simulierte Eingaben für den Demo-Modus
DEMO_EINGABEN = ["2", "50", "abc", "75", "62", "57", "j", "1", "25", "12", "n"]
_demo_index = 0


def frage(text):
    """Holt eine Eingabe - im Demo-Modus aus der Liste."""
    global _demo_index
    if DEMO_MODUS:
        if _demo_index >= len(DEMO_EINGABEN):
            return "n"
        antwort = DEMO_EINGABEN[_demo_index]
        _demo_index += 1
        print(f"{text}{antwort}")
        return antwort
    return input(text)


# ====================================================================
# AUSGABE-HILFEN
# ====================================================================
def rahmen(text, zeichen="═"):
    """Gibt einen Text in einem Rahmen aus."""
    print("╔" + zeichen * BREITE + "╗")
    print("║" + text.center(BREITE) + "║")
    print("╚" + zeichen * BREITE + "╝")


def waehle_schwierigkeit():
    """Fragt den Schwierigkeitsgrad ab und gibt die Einstellungen zurück."""
    print("\nWähle den Schwierigkeitsgrad:")
    for taste, stufe in SCHWIERIGKEITSGRADE.items():
        print(f"  [{taste}] {stufe['name']:<10}"
              f"({stufe['min']}-{stufe['max']}, {stufe['versuche']} Versuche)")

    while True:
        wahl = frage("> ").strip()
        if wahl in SCHWIERIGKEITSGRADE:
            return SCHWIERIGKEITSGRADE[wahl]
        print("  Bitte 1, 2 oder 3 eingeben.")


def hinweis_naehe(tipp, gesucht, spanne):
    """Gibt einen Heiß/Kalt-Hinweis zurück."""
    abstand = abs(tipp - gesucht)
    if abstand <= spanne * 0.02:
        return "   🔥 Du bist ganz nah dran!"
    if abstand <= spanne * 0.08:
        return "   🌡️  Wird wärmer …"
    if abstand >= spanne * 0.5:
        return "   ❄️  Eiskalt."
    return ""


# ====================================================================
# EINE RUNDE SPIELEN
# ====================================================================
def spiele_runde(stufe):
    """Spielt eine Runde. Gibt (gewonnen, benoetigte_versuche) zurück."""
    gesucht = random.randint(stufe["min"], stufe["max"])
    spanne = stufe["max"] - stufe["min"]
    max_versuche = stufe["versuche"]

    print(f"\nIch denke an eine Zahl zwischen {stufe['min']} und {stufe['max']}.")
    print(f"Du hast {max_versuche} Versuche. Los geht's!\n")

    versuch = 0
    while versuch < max_versuche:
        eingabe = frage(f"Versuch {versuch + 1}/{max_versuche} > ").strip()

        # Eingabe prüfen - ohne try/except (Modul 13 kommt erst später)
        if not eingabe.lstrip("-").isdigit():
            print("  ⚠️  Bitte eine ganze Zahl eingeben.")
            continue

        tipp = int(eingabe)
        if not (stufe["min"] <= tipp <= stufe["max"]):
            print(f"  ⚠️  Die Zahl muss zwischen {stufe['min']} "
                  f"und {stufe['max']} liegen.")
            continue

        versuch += 1

        if tipp == gesucht:
            print(f"  🎉 RICHTIG! Die Zahl war {gesucht}.\n")
            return True, versuch
        if tipp < gesucht:
            print(f"  ⬆️  Zu niedrig!{hinweis_naehe(tipp, gesucht, spanne)}")
        else:
            print(f"  ⬇️  Zu hoch!{hinweis_naehe(tipp, gesucht, spanne)}")

    print(f"\n  😢 Verloren! Die Zahl war {gesucht}.\n")
    return False, max_versuche


# ====================================================================
# STATISTIK
# ====================================================================
def zeige_statistik(spiele, siege, bester):
    """Gibt die Sitzungsstatistik aus."""
    quote = siege / spiele if spiele else 0
    print("╔" + "═" * BREITE + "╗")
    print("║" + f" Spiele gesamt:   {spiele}".ljust(BREITE) + "║")
    print("║" + f" Gewonnen:        {siege}  ({quote:.0%})".ljust(BREITE) + "║")
    if bester:
        print("║" + f" Bester Versuch:  {bester} Versuche".ljust(BREITE) + "║")
    print("╚" + "═" * BREITE + "╝")


# ====================================================================
# HAUPTPROGRAMM
# ====================================================================
def main():
    """Startet das Spiel."""
    rahmen("🎲  ZAHLENRATEN  🎲")

    spiele = 0
    siege = 0
    bester = None

    while True:
        stufe = waehle_schwierigkeit()
        gewonnen, versuche = spiele_runde(stufe)

        spiele += 1
        if gewonnen:
            siege += 1
            if bester is None or versuche < bester:
                bester = versuche

            if versuche <= 3:
                print("Wahnsinn! Das war stark. 🌟")
            elif versuche <= 5:
                print("Nicht schlecht! 💪")
            else:
                print("Geschafft ist geschafft. 🙂")

        print()
        zeige_statistik(spiele, siege, bester)

        antwort = frage("\nNochmal? (j/n) > ").strip().lower()
        if antwort not in ("j", "ja", "y", "yes"):
            break

    print("\nDanke fürs Spielen! 👋")


if __name__ == "__main__":
    main()
