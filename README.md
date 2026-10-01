# QuellPass

[TextPass & QuellPass — Olaf Wulf](https://olwulf-commits.github.io/)

Deutsch · [English](README.en.md)

QuellPass von Olaf Wulf recherchiert prüfbare Fragen mit einer unabhängigen Gegenfrage, Originalquellenprüfung und einer Belegakte. Nach dem Beleggate kann auf Auftrag ein lesbarer Forschungsbericht entstehen; ein Artikel oder anderer Textentwurf bleibt ein eigener Schritt aus freigegebenen Aussagen. Das Plugin ist modell- und suchanbieterneutral.

Mein Ziel ist, die Qualität von Texten mit vergleichsweise einfachen Mitteln deutlich zu verbessern. QuellPass macht Aussagen und Quellen prüfbar; TextPass arbeitet anschließend an Sprache und Lesefluss. Beides bleibt für Menschen nachvollziehbar und korrigierbar. Wie gut das im Alltag gelingt, müssen konkrete Texte zeigen. Ein [dokumentierter Bargeld-Test](FALLSTUDIE_BARGELD.md) zeigt einen bewusst umgekehrten Ablauf mit QuellPass vor dem Artikel und benennt auch seine Grenzen.

Mein Ansatz versteht Evaluation als Arbeit am Vorhandenen: Ich prüfe, was bereits trägt und wo Aussagen besser belegt werden müssen, und nutze diese Erkenntnisse für die weitere Arbeit. „Evaluieren“ heißt [bewerten](https://www.duden.de/rechtschreibung/evaluieren); das Wort führt über das Französische auf lateinisch [*valere*](https://www.etymonline.com/word/evaluation) („wert sein“) zurück. Bei der formativen Evaluation dienen Befunde dazu, mögliche Verbesserungen abzuleiten. QuellPass macht dafür Beleglücken sichtbar und hilft, Aussagen auf tragfähigere Quellen zu stützen.

Dieses Repository enthält die **allgemeine** Fassung für Codex, Cursor und Claude Code. Alle drei nutzen denselben [Skill](plugins/quellpass/skills/quellpass/SKILL.md) und dasselbe [Recherche- und Textprotokoll](plugins/quellpass/skills/quellpass/references/protokoll.md). Projektspezifische Anbindungen sind nicht enthalten.

Codex findet den Katalog unter `.agents/plugins/marketplace.json`. Cursor kann das portable Plugin lesen; für den Repository-Import liegt zusätzlich `.cursor-plugin/marketplace.json` bereit. Claude Code findet seinen Katalog unter `.claude-plugin/marketplace.json`. Das öffentliche Repository kann in Claude Code mit `claude plugin marketplace add olwulf-commits/quellpass` eingebunden und danach mit `claude plugin install quellpass@quellpass` installiert werden. Version 0.3.1 ist lokal aus diesem Repository in Codex installiert und mit ihren Quellen abgeglichen. Der Claude-Installationsweg ist hier nicht praktisch geprüft.

Die zwei Suchspuren brauchen tatsächlich getrennte Kontexte, wenn ihre Unabhängigkeit behauptet werden soll. Für den vollständigen Ablauf müssen auch Quellenprüfung und Textgegenprüfung eigene Kontexte erhalten. In Claude Code können diese vier Aufgaben an getrennte Subagenten gehen. In Codex können vier Subagenten eingesetzt werden, sofern die verwendete Umgebung sie unterstützt. In Cursor können vier Subagenten mit jeweils eigenem Kontext eingesetzt werden. Fehlt die Trennung in einem Werkzeug, darf der Lauf keine unabhängige Gegenprüfung behaupten. Das optionale lokale Werkzeug [semantic_feedback.py](plugins/quellpass/scripts/semantic_feedback.py) sortiert bereits abgerufene Seitenabschnitte; für seinen CLI-Aufruf wird `fastembed` und ein lokal verfügbares Embedding-Modell benötigt. Es führt keine Websuche aus. Die ausführende Umgebung muss ein Websuchwerkzeug und lesbaren Zugriff auf Originalquellen bereitstellen. Fehlen diese Voraussetzungen, muss der Lauf seine Grenzen nennen.

## Datenschutz und externe Suchanfragen

Für die Recherche sendet das Suchwerkzeug der verwendeten KI-Anwendung Suchbegriffe an die jeweils eingesetzten Suchmaschinen oder Suchdienste; beim Öffnen von Originalquellen werden die betreffenden Websites aufgerufen. QuellPass hat keine eigenen MCP-Server oder fest angebundenen Suchdienste. Die ausführende Umgebung bestimmt die Anbieter. Persönliche Angaben und vertrauliche Textpassagen gehören nicht in externe Suchanfragen. Olaf Wulf erhält keine Nutzungsdaten aus dem Pluginbetrieb. Belegakten können in der Nutzerumgebung gespeichert werden. Einzelheiten stehen im [Datenschutzhinweis](PRIVACY.md).

## Lizenz

Skilltext, README und Referenztexte stehen unter [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Das Python-Werkzeug und die technischen Paketdateien stehen unter der MIT License. Die genaue Zuordnung und die Lizenztexte stehen in [LICENSE.md](LICENSE.md). Eigene Rechercheberichte und mit dem Plugin erstellte Texte erhalten dadurch keine QuellPass-Lizenz.

## Mithelfen

Tests und konkrete Verbesserungsvorschläge sind willkommen. Wer Zugriff auf das Repository hat, kann dafür einen [Testbericht auf GitHub](https://github.com/olwulf-commits/quellpass/issues/new/choose) anlegen. Die Vorlage fragt nach Werkzeug, Version, Beispiel und beobachtetem Ergebnis. Auch ein gelungener Test hilft mir. Ich prüfe die Rückmeldungen und entscheide, was an der offiziellen Fassung geändert wird.

Das Repository ist auf Olafs Freigabe öffentlich zugänglich. Die Sprach-/Strukturrecherche vom 30. September 2026 mit QuellPass ist dokumentiert; eine vollständige hostübergreifende Erprobung dieser eingefrorenen allgemeinen Fassung wird nicht behauptet. Die Bereitstellung auf GitHub ist keine Aufnahme in ein offizielles Anbieter-Verzeichnis und keine Qualitätsgarantie.
