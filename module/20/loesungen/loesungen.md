# ✅ Modul 20 · Lösungen & Erklärungen

## Aufgabe 1 — Die drei Zustände

```text
📁 Untracked  →  Git kennt die Datei noch gar nicht
📋 Staged     →  vorgemerkt für den nächsten Commit (nach git add)
📦 Committed  →  dauerhaft gespeichert (nach git commit)
```

Dazwischen gibt es noch **Modified**: Git kennt die Datei, sie wurde aber
seit dem letzten Commit geändert und ist noch nicht vorgemerkt.

## Aufgabe 2 — diff vs. diff --staged

| Befehl | Zeigt |
|---|---|
| `git diff` | Änderungen, die **noch nicht** vorgemerkt sind |
| `git diff --staged` | Änderungen, die **schon** vorgemerkt sind |
| `git diff HEAD` | beides zusammen |

Nach `git add` ist `git diff` leer, weil dort nichts Unvorgemerktes mehr liegt.

## Aufgabe 3 — .gitignore

⚠️ **Wichtig:** `.gitignore` wirkt nur auf Dateien, die Git **noch nicht** verfolgt.
Eine bereits committete Datei musst du erst entfernen:

```bash
git rm --cached geheim.env
```

Deshalb: **`.gitignore` immer als einen der ersten Commits anlegen.**

## Aufgabe 4 — restore-Varianten

| Befehl | Wirkung |
|---|---|
| `git restore datei` | Verwirft Änderungen — **Datei wird zurückgesetzt** ⚠️ unwiderruflich |
| `git restore --staged datei` | Nimmt nur aus dem Staging — **Änderungen bleiben erhalten** ✅ |

## Aufgabe 5 — Beispiel für eine gute History

```text
a1b2c3d Fügt Begrüßungsfunktion hinzu
e4f5g6h Ergänzt Docstring für begruesse()
i7j8k9l Fügt Verabschiedungsfunktion hinzu
m0n1o2p Schreibt README mit Installationsanleitung
q3r4s5t Behebt Tippfehler in der Ausgabe
```

Man liest von unten nach oben und versteht die Entwicklung — **ohne den Code zu öffnen**.
Genau das ist das Ziel.

## Aufgabe 6 — Was Branches wirklich sind

Ein Branch ist nur ein **Zeiger auf einen Commit**. Deshalb ist das Anlegen
kostenlos und sofort — Git kopiert keine Dateien.

```bash
git log --oneline --graph --all
```

```text
*   9f2c1a  (main) Merge branch 'experiment'
|\
| * 3d4e5f  (experiment) Baut Experiment ein
* | 7a8b9c  Ergänzt README
|/
* 1a2b3c  Erster Commit
```

## Aufgabe 7 — Konflikte lösen

```text
<<<<<<< HEAD
print("Version aus main")
=======
print("Version aus version-a")
>>>>>>> version-a
```

**Vorgehen:**
1. Datei öffnen
2. Entscheiden: eine Version, die andere, oder eine Mischung
3. **Alle drei Markierungszeilen löschen** (`<<<<<<<`, `=======`, `>>>>>>>`)
4. `git add datei`
5. `git commit`

> 💡 VS Code zeigt Konflikte grafisch mit Buttons: *Accept Current* /
> *Accept Incoming* / *Accept Both*. Viel angenehmer als Handarbeit.

**Konflikte vermeiden:** oft `git pull`, kleine Commits, unterschiedliche Dateien bearbeiten.

## Aufgabe 8 — GitHub-Fehlerbehebung

| Fehler | Lösung |
|---|---|
| `remote origin already exists` | `git remote set-url origin <URL>` |
| `Authentication failed` | Personal Access Token statt Passwort (GitHub → Settings → Developer settings → Tokens) |
| `refusing to merge unrelated histories` | Beim Repo-Anlegen doch ein README erstellt → `git pull --allow-unrelated-histories` |
| `Updates were rejected` | Erst `git pull`, dann `git push` |

## Aufgabe 9 — Checkliste vor jedem ersten Push

```text
□ .gitignore existiert und enthält .venv/, .env, __pycache__/
□ Keine Passwörter/API-Keys im Code
□ README.md erklärt Zweck, Installation und Nutzung
□ requirements.txt vorhanden (falls Pakete nötig)
□ Repo ist auf PRIVATE gestellt 🔒
□ Der Code läuft (letzter Test vor dem Push!)
```

---

## 🎓 Der wichtigste Rat zu Git

**Committe oft.** Ein Commit kostet nichts und dauert 5 Sekunden.
Ein verlorener Arbeitstag kostet einen Arbeitstag.

Faustregel: Immer wenn etwas funktioniert, das vorher nicht funktioniert hat → committen.

🎉 **Modul 20 geschafft!** Dein Code ist jetzt sicher und sichtbar.
