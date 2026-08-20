"""
Modul 25 - Beispiel: PDFs bearbeiten mit pypdf
"""
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("❌ pypdf fehlt. Installieren mit:\n   pip install pypdf\n")
    raise SystemExit(0)

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    HAT_REPORTLAB = True
except ImportError:
    HAT_REPORTLAB = False

ORDNER = Path(__file__).parent / "_pdf25"
ORDNER.mkdir(exist_ok=True)

print("=" * 62, "\nPDF-AUTOMATISIERUNG\n", "=" * 62)

if not HAT_REPORTLAB:
    print("""
  ℹ️  Zum Erzeugen der Test-PDFs wird 'reportlab' gebraucht:
         pip install reportlab

  Die pypdf-Befehle funktionieren auch ohne - du brauchst dann nur
  eigene PDF-Dateien zum Ausprobieren. Hier die wichtigsten:

  ── LESEN ─────────────────────────────────────────────────────
      leser = PdfReader("dokument.pdf")
      print(len(leser.pages))                 # Seitenzahl
      print(leser.pages[0].extract_text())    # Text der 1. Seite
      print(leser.metadata)                   # Titel, Autor, …

  ── ZUSAMMENFÜGEN ─────────────────────────────────────────────
      schreiber = PdfWriter()
      for pfad in ["a.pdf", "b.pdf", "c.pdf"]:
          for seite in PdfReader(pfad).pages:
              schreiber.add_page(seite)
      schreiber.write("zusammen.pdf")

  ── TEILEN ────────────────────────────────────────────────────
      leser = PdfReader("gross.pdf")
      for i, seite in enumerate(leser.pages, start=1):
          w = PdfWriter()
          w.add_page(seite)
          w.write(f"seite_{i:03d}.pdf")

  ── SEITEN AUSWÄHLEN ──────────────────────────────────────────
      w = PdfWriter()
      for i in [0, 2, 4]:                     # Seiten 1, 3, 5
          w.add_page(leser.pages[i])
      w.write("auswahl.pdf")

  ── DREHEN ────────────────────────────────────────────────────
      seite = leser.pages[0]
      seite.rotate(90)

  ── VERSCHLÜSSELN ─────────────────────────────────────────────
      w.encrypt("geheim")
      w.write("geschuetzt.pdf")

  ⚠️ Gescannte PDFs enthalten BILDER, keinen Text.
     extract_text() liefert dann nichts. Dafür bräuchte man OCR
     (pytesseract) - das geht über diesen Kurs hinaus.
""")
    raise SystemExit(0)


# ====================================================================
# TEST-PDFs ERZEUGEN
# ====================================================================
def erzeuge_pdf(pfad, titel, zeilen):
    """Erzeugt ein einfaches Test-PDF."""
    c = canvas.Canvas(str(pfad), pagesize=A4)
    breite, hoehe = A4
    c.setFont("Helvetica-Bold", 18)
    c.drawString(60, hoehe - 80, titel)
    c.setFont("Helvetica", 12)
    for i, zeile in enumerate(zeilen):
        c.drawString(60, hoehe - 120 - i * 20, zeile)
    c.save()


kapitel = {
    "kapitel_1.pdf": ("Kapitel 1: Grundlagen",
                      ["Variablen speichern Werte.", "Funktionen bündeln Code."]),
    "kapitel_2.pdf": ("Kapitel 2: Datenstrukturen",
                      ["Listen sind geordnet.", "Dictionaries haben Schlüssel."]),
    "kapitel_3.pdf": ("Kapitel 3: Automatisierung",
                      ["pathlib verwaltet Pfade.", "shutil kopiert Dateien."]),
}
for name, (titel, zeilen) in kapitel.items():
    erzeuge_pdf(ORDNER / name, titel, zeilen)

print(f"  ✅ {len(kapitel)} Test-PDFs erzeugt\n")

# ====================================================================
print("1. PDF LESEN\n" + "-" * 62)

leser = PdfReader(ORDNER / "kapitel_1.pdf")
print(f"  Seiten:  {len(leser.pages)}")
text = leser.pages[0].extract_text()
print(f"  Text der ersten Seite:")
for zeile in text.strip().splitlines():
    print(f"    | {zeile}")

# ====================================================================
print("\n2. PDFs ZUSAMMENFÜGEN\n" + "-" * 62)

schreiber = PdfWriter()
for name in sorted(kapitel):
    for seite in PdfReader(ORDNER / name).pages:
        schreiber.add_page(seite)

zusammen = ORDNER / "handbuch_komplett.pdf"
with open(zusammen, "wb") as f:
    schreiber.write(f)

print(f"  ✅ {zusammen.name}: {len(PdfReader(zusammen).pages)} Seiten "
      f"aus {len(kapitel)} Dateien")

# ====================================================================
print("\n3. PDF TEILEN\n" + "-" * 62)

einzeln = ORDNER / "einzelseiten"
einzeln.mkdir(exist_ok=True)

leser = PdfReader(zusammen)
for i, seite in enumerate(leser.pages, start=1):
    w = PdfWriter()
    w.add_page(seite)
    ziel = einzeln / f"seite_{i:03d}.pdf"
    with open(ziel, "wb") as f:
        w.write(f)
    print(f"    ✅ {ziel.name}")

# ====================================================================
print("\n4. TEXT AUS ALLEN PDFs EXTRAHIEREN\n" + "-" * 62)

gesamttext = []
for pfad in sorted(ORDNER.glob("kapitel_*.pdf")):
    leser = PdfReader(pfad)
    for nr, seite in enumerate(leser.pages, start=1):
        gesamttext.append(f"--- {pfad.name}, Seite {nr} ---")
        gesamttext.append(seite.extract_text().strip())

textdatei = ORDNER / "gesamttext.txt"
textdatei.write_text("\n".join(gesamttext), encoding="utf-8")
print(f"  ✅ {textdatei.name} ({len(textdatei.read_text(encoding='utf-8'))} Zeichen)")

# Wörter zählen (Modul 12!)
from collections import Counter
woerter = textdatei.read_text(encoding="utf-8").lower().split()
haeufig = Counter(w.strip(".,:;") for w in woerter if len(w) > 4)
print(f"  Häufigste Wörter: {haeufig.most_common(5)}")

# ====================================================================
print("\n5. SEITEN AUSWÄHLEN & DREHEN\n" + "-" * 62)

leser = PdfReader(zusammen)
w = PdfWriter()
for i in (0, 2):                       # Seiten 1 und 3
    seite = leser.pages[i]
    seite.rotate(90)
    w.add_page(seite)

auswahl = ORDNER / "auswahl_gedreht.pdf"
with open(auswahl, "wb") as f:
    w.write(f)
print(f"  ✅ {auswahl.name}: 2 ausgewählte Seiten, um 90° gedreht")

print(f"""
{'=' * 62}
  📁 Alle PDFs liegen in: {ORDNER}

  💡 TYPISCHE ANWENDUNGSFÄLLE:
     • 30 Einzelrechnungen zu einer Sammel-PDF zusammenfügen
     • Aus 200 Rechnungs-PDFs die Beträge extrahieren (+ Regex, Modul 21!)
     • Ein Handbuch in Einzelkapitel zerlegen
     • Nur die unterschriebenen Seiten aus Verträgen ziehen

  ⚠️ Gescannte PDFs = Bilder. Da hilft nur OCR (pytesseract).
{'=' * 62}
""")
