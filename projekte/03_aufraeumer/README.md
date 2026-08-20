# 🗂️ Projekt 3 — Der Ordner-Aufräumer

> 📍 **Nach Modul 13** · ⏱️ ~5 Stunden · 🎯 Dein erstes Programm, das **echte Arbeit** abnimmt

---

## 🎬 So soll es aussehen

```text
╔══════════════════════════════════════════════════════╗
║           🗂️  ORDNER-AUFRÄUMER  v1.0                  ║
╚══════════════════════════════════════════════════════╝

📁 Ordner:   C:\Users\DEINNAME\Downloads
🔍 Gefunden: 247 Dateien, 3 Unterordner
🛡️ Modus:    TROCKENLAUF (nichts wird verändert)

── VORSCHAU ──────────────────────────────────────────
  [TEST] urlaubsfoto.jpg               → Bilder/
  [TEST] Rechnung Müller 2026.pdf      → Dokumente/
  [TEST] budget_2026.xlsx              → Tabellen/
  [TEST] podcast_folge_42.mp3          → Musik/
  ... 243 weitere

── ZUSAMMENFASSUNG ───────────────────────────────────
  📷 Bilder        128  ████████████████
  📄 Dokumente      54  ███████
  🎵 Musik          31  ████
  📊 Tabellen       18  ██
  🎬 Videos          9  █
  📦 Archive         5  ▌
  ❓ Sonstiges       2  ▏

  🔁 3 Duplikatgruppen gefunden (12,4 MB verschwendet)

──────────────────────────────────────────────────────
  Das war ein Trockenlauf. Wirklich ausführen?  (j/n) > 
```

---

## 🚨 Sicherheit zuerst!

> Dieses Programm **verändert echte Dateien**. Halte dich an diese Regeln:

```text
1. 🧪 Erst in einem Testordner mit Wegwerf-Dateien testen
2. 👀 TROCKENLAUF ist der STANDARD - nicht die Option
3. 💾 Vor dem ersten echten Lauf: Backup
4. 🗑️ Niemals löschen - nur verschieben
5. 🛡️ Nie überschreiben - bei Namenskonflikt umbenennen
```

---

## ✅ Pflichtanforderungen

- [ ] Ordner rekursiv einlesen (`pathlib`)
- [ ] Dateien nach Typ in Unterordner sortieren
- [ ] **Trockenlauf als Standard**, echtes Ausführen nur nach Bestätigung
- [ ] Namenskonflikte behandeln (nie überschreiben!)
- [ ] Statistik: Anzahl pro Kategorie mit Balkendiagramm
- [ ] Vollständige Fehlerbehandlung (`PermissionError`, `FileNotFoundError`, …)
- [ ] Programm stürzt **niemals** ab
- [ ] Alles in Funktionen + `main()`

## 🎁 Bonus

- [ ] Duplikate per SHA-256-Hash finden
- [ ] ZIP-Backup vor dem Ausführen
- [ ] „Papierkorb"-Ordner statt Löschen
- [ ] Konfigurierbare Regeln (Dictionary oder JSON-Datei)
- [ ] Dateinamen bereinigen (Umlaute, Leerzeichen)
- [ ] Nach Datum sortieren statt nach Typ (Jahr/Monat-Ordner)
- [ ] Bericht als Textdatei
- [ ] Leere Ordner entfernen

---

## 🦴 Dein Skelett

