## Les 3: templates

Een dynamische webpagina is een pagina die door de server aangepast is aan de gebruiker. Deze aanpassing is meestal maar klein: de overeenkomsten tussen de pagina's voor verschillende gebruikers zijn groot. In een template proberen we het gemeenschappelijke onder te brengen. Dit template parametriseren we met de elementen die per gebruiker kunnen verschillen.

> Een template of sjabloon is een tekst die je kunt parametriseren. De parameters in deze tekst kun je vervangen door andere teksten. Templates kom je op veel verschillende plaatsen tegen:

* mail/merge: je kunt mails personaliseren ("Beste mevrouw Jansen") door in een template (bijvoorbeeld "Beste $naam") de parameter ("$naam") te vervangen door de eigenlijke tekst, die bijvoorbeeld uit een spreadsheet afkomstig is.

### Templates in Python

Python heeft een eenvoudige vorm van templates als onderdeel van de string-library.



### Templates in web.py

Web.py heeft uitgebreidere mogelijkheden voor templates. De syntax voor deze templates is sterk gebaseerd op de Python-syntax.

### Andere template-systemen

Er zijn voor Python nog andere template-systemen in gebruik. Een populair template-systeem is Jinja (Jinja2). 


### Templates: voorbeeld

We gebruiken deze templates in het voorbeeld-programma. We kunnen hiermee een volledige html-pagina genereren, in plaats van alleen een korte tekst. Eventueel kunnen we deze tekst nog uitgebreider opmaken.

We geven twee voorbeelden van de templates:

1. Gebruik van de ingebouwde Python-templates;
2. Gebruik van de web.py templates.

Bij het gebruik van de web.py templates heb je veel meer mogelijk