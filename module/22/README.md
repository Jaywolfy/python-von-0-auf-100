# 🌐 Modul 22 — APIs & requests

> ⏱️ ~5 Stunden · ⬅️ [Modul 21](../21/README.md) · ➡️ [Modul 23](../23/README.md)

---

## 🎯 Lernziele

- [ ] verstehen, was eine API ist
- [ ] mit `requests` Daten abrufen
- [ ] JSON-Antworten verarbeiten
- [ ] Statuscodes, Timeouts und Fehler behandeln
- [ ] API-Keys **sicher** speichern
- [ ] respektvoll mit fremden Servern umgehen 🤝

---

## 🌍 Warum das wichtig ist

Jetzt öffnet sich die Welt: Wetter, Wechselkurse, Nachrichten, Karten, Übersetzungen, Aktienkurse, dein eigenes Notion/Slack/GitHub — **alles per API abrufbar**.

🏠 **Alltagsbild:** Eine API ist die **Speisekarte eines Restaurants**. Du gehst nicht in die Küche und kochst selbst — du bestellst, was auf der Karte steht, und bekommst ein fertiges Gericht. Die API sagt dir, was du bestellen darfst und in welchem Format du es bekommst. 🍽️

---

## 📖 Die Lektion

### 1. HTTP in 60 Sekunden

```text
DU (Client)                          SERVER
     │                                  │
     │  ──── GET /wetter?stadt=Berlin ──►│
     │                                  │
     │  ◄─── 200 OK + JSON ──────────────│
```

| Methode | Bedeutung |
|:---:|---|
| `GET` | Daten holen (99 % deiner Fälle) |
| `POST` | Daten senden/anlegen |
| `PUT` / `PATCH` | ändern |
| `DELETE` | löschen |

**Statuscodes:**

| Code | Bedeutung | Was tun |
|:---:|---|---|
| 🟢 `200` | OK | alles gut |
| 🟡 `301/302` | Umgeleitet | requests folgt automatisch |
| 🔴 `400` | Falsche Anfrage | deine Parameter prüfen |
| 🔴 `401` | Nicht angemeldet | API-Key fehlt/falsch |
| 🔴 `403` | Verboten | keine Berechtigung |
| 🔴 `404` | Nicht gefunden | URL prüfen |
| 🟠 `429` | Zu viele Anfragen | **warten!** ⏳ |
| 💥 `500` | Serverfehler | nicht dein Fehler, später erneut |

### 2. Die erste Anfrage

```bash
pip install requests
```

```python
import requests

antwort = requests.get("https://api.example.com/daten", timeout=10)

print(antwort.status_code)     # 200
print(antwort.json())          # als Python-dict ⭐
print(antwort.text)            # als Rohtext
```

⚠️ **`timeout` IMMER angeben.** Ohne Timeout kann dein Skript ewig hängen, wenn der Server nicht antwortet.

### 3. Parameter mitgeben

```python
# ❌ Nicht per Hand zusammenbauen (Sonderzeichen!)
url = "https://api.de/suche?q=" + suchbegriff

# ✅ requests macht das richtig
antwort = requests.get(
    "https://api.de/suche",
    params={"q": suchbegriff, "limit": 10},
    timeout=10,
)
```

### 4. 🛡️ Robuste Anfragen

```python
import requests

def hole_daten(url, params=None):
    """Holt JSON-Daten von einer URL - mit Fehlerbehandlung."""
    try:
        antwort = requests.get(url, params=params, timeout=10)
        antwort.raise_for_status()          # wirft bei 4xx/5xx
        return antwort.json()
    except requests.exceptions.Timeout:
        print("⏱️ Zeitüberschreitung")
    except requests.exceptions.HTTPError as e:
        print(f"🔴 HTTP-Fehler: {e.response.status_code}")
    except requests.exceptions.ConnectionError:
        print("📡 Keine Verbindung")
    except ValueError:
        print("📄 Antwort war kein gültiges JSON")
    return None
```

**Das ist die Vorlage, die du in jedem API-Projekt brauchst.** Kopier sie dir in dein Werkzeugmodul. 🧰

### 5. 🔑 API-Keys sicher speichern

```python
# ❌ NIEMALS SO
API_KEY = "sk-abc123geheim"      # landet in Git → Leck 🚨

# ✅ SO
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["WETTER_API_KEY"]
```

```text
.env               ← Key steht hier, NICHT in Git
.env.beispiel      ← leere Vorlage, DIE kommt ins Repo
.gitignore         ← enthält .env
```

