## Les 4: gebruikers, headers en cookies

Elke gebruiker van een dynamische website kan pagina's krijgen die voor hem of haar aangepast zijn. Een voorbeeld is een webwinkel: elke gebruiker heeft zijn eigen winkelmandje, en misschien aanbiedingen die daaraan gekoppeld zijn. Maar hoe weet een server met welke gebruiker deze te maken heeft, bij een http-request? 
Deze informatie moet afkomstig zijn van de browser. Een omslachtige mogelijkheid is om een gebruiker voor elke pagina te vragen een formulier in te vullen met zijn gegevens. Maar browsers hebben hiervoor een handiger voorziening: *cookies*.

Een cookie heeft een naam en een waarde; beide zijn string-waarden. De server kan een cookie opsturen naar de browser. De browser stuurt de cookies van die server (eigenlijk van dat domein) bij elk verzoek mee naar de server, in de vorm van een *header*.

### Headers in http-request en http-response

Een http-request bevat naast de URL en eventuele parameters en extra gegevens, een aantal headers met informatie voor de server.

Een http-response bevat naast de status (200 OK, 404 not found, enz.) en de eigenlijke data (het html-document), een aantal headers met informatie voor de browser.

Je kunt deze request-headers en repsonse-headers bekijken met de ontwikkeltools van de browser. Je kunt aan de hand van de request-headers bijvoorbeeld zien welke browser gebruikt wordt, op welk operating system.

### Headers (en cookies) in web.py

Hoe kun je in web.py de header-informatie van een request vinden?

`web.ctx.env['HTTP_USER_AGENT']`

[see](http://webpy.org/cookbook/ctx)

Hoe kun je de header-informatie van een response invullen?

* met behulp van `web.header(name, value)` kun je de waarde van een header invullen. De http-standaard definieert een aantal header-namen, zie verderop.
* 

Voor de mogelijke headers en hun betekenis, zie bijvoorbeeld: 

#### Cookies

* [see web.py - cookies](http://webpy.org/cookbook/cookies)
* `setcookie(name, value, expires="", domain=None, secure=False)`
* `foo = web.cookies(cookieName=defaultValue)`

Opdracht: gebruik cookies om de naam van de gebruiker te onthouden. Deze wordt getoond in de pagina die de gebruiker te zien krijgt.

(In het overzicht van de header-namen worden `Set-cookie` en `Cookie` niet genoemd. Beide hebben een lijst van `name=value` paren, gescheiden door `;`.

(Soms worden de cookies tot de headers gerekend, soms ook niet. In de browser-tools hebben deze meestal een aparte positie. Hoe zit dat met de header-informatie in web.py?)

### Gebruikers (users)



### Sessies (sessions)

Cookies worden vaak gebruikt om de gegevens van een sessie bij te houden. Web.py heeft voor deze speciale vorm van gebruik extra voorzieningen.

Sessie-informatie wordt ook lokaal op de server opgeslagen, in een bestand of in een database. (*Waarom?*)