```python
"""Ordner-Aufräumer - sortiert Dateien nach Typ."""
from pathlib import Path

REGELN = {
    "Bilder":    {".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic"},
    "Dokumente": {".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf"},
    "Tabellen":  {".xlsx", ".xls", ".csv", ".ods"},
    "Musik":     {".mp3", ".wav", ".flac", ".m4a"},
    "Videos":    {".mp4", ".mov", ".avi", ".mkv"},
    "Archive":   {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code":      {".py", ".js", ".html", ".css", ".json"},
}


def sammle_dateien(ordner):
    """Sammelt alle Dateien eines Ordners."""

def ziel_kategorie(datei):
    """Bestimmt die Zielkategorie einer Datei."""

def eindeutiger_pfad(ziel):
    """Findet einen freien Dateinamen, falls das Ziel schon existiert."""

def sortiere(dateien, basis, trockenlauf=True):
    """Sortiert die Dateien. Gibt eine Statistik zurück."""

def finde_duplikate(dateien):
    """Findet Dateien mit identischem Inhalt (per Hash)."""

def erstelle_backup(ordner):
    """Erstellt ein ZIP-Backup."""

def zeige_statistik(statistik):
    """Gibt die Statistik mit Balkendiagramm aus."""

def main():
    """Hauptprogramm."""
```

---

## 🪜 Schritt für Schritt

<details>
<summary><b>Schritt 1 — Nur anzeigen</b></summary>

Alle Dateien auflisten mit Name, Endung, Größe. Noch nichts verschieben. ✅
</details>

<details>
<summary><b>Schritt 2 — Kategorien zuordnen</b></summary>

`ziel_kategorie()` schreiben und für jede Datei anzeigen, wohin sie **würde**.
</details>

<details>
<summary><b>Schritt 3 — Statistik</b></summary>

Zählen pro Kategorie, Balkendiagramm ausgeben.
</details>

<details>
<summary><b>Schritt 4 — Echtes Verschieben (nur im Testordner!)</b></summary>

`ziel.parent.mkdir(exist_ok=True)` und `datei.rename(ziel)`.
⚠️ Vorher `eindeutiger_pfad()` — nie überschreiben!
</details>

<details>
<summary><b>Schritt 5 — Fehlerbehandlung</b></summary>

`PermissionError` (Datei in Benutzung), `FileNotFoundError`, `OSError`.
Fehler sammeln und am Ende berichten — **nicht abbrechen**.
</details>

<details>
<summary><b>Schritt 6 — Bestätigung & Backup</b></summary>

Erst Trockenlauf zeigen, dann fragen, dann Backup, dann ausführen.
</details>

---

## ⚠️ Die vier klassischen Fallen

```python
# 1) Beim Iterieren verändern
for datei in ordner.iterdir():       # ❌ Ordner ändert sich währenddessen!
    datei.rename(...)
for datei in list(ordner.iterdir()): # ✅ erst Liste bilden

# 2) Überschreiben
datei.rename(ziel)                   # ❌ löscht vorhandene Datei!
if ziel.exists():                    # ✅
    ziel = ziel.with_stem(f"{ziel.stem}_1")

# 3) Die eigenen Zielordner mitsortieren
for datei in ordner.iterdir():
    if datei.is_dir():               # ✅ Ordner überspringen!
        continue

# 4) Beim ersten Fehler abbrechen
try:
    datei.rename(ziel)
except PermissionError:
    fehler.append(datei.name)        # ✅ sammeln und weitermachen
```

---

## 💥 Der Härtetest

```text
□ Leerer Ordner
□ Ordner existiert nicht
□ Datei ohne Endung
□ Datei mit Endung in Großbuchstaben (.JPG)
□ Zwei Dateien gleichen Namens in verschiedenen Unterordnern
□ Datei ist in einem anderen Programm geöffnet
□ Schreibgeschützter Ordner
□ Dateinamen mit Umlauten und Sonderzeichen
□ 1000+ Dateien (dauert es zu lange?)
```

---

## 🧠 Reflexion

1. Wie fühlt es sich an, dass dein Code echte Dateien anfasst? 😅
2. Welche Sicherheitsmaßnahme hältst du für die wichtigste?
3. Was würdest du ergänzen, damit du es täglich benutzt?
4. Wie viele Fehlerfälle hast du gefunden, an die du zuerst nicht gedacht hast?

---

## 🔍 Musterlösung

👉 [`loesung/aufraeumer.py`](loesung/aufraeumer.py) — legt sich einen eigenen Testordner an

**➡️ Weiter: [Modul 14 — OOP Teil 1](../../module/14/README.md)**
