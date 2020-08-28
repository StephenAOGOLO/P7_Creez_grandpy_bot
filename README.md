# P7_Creez_grandpy_bot  
[![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeH7711sJeOaZ_HOpwi3M7MjPOQeOPE2TyMxn-_NyxyHu_O2tm&s)](https://openclassrooms.com/fr)
[![](https://grandpybotone.herokuapp.com/static/png/gpb.png)](https://grandpybotone.herokuapp.com/static/png/gpb.png) 
## Introduction  
    
    Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires.  
    Il me suffisait de lui dire un mot pour le voir parti pendant des heures.  
    "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ?  
    C'était en 1974 et..." 😴  

    Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant.  
    Voici donc le projet que je vous propose : créer un robot qui vous répondrait comme votre grand-père !  
    Si vous lui demandez l'adresse d'un lieu,  
    il vous la donnera, certes, mais agrémentée d'un long récit très intéressant.  
    Vous êtes prêt·e ?  

## Cahier des charges  
### Fonctionnalités  

    - Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée  
    et la réponse s'affiche directement dans l'écran, sans recharger la page.  
    
    - Vous utiliserez l'API de Google Maps et celle de Media Wiki.  
    
    - Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page,  
    tout l'historique est perdu.  
    
    - Vous pouvez vous amuser à inventer plusieurs réponses différentes de la part de GrandPy  
    mais ce n'est pas une obligation. Amusez-vous !  

### Parcours utilisateur  

    L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie.  
    Il arrive devant une page contenant les éléments suivants :  

    header : logo et phrase d'accroche  
    zone centrale : zone vide (qui servira à afficher le dialogue) et champ de formulaire pour envoyer une question.  
    footer : votre prénom & nom, lien vers votre repository Github et autres réseaux sociaux si vous en avez  
    L'utilisateur tape "Salut GrandPy !  
    Est-ce que tu connais l'adresse d'OpenClassrooms ?" dans le champ de formulaire puis appuie sur la touche Entrée.  
    Le message s'affiche dans la zone du dessus qui affiche tous les messages échangés.  
    Une icône tourne pour indiquer que GrandPy est en train de réfléchir.  

    Puis un nouveau message apparaît : "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris."  
    En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.  

    GrandPy envoie un nouveau message :  
    "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?  
    La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.  
    Elle est en forme de té, une branche débouche au 43 rue de Paradis,  
    la deuxième au 57 rue d'Hauteville et la troisième en impasse.  
    
### Conception & Réalisation  

La réalisation du projet s'appuie sur une méthodologie agile.  
Ses étapes sont disponibles sur : [Trello](https://trello.com/invite/b/rpLoSERM/1b9969b583e9da8879e4e900f5909e7d/p7creezgrandpybot)  

## Conception  
Le Front-End.   
Le site web est responsive. Il s'adapte à quatre types d'écran:  

    - L’ordinateur portable.
    - Le grand écran.
    - Le mobile tenu à la verticale.
    - Le mobile tenu à l’horizontale.

Le Back-End.  
Les user-story peuvent être regroupées en plusieurs étapes fonctionnelles,
faisant parti du processus algorithmique de l'application.  
Ci-dessous, le processus algorithmique du fonctionnement nominal, gestion d'erreur exclue:  
    
    - Capture du texte saisi par l'utilisateur.  
    - Sécurisation XSS: Hachage et épuration du texte.  
    - Parsing: Hachage et épuration du texte.  
    - API Wikipedia: Envoi du texte formaté vers le serveur MediaWiki.  
    - API GoogleMaps: Envoi du texte formaté vers le serveur GoogleMaps.  
    - API OpenStreetMap: Envoi du texte formaté vers le serveur OpenStreetMap.  
    - Réponse API : Analyse et mise en forme des réponses API.  
    - Centralisation des réponses API.  
    - Génération des messages personnalisées.  
    - Centralisation du texte à afficher.  
    - Affichage de la résponse.  


## Réalisation  
La réalisation du projet s'est appuyé sur le plan d'action suivant:  
 
    - Initialisation de Flask.
    - Création de l’Interface Utilisateur.
    - Création d’une fonction de « Parsing ».
    - Création des gestionnaires APIs (MediaWiki, Google Maps et OpenStreetMap).   
    - Création des messages personnalisés (voir ci dessous)

## Messages personnalisés  
Les messges personnalisés représentent ce dit GrandPyBot à l'affichage de la réponse.  
Il s'exclame au début de la description du lieu demandé puis récite un HAIKU,  
avant d'inviter l'utilisateur à regarder la carte où se trouve la géolocalisation du lieu.  

Un HAIKU est un petit poème japonais de trois vers qui permet de méditer...[Description](https://fr.wikipedia.org/wiki/Haïku)  

Le HAIKU est généré de manière aléatoire à chaque recherche et s'éfforce de correspondre au lieu demandé.   

## API OpenStreetMap  
Cet Api est utilisé en complément de l'API MediaWiki afin de retrouver les coordonnées géogrphiques,  
latitudes et longitudes, du lieu demandé.  

Dans le cas où MediaWiki ne retrouve pas un lieu demandé, OpenStreetMap prend le relais pour effectuer la recherche.  
Cela a pour but d'améliorer l'efficacité de GrandPyBot, en augmentant le succès des recherches.  

Voici à quoi resemble [OpenStreetMap](http://www.openstreetmap.fr)  
### Installation  
## Hébergement  

Le site web a été mis en ligne sur la plateforme [HEROKU](https://www.heroku.com/what).  

## Adresse du site  

Le site web est disponible via [cette adresse](https://grandpybotone.herokuapp.com/).  

## GitHub  
Les informations principales du projet ainsi que  
ses composants de la solution sont disponibles sur : [GitHub](https://github.com/StephenAOGOLO/P7_Creez_grandpy_bot)  

## Versions  
GrandPyBot : 1.4  
Python : 3.6  
Flask : 1.1.2  


## Rappel des liens  
[GrandPyBot](https://grandpybotone.herokuapp.com/)  
[Trello](https://trello.com/invite/b/rpLoSERM/1b9969b583e9da8879e4e900f5909e7d/p7creezgrandpybot)  
[Haiku](https://fr.wikipedia.org/wiki/Haïku)  
[OpenStreetMap](http://www.openstreetmap.fr)  
[Heroku](https://www.heroku.com/what)  
[GitHub](https://github.com/StephenAOGOLO/P7_Creez_grandpy_bot)  

## Auteur
Stephen A.OGOLO

## Remerciements  
Merci pour cette lecture et pour l'attention portée à ces informations.  
Bonne utilisation ;)
  
