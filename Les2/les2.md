## Les 2: formulieren en het afhandelen daarvan

In deze opdracht ga je oefenen met html-formulieren en met het afhandelen daarvan door de server. We beginnen erg eenvoudig: de server stuurt de informatie uit het formulier terug naar de browser.

Een volgende stap is om de informatie uit het formulier te gebruiken voor het aanpassen van de inhoud van een webpagina. Daarvoor maken we gebruik van *templates*.


### HTML formulier

Een HTML-formulier is een onderdeel van een HTML-document bedoeld voor interactie met de gebruiker. De gebruiker vult het formulier is, en "submit" dit door op een knop te klikken. De browser stuur de informatie in het formulier op naar de server.

Een HTML-document kan meerdere formulieren bevatten.

We leggen de structuur en werking van een formulier uit aan de hand van een eenvoudig voorbeeld. (We gebruiken hier maar een deel van de mogelijkheden van formulieren.)

```
<form action="/form1" method="GET">
  x: <input type="text" name="x" value="..."> <br>
  y: <input type="number" name="y" value="123"> <br>
  <button type="submit">Submit</button>
</form>
```

Dit formulier bestaat uit:

* de form-attributen `action` en `method`, die aangeven op welke manier de browser de gegevens naar de server moet sturen.
* een aantal input-elementen; we gebruiken input-elementen van type `number` en van type `text`.
* html-elementen (hier de teksten `x:` en `y:`), bijvoorbeeld om de betekenis van de input-elementen aan te geven.
* een submit-button.

De gebruikelijke gang van zaken is:

1. de gebruiker vult de input-velden van het formulier in, bijvoorbeeld: voor x de waarde `345`, voor y: `hallo`.
2. de gebruiker klikt op de submit-knop
3. de browser stuurt het formulier op, met de volgende gegevens:
    * request-type: `GET`
    * url: `/form1`
    * query-parameters: `x=hallo&y=345` (wat de gebruiker ingevuld heeft)
    * totaal: `GET /form1?x=hallo&y=345`
4. de server handelt dit verzoek af, aan de hand van deze gegevens
    * eventueel werkt de server de "persistent state" bij, bijvoorbeeld in een database;
    * de server stuurt een HTML-document als antwoord (response) naar de browser;
5. de browser geeft het ontvangen HTML-document weer.

Opmerkingen:

* de `method` kan zowel `GET` als `POST` zijn. Als je alleen gegevens opvraagt van de server, dan is `GET` gebruikelijk. Je gebruikt `POST` als het de bedoeling is dat de server iets bewaart van de gegevens uit het request. We komen hier later op terug.
* de parameter-waarde die overgedragen wordt aan de server, is altijd een *strings*, ook al is deze afkomstig van bijvoorbeeld een number-input element. Je moet in de server die string dan eventueel weer omzetten in een getal, een boolean waarde, een datum, enz.
* bij een GET-opdracht geeft de browser de URL met de parameters weer in het URL-venster. Controleer dit.

We hebben als oefening een eenvoudige webpagina gemaakt met een formulier. De webserver handelt het verzoek af dat binnenkomt als dit formulier ingevuld en opgestuurd wordt ("submit").

*Opdracht:* breidt de webpagina uit, door een tweede formulier toe te voegen aan deze webpagina.

Merk op: je kunt ook parameters meegeven in een link.

### Afhandeling door de server

In deze lessen geven we een uitwerking van server-side scripting met behulp van Python. Je kunt veel andere talen en systemen gebruiken voor deze server-side scripting, bijvoorbeeld PHP, JavaScript (node.js), Java, Haskell, enz.

Je moet niet alleen een taal kiezen, maar ook een "framework" voor het organiseren van de server-side scripts. We gebruiken hier een eenvoudig Python-framework: *web.py* (zie webpy.org). Andere voorbeelden van Python frameworks voor webservers zijn Django en Flask; deze zijn wat complexer in het gebruik, maar geven meer mogelijkheden. Als je web.py begrijpt, kun je gemakkelijk de overstap naar die andere frameworks maken.

Je moet eerst aangeven dat je `web.py` gebruikt:

```
import web
```

Als volgende stap geef je op welke URLs gebruikt worden voor deze toepassing. We gebruiken hier 2 URLS: `"/"`, voor de home-pagina, en `"/form1"`, voor het eerste formulier. Per URL geef je aan door welke class dit afgehandeld wordt (zie verderop). `"/"` wordt afgehandeld door de class met naam `"Index"`, `"/form1"` wordt afgehandeld door de class `"Form1"`.

```
urls = (
    '/','Index',
    '/form1','Form1'
)
```

De volgende opdracht start de server-applicatie voor het afhandelen van de binnenkomende http-verzoeken:

```
app = web.application(urls, globals())
```

We nemen hier de volledige tekst van de html-pagina met het formulier op als een string in de Python-code. Later zullen we zien dat dit handiger kan:

```
pageHtml="""
<!doctype html>
  ...
</html>
"""
```

Voor het afhandelen van http-verzoeken voor de url "/" gebruiken we de class `Index`. Voor deze URL handelen we alleen GET-verzoeken af. Het resultaat van de functie `GET` is het antwoord op het verzoek (de *response*). In dit geval is dit de html-pagina met het formulier. 

```
class Index:
    def GET(self):
        return pageHtml
```

Voor het afhandelen van de verzoeken voor de url "/form1" gebruiken we de class `Form1`. Voor deze URL handelen we zowel de GET- als de POST-verzoeken af. In beide gevallen sturen we een simpele string met de ontvangen gegevens terug naar de browser.

Als laatste onderdeel zien we een constructie die je veel tegenkomt in Python: als deze Python-module gebruikt wordt als zelfstandig programma ("main"), dan wordt de functie `app.run()` aangeroepen. Dit gebeurt bijvoorbeeld als je de opdracht geeft: `python les2.py`.

```
if __name__=='__main__':
    app.run()
```
