## Les 5: persistentie en databases

De server moet de gegevens over de verschillende gebruikers bijhouden. Dit kan niet in de variabelen van het programma: elk http-request begint een nieuw proces, "met een schone lei". Gegevens die buiten een programma bestaan noemen we ook wel *persistente gegevens*. Voorbeelden hiervan zijn de bestanden in het filesysteem, of de data in een database.

In het geval van een webserver gebruiken we vaak een database voor de persistente data. Een database kan door meerdere programma's (processen) tegelijk gebruikt worden. Eventueel kan deze database op een andere computer staan (database server), die door meerdere weservers gebruikt kan worden.

Er zijn allerlei verschillende soorten databases in gebruik. Relationele databases worden het meest gebruikt, maar voor webtoepassingen worden steeds vaker ook NoSQL-databases toegepast. Een voorbeeld van een NoSQL-database is MongoDB. In deze les gebruiken we MongoDB om de persistente gegevens van de webserver bij te houden.

De wachtwoorden van de gebruikers moet je bij de server opslaan. Dit is een eerste voorbeeld van persistente data.

In dit voorbeeld maken we een todo-lijst, die we opslaan bij de server. In de eerste versie hiervan maken we nog geen onderscheid tussen gebruikers.

> In een volgende versie houden we een lijst bij per gebruiker. Moeten we de gebruiker dan ook vermelden in het REST-interface, of laten we dat impliciet - via de headers/cookies? Een argument voor het laatste is dat een gebruiker niet de todo van een andere gebruiker kan opvragen. Een argument tegen het laatste is dat we dan geen uniek interface hebben voor de afzonderelijke elementen.

### MongoDB

Voordat we een MongoDB database kunnen gebruiken, moeten we eerst de bijbehorende library importeren:

```
import pymongo
```

Een beschrijving van deze library vind je: 

Een volgende stap is dat we een *client* van de MongoDB definiëren. Hierbij geven we de naam van de *database* op (hier: `blog`).

```
client = pymongo.MongoClient()
db = client["blog"]
```

Een MongoDB database management systeem kan meerdere databases bevatten. (Meestal gebruik je maar één database tegelijk in een toepassing.) Een database bevat één of meer Collections. Een Collection is een verzameling (min of meer) gelijksoortige documenten.
Een document is te vergelijken met een object: een verzameling properties (eigeschappen); een property is een (naam, waarde) paar. Eén van de properties is de identificatie (key). Aan de hand van de unieke key kun je een document in een collection vinden.

In een database kun je documenten ook vinden aan de hand van de inhoud, door middel van queries. Als je efficient wilt zoeken op een bepaalde eigenschap (of combinatie van eigenschappen?), dan moet je voor die eigenschap een *index* maken.





#### Opslaan van gegevens

In MongoDB kunnen we de todo-lijst van een gebruiker opslaan als onderdeel van het document van de gebruiker:

```
user-doc: {
  username: String;
  todos: [ {
    id: Number;
    description: String;
    done: Boolean;
  } ]
```

We hebben dan één Collection van documenten: `users`.

We moeten de verschillende todo-elementen kunnen identificeren. Hiervoor moeten we dan een eigen identificatie bedenken - bijvoorbeeld in de vorm van een timestamp (voor een gebruiker zal deze uniek zijn).

> We kunnen de "description" niet gebruiken als identificatie: een gebruiker kan de beschrijving achteraf nog veranderen.

```
user = db.users.find_one({"username": data.user})
db.users.update_one(
        {"username": data.user},
        {"$set": {"password": data.passwd}},
        upsert=True
      )
```

(Voorstel: (i) begin met de klassieke aanpak, met twee Collections; en (ii) laat dan zien dat het in MongoDB ook met één kan. Deze klassieke aanpak kunnen we eenvoudig omzetten in een SQL-database, of in een Google Store aanpak.)

### SQL-databases

In dit geval moeten we afzonderlijke tabellen gebruiken voor de gebruikers en voor de todo-elementen. Als onderdeel van een todo-element moeten we dan de identificatie (key) van de bijbehorende gebruiker opnemen.



### CRUD

Bij een database spreken we vaak over CRUD: create, read, update, delete. De verschillende documenten (objecten, e.d.) die we willen opslaan moeten we kunnen aanmaken, aanpassen, en verwijderen.

Het kan handig zijn om ook het interface van de server op deze manier vorm te geven. 

Voor een REST interface worden meestal de volgende afspraken gebruikt:

| resource  | POST           | GET          | PUT            | DELETE  |
| :---      | :---           | :---         | :---           | :---    |
| todos     | create element | read list    | update list    | delete list |
| todos/123 |   ---          | read element | update element | delete element |

