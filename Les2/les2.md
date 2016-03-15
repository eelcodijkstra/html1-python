## Les 2: formulieren en het afhandelen daarvan

In deze opdracht ga je oefenen met html-formulieren, en met het afhandelen daarvan door de server. Deze afhandeling is hier nog erg eenvoudig: je stuurt de informatie uit het formulier terug naar de browser.

Een volgende stap is om de informatie uit het formulier te gebruiken voor het aanpassen van de inhoud van een webpagina. Daarvoor maken we gebruik van *templates*.


### HTML formulier

Een HTML-formulier is een onderdeel van een HTML-document bedoeld voor interactie met de gebruiker; de informatie die de gebruiker opgeeft in het formulier wordt opgestuurd naar de server.

Een HTML-document kan meerdere formulieren bevatten.

We leggen de structuur en werking van een formulier uit aan de hand van een eenvoudig voorbeeld. (Dit voorbeeld geeft niet de volledige mogelijkheden en onderdelen van formulieren weer.)

```
<form action="myform" method="GET">
  x: <input  name="x" value="123">
  y: <input ... name="y" value="hi">
  <button type="submit">Send</button>
</form>
```

Een formulier kan ook allerlei andere elementen bevatten, bijvoorbeeld om aan te geven wat de betekenis is van de input-elementen.

De gebruikelijke gang van zaken is:

1. de gebruiker vult de input-velden van het formulier in, bijvoorbeeld: voor x de waarde `345`, voor y: `hallo`.
2. de gebruiker klikt op de submit-knop
3. de browser stuurt het formulier op, met de volgende gegevens:
    * request-type: `GET`
    * url: `myform`
    * query-parameters: `x=345&y=hallo` (wat de gebruiker ingevuld heeft)
    * totaal: `GET myformurl?x=345&y=hallo`
4. de server handelt dit verzoek af, aan de hand van deze gegevens
    * eventueel werkt de server de "persistent state" bij, bijvoorbeeld in een database;
    * de server stuurt een HTML-document als antwoord (response) naar de browser;
5. de browser geeft het ontvangen HTML-document weer.

Opmerkingen:

* de `method` kan zowel `GET` als `POST` zijn. Als je alleen gegevens opvraagt van de server, dan is `GET` gebruikelijk. Je gebruikt `POST` als het de bedoeling is dat de server iets bewaart van de gegevens uit het request. We komen hier later op terug.
* de parameter-waarde die overgedragen wordt aan de server, is altijd een *strings*, ook al is deze afkomstig van bijvoorbeeld een number-input element. Je moet in de server die string dan eventueel weer omzetten in een getal, een boolean waarde, een datum, enz.

We hebben als oefening een eenvoudige webpagina gemaakt met een formulier. De webserver handelt het verzoek af dat binnenkomt als dit formulier ingevuld en opgestuurd wordt ("submit").

Opdracht: breidt de webpagina uit: voeg een tweede formulier toe aan deze webpagina.
 
