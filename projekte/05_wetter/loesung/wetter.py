"""
⛅ Wetter-Dashboard - Musterlösung Projekt 5

Ruft Wetterdaten von Open-Meteo ab (kostenlos, ohne API-Key),
speichert sie zwischen und zeigt ein Dashboard im Terminal.

Benutzt Modul 00-22: requests, JSON, Exceptions, Funktionen, Cache.

AUFRUF:
    python wetter.py

⚠️ Läuft auch OHNE Internet: OFFLINE = True nutzt Demo-Daten.
"""
import json
import time
from datetime import datetime
from pathlib import Path

OFFLINE = True          # 👈 auf False setzen für echte Abfragen

try:
    import requests
except ImportError:
    requests = None
    OFFLINE = True

# ====================================================================
# EINSTELLUNGEN
# ====================================================================
STAEDTE = {
    "Berlin":   (52.52, 13.41),
    "Hamburg":  (53.55, 9.99),
    "München":  (48.14, 11.58),
}

API_URL = "https://api.open-meteo.com/v1/forecast"
CACHE_ORDNER = Path(__file__).parent / "_cache"
CACHE_ORDNER.mkdir(exist_ok=True)
CACHE_MINUTEN = 30
BREITE = 54

WETTER_CODES = {
    0: ("Klar", "☀️"), 1: ("Überwiegend klar", "🌤️"),
    2: ("Teilweise bewölkt", "⛅"), 3: ("Bedeckt", "☁️"),
    45: ("Nebel", "🌫️"), 48: ("Reifnebel", "🌫️"),
    51: ("Leichter Nieselregen", "🌦️"), 53: ("Nieselregen", "🌦️"),
    61: ("Leichter Regen", "🌧️"), 63: ("Mäßiger Regen", "🌧️"),
    65: ("Starker Regen", "⛈️"), 71: ("Leichter Schneefall", "🌨️"),
    73: ("Schneefall", "❄️"), 80: ("Regenschauer", "🌦️"),
    95: ("Gewitter", "⛈️"),
}

SPARKS = "▁▂▃▄▅▆▇█"

# Demo-Daten (falls kein Internet)
DEMO = {
    "Berlin": {"temp": 24.3, "gefuehlt": 25.1, "feuchte": 58, "wind": 12.4,
               "code": 0, "min": 15.3, "max": 26.1,
               "stunden": [16, 17, 19, 22, 24, 25, 24, 21],
               "tage": [("2026-07-26", 15.3, 26.1, 0),
                        ("2026-07-27", 17.1, 28.4, 2),
                        ("2026-07-28", 14.2, 22.0, 61)]},
    "Hamburg": {"temp": 21.8, "gefuehlt": 21.2, "feuchte": 72, "wind": 18.9,
                "code": 61, "min": 14.1, "max": 22.4,
                "stunden": [15, 16, 17, 19, 21, 22, 21, 18],
                "tage": [("2026-07-26", 14.1, 22.4, 61),
                         ("2026-07-27", 15.0, 23.1, 3),
                         ("2026-07-28", 13.8, 20.5, 63)]},
    "München": {"temp": 26.7, "gefuehlt": 27.9, "feuchte": 45, "wind": 8.1,
                "code": 0, "min": 16.8, "max": 28.4,
                "stunden": [18, 20, 23, 26, 28, 28, 26, 22],
                "tage": [("2026-07-26", 16.8, 28.4, 0),
                         ("2026-07-27", 18.2, 30.1, 1),
                         ("2026-07-28", 17.0, 27.3, 2)]},
}


# ====================================================================
# AUSGABE-HILFEN
# ====================================================================
def kopfzeile():
    """Gibt den Dashboard-Kopf aus."""
    print("╔" + "═" * BREITE + "╗")
    print("║" + "⛅  WETTER-DASHBOARD".center(BREITE - 1) + "║")
    print("║" + f"Stand: {datetime.now():%d.%m.%Y %H:%M}".center(BREITE) + "║")
    print("╚" + "═" * BREITE + "╝")