Vanuit een formulier kunnen we alleen `GET` en `POST` gebruiken. Dit betekent dat we voor ons voorbeeld een kleine variatie gebruiken:

* we gebruiken `POST todos/123` voor een update van element `123`.
* we gebruiken een extra boolean input in het formulier `delete`, voor het verwijderen van een element: `POST todos/123?delete=true`

> In een volgende module maken we gebruik van de mogelijkheden van AJAX. In dat geval kunnen we wel de normale afspraken gebruiken.

### Todo-voorbeeld

Een todo-element bestaat uit:

* een beschrijving (string)
* een boolean "done"

Om een dergelijk element te kunnen onderscheiden in een lijst, voegen we er nog een identificatie aan toe.

Bij de todo-list gebruiken we een form voor elk todo-element, zodat we dit element kunnen veranderen: de gebruiker kan de beschrijving aanpassen, of het element "done" maken.

> In een latere versie willen we ook elementen kunnen verwijderen.

We beginnen met een formulier voor het aanmaken van een nieuw element.

### Over het gebruik van checkbox

De eigenschap "done" van een todo-element heeft verschillende representaties in de html-pagina die naar de browser gestuurd wordt, in het formulier dat naar de server teruggestuurd wordt, en in de database. We moeten deze waarden omzetten op een aantal punten in het programma.

#### Van database naar html

Een todo-element heeft een boolean eigenschap `done`. Deze stellen we in het html-formulier voor door middel van een checkbox. De aanwezigheid van het attribuut `checked` van een checkbox geeft aan dat dit aangevinkt is; niet-aangevinkt komt overeen met de afwezigheid van dit attribuut.

Bij het omzetten van de Boolean waarde *vanuit de database* moeten we dit `checked` attribuut zetten. Dit doen we in het template.

```
$if elt['done']: checked
```

#### Van formulier naar database

De browser stuur het ingevulde formulier naar de server. De parameter van de checkbox in het http-request heeft het naam/waarde paar van de checkbox als deze aangevinkt is. Als de checkbox niet aangevinkt is, ontbreekt dit naam/waarde-paar in de http-parameters.

In het http-interface van een opgestuurd formulier komt de het naam/waarde-paar waarde van het checkbox-element alleen voor als deze checkbox aangevinkt is. 

In het geval van een checkbox met `name="done" value="True` hebben we dan twee mogelijkheden (met `data = web.input()`) (i) `data["done"] == "True"`; (ii) "done" ontbreekt als key in `data`. Met de volgende formule zetten we dit om in een Boolean waarde:

```
done = "done" in data.keys()
```

Deze omzetting doen we voordat we deze waarde in de database opslaan.

### Redirection

Na het afhandelen van een formulier met een todo, willen we weer terug naar de pagina met de lijst met todo's. Hiervoor kunnen we een redirect gebruiken. In web.py gebruik je daarvoor de constructie:

```
raise web.seeother(url)
```

Omdat dit het normale patroon van return/rendering onderbreekt, wordt hiervoor het Python exception mechanisme gebruikt.

### Cleanup

We hebben aan de todo-pagina en aan het server-programma een actie toegevoegd om de voltooide acties te verwijderen uit de database.

In de todo-pagina geven we deze actie weer door middel van een eenvoudige link: als de gebruiker de link aanklikt, wordt het verzoek verstuurd, en wordt de actie uitgevoerd.

> We gebruiker hiervoor een GET-request, omdat er sprake is van een *idempotente* operatie: het maakt niet uit of deze actie eenmaal of vaker uitgevoerd wordt, het resultaat blijft hetzelfde.

> In een interface volgens de REST regels gebruik je hiervoor het http `DELETE` request, maar dit kunnen we niet verzenden via een formulier. Bovendien kunnen we niet zomaar aangeven welke elementen wel of niet verwijderd moeten worden. In de latere module over AJAX (enz.) komen we hierop terug.

### Spaties en lege regels in html

Door het gebruik van templates krijgen we vaak overbodige spaties en regelovergangen in de html-tekst. Voor het weergeven van het resultaat maakt dat geen verschil, maar de html-tekst wordt er minder leesbaar door, en soms ook veel groter: je hebt wel bytes nodig om die spaties weer te geven in het bestand.

Door middel van `\` aan het einde van een regel in een template voorkom je een  regelovergang in de resulterende html-tekst.

Overbodige spaties zijn wat lastiger te voorkomen, ook omdat je rekening moet houden met de layout-regels voor Python.
