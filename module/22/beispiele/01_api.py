"""
Modul 22 - Beispiel: APIs mit requests

⚠️ Diese Datei läuft AUCH OHNE INTERNET.
   OFFLINE = True benutzt eingebaute Beispieldaten.
   Setz OFFLINE = False, um echte Anfragen zu machen.
"""
import json
import time

OFFLINE = True          # 👈 auf False setzen für echte API-Aufrufe

try:
    import requests
except ImportError:
    requests = None
    OFFLINE = True
    print("ℹ️  'requests' nicht installiert -> Offline-Modus")
    print("   Installieren mit:  pip install requests\n")


# ====================================================================
# BEISPIELDATEN (simulieren echte API-Antworten)
# ====================================================================
DEMO_WETTER = {
    "latitude": 52.52, "longitude": 13.41,
    "current": {"time": "2026-07-26T14:00", "temperature_2m": 24.3,
                "relative_humidity_2m": 58, "wind_speed_10m": 12.4,
                "weather_code": 1},
    "daily": {
        "time": ["2026-07-26", "2026-07-27", "2026-07-28"],
        "temperature_2m_max": [26.1, 28.4, 22.0],
        "temperature_2m_min": [15.3, 17.1, 14.2],
    },
}

DEMO_LAND = [{
    "name": {"common": "Deutschland", "official": "Bundesrepublik Deutschland"},
    "capital": ["Berlin"], "population": 83240525,
    "area": 357114.0, "region": "Europe",
    "languages": {"deu": "German"},
    "currencies": {"EUR": {"name": "Euro", "symbol": "€"}},
}]

DEMO_KURSE = {"amount": 1.0, "base": "EUR", "date": "2026-07-25",
              "rates": {"USD": 1.0842, "GBP": 0.8531, "CHF": 0.9612,
                        "JPY": 168.44, "PLN": 4.2810}}


# ====================================================================
# ⭐ DIE VORLAGE FÜR ROBUSTE API-AUFRUFE
# ====================================================================
def hole_daten(url, params=None, demo_antwort=None):
    """Holt JSON-Daten von einer URL - mit vollständiger Fehlerbehandlung.

    Args:
        url: Die abzufragende URL.
        params: Optionale Query-Parameter als dict.
        demo_antwort: Wird im Offline-Modus stattdessen zurückgegeben.

    Returns:
        Die geparsten JSON-Daten oder None bei einem Fehler.
    """
    if OFFLINE:
        print(f"  📴 [Demo] {url}")
        if params:
            print(f"     params: {params}")
        return demo_antwort

    try:
        antwort = requests.get(url, params=params, timeout=10)
        antwort.raise_for_status()
        print(f"  ✅ {antwort.status_code} {antwort.url[:70]}")
        return antwort.json()

    except requests.exceptions.Timeout:
        print("  ⏱️  Zeitüberschreitung - Server antwortet nicht")
    except requests.exceptions.HTTPError as fehler:
        code = fehler.response.status_code
        hinweise = {400: "Anfrage fehlerhaft", 401: "Nicht autorisiert",
                    403: "Zugriff verboten", 404: "Nicht gefunden",
                    429: "Zu viele Anfragen - bitte warten!",
                    500: "Serverfehler (nicht dein Fehler)"}
        print(f"  🔴 HTTP {code}: {hinweise.get(code, 'Unbekannter Fehler')}")
    except requests.exceptions.ConnectionError:
        print("  📡 Keine Verbindung - Internet prüfen")
    except ValueError:
        print("  📄 Antwort war kein gültiges JSON")

    return None


# ====================================================================
# 1. WETTER (Open-Meteo, kein API-Key nötig)
# ====================================================================
print("=" * 62, "\n1. ⛅ WETTER\n", "=" * 62)

wetter = hole_daten(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 52.52, "longitude": 13.41,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "Europe/Berlin", "forecast_days": 3},
    demo_antwort=DEMO_WETTER,
)

if wetter:
    jetzt = wetter["current"]
    print(f"\n  📍 Berlin ({wetter['latitude']}, {wetter['longitude']})")
    print(f"  🌡️  {jetzt['temperature_2m']} °C")
    print(f"  💧 {jetzt['relative_humidity_2m']} % Luftfeuchte")
    print(f"  💨 {jetzt['wind_speed_10m']} km/h Wind")

    print("\n  Vorhersage:")
    tage = wetter["daily"]
    for datum, hoch, tief in zip(tage["time"], tage["temperature_2m_max"],
                                 tage["temperature_2m_min"]):
        balken = "█" * int(hoch / 2)
        print(f"    {datum}  {tief:>5.1f} … {hoch:>5.1f} °C  {balken}")


