## Opdrachten les 1

### "unplugged" opdracht: browser en server

Het doel van deze opdracht is om te begrijpen wat de taakverdeling is tussen de browser en de server in het geval van een dynamische website, en welke problemen daarbij een rol spelen.

*Speel met een groep het gedrag van de browser en de server na, voor een dynamische website.*

> Een dynamische website is een website waarbij de inhoud van de pagina's voor elke gebruiker verschillend kan zijn. Een voorbeeld is een webwinkel, waarbij elke gebruiker zijn eigen winkelmandje heeft, en zijn eigen gebruikers-account.

*Opdracht*: geef drie voorbeelden van dynamische websites. Geef voor elk voorbeeld aan welke informatie verschillend is per gebruiker.

Je hebt in elk geval 3 spelers nodig:

* de browser/gebruiker
* het web/internet
* de server

De communicatie tussen de browser en de server gebeurt door middel van vellen papier die uitgewisseld worden. Er mag verder niet gesproken worden bij de interactie tussen de verschillende spelers. Gebruik voor elk bericht (request, respons) een afzonderlijk vel papier.

> Je moet van te voren goed nadenken wat er op zo'n vel moet staan: aan de hand van die informatie moeten de andere spelers (web, browser, server) weten wat ze moeten doen.

> Je mag wel overleggen om de manier van samenwerken te veranderen, bijvoorbeeld: wat je op de papieren schrijft, en wat dat betekent. Na dit overleg begin je opnieuw met de nieuwe afspraken.

De server handelt elk verzoek afzonderlijk af, onafhankelijk van de eerdere verzoeken. Bij het afhandelen van een verzoek "weet" de server niets van andere verzoeken. Je kunt dit naspelen door de verzoeken aan de kant van de server door verschillende personen af te laten handelen; na het afhandelen van een verzoek krijgt een andere persoon de beurt, voor een volgend verzoek.

Alleen als een server iets "opschrijft" kan de informatie doorgegeven worden en gebruikt worden bij volgende verzoeken. We noemen dit "persistente data": data die bewaard wordt terwijl het proces dat de data aangemaakt heeft niet meer bestaat.

> In een computersysteem gebruik je bestanden en databases voor dergelijke persistente data. Je bewaart deze bijvoorbeeld op een harde schijf: de gegevens blijven daar staan, ook als de computer uitgeschakeld wordt.

Mogelijke problemen die je ondervindt:

* hoe kan de server bepalen van welke gebruiker een verzoek (request) afkomstig is?
* hoe kan de server bij het afhandelen van een verzoek (request), informatie uit vorige verzoeken gebruiken?
