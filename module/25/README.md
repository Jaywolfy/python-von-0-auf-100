# 🤖 Modul 25 — Dateien, Ordner & PDFs automatisieren

> ⏱️ ~5 Stunden · ⬅️ [Modul 24](../24/README.md) · ➡️ [Modul 26](../26/README.md)

---

## 🎯 Lernziele

- [ ] Dateien massenhaft umbenennen, kopieren, verschieben
- [ ] Ordner nach Regeln sortieren
- [ ] Duplikate finden
- [ ] PDFs zusammenfügen, teilen, Text extrahieren
- [ ] **sicher** arbeiten: Trockenlauf, Backups, Bestätigung 🛡️

---

## 🚨 ZUERST: Die Sicherheitsregeln

> Ab hier verändert dein Code **echte Dateien**. Ein Tippfehler kann Daten löschen.
> Diese vier Regeln sind nicht optional:

```text
1. 🧪 TESTORDNER  — Erst in einem Wegwerf-Ordner testen. Immer.
2. 👀 TROCKENLAUF — Erst nur ANZEIGEN, was passieren würde. Dann ausführen.
3. 💾 BACKUP      — Vor dem ersten echten Lauf: Kopie anlegen.
4. 🗑️ NIE LÖSCHEN — Verschiebe in einen "Papierkorb"-Ordner statt zu löschen.
```

```python
TROCKENLAUF = True          # 👈 Standard: True. Erst nach dem Test auf False.

for datei in dateien:
    ziel = zielordner / datei.name
    if TROCKENLAUF:
        print(f"[TEST] {datei.name} → {ziel}")
    else:
        datei.rename(ziel)
```

> 🧠 **Tutor sagt:** Diese eine Variable hat schon unzählige Datenverluste verhindert. Bau sie in **jedes** Skript ein, das Dateien anfasst. 🛡️

---

## 📖 Die Lektion

### 1. Ordner durchsuchen (Wiederholung + mehr)

```python
from pathlib import Path

ordner = Path("dokumente")

ordner.iterdir()               # eine Ebene
ordner.glob("*.pdf")           # PDFs, eine Ebene
ordner.rglob("*.pdf")          # ⭐ PDFs in ALLEN Unterordnern
ordner.glob("rechnung_*.pdf")  # mit Muster

for p in ordner.rglob("*"):
    if p.is_file():
        print(p.relative_to(ordner), p.stat().st_size)
```

### 2. `shutil` — kopieren, verschieben, löschen

```python
import shutil

shutil.copy2("a.txt", "b.txt")            # Datei kopieren (mit Zeitstempeln)
shutil.copytree("quelle", "ziel")         # ganzen Ordner kopieren
shutil.move("a.txt", "ordner/a.txt")      # verschieben
shutil.rmtree("ordner")                   # 🚨 ORDNER + INHALT LÖSCHEN
shutil.make_archive("backup", "zip", "ordner")   # ZIP erstellen
shutil.disk_usage("/")                    # Speicherplatz
```

⚠️ `shutil.rmtree()` löscht **ohne Rückfrage und ohne Papierkorb**. Behandle es wie eine geladene Waffe. 🔫

### 3. Dateien umbenennen

```python
p = Path("foto.jpg")
p.rename("neuer_name.jpg")
p.rename(p.with_suffix(".png"))                    # Endung ändern
p.rename(p.with_name("anders.jpg"))                # Name ändern
p.rename(p.parent / "unterordner" / p.name)        # verschieben
```

🌍 **Massen-Umbenennung mit Nummerierung:**

```python
for nr, datei in enumerate(sorted(ordner.glob("*.jpg")), start=1):
    neu = ordner / f"urlaub_{nr:03d}{datei.suffix}"      # urlaub_001.jpg
    print(f"{datei.name} → {neu.name}")
    if not TROCKENLAUF:
        datei.rename(neu)
```

### 4. 🗂️ Ordner sortieren

```python
REGELN = {
    "Bilder":     {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Dokumente":  {".pdf", ".docx", ".txt", ".odt"},
    "Tabellen":   {".xlsx", ".csv", ".ods"},
    "Musik":      {".mp3", ".wav", ".flac"},
    "Videos":     {".mp4", ".mov", ".mkv"},
    "Archive":    {".zip", ".rar", ".7z"},
}

def ziel_ordner(datei):
    """Findet den passenden Zielordner für eine Datei."""
    for name, endungen in REGELN.items():
        if datei.suffix.lower() in endungen:
            return name
    return "Sonstiges"
```

### 5. 🔍 Duplikate finden (per Hash)

Gleicher Name heißt nicht gleicher Inhalt — und umgekehrt. Deshalb: **Hash** vergleichen.

```python
import hashlib

def datei_hash(pfad, block=65536):
    """Berechnet den SHA-256-Hash einer Datei."""
    h = hashlib.sha256()
    with open(pfad, "rb") as f:
        while stueck := f.read(block):
            h.update(stueck)
    return h.hexdigest()

nach_hash = {}
for datei in ordner.rglob("*"):
    if datei.is_file():
        nach_hash.setdefault(datei_hash(datei), []).append(datei)

duplikate = {h: p for h, p in nach_hash.items() if len(p) > 1}
```

