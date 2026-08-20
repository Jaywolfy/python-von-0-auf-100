# ⌨️ Spickzettel · VS Code

## Ausführen
| Shortcut | Aktion |
|---|---|
| `F5` | ▶️ Mit Debugger starten |
| `Strg + F5` | ▶️ Einfach ausführen (schneller) |
| `Shift + F5` | ⏹️ Stoppen |
| `Strg + C` (im Terminal) | 🛑 Laufendes Programm abbrechen |

## Editieren
| Shortcut | Aktion |
|---|---|
| `Strg + S` | 💾 Speichern |
| `Strg + Z` / `Strg + Y` | ↩️ Rückgängig / Wiederholen |
| `Strg + /` | 💬 Zeile aus-/einkommentieren |
| `Alt + ↑ / ↓` | ↕️ Zeile verschieben |
| `Shift + Alt + ↓` | 📄 Zeile duplizieren |
| `Strg + D` | 🎯 Nächstes gleiches Wort mitmarkieren |
| `Alt + Klick` | ✏️ Zusätzlichen Cursor setzen |
| `Strg + Shift + K` | 🗑️ Zeile löschen |
| `Tab` / `Shift + Tab` | ➡️⬅️ Ein-/Ausrücken |
| `F2` | 🔤 Symbol überall umbenennen |
| `Shift + Alt + F` | 🧼 Datei formatieren |

## Navigieren
| Shortcut | Aktion |
|---|---|
| `Strg + P` | 🔍 Datei schnell öffnen |
| `Strg + Shift + P` | 🎛️ Befehlspalette (alles!) |
| `Strg + F` / `Strg + H` | Suchen / Ersetzen |
| `Strg + Shift + F` | 🔎 In allen Dateien suchen |
| `Strg + G` | Zu Zeile springen |
| `F12` | Zur Definition springen |
| `Alt + ←` | ↩️ Zurück |
| `Strg + ö` | 🖥️ Terminal ein-/ausblenden |
| `Strg + B` | 📁 Seitenleiste ein-/ausblenden |

## 🐞 Debugger (Modul 09)
| Shortcut | Aktion |
|---|---|
| `F9` | 🔴 Breakpoint setzen/entfernen |
| `F5` | ▶️ Starten / Weiterlaufen |
| `F10` | ⤵️ **Step Over** — nächste Zeile (Funktionen überspringen) |
| `F11` | ⤴️ **Step Into** — in die Funktion hineingehen |
| `Shift + F11` | ⤴️ **Step Out** — aus der Funktion raus |
| `Shift + F5` | ⏹️ Stoppen |

**Debugger-Panels links:**
- **Variables** 👀 — alle aktuellen Werte, live
- **Watch** 🔭 — eigene Ausdrücke beobachten (z. B. `len(liste)`)
- **Call Stack** 📚 — wer hat wen aufgerufen

## 🧩 Empfohlene Extensions
| Extension | Zweck |
|---|---|
| **Python** (Microsoft) | 🔴 Pflicht |
| **Pylance** | 🔴 Autovervollständigung |
| **Ruff** | 🟡 Linting + Formatierung |
| **indent-rainbow** | 🌈 Einrückungen farbig — Gold für Anfänger! |
| **Error Lens** | 👀 Fehler direkt in der Zeile |
| **Path Intellisense** | 📁 Pfad-Autovervollständigung |
| **Rainbow CSV** | 📊 CSV-Dateien lesbar färben |

## 💡 Kleine Tricks
```text
Strg+Shift+P → "Python: Select Interpreter"   → richtige Python-Version wählen
Strg+Shift+P → "Python: Create Environment"   → venv anlegen (Modul 17)
Strg+Shift+P → "Convert Indentation to Spaces" → Tab-Chaos beheben
Strg+Leertaste                                → Autovervollständigung erzwingen
```
