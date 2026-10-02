# QuellPass

[TextPass & QuellPass — Olaf Wulf](https://olwulf-commits.github.io/)

Deutsch · [English](README.en.md)

QuellPass von Olaf Wulf recherchiert prüfbare Fragen mit einer unabhängigen Gegenfrage, Originalquellenprüfung und einer Belegakte. Im üblichen Artikelablauf folgt QuellPass auf die gewöhnliche Recherche und den mit TextPass geschriebenen Artikel: Er prüft dessen Aussagen und Originalquellen. Bei einem ausdrücklich vorgezogenen QuellPass-Rechercheauftrag kann nach dem Beleggate auf Auftrag ein lesbarer Forschungsbericht oder später ein Artikel entstehen. Das Plugin ist modell- und suchanbieterneutral.

Mein Ziel ist, die Qualität von Texten mit vergleichsweise einfachen Mitteln deutlich zu verbessern. Nach der ersten Recherche schreibt TextPass den Artikel; QuellPass prüft danach seine Aussagen und Quellen. Nicht getragene Stellen werden korrigiert, bevor der ganze Text einen abschließenden Stil- und Strukturpass erhält. Beides bleibt für Menschen nachvollziehbar und korrigierbar. Wie gut das im Alltag gelingt, müssen konkrete Texte zeigen. Ein [dokumentierter Bargeld-Test](FALLSTUDIE_BARGELD.md) zeigt einen bewusst umgekehrten Ablauf mit QuellPass vor dem Artikel und benennt auch seine Grenzen.

Mein Ansatz versteht Evaluation als Arbeit am Vorhandenen: Ich prüfe, was bereits trägt und wo Aussagen besser belegt werden müssen, und nutze diese Erkenntnisse für die weitere Arbeit. „Evaluieren“ heißt [bewerten](https://www.duden.de/rechtschreibung/evaluieren); das Wort führt über das Französische auf lateinisch [*valere*](https://www.etymonline.com/word/evaluation) („wert sein“) zurück. Bei der formativen Evaluation dienen Befunde dazu, mögliche Verbesserungen abzuleiten. QuellPass macht dafür Beleglücken sichtbar und hilft, Aussagen auf tragfähigere Quellen zu stützen.

Dieses Repository enthält die **allgemeine** Fassung für Codex, Cursor, Claude Code und Grok Build. Hermes Agent kann sie zusätzlich als externe Skillquelle laden. Alle vier nutzen denselben [Skill](plugins/quellpass/skills/quellpass/SKILL.md) und dasselbe [Recherche- und Textprotokoll](plugins/quellpass/skills/quellpass/references/protokoll.md). Projektspezifische Anbindungen sind nicht enthalten.

Codex findet den Katalog unter `.agents/plugins/marketplace.json`. Cursor kann das portable Plugin lesen; für den Repository-Import liegt zusätzlich `.cursor-plugin/marketplace.json` bereit. Claude Code findet seinen Katalog unter `.claude-plugin/marketplace.json`. Das öffentliche Repository kann in Claude Code mit `claude plugin marketplace add olwulf-commits/quellpass` eingebunden und danach mit `claude plugin install quellpass@quellpass` installiert werden. Diese öffentliche Fassung trägt Version 0.3.3. Der vorherige Stand 0.3.1 war lokal in Codex installiert und mit seinen Quellen abgeglichen; ein praktischer Lauf von 0.3.3 steht noch aus. Der Claude-Installationsweg ist hier nicht praktisch geprüft.

Für Grok Build ist `.grok-plugin/marketplace.json` als öffentlicher Repository-Katalog vorbereitet. Nach dem GitHub-Nachzug lässt sich das Repository mit `grok plugin marketplace add olwulf-commits/quellpass` hinzufügen; der Skill wird erst nach eigener Installation aktiv. Der neue Katalog wurde noch nicht praktisch in Grok Build getestet und ist kein Eintrag im offiziellen xAI-Verzeichnis.

Für Hermes Agent das Repository klonen und in `~/.hermes/config.yaml` unter `skills.external_dirs` den absoluten Pfad `plugins/quellpass/skills` innerhalb des Klons eintragen. Der vollständige Klon hält auch die Referenzen an ihren relativen Pfaden bereit. Hermes unterstützt [Grok als Modellanbieter](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md); damit ist keine Aufnahme in Grok Build oder grok.com verbunden. Die öffentliche Fassung 0.3.3 wurde in Hermes mit Grok noch nicht praktisch getestet. Siehe die [Hermes-Anleitung für externe Skills](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md#external-skill-directories).

Die zwei Suchspuren brauchen tatsächlich getrennte Kontexte, wenn ihre Unabhängigkeit behauptet werden soll. Für den vollständigen Ablauf müssen auch Quellenprüfung und Textgegenprüfung eigene Kontexte erhalten. In Claude Code können diese vier Aufgaben an getrennte Subagenten gehen. In Codex können vier Subagenten eingesetzt werden, sofern die verwendete Umgebung sie unterstützt. In Cursor können vier Subagenten mit jeweils eigenem Kontext eingesetzt werden. Fehlt die Trennung in einem Werkzeug, darf der Lauf keine unabhängige Gegenprüfung behaupten. Die ausführende Umgebung muss ein Websuchwerkzeug und lesbaren Zugriff auf Originalquellen bereitstellen. Fehlen diese Voraussetzungen, muss der Lauf seine Grenzen nennen.

## Datenschutz und externe Suchanfragen

Für die Recherche sendet das Suchwerkzeug der verwendeten KI-Anwendung Suchbegriffe an die jeweils eingesetzten Suchmaschinen oder Suchdienste; beim Öffnen von Originalquellen werden die betreffenden Websites aufgerufen. QuellPass hat keine eigenen MCP-Server oder fest angebundenen Suchdienste. Die ausführende Umgebung bestimmt die Anbieter. Persönliche Angaben und vertrauliche Textpassagen gehören nicht in externe Suchanfragen. Olaf Wulf erhält keine Nutzungsdaten aus dem Pluginbetrieb. Belegakten können in der Nutzerumgebung gespeichert werden. Einzelheiten stehen im [Datenschutzhinweis](PRIVACY.md).

## Lizenz

Skilltext, README und Referenztexte stehen unter [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Die technischen Paketdateien stehen unter der MIT License. Die genaue Zuordnung und die Lizenztexte stehen in [LICENSE.md](LICENSE.md). Eigene Rechercheberichte und mit dem Plugin erstellte Texte erhalten dadurch keine QuellPass-Lizenz.

## Mithelfen

Tests und konkrete Verbesserungsvorschläge sind willkommen. Wer Zugriff auf das Repository hat, kann dafür einen [Testbericht auf GitHub](https://github.com/olwulf-commits/quellpass/issues/new/choose) anlegen. Die Vorlage fragt nach Werkzeug, Version, Beispiel und beobachtetem Ergebnis. Auch ein gelungener Test hilft mir. Ich prüfe die Rückmeldungen und entscheide, was an der offiziellen Fassung geändert wird.

Das Repository ist auf Olafs Freigabe öffentlich zugänglich. Die Sprach-/Strukturrecherche vom 30. September 2026 mit QuellPass ist dokumentiert; eine vollständige hostübergreifende Erprobung dieser eingefrorenen allgemeinen Fassung wird nicht behauptet. Die Bereitstellung auf GitHub ist keine Aufnahme in ein offizielles Anbieter-Verzeichnis und keine Qualitätsgarantie.
