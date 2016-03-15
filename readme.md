## Html-1 met Python

Deze module bevat de stof voor de badge HTML-1.

## Aanmaken en initialiseren van de Cloud9-workspace

Voordat je aan de slag kunt met Python-web.py en MongoDB, moet je eerst de volgende acties uitvoeren. Dit hoeft maar één keer per workspace: daarna is je workspace klaar voor gebruikt.

### Cloud9

* maak een nieuwe Cloud9-workspace aan, via "clone from git", met de URL van dit repository: `https://github.com/infvo/nosql.git`
* geef deze readme weer als preview: selecteer `readme.md`, en selecteer via het dropdown-menu "preview". (Of, open `readme.md`, en selecteer in het menu bovenin "Preview".)

### MongoDB

MongoDB is al geïnstalleerd in je Cloud9 Virtuele Machine, maar je moet nog ruimte voor de data maken, en MongoDB opstarten. Zie: https://docs.c9.io/docs/setting-up-mongodb

Open nieuw terminal-venster (onderaan), en voer daarin de onderstaande opdrachten één voor één uit:

```shell
$ mkdir data
$ echo 'mongod --bind_ip=$IP --dbpath=data --nojournal --rest "$@"' > mongod
$ chmod a+x mongod
$ mongod
```

* houd het programma `mongod` actief in dit venster; gebruik voor andere opdrachten een ander terminal-venster.
* in dit terminal-venster krijg je de mededelingen van de database-driver.

Je kunt database-opdrachten uitvoeren via de mongodb-shell. Open hiervoor een nieuw terminal-venster, en start daarin de mongodb-shell via het commando: 

* `$ mongo`

Daarn kun je mongodb-shell opdrachten geven, bijvoorbeeld: 

* `> show databases`

### Python

We hebben de volgende python-onderdelen nodig:

* `pymongo`: de library om vanuit Python MongoDB aan te sturen ("driver").
* `web.py`: een eenvoudig framework voor het maken van websites vanuit Python

Deze onderdelen kun je installeren door middel van de volgende shell-opdrachten:

```shell
$ sudo pip install pymongo
$ sudo pip install web.py
```

Je kunt de werking van `web.py` controleren via:

```
$ python webdemo.py
```
