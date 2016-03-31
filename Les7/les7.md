## Les 7: identificatie en authenticatie

De eerste stap die we in de vorige les(sen) gemaakt hebben is dat een gebruiker kan aangeven wie hij is (identificatie). Als deze identificatie toegang geeft tot vertrouwelijke gegevens, dan combineren we deze vaak met authenticatie: de gebruiker moet duidelijk kunnen maken dat hij het echt ("authentiek") is. Een veelgebruikte vorm daarvoor is het wachtwoord: een geheim dat alleen de gebruiker kent (en degene die het moet controleren), en dat niet eenvoudig geraden kan worden door anderen.


### Over authenticatie en autorisatie

Er zijn nog andere vormen van authenticatie, zowel in combinatie met computers, als in de wereld daarbuiten. Denk bijvoorbeeld aan een paspoort of identiteitskaart; een bankpas in combinatie met een pincode.

Wachtwoorden zijn steeds minder betrouwbaar: deze kunnen steeds gemakkelijker door compputers geraden worden. Alternatieven zijn bijvoorbeeld: combineren van twee of meer  verschillende methodes (two-factor authentication, enz.); gebruik van certificaten - in combinatie met public-key encryption; het gebruik van biometrische gegevens (vingerafdruk, irisscan, stemherkenning);

* de persoon (of organisatie) heeft iets (unieks)
* de persoon (of organisatie) weet iets (unieks)

Vaak heeft een gebruiker die zich geïdentificeerd en geauthenticeerd heeft, bepaalde rechten: hij is *geautoriseerd* - bijvoorbeeld om bepaalde gegevens in te zien of te wijzigen, om geld op te nemen (betaalpas), enz. Het verlenen van dergelijke rechten noemen we *autorisatie*.

> Is een sleutel (bijvoorbeeld van een huis) een voorbeeld van authenticatie of van autorisatie? Ik zou zeggen: het laatste, omdat de identiteit van de bezitter geen rol speelt. Aan een sleutel kun je niet zien wie deze bezit.

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

## Sessions

Een sessie is een min of meer aaneengesloten periode waarin een gebruiker gebruik maakt van een server (service). In sommige gevallen is de gebruiker expliciet bekend; in andere gevallen wordt gebruik gemaakt van de persistente data van de browser.

Er zijn verschillende manieren om een session bij te houden. In alle gevallen is het nodig om gebruik te maken van opslag aan de kant van de browser. Dit kan in de vorm van cookies, van authenticatie-headers, of via een van de andere vormen van lokale opslag (sessionStorage, localStorage, IndexedDB).

### Een eenvoudige aanpak

* we houden in de server een persistente administratie van sessions bij, in de database.
* we houden in de browser de key van de session bij (bijvoorbeeld via een cookie).
* een session kan op twee manieren verlopen: (i) door een time-out van het session-cookie in de browser; (ii) door een time-out aan de kant van de server.
    * mogelijk moeten we hieraan toevoegen: het uitloggen van de gebruiker. Dit kunnen we vorm geven door het session-cookie te overschrijven met een "lege" session.

We hanteren als invariant: er is alleen een session-cookie in de browser als de gebruiker ingelogd is.

Welke data houden we bij voor een session?

* de naam van de gebruiker (of de userid? dan weet je zeker dat deze in de DB voorkomt...)
* het begintijdstip van de sessie
* eventueel gegevens die de toepassing voor de session bij wil houden.
    * het gebruik van MongoDB maakt dit relatief eenvoudig.

### SessionStorage: niet persistent

Eén van de beschikbare manieren voor lokale opslag (in de browser) is "SessionStorage". De inhoud hiervan blijft bewaard zolang de browser aktief is; als de browser afgesloten wordt (bijvoorbeeld als de computer uitgezet wordt), dan verdwijnt de inhoud hiervan. Met andere woorden: "SessionStorage" is *niet persistent*.

