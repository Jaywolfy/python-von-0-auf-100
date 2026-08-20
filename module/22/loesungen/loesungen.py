"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 22 · MUSTERLÖSUNGEN — APIs                                ║
╚══════════════════════════════════════════════════════════════════╝
"""
import json
import time
from pathlib import Path

OFFLINE = True

DEMO_BENUTZER = [
    {"id": 1, "name": "Leanne Graham", "username": "Bret",
     "email": "sincere@april.biz",
     "address": {"street": "Kulas Light", "city": "Gwenborough", "zipcode": "92998"},
     "company": {"name": "Romaguera-Crona"}},
    {"id": 2, "name": "Ervin Howell", "username": "Antonette",
     "email": "shanna@melissa.tv",
     "address": {"street": "Victor Plains", "city": "Wisokyburgh", "zipcode": "90566"},
     "company": {"name": "Deckow-Crist"}},
    {"id": 3, "name": "Clementine Bauch", "username": "Samantha",
     "email": "nathan@yesenia.net",
     "address": {"street": "Douglas Extension", "city": "McKenziehaven", "zipcode": "59590"},
     "company": {"name": "Romaguera-Jacobson"}},
]

DEMO_BEITRAEGE = [
    {"userId": 1, "id": 1, "title": "Erster Beitrag", "body": "Text " * 20},
    {"userId": 1, "id": 2, "title": "Zweiter Beitrag", "body": "Text " * 15},
    {"userId": 2, "id": 3, "title": "Dritter Beitrag", "body": "Text " * 30},
    {"userId": 3, "id": 4, "title": "Vierter Beitrag", "body": "Text " * 10},
    {"userId": 1, "id": 5, "title": "Fünfter Beitrag", "body": "Text " * 25},
]

DEMO_KURSE = {"base": "EUR", "date": "2026-07-25",
              "rates": {"USD": 1.0842, "GBP": 0.8531, "CHF": 0.9612,
                        "JPY": 168.44, "PLN": 4.2810, "SEK": 11.234}}

DEMO_WETTER_STAEDTE = {
    "Berlin": {"temp": 24.3, "wind": 12.4, "feuchte": 58},
    "Hamburg": {"temp": 21.8, "wind": 18.9, "feuchte": 72},
    "München": {"temp": 26.7, "wind": 8.1, "feuchte": 45},
    "Köln": {"temp": 23.1, "wind": 14.2, "feuchte": 63},
}


print("=" * 62, "\nAUFGABE 1 🟢\n", "=" * 62)

print(f"  a) Namen:  {[b['name'] for b in DEMO_BENUTZER]}")
print(f"  b) E-Mails:{[b['email'] for b in DEMO_BENUTZER]}")
print(f"  c) Städte: {[b['address']['city'] for b in DEMO_BENUTZER]}")
print(f"\n  d) {'Name':<20}{'Stadt':<18}Firma")
print("     " + "-" * 58)
for b in DEMO_BENUTZER:
    print(f"     {b['name']:<20}{b['address']['city']:<18}{b['company']['name']}")


print("\n" + "=" * 62, "\nAUFGABE 2 🟢\n", "=" * 62)

erster = DEMO_BENUTZER[0]
adresse = erster.get("address", {})
firma = erster.get("company", {})

print(f"  Straße: {adresse.get('street', 'unbekannt')}")
print(f"  PLZ:    {adresse.get('zipcode', 'unbekannt')}")
print(f"  Stadt:  {adresse.get('city', 'unbekannt')}")
print(f"  Firma:  {firma.get('name', 'unbekannt')}")
print(f"  Handy:  {erster.get('phone', 'nicht angegeben')}   ← Feld fehlt, kein Absturz ✅")


print("\n" + "=" * 62, "\nAUFGABE 3 🟡\n", "=" * 62)

beitraege_nach_benutzer = {}
for beitrag in DEMO_BEITRAEGE:
    beitraege_nach_benutzer.setdefault(beitrag["userId"], []).append(beitrag["title"])

for benutzer in DEMO_BENUTZER:
    titel = beitraege_nach_benutzer.get(benutzer["id"], [])
    print(f"  {benutzer['name']} ({len(titel)} Beiträge):")
    for t in titel:
        print(f"      • {t}")
    if not titel:
        print("      (keine)")


print("\n" + "=" * 62, "\nAUFGABE 4 🟡\n", "=" * 62)


def hole_daten(url, params=None, demo=None):
    """Holt JSON-Daten von einer URL - mit vollständiger Fehlerbehandlung."""
    if OFFLINE:
        print(f"  📴 [Demo] {url}")
        return demo

    try:
        import requests
        antwort = requests.get(url, params=params, timeout=10)
        antwort.raise_for_status()
        return antwort.json()
    except requests.exceptions.Timeout:
        print("  ⏱️  Zeitüberschreitung")
    except requests.exceptions.HTTPError as fehler:
        print(f"  🔴 HTTP {fehler.response.status_code}")
    except requests.exceptions.ConnectionError:
        print("  📡 Keine Verbindung")
    except ValueError:
        print("  📄 Kein gültiges JSON")
    return None


daten = hole_daten("https://jsonplaceholder.typicode.com/users",
                   demo=DEMO_BENUTZER)
print(f"  Ergebnis: {len(daten)} Benutzer geladen ✅")


print("\n" + "=" * 62, "\nAUFGABE 5 🟡\n", "=" * 62)


def rechne_um(betrag, ziel_waehrung, kurse):
    """Rechnet einen Betrag von der Basiswährung in eine Zielwährung um.

    Raises:
        KeyError: Wenn die Zielwährung nicht in den Kursen vorkommt.
    """
    if ziel_waehrung not in kurse["rates"]:
        raise KeyError(f"Unbekannte Währung: {ziel_waehrung}")
    return round(betrag * kurse["rates"][ziel_waehrung], 2)


betrag = 250
print(f"  {betrag} EUR = {rechne_um(betrag, 'USD', DEMO_KURSE)} USD\n")
print(f"  {'Währung':<10}{'Kurs':>10}{'250 EUR ergibt':>20}")
print("  " + "-" * 40)
for waehrung, kurs in sorted(DEMO_KURSE["rates"].items(), key=lambda p: p[1]):
    print(f"  {waehrung:<10}{kurs:>10.4f}{rechne_um(betrag, waehrung, DEMO_KURSE):>20,.2f}")

try:
    rechne_um(100, "XYZ", DEMO_KURSE)
except KeyError as fehler:
    print(f"\n  Fehlerfall: {fehler}")


print("\n" + "=" * 62, "\nAUFGABE 6 🔴\n", "=" * 62)


def wetter_dashboard(staedte):
    """Gibt ein formatiertes Wetter-Dashboard aus."""
    breite = 44
    sortiert = sorted(staedte.items(), key=lambda p: -p[1]["temp"])
    temps = [d["temp"] for d in staedte.values()]

    print("  ╔" + "═" * breite + "╗")
    print("  ║" + "WETTER-ÜBERSICHT ⛅".center(breite - 1) + "║")
    print("  ╠" + "═" * breite + "╣")

    for stadt, d in sortiert:
        symbol = "🔥" if d["temp"] > 25 else "🌤️" if d["temp"] > 22 else "🌥️"
        balken = "█" * int(d["temp"] / 2)
        zeile = f" {stadt:<10}{d['temp']:>5.1f} °C {symbol} {balken}"
        print(f"  ║{zeile:<{breite}}║")

    print("  ╠" + "═" * breite + "╣")
    waermste = max(staedte, key=lambda s: staedte[s]["temp"])
    kaelteste = min(staedte, key=lambda s: staedte[s]["temp"])
    z1 = f" Wärmste: {waermste} | Kälteste: {kaelteste}"
    z2 = f" Durchschnitt: {sum(temps) / len(temps):.1f} °C"
    print(f"  ║{z1:<{breite}}║")
    print(f"  ║{z2:<{breite}}║")
    print("  ╚" + "═" * breite + "╝")


wetter_dashboard(DEMO_WETTER_STAEDTE)


print("\n" + "=" * 62, "\nAUFGABE 7 🔴\n", "=" * 62)

STATUS_HINWEISE = {
    200: "✅ OK - weiter im Programm",
    201: "✅ Erstellt - Ressource wurde angelegt",
    204: "✅ OK, aber kein Inhalt in der Antwort",
    301: "↪️  Dauerhaft umgeleitet - URL im Code aktualisieren",
    400: "🔴 Anfrage fehlerhaft - Parameter prüfen",
    401: "🔑 Nicht autorisiert - API-Key prüfen",
    403: "🚫 Verboten - Berechtigung fehlt",
    404: "🔍 Nicht gefunden - URL prüfen",
    429: "⏳ Rate Limit - 60 Sekunden warten und erneut versuchen",
    500: "💥 Serverfehler - nicht dein Fehler, später erneut",
    502: "💥 Bad Gateway - Server überlastet, später erneut",
    503: "💥 Dienst nicht verfügbar - Wartung? Später erneut",
}


def behandle_status(code):
    """Gibt eine Handlungsempfehlung zu einem HTTP-Statuscode zurück."""
    if code in STATUS_HINWEISE:
        return STATUS_HINWEISE[code]
    if 200 <= code < 300:
        return "✅ Erfolg (unbekannter 2xx-Code)"
    if 400 <= code < 500:
        return "🔴 Fehler auf deiner Seite - Anfrage prüfen"
    if code >= 500:
        return "💥 Serverfehler - später erneut versuchen"
    return "❓ Unbekannter Statuscode"


for code in (200, 201, 301, 400, 401, 403, 404, 429, 500, 503, 418):
    print(f"  {code}  {behandle_status(code)}")


print("\n" + "=" * 62, "\nAUFGABE 8 ⭐\n", "=" * 62)

CACHE_ORDNER = Path(__file__).parent / "_cache22"
CACHE_ORDNER.mkdir(exist_ok=True)


def hole_mit_cache(url, cache_datei, max_alter_min=60, demo=None):
    """Holt Daten - benutzt aber den Cache, wenn er noch frisch genug ist.

    Args:
        url: Die abzufragende URL.
        cache_datei: Pfad zur Cache-Datei.
        max_alter_min: Maximales Alter des Caches in Minuten.
        demo: Demo-Antwort für den Offline-Modus.

    Returns:
        Die Daten (aus Cache oder frisch abgerufen).
    """
    cache_datei = Path(cache_datei)

    if cache_datei.exists():
        alter_min = (time.time() - cache_datei.stat().st_mtime) / 60
        if alter_min < max_alter_min:
            print(f"  💾 Aus dem Cache ({alter_min:.1f} Min alt) - keine Anfrage nötig")
            return json.loads(cache_datei.read_text(encoding="utf-8"))
        print(f"  ⏰ Cache zu alt ({alter_min:.1f} Min) - wird erneuert")

    daten = hole_daten(url, demo=demo)
    if daten is not None:
        cache_datei.write_text(json.dumps(daten, ensure_ascii=False, indent=2),
                               encoding="utf-8")
        print(f"  💾 Im Cache gespeichert: {cache_datei.name}")
    return daten


ziel = CACHE_ORDNER / "kurse.json"
print("  Erster Aufruf:")
hole_mit_cache("https://api.frankfurter.app/latest", ziel, demo=DEMO_KURSE)
print("\n  Zweiter Aufruf (direkt danach):")
ergebnis = hole_mit_cache("https://api.frankfurter.app/latest", ziel, demo=DEMO_KURSE)
print(f"\n  Daten vorhanden: {len(ergebnis['rates'])} Wechselkurse ✅")

print("""
  💡 Ein Cache ist doppelt gut:
     • Dein Programm wird schneller
     • Der fremde Server wird geschont (API-Etikette 🤝)
""")

print("🎉 Modul 22 geschafft! Die Daten der Welt stehen dir offen. 🌐")