def abschnitt(text):
    """Gibt eine Abschnittsüberschrift aus."""
    print(f"\n── {text} " + "─" * max(0, BREITE - len(text) - 4))


def wetter_symbol(code):
    """Übersetzt einen WMO-Wettercode in (Text, Emoji)."""
    return WETTER_CODES.get(code, ("Unbekannt", "❓"))


def sparkline(werte):
    """Erzeugt eine Mini-Grafik aus Zahlen: ▁▂▄▆█▇▅▃"""
    if not werte:
        return ""
    tief, hoch = min(werte), max(werte)
    spanne = hoch - tief or 1
    return "".join(SPARKS[int((w - tief) / spanne * (len(SPARKS) - 1))]
                   for w in werte)


# ====================================================================
# DATEN HOLEN
# ====================================================================
def hole_daten(url, params, demo=None):
    """Holt JSON-Daten - mit vollständiger Fehlerbehandlung.

    Returns:
        Die geparsten Daten oder None bei einem Fehler.
    """
    if OFFLINE:
        return demo

    try:
        antwort = requests.get(url, params=params, timeout=10)
        antwort.raise_for_status()
        return antwort.json()
    except requests.exceptions.Timeout:
        print("    ⏱️  Zeitüberschreitung")
    except requests.exceptions.HTTPError as fehler:
        print(f"    🔴 HTTP {fehler.response.status_code}")
    except requests.exceptions.ConnectionError:
        print("    📡 Keine Verbindung zum Server")
    except ValueError:
        print("    📄 Antwort war kein gültiges JSON")
    return None


def hole_wetter(stadt, koordinaten):
    """Holt die Wetterdaten einer Stadt - mit Cache.

    Returns:
        (daten, cache_alter_in_minuten) - daten ist None bei Fehler.
    """
    cache = CACHE_ORDNER / f"{stadt.lower().replace('ü', 'ue')}.json"

    # 1) Cache prüfen
    if cache.exists():
        alter = (time.time() - cache.stat().st_mtime) / 60
        if alter < CACHE_MINUTEN:
            try:
                return json.loads(cache.read_text(encoding="utf-8")), alter
            except json.JSONDecodeError:
                print(f"    ⚠️  Cache für {stadt} beschädigt - wird erneuert")

    # 2) Frisch abrufen
    breite, laenge = koordinaten
    params = {
        "latitude": breite, "longitude": laenge,
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,"
                   "wind_speed_10m,weather_code",
        "daily": "temperature_2m_max,temperature_2m_min,weather_code",
        "hourly": "temperature_2m",
        "timezone": "Europe/Berlin", "forecast_days": 3,
    }

    roh = hole_daten(API_URL, params, demo=DEMO.get(stadt))
    if roh is None:
        # 3) Notfall: alter Cache ist besser als nichts
        if cache.exists():
            print(f"    💾 Nutze alten Cache für {stadt}")
            try:
                return json.loads(cache.read_text(encoding="utf-8")), 999
            except json.JSONDecodeError:
                pass
        return None, 0

    daten = roh if OFFLINE else umwandeln(roh)
    try:
        cache.write_text(json.dumps(daten, ensure_ascii=False), encoding="utf-8")
    except OSError:
        pass          # Cache ist nur Komfort - kein Grund abzubrechen
    return daten, 0


def umwandeln(roh):
    """Wandelt die API-Antwort in unser internes Format um."""
    jetzt = roh["current"]
    taeglich = roh["daily"]
    stuendlich = roh.get("hourly", {}).get("temperature_2m", [])

    return {
        "temp": jetzt["temperature_2m"],
        "gefuehlt": jetzt.get("apparent_temperature", jetzt["temperature_2m"]),
        "feuchte": jetzt["relative_humidity_2m"],
        "wind": jetzt["wind_speed_10m"],
        "code": jetzt["weather_code"],
        "min": taeglich["temperature_2m_min"][0],
        "max": taeglich["temperature_2m_max"][0],
        "stunden": stuendlich[6:22:2],          # tagsüber, alle 2 Stunden
        "tage": list(zip(taeglich["time"],
                         taeglich["temperature_2m_min"],
                         taeglich["temperature_2m_max"],
                         taeglich["weather_code"])),
    }


