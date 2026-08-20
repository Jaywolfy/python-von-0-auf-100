"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 26 · MUSTERLÖSUNGEN                                       ║
║                                                                  ║
║  Diese Datei demonstriert alle Konzepte in EINER Datei.          ║
║  Die eigenständigen Skripte liegen daneben (gruss.py).           ║
╚══════════════════════════════════════════════════════════════════╝
"""
import argparse
import json
import logging
import time
from pathlib import Path

LOES = Path(__file__).parent / "_demo26"
LOES.mkdir(exist_ok=True)

print("=" * 62, "\nAUFGABE 1 + 2 🟢 - argparse\n", "=" * 62)

# argparse lässt sich auch aus dem Code heraus testen: einfach eine
# Argumentliste übergeben statt sys.argv zu benutzen.
from gruss import main as gruss_main       # noqa: E402

print("  python gruss.py Anna")
gruss_main(["Anna"])
print("\n  python gruss.py Bernd --gross --anzahl 2 --sprache en")
gruss_main(["Bernd", "--gross", "--anzahl", "2", "--sprache", "en"])


def rechner(argv=None):
    """Musterlösung Aufgabe 2 - Rechner mit choices und Exit-Codes."""
    parser = argparse.ArgumentParser(description="Kleiner Taschenrechner.")
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    parser.add_argument("-o", "--operation",
                        choices=["add", "sub", "mul", "div"], default="add")
    parser.add_argument("-n", "--nachkomma", type=int, default=2)
    args = parser.parse_args(argv)

    if args.operation == "div" and args.b == 0:
        print("  ❌ Division durch Null nicht möglich")
        return 1

    ergebnis = {"add": args.a + args.b, "sub": args.a - args.b,
                "mul": args.a * args.b,
                "div": args.a / args.b if args.b else 0}[args.operation]

    zeichen = {"add": "+", "sub": "-", "mul": "*", "div": "/"}[args.operation]
    print(f"  {args.a} {zeichen} {args.b} = {ergebnis:.{args.nachkomma}f}")
    return 0


print("\n  Rechner:")
rechner(["12", "5", "-o", "mul"])
rechner(["1", "3", "-o", "div", "-n", "5"])
print(f"  Exit-Code bei Division durch 0: {rechner(['1', '0', '-o', 'div'])}")


print("\n" + "=" * 62, "\nAUFGABE 3 🟡 - Logging\n", "=" * 62)

LOGDATEI = LOES / "demo.log"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)-8s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.FileHandler(LOGDATEI, encoding="utf-8", mode="w"),
              logging.StreamHandler()],
    force=True,
)
log = logging.getLogger("demo")

log.debug("Details für die Fehlersuche (nur bei --verbose sichtbar)")
log.info("Normale Statusmeldung")
log.warning("Achtung - aber es geht weiter")
log.error("Etwas ist schiefgegangen")
log.critical("Schwerer Fehler - Abbruch")

try:
    1 / 0
except ZeroDivisionError:
    log.exception("Fehler beim Rechnen")     # ⭐ schreibt auch den Traceback!

print(f"\n  📄 Logdatei: {LOGDATEI.name}")
print(f"     {len(LOGDATEI.read_text(encoding='utf-8').splitlines())} Zeilen geschrieben")
print("  💡 log.exception() schreibt den kompletten Traceback in die Datei -")
print("     genau das brauchst du, wenn ein Skript nachts um 3 abgestürzt ist.")


print("\n" + "=" * 62, "\nAUFGABE 4 🟡 - Fortschrittsbalken\n", "=" * 62)


def fortschritt(aktuell, gesamt, breite=30):
    """Erzeugt einen Fortschrittsbalken als String."""
    anteil = aktuell / gesamt if gesamt else 1
    gefuellt = int(anteil * breite)
    return (f"[{'█' * gefuellt}{'░' * (breite - gefuellt)}] "
            f"{anteil:>4.0%}  ({aktuell}/{gesamt})")


logging.disable(logging.CRITICAL)      # Log-Ausgabe kurz stumm schalten
for i in range(1, 51):
    print(f"\r  {fortschritt(i, 50)}", end="", flush=True)
    time.sleep(0.005)
print("\n  ✅ Fertig")
logging.disable(logging.NOTSET)


print("\n" + "=" * 62, "\nAUFGABE 5 🟡 - Konfiguration mit Priorität\n", "=" * 62)

STANDARD = {"quellordner": "~/Downloads", "backup": True,
            "log_level": "INFO", "backups_behalten": 5}


def lade_konfig(pfad=None, argumente=None):
    """Lädt die Konfiguration nach Priorität.

    Priorität (hoch → niedrig):
        1. Kommandozeilenargumente
        2. Konfigurationsdatei
        3. Standardwerte

    Args:
        pfad: Pfad zur JSON-Konfigurationsdatei (optional).
        argumente: dict mit Werten aus der Kommandozeile (optional).

    Returns:
        Die zusammengeführte Konfiguration.
    """
    konfig = STANDARD.copy()

    if pfad and Path(pfad).exists():
        try:
            konfig.update(json.loads(Path(pfad).read_text(encoding="utf-8")))
            print(f"    ✅ Konfigurationsdatei gelesen: {Path(pfad).name}")
        except json.JSONDecodeError as fehler:
            print(f"    ⚠️  Konfigurationsdatei fehlerhaft ({fehler.msg}) - Standardwerte")

    if argumente:
        konfig.update({k: v for k, v in argumente.items() if v is not None})
        print("    ✅ Kommandozeilenargumente angewendet")

    return konfig


print("  Fall 1 - nur Standardwerte:")
print(f"    {lade_konfig()}")

konfig_datei = LOES / "konfig.json"
konfig_datei.write_text(json.dumps({"backup": False, "log_level": "DEBUG"}),
                        encoding="utf-8")
print("\n  Fall 2 - mit Konfigurationsdatei:")
print(f"    {lade_konfig(konfig_datei)}")

print("\n  Fall 3 - Argumente überschreiben alles:")
print(f"    {lade_konfig(konfig_datei, {'backup': True, 'quellordner': '/tmp'})}")

kaputt = LOES / "kaputt.json"
kaputt.write_text("{ das ist kein json", encoding="utf-8")
print("\n  Fall 4 - kaputte Konfigurationsdatei (darf nicht abstürzen!):")
print(f"    {lade_konfig(kaputt)}")


print("\n" + "=" * 62, "\nAUFGABE 6 + 7 🔴\n", "=" * 62)
print("""
  Die vollständige Musterlösung für ein produktionsreifes Werkzeug
  findest du in:

      module/26/beispiele/01_werkzeug.py

  Probier aus:
      python module/26/beispiele/01_werkzeug.py --help
      python module/26/beispiele/01_werkzeug.py <ordner>
      python module/26/beispiele/01_werkzeug.py <ordner> --ausfuehren -b -v

  Es enthält alles aus 27 Modulen:
    ✅ argparse mit 6 Optionen und automatischer Hilfe
    ✅ logging in Datei + Konsole, Level per --verbose
    ✅ Konfigurationsdatei mit Standardwerten
    ✅ Fortschrittsbalken
    ✅ Fehlerbehandlung mit log.exception()
    ✅ Trockenlauf als STANDARD 🛡️
    ✅ Backup-Funktion mit Rotation
    ✅ Type Hints und Docstrings
    ✅ Saubere Exit-Codes
""")

print("=" * 62, "\nAUFGABE 8 ⭐ - Zeitsteuerung\n", "=" * 62)
print(r"""
  🪟 WINDOWS (Aufgabenplanung):
     Programm:      C:\projekt\.venv\Scripts\python.exe
     Argumente:     C:\projekt\src\haupt.py --ausfuehren
     Starten in:    C:\projekt

  🍎🐧 macOS / LINUX (crontab -e):
     0 8 * * *   /projekt/.venv/bin/python /projekt/haupt.py >> /projekt/cron.log 2>&1

  ⚠️ DIE ZWEI HÄUFIGSTEN FEHLER:
     1. Relative Pfade  -> geplante Aufgaben starten in einem anderen
        Arbeitsverzeichnis. IMMER absolute Pfade!
     2. System-Python statt venv-Python -> ModuleNotFoundError.
""")

print(f"  📁 Demo-Dateien: {LOES}")
print("\n🎉 MODUL 26 GESCHAFFT — und damit der ganze Kurs! 🎓")
print("   ➡️  Weiter zum Capstone: projekte/capstone/README.md")