# ====================================================================
# 2. LÄNDERDATEN
# ====================================================================
print("\n" + "=" * 62, "\n2. 🌍 LÄNDERDATEN\n", "=" * 62)

laender = hole_daten("https://restcountries.com/v3.1/name/germany",
                     demo_antwort=DEMO_LAND)

if laender:
    land = laender[0]
    waehrung = list(land["currencies"].values())[0]
    print(f"\n  Land:         {land['name']['common']}")
    print(f"  Offiziell:    {land['name']['official']}")
    print(f"  Hauptstadt:   {land['capital'][0]}")
    print(f"  Einwohner:    {land['population']:,}".replace(",", "."))
    print(f"  Fläche:       {land['area']:,.0f} km²".replace(",", "."))
    print(f"  Sprachen:     {', '.join(land['languages'].values())}")
    print(f"  Währung:      {waehrung['name']} ({waehrung['symbol']})")
    dichte = land["population"] / land["area"]
    print(f"  Bevölk.dichte:{dichte:>6.1f} Einwohner/km²")


# ====================================================================
# 3. WECHSELKURSE
# ====================================================================
print("\n" + "=" * 62, "\n3. 💱 WECHSELKURSE\n", "=" * 62)

kurse = hole_daten("https://api.frankfurter.app/latest",
                   params={"from": "EUR"}, demo_antwort=DEMO_KURSE)

if kurse:
    betrag = 100
    print(f"\n  {betrag} {kurse['base']} entsprechen (Stand {kurse['date']}):")
    for waehrung, kurs in sorted(kurse["rates"].items()):
        print(f"    {betrag * kurs:>12,.2f} {waehrung}   (Kurs {kurs})")


# ====================================================================
# 4. MEHRERE ANFRAGEN - mit Pause! 🤝
# ====================================================================
print("\n" + "=" * 62, "\n4. 🤝 MEHRERE ANFRAGEN (mit Etikette)\n", "=" * 62)

STAEDTE = {"Berlin": (52.52, 13.41), "Hamburg": (53.55, 9.99),
           "München": (48.14, 11.58)}

DEMO_TEMPS = {"Berlin": 24.3, "Hamburg": 21.8, "München": 26.7}

print("  Wetter für mehrere Städte:")
for stadt, (lat, lon) in STAEDTE.items():
    daten = hole_daten(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current": "temperature_2m"},
        demo_antwort={"current": {"temperature_2m": DEMO_TEMPS[stadt]}},
    )
    if daten:
        temp = daten["current"]["temperature_2m"]
        print(f"    {stadt:<10}{temp:>6.1f} °C  {'🔥' if temp > 25 else '🌤️'}")

    if not OFFLINE:
        time.sleep(1)        # 🤝 fair gegenüber dem Server!

print("""
  💡 time.sleep(1) zwischen den Anfragen ist keine Höflichkeitsfloskel:
     Ohne Pause sperren viele APIs deine IP-Adresse nach kurzer Zeit.
""")


# ====================================================================
# 5. ERGEBNISSE SPEICHERN (Modul 16!)
# ====================================================================
print("=" * 62, "\n5. 💾 ANTWORT SPEICHERN\n", "=" * 62)

from pathlib import Path

ORDNER = Path(__file__).parent / "_api_daten"
ORDNER.mkdir(exist_ok=True)

if wetter:
    ziel = ORDNER / "wetter.json"
    with open(ziel, "w", encoding="utf-8") as f:
        json.dump(wetter, f, indent=2, ensure_ascii=False)
    print(f"  ✅ Gespeichert: {ziel.name} ({ziel.stat().st_size} Bytes)")
    print("  💡 Zwischenspeichern spart Anfragen - gut für dich UND den Server.")

print(f"\n{'=' * 62}")
print("  📴 Läuft gerade im Demo-Modus." if OFFLINE else "  🌐 Echte Daten geladen.")
print("     Setz OFFLINE = False (Zeile 12) für echte Anfragen.")
print("=" * 62)