> Het begrip "session" is hier een ander begrip dan dat we hier bespreken. "SessionStorage" heeft betrekking op de browser. De sessions die wij hier bespreken hebben betrekking op de relatie tussen de browser (en/of de gebruiker) en de server. Deze kan korter zijn, of langer, dan de periode van activiteit van de browser.


## Opmerkingen

Hoe houd het systeem bij dat je ingelogd bent? Daarvoor moet er in elk geval iets bijgehouden worden aan de kant van de client (browser). Dit kan zijn:

* cookie
* header-informatie (in het geval van http-authenticatie)

Het cookie kan bijvoorbeeld de naam van de gebruiker bevatten, of een indicatie van de sessie. Aan de kant van de server kun je dan de eigenlijke administratie bijhouden. Daarvoor heb je persistente opslag nodig, in de vorm van een database, of in de vorm van een bestand in het filesysteem.

Als invariant hanteren we dat een userid in een URL aangeeft dat deze gebruiker ingelogd is?

(Kan een gebruiker via verschillende clients ingelogd zijn? Dit scenario is niet zo ver gezocht: sommige gebruikers hebben meerdere computers; of, wat een gebruiker is voor het systeem, kan in werkelijkheid een groep personen zijn.)

### Controleren van input

De input van username/password kan op veel manieren foutgaan.

Kunnen we ervan uitgaan dat bepaalde velden gedefinieerd zijn in de input?

* ja - want we gebruiken een formulier;
* nee - want een url kan altijd gefabriceerd worden, buiten het formulier om.

Er is dus voor beide iets te zeggen.


### Reset van wachtwoorden

Als je wachtwoorden gebruikt, moet je ook voorzieningen hebben voor het veranderen van een wachtwoord, en voor het geval dat een gebruiker zijn wachtwoord vergeten is.

Wat dit laatste betreft: een veel-gebruikte methode is om van de gebruiker ook een mail-adres op te slaan. Als een gebruiker zijn wachtwoord vergeten is, kun je hem een nieuw wachtwoord toesturen. In veel gevallen is dit een eenmalig wachtwoord: een gebruiker moet dan zodra hij met dit eenmalige wachtwoord ingelogd heeft, een nieuw wachtwoord opgeven.

### Structuur van controles

Als je op veel input-condities moet controleren, kun je die geneste if-statements krijgen. Een alternatieve aanpak is om elke controle die faalt een directe "exit" te geven, bijvoorbeeld via een `return`. Je weet dan op een bepaald punt in de programmatekst dat alle voorgaande controles succesvol waren.

(Wat zeggen style-guides hierover? Persoonlijk geef ik hieraan de voorkeur, boven de diep-geneste if-statements. Hoe pak je dit aan in een functionele taal?)

### Aanpassen van de database

We hebben,op grond van de vorige lessen, een database waarin alleen gebruikersnamen voorkomen, en geen wachtwoorden. Voor het invoeren van wachtwoorden hebben we een andere structuur van de database nodig.

Een dergelijke situatie komt vaak voor bij het verder ontwikkelen van een toepassing: de structuur van de database moet aangepast worden.

In het geval van MongoDB kunnen we dit op verschillende manieren oplossen:

* we kunnen met een afzonderlijke toepassing ("update") de structuur van de database aanpassen volgens de nieuwe situatie;
* we kunnen in de toepassing zelf rekening houden met oude en nieuwe "record" (documenten) in de database.

### Gebruik van ObjectId

Er is een verschil tussen de string-waarde en de ObjectId-waarde. We moeten op sommige plaatsen expliciet een `ObjectId`-functie gebruiken voor de type-conversie.
Als we direct een element uit een MongoDB-document gebruiken gaat dit goed, maar zodra dit naar een string omgezet wordt - bijvoorbeeld via een html-pagina - gaat dit mis.

### Uitloggen

We moeten ook nog een opdracht toevoegen om uit te loggen.

### Gebruikers en REST

* hoe past het inloggen e.d. bij een REST interface?
* hoe kun je een API maken met een redelijke beveiliging?

