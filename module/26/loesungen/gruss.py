"""Musterlösung Aufgabe 1 - Ein einfaches argparse-Skript.

AUFRUF:
    python gruss.py Anna
    python gruss.py Anna --gross --anzahl 3
    python gruss.py Anna --sprache en
    python gruss.py --help
"""
import argparse

GRUESSE = {"de": "Hallo", "en": "Hello", "fr": "Bonjour", "es": "Hola"}


def parse_argumente(argv=None):
    """Liest die Kommandozeilenargumente."""
    parser = argparse.ArgumentParser(
        description="Grüßt eine Person - beliebig oft und in mehreren Sprachen.",
        epilog="Beispiel: %(prog)s Anna --gross --anzahl 3",
    )
    parser.add_argument("name", help="Wer soll gegrüßt werden?")
    parser.add_argument("-g", "--gross", action="store_true",
                        help="Ausgabe in Großbuchstaben")
    parser.add_argument("-n", "--anzahl", type=int, default=1,
                        help="Wie oft grüßen? (Standard: 1)")
    parser.add_argument("-s", "--sprache", choices=list(GRUESSE), default="de",
                        help="Sprache der Begrüßung (Standard: de)")
    return parser.parse_args(argv)


def main(argv=None):
    """Hauptprogramm."""
    args = parse_argumente(argv)

    if args.anzahl < 1:
        print("Fehler: --anzahl muss mindestens 1 sein")
        return 1

    text = f"{GRUESSE[args.sprache]}, {args.name}!"
    if args.gross:
        text = text.upper()

    for _ in range(args.anzahl):
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
