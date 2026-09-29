---
name: deep-research-plugin
description: Recherchiere eine prüfbare Frage mit semantisch gelesenen Webquellen, unabhängiger Gegenfrage und überprüften Originalen; erstelle auf ausdrücklichen Auftrag einen beleggebundenen Textentwurf. Für reine Meinungs- oder Kreativfragen ohne Tatsachenkern nicht verwenden.
---

# Deep Research Plugin

Lizenz dieses Skilltexts: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) · © 2026 Olaf Wulf. Bearbeitungen müssen als solche gekennzeichnet und unter derselben Lizenz weitergegeben werden. Die allgemeine Originalfassung liegt in diesem Repository.

Arbeite modell- und anbieterneutral. Die ausführende KI steuert den Ablauf und schreibt einen beauftragten Entwurf selbst. Recherche, Belegprüfung und Textgegenprüfung sind getrennte Aufgaben. Lies vor dem Lauf [das Recherche- und Textprotokoll](references/protokoll.md). Es setzt die Verfahrensgrenzen und erläutert die Durchführung.

## Auftrag und Gegenfrage

Halte vor der Suche die Frage im Wortlaut, deine Auslegung, eine plausible andere Lesart, den Stichtag, Geltungsbereich und den gewünschten Umfang fest. Frage die nutzende Person nicht routinemäßig nach dem Zweck. Wenn ein einzelnes System für Recherche und anschließenden Artikel gesucht ist, prüfe diesen durchgehenden Ablauf; empfehle nicht zwei getrennte Sieger als Antwort. Der Zweck darf die Recherche nicht auf ein Wunschergebnis festlegen.

Formuliere zu jeder tragenden Teilfrage eine **eigenständige Gegenfrage**. Ein dafür zuständiger Agent entwickelt sie nur aus der Ausgangsfrage und recherchiert sie in getrenntem Kontext, ohne Ergebnisse der bejahenden Suche zu sehen. Ein Nullergebnis nennt Gegenfrage und Suchwege; es wird kein Gegenargument erfunden.

## Vier spezialisierte Agenten

1. Spur A findet Belege für die prüfbare Ausgangsfrage.
2. Spur B formuliert und recherchiert unabhängig die Gegenfrage und sucht Einschränkungen oder Widerlegungen.
3. Der Belegprüfer verifiziert die Originaltexte, Belegstellen, Zahlen, Aktualität, Ersturheber, Dubletten und Widersprüche; er erstellt die Belegakte und das Gate-Urteil.
4. Der unabhängige Gegenprüfer greift den fertigen Bericht oder Entwurf an und gleicht jede Aussage rückwärts mit der Belegakte ab.

Die ausführende KI koordiniert und redigiert; sie ist keine fünfte unabhängige Prüfinstanz. Wenn die Umgebung keine vier wirklich getrennten Agentenkontexte erlaubt, benenne die Einschränkung und behaupte keine unabhängige Gegenprüfung.

## Suche und Belege

Prüfe bei jedem Recherchelauf vor der ersten Websuche die [deutschsprachigen Hochschulquellen](references/deutsche-hochschulen-fragenquellen.md). Spur A und Spur B wählen daraus jeweils unabhängig fachlich passende Einstiege und suchen mit dem verfügbaren Websuchwerkzeug in ihrer ersten Runde nach konkreten Originaltexten. Halte gewählte Einstiege und Suchanfragen fest. Gibt es keinen passenden Einstieg, suche in derselben ersten Runde offen im Web und vermerke den fehlenden Katalogtreffer. Auch bei einem Treffer suche nach weiteren und kritischen Quellen. Der Katalog ist weder ein Beleg noch eine Beschränkung auf Hochschulen; er schafft keine zusätzliche Frage, Rolle oder Suchrunde.

Führe in Spur A und B jeweils eine erste Websuche aus. Lies dabei identifizierbare Volltexte der Ersturheber oder gekennzeichnete offizielle Spiegel und vergleiche deren Abschnitte mit der jeweiligen Frage. Dafür kann [semantic_feedback.py](../../scripts/semantic_feedback.py) mit einem zur Laufzeit gewählten lokalen Embedding-Modell verwendet werden; die Bibliotheksfunktion akzeptiert auch einen anderen Embedding-Anschluss. Das Werkzeug sortiert bereits abgerufene Abschnitte und führt keine Websuche aus. Ein passender Abschnitt ist zunächst ein Hinweis; das Sortierwerkzeug stellt keinen Suchanlass fest. Nach den getrennten ersten Suchen prüft Agent C die Originale beider Spuren. Nur wenn ein Original fehlt, zwei gelesene Originale einander widersprechen oder eine Zahl ohne Rechnung steht, erhält die betroffene Spur eine **semantisch begründete Anschlussanfrage**. Benenne davor den Bezugspunkt: die Behauptung und ihre eindeutig bezeichnete Erstquelle, die zwei Originale oder die Zahlenbehauptung und ihre Messung beziehungsweise Datengrundlage. Ohne dieses Paar bleibt der Befund offen und es gibt keine zweite Suche. Entsteht der Anlass durch den Vergleich von A und B, ist die Anschlussrunde informiert und nicht mehr unabhängig. Dokumentiere auslösenden Abschnitt mit URL, Anlass, Bezugspunkt und neue Suchrichtung. Höchstens zwei Suchrunden pro Teilfrage; gleiche Treffer und Ersturheber zusammenführen. Kann der Vergleich oder eine durch Anlass und Bezugspunkt erforderliche Anschlussrunde nicht ausgeführt werden, kennzeichne die Pflicht als unerfüllt. Suchtreffer und Snippets sind Kandidaten, keine Belege.

Eine Aussage darf nur auf eine Quelle gestützt werden, wenn URL, tatsächlicher Abruf, Lesbarkeit, wörtliche Fundstelle und alle genannten Zahlen geprüft wurden. Fällt eine Quelle aus, fallen alle Aussagen, die nur sie trug. Herkunft und Unabhängigkeit der Quellen zählen mehr als die Zahl der Treffer.

## Ergebnis und Text

Gib zuerst eine kurze Antwort mit tragenden Belegen, Gegenbefunden und offenen Lücken, danach die prüfbare Belegakte. Trenne normative, empirische, attributive und kausale Aussagen. „Offen“ ist ein Befundzustand, kein viertes Gate-Urteil: Ohne Bezugspunkt oder bei ungeklärtem tragendem Widerspruch SPERREN für die betroffene Aussage; ÜBERARBEITEN nur bei konkret möglicher Korrektur aus vorhandenen Belegen; sonst FREIGEBEN nur für belegte Aussagen. Benenne Teilfreigaben ausdrücklich.

Schreibe einen Artikel oder anderen Entwurf nur, wenn er beauftragt und das Recherchegate bestanden ist. Stelle vor dem Schreiben für die geplanten Aussagen und Absätze drei Fragen: Ist die Behauptung konkret genug? Wird eine Unsicherheit ehrlich benannt? Dient dieser Absatz dem Zweck des Textes? Leite den Textzweck aus dem Auftrag ab; frage nicht routinemäßig nach dem Verwendungszweck der Recherche. Diese Textfragen eröffnen keine weitere Suche. Stil darf die belegte Substanz nicht erweitern. Der unabhängige Gegenprüfer stellt die drei Fragen am fertigen Text und bei jeder späteren Umschreibung erneut und gleicht die Aussagen mit der Belegakte ab. Externe Schreibvorgänge, Einpflegen und Veröffentlichung benötigen jeweils die dafür geltende ausdrückliche Freigabe; dieses Plugin erteilt keine Rechte.
