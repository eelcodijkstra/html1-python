## Les 5: persistentie en databases

De server moet de gegevens over de verschillende gebruikers bijhouden. Dit kan niet in de variabelen van het programma: elk http-request begint een nieuw proces, "met een schone lei". Gegevens die buiten een programma bestaan noemen we ook wel *persistente gegevens*. Voorbeelden hiervan zijn de bestanden in het filesysteem, of de data in een database.

In het geval van een webserver gebruiken we vaak een database voor de persistente data. Een database kan door meerdere programma's (processen) tegelijk gebruikt worden. Eventueel kan deze database op een andere computer staan (database server), die door meerdere weservers gebruikt kan worden.

Er zijn allerlei verschillende soorten databases in gebruik. Relationele databases worden het meest gebruikt, maar voor webtoepassingen worden steeds vaker ook NoSQL-databases toegepast. Een voorbeeld van een NoSQL-database is MongoDB. In deze les gebruiken we MongoDB om de persistente gegevens van de webserver bij te houden.

De wachtwoorden van de gebruikers moet je bij de server opslaan. Dit is een eerste voorbeeld van persistente data.

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




