## Les 5: persistentie en databases

De server moet de gegevens over de verschillende gebruikers bijhouden. Dit kan niet in de variabelen van het programma: elk http-request begint een nieuw proces, "met een schone lei". Gegevens die buiten een programma bestaan noemen we ook wel *persistente gegevens*. Voorbeelden hiervan zijn de bestanden in het filesysteem, of de data in een database.

In het geval van een webserver gebruiken we vaak een database voor de persistente data. Een database kan door meerdere programma's (processen) tegelijk gebruikt worden. Eventueel kan deze database op een andere computer staan (database server), die door meerdere weservers gebruikt kan worden.

Er zijn allerlei verschillende soorten databases in gebruik. Relationele databases worden het meest gebruikt, maar voor webtoepassingen worden steeds vaker ook NoSQL-databases toegepast. Een voorbeeld van een NoSQL-database is MongoDB. In deze les gebruiken we MongoDB om de persistente gegevens van de webserver bij te houden.



