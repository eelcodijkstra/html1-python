## Les 7: identificatie en authenticatie

De eerste stap die we in de vorige les(sen) gemaakt hebben is dat een gebruiker kan aangeven wie hij is (identificatie). Als deze identificatie toegang geeft tot vertrouwelijke gegevens, dan combineren we deze vaak met authenticatie: de gebruiker moet duidelijk kunnen maken dat hij het echt ("authentiek") is. Een veelgebruikte vorm daarvoor is het wachtwoord: een geheim dat alleen de gebruiker kent (en degene die het moet controleren), en dat niet eenvoudig geraden kan worden door anderen.


### Over authenticatie en autorisatie

Er zijn nog andere vormen van authenticatie, zowel in combinatie met computers, als in de wereld daarbuiten. Denk bijvoorbeeld aan een paspoort of identiteitskaart; een bankpas in combinatie met een pincode.

Wachtwoorden zijn steeds minder betrouwbaar: deze kunnen steeds gemakkelijker door compputers geraden worden. Alternatieven zijn bijvoorbeeld: combineren van twee of meer  verschillende methodes (two-factor authentication, enz.); gebruik van certificaten - in combinatie met public-key encryption; het gebruik van biometrische gegevens (vingerafdruk, irisscan, stemherkenning);

* de persoon (of organisatie) heeft iets (unieks)
* 

Vaak heeft een gebruiker die zich geïdentificeerd en geauthenticeerd heeft, bepaalde rechten: hij is *geautoriseerd* - bijvoorbeeld om bepaalde gegevens in te zien of te wijzigen, om geld op te nemen (betaalpas), enz. Het verlenen van dergelijke rechten noemen we *autorisatie*.

In het geval van een twee-weg commununicatie is eigenlijk de authenticatie van beide partijen nodig. Voordat je je wachtwoord verstuurd naar een server, wil je wel zeker weten dat dit inderdaad de server is die je bedoelt. Als je inlogt op de webpagina van je bank, moet je eerst wel nagaan dat dit inderdaad de website is van je bank - en niet een website die heel erg lijkt op de website van je bank.

Voor de authenticatie van een webserver maakt de browser gebruik van *certificaten*.

## inloggen: primitieve, onveilige aanpak

Via de login-pagina kan een gebruiker inloggen.

We geven hiervan twee voorbeelden. In het eerste voorbeeld gebruiken we een normaal formulier voor de gebruikersnaam en het wachtwoord. Aan de hand van de gebruikersnaam wordt de gebruiker in de database opgezocht, en wordt het opgegeven wachtwoord vergeleken met het wachtwoord in de database.

Een nieuwe gebruiker kan zich ook aanmelden via een apart formulier. Hierbij geeft hij zijn gebruikersnaam en wachtwoord op.

## inloggen: http authenticatie

De methode die we hierboven gebruikt hebben is niet zo veilig:

* het is niet verstandig om wachtwoorden zonder encryptie op te slaan in een database. Als deze database op de een of andere manier "op straat komt te liggen", zijn direct alle gebruikersgegevens toegankelijk. Door het opslaan van gecodeerde wachtwoorden kan dit aanzienlijk lastiger gemaakt worden.
* het is helemaal niet verstandig om wachtwoorden zonder encryptie over het internet te versturen. Een http-verbinding heeft, in tegenstelling tot een https-verbinding, geen encryptie: alle gegevens kunnen door de andere gebruikers van hetzelfde fysieke netwerk afgeluisterd worden.

Het gebruik van https is in dit geval de beste stap.

NB: ook Http Basic Authenticatie is niet veilig: de combinatie van gebruikersnaam en wachtwoord wordt verstuurd met een codering die eenvoudig te decoderen is, voor iedereen die deze combinatie kan ontvangen (bijvoorbeeld via een publiek WiFi netwerk).

## inloggen: opslaan van gecodeerde wachtwoorden

De eerste stap naar een veiliger oplossing is het opslaan van gecodeerde wachtwoorden. Voor deze codering maken we gebruik van  MD5 (via de library `hashlib`).

* zie: https://nl.wikipedia.org/wiki/MD5

Als alle wachtwoorden dezelfde hashfunctie gebruiken, kun je wachtwoorden raden door een woordenboek te maken van alle mogelijke wachtwoorden: als de hashwaarde gelijk is, is het wachtwoord ook gelijk. 

Dit probleem kun je voorkomen door het gebruik van "salt": je voegt dit toe voor het uitrekenen van de hashwaarde.

* zie: https://en.wikipedia.org/wiki/Salt_%28cryptography%29

## Opmerkingen

Hoe houd het systeem bij dat je ingelogd bent? Daarvoor moet er in elk geval iets bijgehouden worden aan de kant van de client (browser). Dit kan zijn:

* cookie
* header-informatie (in het geval van http-authenticatie)

Het cookie kan bijvoorbeeld de naam van de gebruiker bevatten, of een indicatie van de sessie. Aan de kant van de server kun je dan de eigenlijke administratie bijhouden. Daarvoor heb je persistente opslag nodig, in de vorm van een database, of in de vorm van een bestand in het filesysteem.

Als invariant hanteren we dat een userid in een URL aangeeft dat deze gebruiker ingelogd is?

(Kan een gebruiker via verschillende clients ingelogd zijn? Dit scenario is niet zo ver gezocht: sommige gebruikers hebben meerdere computers; of, wat een gebruiker is voor het systeem, kan in werkelijkheid een groep personen zijn.)
