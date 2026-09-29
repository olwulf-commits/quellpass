# Deep Research Plugin

Deep Research von Olaf Wulf recherchiert prüfbare Fragen mit einer unabhängigen Gegenfrage, Originalquellenprüfung und einer Belegakte. Ein Textentwurf entsteht nur auf ausdrücklichen Auftrag aus freigegebenen Aussagen. Das Plugin ist modell- und suchanbieterneutral.

Dieses Repository enthält die **allgemeine** Codex-Fassung. Der private Arbeitsvertrag, persönliche Varianten und die Vitis-Prima-Anbindung sind nicht enthalten. Der Ablauf steht im [Skill](plugins/deep-research-plugin/skills/deep-research-plugin/SKILL.md) und im [Recherche- und Textprotokoll](plugins/deep-research-plugin/skills/deep-research-plugin/references/protokoll.md).

Die zwei Suchspuren brauchen tatsächlich getrennte Kontexte, wenn ihre Unabhängigkeit behauptet werden soll. Das optionale lokale Werkzeug `scripts/semantic_feedback.py` sortiert bereits abgerufene Seitenabschnitte; für seinen CLI-Aufruf wird `fastembed` und ein lokal verfügbares Embedding-Modell benötigt. Es führt keine Websuche aus. Die ausführende Umgebung muss ein Websuchwerkzeug und lesbaren Zugriff auf Originalquellen bereitstellen. Fehlen diese Voraussetzungen, muss der Lauf seine Grenzen nennen.

Das Repository ist noch privat. Installation aus diesem Repository, ein vollständiger Recherchelauf, Lizenz und öffentliche Freigabe sind noch nicht geprüft beziehungsweise entschieden. Es gibt noch keinen öffentlichen Release.