> 🚨 **Wenn du versehentlich einen Key gepusht hast:** Sofort **widerrufen und neu erzeugen**. Löschen aus dem Repo reicht **nicht** — er bleibt in der Git-History.

### 6. Header & Authentifizierung

```python
kopfzeilen = {
    "Authorization": f"Bearer {API_KEY}",
    "User-Agent": "MeinLernprojekt/1.0",
}
antwort = requests.get(url, headers=kopfzeilen, timeout=10)
```

### 7. 🤝 API-Etikette

```text
✅ timeout setzen
✅ Antworten zwischenspeichern statt 100× dasselbe abfragen
✅ time.sleep() zwischen Anfragen in Schleifen
✅ Bei 429: warten und später erneut versuchen
✅ Nutzungsbedingungen und Limits lesen
❌ Keine Schleife ohne Pause über 10.000 Anfragen
```

```python
import time

for stadt in staedte:
    daten = hole_daten(url, {"q": stadt})
    time.sleep(1)          # 🤝 fair gegenüber dem Server
```

### 8. 🆓 Kostenlose APIs zum Üben (kein Key nötig)

| API | URL | Was |
|---|---|---|
| Open-Meteo | `api.open-meteo.com` | Wetter ⛅ |
| REST Countries | `restcountries.com` | Länderdaten 🌍 |
| JSONPlaceholder | `jsonplaceholder.typicode.com` | Testdaten 🧪 |
| Frankfurter | `api.frankfurter.app` | Wechselkurse 💱 |
| Open Library | `openlibrary.org` | Bücher 📚 |
| Deutscher Wetterdienst | `dwd.api.bund.dev` | Amtliches Wetter 🇩🇪 |

📌 Weitere: [github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| kein `timeout` | Skript hängt ewig | `timeout=10` |
| Statuscode ignoriert | Fehler bleibt unbemerkt | `raise_for_status()` |
| API-Key im Code | 🚨 Leck | `.env` |
| URL per String gebaut | Sonderzeichen kaputt | `params={}` |
| Schleife ohne Pause | IP gesperrt | `time.sleep()` |
| `.json()` ohne Prüfung | `ValueError` | in `try` packen |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — funktioniert **auch offline** (Demo-Modus mit lokalen Beispieldaten) 📴

---

## 🛠️ Mini-Projekt: Wetter-Dashboard ⛅

Siehe [`projekte/05_wetter/`](../../projekte/05_wetter/README.md) — das ist Projekt 5.

---

## 🧠 Selbsttest

1. Was ist eine API — mit eigenem Bild?
2. Was bedeuten 200, 404, 429, 500?
3. Warum immer `timeout`?
4. Was macht `raise_for_status()`?
5. Wie gibst du Parameter richtig mit?
6. Wo gehören API-Keys hin?
7. Was tust du bei Statuscode 429?
8. Wie wandelst du eine Antwort in ein dict?
9. Welche Exceptions solltest du abfangen?
10. ✍️ Nenne drei Regeln der API-Etikette.

<details>
<summary>💡 Antworten</summary>

1. Eine definierte Schnittstelle, über die Programme Daten austauschen — wie eine Speisekarte.
2. 200 = OK · 404 = nicht gefunden · 429 = zu viele Anfragen · 500 = Serverfehler.
3. Sonst hängt das Programm unbegrenzt, wenn der Server nicht antwortet.
4. Wirft eine Exception bei Statuscodes ab 400.
5. Über `params={...}` statt String-Verkettung.
6. In eine `.env`-Datei, die per `.gitignore` ausgeschlossen ist.
7. Warten und später erneut versuchen (Rate Limit).
8. `antwort.json()`
9. `Timeout`, `HTTPError`, `ConnectionError`, `ValueError`.
10. Timeout setzen · Pausen zwischen Anfragen · Ergebnisse zwischenspeichern statt wiederholt abfragen.
</details>

---

## 🔄 Wiederholung (Modul 19–21)

1. Was ist eine magische Zahl?
2. Was gehört in `.gitignore`?
3. Was macht `re.findall`?
4. Warum `r"..."` bei Regex?

---

## 🔗 Vertiefung

- 📖 [requests-Doku](https://requests.readthedocs.io/)
- 📖 [Real Python — APIs](https://realpython.com/api-integration-in-python/)

**➡️ [Modul 23 — Web-Scraping](../23/README.md)** 🕷️
