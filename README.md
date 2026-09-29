# Deep Research Plugin

Deep Research von Olaf Wulf recherchiert prüfbare Fragen mit einer unabhängigen Gegenfrage, Originalquellenprüfung und einer Belegakte. Ein Textentwurf entsteht nur auf ausdrücklichen Auftrag aus freigegebenen Aussagen. Das Plugin ist modell- und suchanbieterneutral.

Unser Ziel ist, die Qualität von Texten mit vergleichsweise einfachen Mitteln deutlich zu verbessern. Deep Research macht Aussagen und Quellen prüfbar; TextPass arbeitet anschließend an Sprache und Lesefluss. Beides bleibt für Menschen nachvollziehbar und korrigierbar. Wie gut das im Alltag gelingt, müssen konkrete Texte zeigen.

Dieses Repository enthält die **allgemeine** Fassung für Codex, Cursor und Claude Code. Alle drei nutzen denselben [Skill](plugins/deep-research-plugin/skills/deep-research-plugin/SKILL.md) und dasselbe [Recherche- und Textprotokoll](plugins/deep-research-plugin/skills/deep-research-plugin/references/protokoll.md). Der private Arbeitsvertrag, persönliche Varianten und die Vitis-Prima-Anbindung sind nicht enthalten.

Codex findet den Katalog unter `.agents/plugins/marketplace.json`. Cursor kann das portable Plugin lesen; für den Repository-Import liegt zusätzlich `.cursor-plugin/marketplace.json` bereit. Claude Code findet seinen Katalog unter `.claude-plugin/marketplace.json`. Wer Zugriff auf das private Repository hat, kann es in Claude Code mit `claude plugin marketplace add olwulf-commits/deep-research-plugin` einbinden und danach `claude plugin install deep-research-plugin@deep-research` ausführen. Eine Installation aus diesem Repository wurde in keinem der drei Werkzeuge geprüft.

Die zwei Suchspuren brauchen tatsächlich getrennte Kontexte, wenn ihre Unabhängigkeit behauptet werden soll. Das optionale lokale Werkzeug `scripts/semantic_feedback.py` sortiert bereits abgerufene Seitenabschnitte; für seinen CLI-Aufruf wird `fastembed` und ein lokal verfügbares Embedding-Modell benötigt. Es führt keine Websuche aus. Die ausführende Umgebung muss ein Websuchwerkzeug und lesbaren Zugriff auf Originalquellen bereitstellen. Fehlen diese Voraussetzungen, muss der Lauf seine Grenzen nennen.

Das Repository ist privat. Ein vollständiger Recherchelauf wurde mit dieser Fassung noch nicht geprüft. Über die Lizenz und eine öffentliche Freigabe ist noch nicht entschieden.
