# Django-simple-blog
![python](https://img.shields.io/badge/Language-Python-blueviolet)
![MIT License](https://img.shields.io/npm/l/all-contributors.svg?style=flat)
![Travis CI](https://api.travis-ci.com/florent6001/django-simple-blog.png?branch=master)

Django-simple-blog est un blog / portfolio personnel. Vous pouvez récupérez le projet telle-que et le modifier comme vous le souhaitez. 
Il serait favorable de modifier le template HTML lors de votre déploiement en production pour ne pas faire "copie".

## Screenshot
[Home Page](https://image.noelshack.com/fichiers/2020/29/7/1595194468-homepage.png)  
[Contact](https://image.noelshack.com/fichiers/2020/29/7/1595194469-contact-page.png)  
[Blog](https://image.noelshack.com/fichiers/2020/29/7/1595194468-blog-page.png)  
[Article](https://image.noelshack.com/fichiers/2020/29/7/1595194526-post-page.png)  

## Installation
- Clonez le repository github
```
git clone https://github.com/florent6001/django-simple-blog.git
cd django-simple-blog/
```
- Installer les dépendances avec PIP
```
pip install -r requirements.txt
```
- Duplier le fichier .env.exemple en .env
```
cp .env.exemple .env
```
- Modifier le fichier .env avec votre configuration
- Migrer la bade de donnée
```
python manage.py migrate
```
- Installer NPM (Si vous ne l'avez pas) 
  
linux:
```
sudo apt-get install npm
```
Windows:  
Téléchargez et installez : https://www.npmjs.com/get-npm

- Générer le fichier CSS à partir de SASS
```
npm run build:css
```
- Tput est prêt, vous pouvez maintenant lancer le serveur de développement python.
```
python manage.py runserver
```

## Architecture
Voici la liste des dossiers à la racine de l'application, avec leurs utilités

- Assets: Stockage des fichiers statiques, upload CKEditor également
- Base: Page statique du site (page d'accueil, Mentions légales, ...)
- Blog: Tout ce qui concerne le blog (Pages d'article, catégories, ..)
- Contact: Fprmulaire de contact
- Main: Dossier générer par Django, dossier principale reliant tout les dossiers ensemble (routing, ..)
- Template: Tous les fichiers HTML du site (header et footer inclus)

## Fonctionnalitées
- Page statique (page d'accueil, politique de protection des données, mentions légales)
- Formulaire de contact
- Système de blog (Articles, Catégories , Pagination, système de brouillon)
- Système de commentaire utilisant [Disqus](https://disqus.com/)
- Robots.txt & Sitemap.xml.
- CKEditor pour le contenu des articles.
- Configuration en fichier .env
- Intégration de Google Analytics
- Style du site utilisant SCSS (SASS)
- Optimisation du style pour Google Analytics (PurgeCSS & PostCSS)
- Lazy loading pour les images
- Test unitaires pour chaque dossier (blog, contact, ..)

## Fonctionnalitées à venir
Voici une liste des fonctionnalitées prévu par la suite :

- Nouvelle icône de navigation en mode mobile (moins épaisse)
- Internationalisation du projets

Vous pensez qu'une fonctionnalité pourrait être intéressante ? Merci de m'en faire part !

## Support
Si vous avez un problème en utilisant ce projet. Vous pouvez créer un ticket ici [here](https://github.com/florent6001/django-simple-blog/issues). Je répondrais le plus rapidement possible.

## Contribution
Si vous remarquez un bug ou souhaitez améliorer / optimiser une parti du code. Vous pouvez faire un pull-request.
Vous pouvez également faire un pull request si vous avez développer une fonctionnalitées qui est prévu dans la catégorie "Fonctionnalitées à venir"

Merci de mettre à jour les tests unitaires en fonction de vos ajouts.

## Auteur
Ce projet a été créé par [Florent Vandroy](https://florent-vandroy.fr/).  
Merci à toutes les personnes qui contribueront au projets (leurs pseudonyme seront listé ci-dessous) 

## License
Ce projet est sous [License MIT](https://choosealicense.com/licenses/mit/).
