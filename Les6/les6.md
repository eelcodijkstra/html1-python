## Les 6: gebruikers en todo's

In deze les combineren we gebruikers en todo's. We maken het mogelijk dat elke gebruiker zijn eigen lijst met todo's kan maken.

> We bouwen nog niet de beveiliging in dat elke gebruiker alleen zijn eigen lijst met todo's mag zien. Dit behandelen we in een latere les.

### REST urls

In dit geval beschouwen we de lijst met todo's van een gebruiker als een eigenschap van een gebruiker. De URLs voor de todo's hebben daarom de vorm:

```
home/users/user-id/todos/todo-id
```

Als onderdeel van een todo-element nemen we de identificatie van de betreffende gebruiker op.

> In MongoDB kunnen we de lijst met todo-elementen van een gebruiker ook opnemen in het document van de gebruiker: we hoeven dan niet een aparte collection te hebben voor todo-elementen.

(Een alternatief is om voor een lijst met todo's een aparte identificatie te maken. Dat is een zinvol alternatief. We moeten)

Het is nog steeds mogelijk afzonderlijke todo's te verwerken: de identificatie van de todo-elementen is globaal.

> Vraag over REST: hoe identificeer je in een REST-interface de collection? Hoe maak je het onderscheid tussen een element in een collection, en de collection zelf? Moet je dan een collection beschouwen als onderdeel van een andere collection? (Meestal kun je een collection niet aanmaken, zoals een element: de structuur van de URLs ligt gewoonlijk vast, maar niet de elementen in die structuur.)

**Vraag**: we hebben nog geen formulier voor het aanmaken van een nieuwe gebruiker. Mogelijk vereenvoudigt dit de aanpak. We geven dan een foutmelding als een gebruiker zich meldt die nog niet aangemeld is. (Het is nu nog wat onduidelijk wanneer we een nieuwe gebruiker moeten aanmaken. Bij de GET user?)

*Opdracht:* voeg aan de pagina met todo-lijsten de naam van de gebruiker toe.
Hint: (i) geef deze door als parameter aan het template; (ii) je kunt de naam van de gebruiker ook in de URL opnemen, als parameter (direct; of via een verborgen veld in een formulier).

In de functie `Users.GET` zetten we het cookie `username`. Voor een nieuwe gebruiker zorgen we er ook voor dat deze aan de database toegevoegd wordt. We weten dan altijd zeker dat een naam die we via dit cookie krijgen, in de database bestaat.

(Naamgeving van input-data: consistenter gemaakt.)
