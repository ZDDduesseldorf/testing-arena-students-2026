# Testing Arena 2026 – Weather Data

> **Woher wissen wir, dass Code wirklich korrekt ist?**

Eine kleine Wetterbibliothek verarbeitet Messungen wie

```text
Köln;14:21;21.7
Düsseldorf;09:05;18.3
```

Die vorhandene Implementierung sieht plausibel aus und die mitgelieferten Tests sind
grün. Ihre Aufgabe ist es herauszufinden, wie belastbar diese Aussage wirklich ist.

## Lernziele

Nach dem Praktikum kannst du:

- aus einer Spezifikation sinnvolle Testfälle ableiten,
- normale Fälle, Grenzwerte, Sonderfälle und ungültige Eingaben unterscheiden,
- Tests mit `pytest` formulieren,
- `pytest.raises(...)` und bei Bedarf `pytest.mark.parametrize(...)` einsetzen,
- verstehen, warum **grüne Tests nicht automatisch korrekten Code bedeuten**,
- eine Testsuite anhand unbekannter fehlerhafter Implementierungen beurteilen.

## 1. Repository forken und klonen

"Forke" dieses Repository in den eigenen GitHub-Account.

> Für diese Übung bitte **keinen Pull Request an das ZDD-Originalrepository** öffnen.

Erstellen Sie für Ihre Arbeit einen eigenen Branch, zum Beispiel:

```bash
git switch -c testing/<github-name>
```

## 2. Umgebung und Startertests

Mit `uv`:

```bash
uv sync
uv run pytest
```

Die mitgelieferten Tests sollten grün sein.

**Aber:** Die Startertests prüfen absichtlich fast nur gewöhnliche Beispiele. Sie sind
kein Nachweis dafür, dass die Bibliothek vollständig korrekt ist.

## 3. Erst Spezifikation, dann Tests

Lest bitte zuerst [`SPECIFICATION.md`](SPECIFICATION.md).

Bevor ihr neue Tests schreibt, sammelt im [`TEST_PLAN.md`](TEST_PLAN.md) mögliche
Fälle. Denken Sie insbesondere an unterschiedliche Klassen von Tests:

- gewöhnliche Beispiele,
- Grenzwerte,
- Spezialfälle,
- ungültige Eingaben,
- Seiteneffekte bzw. Veränderungen von Eingabedaten.

Danach erweitert `tests/test_weather.py`.

Ihr dürft die vorhandenen Tests verändern, aufteilen oder durch bessere Tests ersetzen.
Die Qualität der Testsuite ist wichtiger als die Anzahl der Tests.

## 4. Was darf verändert werden?

Für die eigentliche Challenge verändert bitte nur:

- `tests/`
- `TEST_PLAN.md`

Die Dateien

- `weather.py`
- `.github/workflows/tests.yml`
- `.github/workflows/mutant_runs.yml`

gehören zur Aufgabenstellung und sollen nicht verändert werden, um einen besseren
Arena-Score zu erzielen.

## 5. Committen und pushen

Arbeitet mit nachvollziehbaren Commits. Zum Beispiel:

```bash
git add tests TEST_PLAN.md
git commit -m "Add boundary tests for time parsing"
git push -u origin HEAD
```

Bei jedem Push führt GitHub Actions automatisch eure reguläre Testsuite gegen die
Referenzimplementierung aus.

## 6. Mutation Test Arena

Wenn die regulären Tests grün sind, kann die Arena manuell gestartet werden:

1. Öffne in **Deinem Fork** den Tab **Actions**.
2. Falls GitHub danach fragt, aktiviere Actions für den Fork.
3. Wähle **Mutation Test Arena**.
4. Klicke auf **Run workflow**.
5. Wähle den Branch, auf dem deine aktuellen Tests liegen.
6. Starte den Workflow.

Die Arena prüft zuerst noch einmal die korrekte Referenzimplementierung. Lehnen deine
Tests bereits diese Implementierung ab, wird die Arena abgebrochen.

Danach werden deine Tests gegen zehn unbekannte fehlerhafte Implementierungen ausgeführt.
Danach erhält man beispielsweise:

```text
M001: killed
M002: survived
M003: killed
...

Score: 7 / 10 faulty implementations detected
```

- **killed** bedeutet: Mindestens ein Test hat die fehlerhafte Variante erkannt.
- **survived** bedeutet: Die fehlerhafte Variante erfüllt Ihre aktuelle Testsuite noch.

Ein hoher Score entsteht nicht dadurch, dass möglichst viele fast identische Tests
schreiben. Suche stattdessen nach unterschiedlichen Fehlermöglichkeiten.

### Wichtig zur Arena

Das Arena-Repository ist aus technischen Gründen öffentlich. Die Varianten sind dort
nur mit IDs wie `M001` bezeichnet und bewusst nicht Teil dieses Repositories.

Bitte schaut während der Challenge nicht in deren Implementierungen. Technisch wäre
das möglich, macht die Idee dieses Praktikums aber zunichte.

## 7. Iterieren

Nach einem Arena-Lauf:

1. Welche Fehlerklasse konnte die Testsuite noch nicht abdecken?
3. Ergänze oder verbessere einen Test.
4. Committen und pushen der Änderung.
5. Starte die Arena erneut.

Das Ziel ist nicht nur ein Score, sondern dass man erklären kann, **warum** die eigenen Tests
ein bestimmtes Verhalten prüfen.
