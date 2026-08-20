# ⛅ Projekt 5 — Wetter-Dashboard

> 📍 **Nach Modul 22** · ⏱️ ~5 Stunden · 🎯 Dein erstes Programm mit Daten aus dem Internet

---

## 🎬 So soll es aussehen

```text
╔══════════════════════════════════════════════════════╗
║              ⛅  WETTER-DASHBOARD                     ║
║                 Stand: 26.07.2026 14:30              ║
╚══════════════════════════════════════════════════════╝

  📍 BERLIN                                    ☀️ 24.3 °C
     Gefühlt 25.1 °C  ·  💧 58 %  ·  💨 12 km/h
     ▁▂▄▆█▇▅▃  Heute:  15.3 – 26.1 °C

  📍 HAMBURG                                   🌧️ 21.8 °C
     Gefühlt 21.2 °C  ·  💧 72 %  ·  💨 19 km/h
     ▁▂▃▅▆▅▄▂  Heute:  14.1 – 22.4 °C

  📍 MÜNCHEN                                   ☀️ 26.7 °C
     Gefühlt 27.9 °C  ·  💧 45 %  ·  💨  8 km/h
     ▂▃▅▇█▇▆▄  Heute:  16.8 – 28.4 °C

── 3-TAGE-VORHERSAGE BERLIN ───────────────────────────
  Sa 26.07.  ☀️  15.3 – 26.1 °C  ████████████████
  So 27.07.  ⛅  17.1 – 28.4 °C  ██████████████████
  Mo 28.07.  🌧️  14.2 – 22.0 °C  ████████████

── VERGLEICH ──────────────────────────────────────────
  🔥 Wärmste Stadt:  München (26.7 °C)
  ❄️ Kälteste Stadt: Hamburg (21.8 °C)
  📊 Durchschnitt:   24.3 °C
  💾 Daten aus dem Cache (12 Min alt) — keine Anfrage nötig
```

---

## 🌐 Die API: Open-Meteo

**Kostenlos, kein API-Key nötig, keine Registrierung.** 🎉

```text
https://api.open-meteo.com/v1/forecast
    ?latitude=52.52
    &longitude=13.41
    &current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code
    &daily=temperature_2m_max,temperature_2m_min,weather_code
    &hourly=temperature_2m
    &timezone=Europe/Berlin
    &forecast_days=3
```

📖 Doku: [open-meteo.com/en/docs](https://open-meteo.com/en/docs)

**Koordinaten deutscher Städte:**

| Stadt | Breite | Länge |
|---|---|---|
| Berlin | 52.52 | 13.41 |
| Hamburg | 53.55 | 9.99 |
| München | 48.14 | 11.58 |
| Köln | 50.94 | 6.96 |
| Frankfurt | 50.11 | 8.68 |

---

## ✅ Pflichtanforderungen

- [ ] Wetterdaten für **mindestens 3 Städte** abrufen
- [ ] Aktuelle Temperatur, Luftfeuchte und Wind anzeigen
- [ ] 3-Tage-Vorhersage
- [ ] Wettercode in Emoji übersetzen (☀️🌤️🌧️❄️)
- [ ] **`timeout` bei jeder Anfrage**
- [ ] Vollständige Fehlerbehandlung (kein Internet, Timeout, 404, kaputtes JSON)
- [ ] `time.sleep()` zwischen den Anfragen 🤝
- [ ] Städte-Vergleich (wärmste/kälteste/Durchschnitt)

## 🎁 Bonus

- [ ] **Cache**: Daten max. 30 Minuten alt wiederverwenden 💾
- [ ] Offline-Modus mit den zuletzt gespeicherten Daten
- [ ] Temperaturverlauf als Sparkline (`▁▂▃▄▅▆▇█`)
- [ ] Städte über `argparse` wählbar (nach Modul 26)
- [ ] Regenwarnung, wenn Niederschlagswahrscheinlichkeit > 50 %
- [ ] Verlauf mitschreiben und Trends anzeigen
- [ ] Als HTML-Datei exportieren

---

## 🌦️ Wettercodes übersetzen

Open-Meteo liefert einen `weather_code` (WMO-Standard):

```python
WETTER_CODES = {
    0: ("Klar", "☀️"),
    1: ("Überwiegend klar", "🌤️"),
    2: ("Teilweise bewölkt", "⛅"),
    3: ("Bedeckt", "☁️"),
    45: ("Nebel", "🌫️"),
    48: ("Reifnebel", "🌫️"),
    51: ("Leichter Nieselregen", "🌦️"),
    61: ("Leichter Regen", "🌧️"),
    63: ("Mäßiger Regen", "🌧️"),
    65: ("Starker Regen", "⛈️"),
    71: ("Leichter Schneefall", "🌨️"),
    73: ("Mäßiger Schneefall", "❄️"),
    95: ("Gewitter", "⛈️"),
}

def wetter_symbol(code):
    """Übersetzt einen WMO-Wettercode in Text und Emoji."""
    return WETTER_CODES.get(code, ("Unbekannt", "❓"))
```

---

## 💾 Der Cache — Pflichtübung in API-Etikette

```python
def hole_mit_cache(stadt, url, params, max_alter_min=30):
    """Holt Daten - nutzt den Cache, wenn er frisch genug ist."""
    cache = CACHE_ORDNER / f"{stadt.lower()}.json"

    if cache.exists():
        alter = (time.time() - cache.stat().st_mtime) / 60
        if alter < max_alter_min:
            return json.loads(cache.read_text(encoding="utf-8")), alter

    daten = hole_daten(url, params)
    if daten:
        cache.write_text(json.dumps(daten, ensure_ascii=False), encoding="utf-8")
    return daten, 0
```

**Warum das wichtig ist:** Beim Entwickeln startest du dein Skript 50-mal. Ohne Cache sind das 150 Anfragen an einen fremden Server — für Daten, die sich stündlich ändern. Mit Cache sind es 3. 🤝

---

## 💥 Der Härtetest

```text
□ Internet trennen (WLAN aus) → sinnvolle Meldung? Offline-Modus?
□ URL absichtlich falsch schreiben → 404 abgefangen?
□ Ungültige Koordinaten (999, 999)
□ Cache-Datei mit kaputtem JSON füllen
□ Cache-Ordner löschen, während das Programm läuft
□ 10 Städte auf einmal → wie lange dauert es? Pausen eingebaut?
```

---

## 🧠 Reflexion

1. Wie viele API-Anfragen hast du beim Entwickeln gespart — durch den Cache?
2. Welche Fehlerfälle hattest du zuerst nicht bedacht?
3. Was wäre nötig, damit das Dashboard jeden Morgen automatisch läuft?
4. Wie würdest du es erweitern, wenn du es täglich benutzen wolltest?

---

## 🔍 Musterlösung

👉 [`loesung/wetter.py`](loesung/wetter.py) — läuft **auch offline** mit eingebauten Demo-Daten

**➡️ Weiter: [Modul 23 — Web-Scraping](../../module/23/README.md)**
