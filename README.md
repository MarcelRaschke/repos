Wenn Sie Code im Editor eingeben, präsentiert Copilot Ihnen automatisch Codevorschläge im Editor, die Ihnen helfen, effizienter zu codieren.

    Öffnen Sie Visual Studio Code und erstellen Sie eine neue JavaScript-Datei calculator.js.

    Beginnen Sie in der JavaScript-Datei folgenden Code:

    class Calculator

Copilot schlägt automatisch eine Methode für unsere CalculatorKlasse in grau gedimmtem Text (Geistertext). In unserem Beispiel addund subtractEs werden Methoden vorgeschlagen. Die genauen Vorschläge, die Sie erhalten, können variieren.

Screenshot des VS Code-Editors, der Copilot zeigt, der die Methode in der Klasse vorschlägt.

Um den Vorschlag zu akzeptieren, drücken Sie die TabTab-Taste.

Gratulation! Sie haben gerade Ihren ersten KI-gestützten Inline-Vorschlag akzeptiert. Wenn Sie weiter tippen, aktualisiert Copilot den Inline-Vorschlag entsprechend.

Bei einer bestimmten Eingabe könnte es mehrere Vorschläge geben. Geben Sie den folgenden Code in der Klasse ein factorialMethode:

factorial(n) {

    Fahren Sie über den Vorschlag im Editor und bemerken Sie, dass es mehrere Vorschläge gibt.

    Screenshot des VS Code-Editors, der Copilot zeigt, wie er mehrere Vorschläge gibt, wenn er darüber schwebt.

    Sie können die Pfeilsteuerungen verwenden oder die Tastenkombinationen verwenden, um den nächsten (Alt+]) oder früheren (Alt+[) Vorschlag anzuzeigen.

KI-gestützte Code-Vervollständigungen können Ihnen bei der Erstellung von Kesselplatten oder sich wiederholendem Code helfen, sodass Sie im Entwicklerfluss bleiben und sich auf komplexere Codierungsaufgaben konzentrieren können.
Verwenden Sie Inline Chat, um einen Basis-Webserver zu generieren

Mit Copilot Chat können Sie ein Chat-Gespräch mit Copilot im VS Code beginnen, um bestimmte Aufgaben über Ihren Code zu fragen, indem Sie natürliche Sprache verwenden.

Verwenden wir Inline Chat, um einen einfachen Express-Webserver zu generieren.

    Zuerst fügen Sie eine neue TypeScript-Datei hinzu server.tszu Ihrem Arbeitsplatz.

    Drücken Sie nun Strg+I auf Ihrer Tastatur, um Copilot Inline Chat zu erstellen.

    Copilot Inline Chat bietet Ihnen eine Chat-Schnittstelle, mit der Sie Fragen zum Code im aktiven Editor stellen können.

    Screenshot des VS Code-Editors, der die Copilot Inline Chat-Steuerung zeigt.

    Geben Sie im Feld Chat-Eingangen Eingabe "einen einfachen Express-Webserver" ein und drücken Sie Enter, um die Eingabeaufforderung an Copilot zu senden.

    Beachten Sie, dass Copilot eine Streaming-Antwort im Editor zurückgibt. Die Antwort ist eine Implementierung für einen einfachen Node.js Express Webserver.

    Screenshot des VS Code Editors, der die Copilot Inline Chat-Antwort für das Hinzufügen eines Express-Webservers zeigt.

    Wählen Sie Akzeptieren oder drücken Sie Strg+Enter, um die vorgeschlagenen Codeänderungen anzuwenden.

    Gratulation! Sie haben Copilot Chat zum Generieren von Code mit Chat und natürlicher Sprache verwendet.

Refactor deinen Code durch KI-Chat

Sie können Inline Chat auch verwenden, um den vorhandenen Code im Editor zu reflektieren oder zu verbessern.

Beachten Sie, dass unser Webserver derzeit eine statische Portnummer verwendet 3000. Lassen Sie uns dies ändern, um eine Umgebungsvariable für die Portnummer zu verwenden.

    Wählen Sie im Editor 3000Portzahl im server.tsfile, und drücken Sie dann Strg+I, um Inline Chat zu starten.

    Geben Sie im Feld Chat-Eingabe "eine Umgebungsvariable für die Portnummer" ein und drücken Sie Enter, um die Chat-Anfrage oder Aufforderung zu senden.

    Beachten Sie, wie Copilot den bestehenden Code aktualisiert, um eine Umgebungsvariable für die Portnummer zu verwenden.

    Screenshot des VS Code Editors, der Inline Chat zeigt, dass er eine Umgebungsvariable für die Portnummer verwendet.

    Wählen Sie Akzeptieren oder drücken Sie Strg+Enter, um die vorgeschlagenen Codeänderungen anzuwenden.

    Wenn Sie mit einer vorgeschlagenen Änderung nicht zufrieden sind, können Sie die Aufforderung ändern und Copilot bitten, eine andere Lösung anzubieten.

    Zum Beispiel können Sie Copilot bitten, einen anderen Umgebungsvariablennamen für die Portnummer zu verwenden.

Verwenden Sie Copilot Chat für allgemeine Programmierfragen

Da Sie in einer neuen Codebasis arbeiten oder eine neue Programmiersprache erkunden, haben Sie vielleicht allgemeinere Kodierungsfragen. Mit Copilot Chat können Sie ein Chat-Gespräch an der Seite öffnen und die Geschichte Ihrer Fragen verfolgen.

    Öffnen Sie den Chat-Ansicht im Command Center Copilot Menü oder drücken Sie Strg+Alt+I.

    Screenshot des VS Code-Editors, der die Copilot-Chat-Ansicht zeigt und das Copilot-Menü im Command Center hervorhebt.

    Tipp

    Sie können jederzeit auf verschiedene Copilot-Funktionen aus dem Command Center-Menü zugreifen.

    Typ "Was ist Rekurs?" im Chat-Eingangsfeld und drücken Sie Enter, um die Anfrage an Copilot zu senden.

    Screenshot des VS Code-Editors, der die Copilot Chat-Ansicht zeigt, die die Antwort auf das enthält, was Rekursion ist. Das Ergebnis enthält Text und einen Codeblock.

    Beachten Sie, wie die Chat-Reaktion reiche Ergebnisse enthält, bestehend aus Text und einem Codeblock. Der Codeblock im Chat unterstützt IntelliSense, mit dem Sie Informationen über Methoden und Symbole erhalten können, indem Sie darüber schweben oder zu ihrer Definition gehen.

    Folgen Sie den Schritten im Copilot Chat Tutorial, um zu erfahren, wie Sie auch Copilot Chat verwenden können, um Fragen zu Ihrer spezifischen Codebasis zu stellen.

Bearbeiten Sie mehrere Dateien mit Copilot Edits

Größere Codeänderungen können Änderungen an mehreren Dateien beinhalten. Mit Copilot Edits erhalten Sie KI-gestützte Vorschläge im Editor über mehrere Dateien in Ihrem Arbeitsbereich. Anstatt einzelne Codeblöcke anzuwenden, erledigt Copilot Edits Änderungen in Ihrem Arbeitsbereich.

Mit Copilot Edits können wir den Inhalt einer HTML-Datei in einer Webserverantwort zurückgeben.

    Wählen Sie Open Copilot Edits im Command Center Copilot Menü oder drücken Sie Strg+Shift+I.

    Screenshot mit dem Copilot-Menü im Command Center, Hervorhebung des Open Edit Session-Elements

    Der Blick Copilot Edits wird geöffnet. Beachten Sie, dass server.tsDatei wird dem Auftrag gegeben.

    Copilot fügt den aktiven Editor automatisch zur Eingabeaufforderung hinzu. Wenn die Datei nicht hinzugefügt wird, verwenden Sie Dateien hinzufügen..., um die Datei manuell zum Lösungsmittel hinzuzufügen.

    Screenshot der Copilot Edits Ansicht, die das Eingabefeld mit der Datei anzeigt.

    Geben Sie eine statische HTML-Seite als Startseite zurück und implementieren Sie sie im Chat-Eingangsfeld und drücken Sie Enter, um eine neue Bearbeitungssitzung zu starten.

    Beachten Sie, dass Copilot Edits mehrere Änderungen vornimmt: Es aktualisiert die server.tsDatei, um eine statische HTML-Seite zurückzugeben, und sie fügt auch eine neue Datei hinzu index.html.

    Screenshot des VS Code-Editors, der die Copilot Edits-Antwort für die Rückgabe einer statischen HTML-Seite in der Webserver-Antwort zeigt.

    Wenn Sie mit den Ergebnissen zufrieden sind, wählen Sie Keep, um alle vorgeschlagenen Änderungen anzuwenden.

    Sie können auch zwischen den verschiedenen bearbeiteten Dateien navigieren und sie akzeptieren/lehnen, indem Sie die Editor-Overlay-Steuerelemente verwenden.

    Screenshot der Copilot Edits-Ansicht, die die Taste Keep markiert, um die Änderungen anzuwenden.

Fixe Codierungsfehler mit Copilot

Abgesehen von Inline-Abschlüssen und Chat-Gesprächen ist GitHub Copilot an verschiedenen Orten und in Ihrem gesamten Entwicklerfluss im VS Code verfügbar. Sie können das Vorhandensein von Copilot-Funktionalität durch das sparkleFunkensymbol in der VS Code-Benutzeroberfläche bemerken.

Ein solcher Ort ist die Copilot-Codierungsaktionen im Editor, wann immer Sie dort wegen eines Compilerfehlers einen roten Schnörkel haben. Mal sehen, wie Copilot bei der Lösung von Codierungsfehlern helfen kann.

    Öffnen Sie die server.tsTypScript-Datei, die Sie früher im Editor erstellt haben.

    Beachten Sie, dass import express from 'express';Die Aussage enthält ein rotes Schnickschnack. Wenn Sie den Cursor auf den roten Schnörkel legen, können Sie das Copilot-Glitzern sehen.

    Screenshot des VS Code-Editors, der den Copiloten wegen eines Fehlers mit der ausdrücklichen Importaussage zeigt.

    Wählen Sie das Funkeln aus, um die Copilot-Code-Aktionen anzuzeigen, und wählen Sie dann Fix mit Copilot.

    Screenshot des VS Code Editors, der die Copilot-Code-Aktionen zeigt, Hervorhebung .

    Beachten Sie, dass der Copilot Inline Chat kommt, vorbevölkert mit der Fehlermeldung und eine Lösung, um das Problem zu beheben.

    Screenshot des VS Code-Editors, der zeigt, wie der Copilot Inline Chat vorschlägt, das Express-Benpm-Paket zu installieren, um das Problem zu lösen.

    Direkt aus der Chat-Antwort können Sie optional die Schaltfläche Einfügen in Terminal auswählen, um den vorgeschlagenen Befehl in Ihrem Terminal zu kopieren.

Die nächsten Schritte

Herzlichen Glückwunsch, Sie haben jetzt künstliche Intelligenz verwendet, um Ihre Codierung zu verbessern! In diesem Tutorial haben Sie erfolgreich Copilot in VS Code eingerichtet und Copilot-Code-Vervollständigungen, Copilot-Chat und Code-Aktionen verwendet, um Ihnen zu helfen, effizienter zu codieren.

    Um mehr über Copilot Chat zu erfahren, gehen Sie zum Copilot Chat Tutorial.

    Um mehr über Copilot Edits zu erfahren, gehen Sie zur Copilot Edits Dokumentation.

Ähnliche Ressourcen
