## Aantekeningen bij html-1

## Lessen

* les 1: unplugged activiteit: naspelen van browser en server-interactie
* les 2: html-formulieren
* les 3: sjablonen (templates) voor web-pagina's
* les 4: gebruikers (en cookies)
* les 5: databases, todo's, 
* les 6: gebruikers en todo's
* les 7: identificatie en authenticatie
* les 8: (zelf uitwerken: een blog-website)
* les 9: (sessions)
* les 10:

Welke voorbeelden gebruiken we in de verschillende lessen?

* todo's
     * eerst: zonder users, globale lijst van todo's
     * dan: met users, lijst van todo's per gebruiker
     
Voor de globale lijst van todo's hebben we een database nodig, en een redelijk ontworpen interface.


"Connection refused" - mogelijk is de database-daemon niet actief.

Nog toevoegen:

* afhandelen van statische bestanden; css, enz.

NB: Les6 is nogal wat complexer dan de lessen daarvoor. De combinatie van gebruikers en todo-lijsten vraagt om nadere uitwerking.

* [x] klopt de representatie van "done" in de database? De representatie van "True" is een string, zoals deze uit het formulier komt. Deze moet omgezet worden in een Python boolean representatie.
* [ ] je kunt een Cursor-object maar eenmaal doorlopen: het is geen normale collectie. Moeten we daarom het Cursor-object eerst kopiëren?

Het omzetten van de formulier-representatie van "done" in de Python-representatie:

* de formulier-representatie van True is de aanwezigheid van het naam/waarde-paar: `done==True` in `web.input()`.; de waarde is altijd een string, in dit geval `"True"`. Een andere dan deze string kan op grond van het formulier niet voorkomen. (Maar: je kunt in principe nooit vertrouwen op de input van de browser. Een URL kan in elke willekeurige vorm aangemaakt worden.)
* de formulier-representatie van False is de *afwezigheid* van `"done"` in de naam/waarde-paren in `web.input()`.
* we kunnen de formulier-representatie dan omzetten in een boolean waarde met de constructie: `"done" in input.keys()`.
