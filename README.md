# QuellPass

QuellPass von Olaf Wulf recherchiert prüfbare Fragen mit einer unabhängigen Gegenfrage, Originalquellenprüfung und einer Belegakte. Nach dem Beleggate kann auf Auftrag ein lesbarer Forschungsbericht entstehen; ein Artikel oder anderer Textentwurf bleibt ein eigener Schritt aus freigegebenen Aussagen. Das Plugin ist modell- und suchanbieterneutral.

Mein Ziel ist, die Qualität von Texten mit vergleichsweise einfachen Mitteln deutlich zu verbessern. QuellPass macht Aussagen und Quellen prüfbar; TextPass arbeitet anschließend an Sprache und Lesefluss. Beides bleibt für Menschen nachvollziehbar und korrigierbar. Wie gut das im Alltag gelingt, müssen konkrete Texte zeigen.

Mein Ansatz versteht Evaluation als Arbeit am Vorhandenen: Ich prüfe, was bereits trägt und wo Aussagen besser belegt werden müssen, und nutze diese Erkenntnisse für die weitere Arbeit. „Evaluieren“ heißt [bewerten](https://www.duden.de/rechtschreibung/evaluieren); das Wort führt über das Französische auf lateinisch [*valere*](https://www.etymonline.com/word/evaluation) („wert sein“) zurück. Bei der formativen Evaluation dienen Befunde dazu, mögliche Verbesserungen abzuleiten. QuellPass macht dafür Beleglücken sichtbar und hilft, Aussagen auf tragfähigere Quellen zu stützen.

Dieses Repository enthält die **allgemeine** Fassung für Codex, Cursor und Claude Code. Alle drei nutzen denselben [Skill](plugins/quellpass/skills/quellpass/SKILL.md) und dasselbe [Recherche- und Textprotokoll](plugins/quellpass/skills/quellpass/references/protokoll.md). Projektspezifische Anbindungen sind nicht enthalten.

Codex findet den Katalog unter `.agents/plugins/marketplace.json`. Cursor kann das portable Plugin lesen; für den Repository-Import liegt zusätzlich `.cursor-plugin/marketplace.json` bereit. Claude Code findet seinen Katalog unter `.claude-plugin/marketplace.json`. Wer Zugriff auf das private Repository hat, kann es in Claude Code mit `claude plugin marketplace add olwulf-commits/quellpass` einbinden und danach `claude plugin install quellpass@quellpass` ausführen. Eine Installation aus diesem Repository wurde in keinem der drei Werkzeuge geprüft.

Die zwei Suchspuren brauchen tatsächlich getrennte Kontexte, wenn ihre Unabhängigkeit behauptet werden soll. Für den vollständigen Ablauf müssen auch Quellenprüfung und Textgegenprüfung eigene Kontexte erhalten. In Claude Code können diese vier Aufgaben an getrennte Subagenten gehen. In Codex können vier Subagenten eingesetzt werden, sofern die verwendete Umgebung sie unterstützt. In Cursor können vier Subagenten mit jeweils eigenem Kontext eingesetzt werden. Fehlt die Trennung in einem Werkzeug, darf der Lauf keine unabhängige Gegenprüfung behaupten. Das optionale lokale Werkzeug [semantic_feedback.py](plugins/quellpass/scripts/semantic_feedback.py) sortiert bereits abgerufene Seitenabschnitte; für seinen CLI-Aufruf wird `fastembed` und ein lokal verfügbares Embedding-Modell benötigt. Es führt keine Websuche aus. Die ausführende Umgebung muss ein Websuchwerkzeug und lesbaren Zugriff auf Originalquellen bereitstellen. Fehlen diese Voraussetzungen, muss der Lauf seine Grenzen nennen.

## Lizenz

Skilltext, README und Referenztexte stehen unter [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Das Python-Werkzeug und die technischen Paketdateien stehen unter der MIT License. Die genaue Zuordnung und die Lizenztexte stehen in [LICENSE.md](LICENSE.md). Eigene Rechercheberichte und mit dem Plugin erstellte Texte erhalten dadurch keine QuellPass-Lizenz.

## Mithelfen

Tests und konkrete Verbesserungsvorschläge sind willkommen. Wer Zugriff auf das Repository hat, kann dafür einen [Testbericht auf GitHub](https://github.com/olwulf-commits/quellpass/issues/new/choose) anlegen. Die Vorlage fragt nach Werkzeug, Version, Beispiel und beobachtetem Ergebnis. Auch ein gelungener Test hilft mir. Ich prüfe die Rückmeldungen und entscheide, was an der offiziellen Fassung geändert wird.

Das Repository ist privat. Ein vollständiger Recherchelauf wurde mit dieser bereinigten Fassung noch nicht geprüft. Über eine öffentliche Freigabe ist noch nicht entschieden.