# ====================================================================
# DARSTELLUNG
# ====================================================================
def zeige_stadt(stadt, daten):
    """Gibt den Wetterblock einer Stadt aus."""
    text, symbol = wetter_symbol(daten["code"])
    kopf = f"  📍 {stadt.upper()}"
    rechts = f"{symbol} {daten['temp']:.1f} °C"
    print()
    print(f"{kopf}{rechts.rjust(BREITE - len(kopf) + 2)}")
    print(f"     {text}")
    print(f"     Gefühlt {daten['gefuehlt']:.1f} °C  ·  "
          f"💧 {daten['feuchte']} %  ·  💨 {daten['wind']:.0f} km/h")
    print(f"     {sparkline(daten['stunden'])}  Heute: "
          f"{daten['min']:.1f} – {daten['max']:.1f} °C")


def zeige_vorhersage(stadt, daten):
    """Gibt die Mehrtagesvorhersage einer Stadt aus."""
    abschnitt(f"3-TAGE-VORHERSAGE {stadt.upper()}")
    hoechste = max(t[2] for t in daten["tage"]) or 1
    for datum, tief, hoch, code in daten["tage"]:
        tag = datetime.strptime(datum, "%Y-%m-%d")
        _, symbol = wetter_symbol(code)
        balken = "█" * int(hoch / hoechste * 18)
        print(f"  {tag:%a %d.%m.}  {symbol}  {tief:>5.1f} – {hoch:>5.1f} °C  {balken}")


def zeige_vergleich(alle):
    """Gibt den Städtevergleich aus."""
    abschnitt("VERGLEICH")
    temps = {stadt: d["temp"] for stadt, d in alle.items()}
    waermste = max(temps, key=temps.get)
    kaelteste = min(temps, key=temps.get)

    print(f"  🔥 Wärmste Stadt:  {waermste} ({temps[waermste]:.1f} °C)")
    print(f"  ❄️ Kälteste Stadt: {kaelteste} ({temps[kaelteste]:.1f} °C)")
    print(f"  📊 Durchschnitt:   {sum(temps.values()) / len(temps):.1f} °C")

    spanne = temps[waermste] - temps[kaelteste]
    print(f"  📏 Spannweite:     {spanne:.1f} °C")


# ====================================================================
# HAUPTPROGRAMM
# ====================================================================
def main():
    """Hauptprogramm."""
    kopfzeile()

    if OFFLINE:
        print("\n  📴 Offline-Modus: es werden Demo-Daten verwendet.")
        print("     Setz OFFLINE = False für echte Abfragen.")

    alle = {}
    for nr, (stadt, koordinaten) in enumerate(STAEDTE.items()):
        daten, cache_alter = hole_wetter(stadt, koordinaten)

        if daten is None:
            print(f"\n  ❌ {stadt}: keine Daten verfügbar")
            continue

        alle[stadt] = daten
        zeige_stadt(stadt, daten)
        if cache_alter:
            print(f"     💾 Aus dem Cache ({cache_alter:.0f} Min alt)")

        # 🤝 API-Etikette: Pause zwischen den Anfragen
        if not OFFLINE and nr < len(STAEDTE) - 1:
            time.sleep(1)

    if not alle:
        print("\n  ❌ Für keine Stadt konnten Daten geladen werden.")
        print("     Prüfe deine Internetverbindung.")
        return 1

    erste = next(iter(alle))
    zeige_vorhersage(erste, alle[erste])
    zeige_vergleich(alle)

    print(f"\n  💾 Cache: {CACHE_ORDNER}")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
