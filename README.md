# Django-simple-blog
Django-Freelance-Blog est un projet Django que j'ai créé afin d'avoir un portfolio avec un blog.

## Architecture du projet
Voici la liste des dossiers à la racine du projet, ainsi que leurs rôles.  

- Assets : Dossier de stockage des fichiers statiques ainsi que les upload ckeditor.
- Base: Pages statiques du site (page d'accueil, mentions légales, ...)
- Blog: Tout ce qui concerne le blog (article et catégorie)
- Contact: Gère le formulaire de contact
- Main: Dossier d'initialisation du projet. (fait le lien avec les autres dossiers du projet)
- Template: Contient uniquement le layout du site (header et le footer du site)

## Support
Si vous rencontrez un problème lors de l'utilisation de ce projet. Merci de créer un ticket [ici](https://github.com/florent6001/django-simple-blog/issues). Une réponse vous seras donné le plus rapidement possible.

## Fonctionnalités
- Pages statiques (homepage, politique de confidentialité des données, mentions légales)
- Formulaire de contact
- Système de blog (Article, Catégorie d'article) avec système de brouillon et de pagination
- Robots.txt et Sitemap.xml gérer dans les urls de chaque app.
- CKEditor pour la création de contenu pour les articles dans l'administration de django.
- Configuration stockée dans un fichier .env
- Intégration de Google analytics
- Supporte les fichiers SCSS (SASS)
- Optimiser pour google pagespeed (Retire automatiquement les classes non utilisé et minifie les fichiers CSS avec PurgeCSS et postcss)
- Compressiin GZIP
- Lazy loading des images

## Fonctionnalités à venir
Voici une liste des fonctionnalités à venir prévu dans l'application :

- Créer une erreur 404
- Changer l'icon toggler pour une plus fine
- Ajouter un système de commentaire (voir disqus)
- Ajouter schema.org dans les fichiers HTML afin d'améliorer le référencement naturel du projet

Vous pensez qu'une fonctionné non-listé serait intéréssante ? Merci de m'en faire part.

## Contribution
Vous pouvez faire un pull request afin d'optimiser le code déjà existant ou pour corriger un bug.  
Vous pouvez également faire un pull request afin d'ajouter une fonctionnalité qui est à venir ci-dessus.

## Auteur et remerciement
Ce projet a été créé par [Florent Vandroy](https://florent-vandroy.fr/).  
Merci à toutes les personnes ayant contribué à rendre ce projet plus complet. (Les pseudonymes des personnes ayant contribués seront listés ci-dessous)

## License
Ce projet est partagé sous [license MIT](https://choosealicense.com/licenses/mit/).