### 6. 📄 PDFs

```bash
pip install pypdf
```

```python
from pypdf import PdfReader, PdfWriter

# Lesen
leser = PdfReader("dokument.pdf")
print(len(leser.pages))
print(leser.pages[0].extract_text())
print(leser.metadata.title)

# Zusammenfügen
schreiber = PdfWriter()
for pfad in ["a.pdf", "b.pdf"]:
    for seite in PdfReader(pfad).pages:
        schreiber.add_page(seite)
schreiber.write("zusammen.pdf")

# Teilen
leser = PdfReader("gross.pdf")
for i, seite in enumerate(leser.pages, start=1):
    w = PdfWriter()
    w.add_page(seite)
    w.write(f"seite_{i:03d}.pdf")

# Drehen
seite.rotate(90)
```

⚠️ **Gescannte PDFs enthalten keinen Text**, sondern Bilder. Dafür braucht man OCR (`pytesseract`) — das geht über den Kurs hinaus, aber jetzt weißt du, warum `extract_text()` manchmal leer bleibt. 🔍

### 7. 🌍 Das komplette Muster für sichere Automatisierung

```python
def sortiere_ordner(quelle: Path, trockenlauf: bool = True) -> dict:
    """Sortiert Dateien nach Typ in Unterordner.

    Args:
        quelle: Der zu sortierende Ordner.
        trockenlauf: Wenn True, wird nur angezeigt, nichts verschoben.

    Returns:
        Statistik als dict.
    """
    statistik = {}
    for datei in quelle.iterdir():
        if not datei.is_file():
            continue
        ziel_name = ziel_ordner(datei)
        ziel = quelle / ziel_name / datei.name

        if trockenlauf:
            print(f"  [TEST] {datei.name:<30} → {ziel_name}/")
        else:
            ziel.parent.mkdir(exist_ok=True)
            if ziel.exists():                   # 🛡️ nichts überschreiben!
                ziel = ziel.with_stem(f"{ziel.stem}_1")
            datei.rename(ziel)
        statistik[ziel_name] = statistik.get(ziel_name, 0) + 1
    return statistik
```

---

## ⚠️ Typische Anfängerfehler

| Fehler | Folge | Fix |
|---|---|---|
| Kein Trockenlauf | Chaos im echten Ordner 💀 | `TROCKENLAUF = True` |
| Datei überschrieben | Daten weg | vorher `ziel.exists()` prüfen |
| `rmtree` auf falschem Pfad | Ordner weg 💀 | Pfad ausgeben und prüfen |
| Beim Iterieren umbenennen | Dateien doppelt/übersprungen | erst `list(...)` bilden |
| Original statt Kopie bearbeitet | Ausgangsdaten weg | Backup zuerst |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — erzeugt sich einen kompletten Testordner 🧪

---

## 🛠️ Mini-Projekt: Der Ordner-Aufräumer 🗂️

Siehe [`projekte/03_aufraeumer/`](../../projekte/03_aufraeumer/README.md) — das ist Projekt 3.

---

## 🧠 Selbsttest

1. Welche vier Sicherheitsregeln gelten hier?
2. Was macht ein Trockenlauf?
3. Unterschied `glob` / `rglob`?
4. Was macht `shutil.rmtree()` — und warum Vorsicht?
5. Wie änderst du eine Dateiendung?
6. Warum Duplikate per Hash statt per Name suchen?
7. Wie fügst du zwei PDFs zusammen?
8. Warum liefert `extract_text()` manchmal nichts?
9. Wie verhinderst du das Überschreiben beim Verschieben?
10. ✍️ Beschreibe dein Vorgehen, bevor du ein Skript zum ersten Mal echt laufen lässt.

<details>
<summary>💡 Antworten</summary>

1. Testordner, Trockenlauf, Backup, nie direkt löschen.
2. Er zeigt nur an, was passieren **würde**, ohne etwas zu verändern.
3. `glob` sucht in einer Ebene, `rglob` rekursiv in allen Unterordnern.
4. Löscht einen Ordner samt Inhalt — ohne Rückfrage und ohne Papierkorb.
5. `pfad.with_suffix(".png")`
6. Weil gleicher Inhalt unterschiedlich heißen kann und umgekehrt.
7. Alle Seiten beider Dateien in einen `PdfWriter` legen und schreiben.
8. Bei gescannten PDFs ist der Inhalt ein Bild, kein Text — dafür braucht man OCR.
9. Vorher `ziel.exists()` prüfen und den Namen anpassen.
10. Testordner anlegen → Trockenlauf → Ausgabe prüfen → Backup → erst dann echt laufen lassen.
</details>

---

## 🔄 Wiederholung (Modul 22–24)

1. Warum `timeout` bei requests?
2. Wozu `data_only=True` bei openpyxl?
3. Warum `time.sleep()` beim Scrapen?
4. Was macht `Path("a") / "b"`?

---

## 🔗 Vertiefung

- 📖 [Automate the Boring Stuff — Kap. 9–10 & 15](https://automatetheboringstuff.com/)
- 📖 [pypdf-Doku](https://pypdf.readthedocs.io/)

**➡️ [Modul 26 — Skripte alltagstauglich machen](../26/README.md)** 🎁
