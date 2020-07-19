# Django-simple-blog
![python](https://img.shields.io/badge/Language-Python-blueviolet)
![MIT License](https://img.shields.io/npm/l/all-contributors.svg?style=flat)
![Travis CI](https://api.travis-ci.com/florent6001/django-simple-blog.png?branch=master)

Django-simple-blog is the code of my personal blog / portfolio. You can take the source and edit it as you want. 
If you deploy this project in production, i just ask you to change the html template.

## Screenshot
[HomePage](https://image.noelshack.com/fichiers/2020/29/7/1595194468-homepage.png)  
[Contact Page](https://image.noelshack.com/fichiers/2020/29/7/1595194469-contact-page.png)  
[Blog Page](https://image.noelshack.com/fichiers/2020/29/7/1595194468-blog-page.png)  
[Post page](https://image.noelshack.com/fichiers/2020/29/7/1595194526-post-page.png)  

## Installation
- Clone this repository.
```
git clone https://github.com/florent6001/django-simple-blog.git
cd django-simple-blog/
```
- Install the requirements.txt using PIP
```
pip install -r requirements.txt
```
- Copy .env.exemple to .env
```
cp .env.exemple .env
```
- Customize the .env with your configuration.
- Migrate the database
```
python manage.py migrate
```
- Install NPM (if you don't have it) 
  
linux:
```
sudo apt-get install npm
```
Windows:  
Download and install : https://www.npmjs.com/get-npm

- Generate the CSS file from SASS:
```
npm run build:css
```
- Done, you can now run your server
```
python manage.py runserver
```

## Architecture
Here is the list of folders at the root of the project, with their functionnality.

- Assets: Storage folder for static files. (ckeditor upload too)
- Base: Static page of the website (homepage, legal notice, ...)
- Blog: All about the blog (Post, Category, ..)
- Contact: Contact Form
- Main: Main folder of the website, generated by django and linking others folders.
- Template: HTML of the website (header and footer too)

## Functionality
- Static page (homepage, data policy, legal notice)
- Contact Form
- Blog system (Post, Category, Pagination, draft)
- Comment system using [Disqus](https://disqus.com/)
- Robots.txt & Sitemap.xml.
- CKEditor for the Post administration.
- Configuration in .env
- Google Analytics
- SCSS (SASS) with NPM
- Optimized for Google PageSpeed (PurgeCSS & PostCSS)
- Lazy loading for img
- Test.py in every app

## Upcoming Functionality
Here is an upcoming list of functionality: 

- Change the navbar toggler icon for a thinner one.
- i18n for the project.

Do you think a feature could improve the user experience? Thanks for letting me know!

## Support
If you run into a problem while using this project. Please create a ticket [here](https://github.com/florent6001/django-simple-blog/issues). I will answer as soon as i can.

## Contributing
You can make a pull request in order to optimize the already existing code or to correct a bug.
You can also make a pull request in order to add an upcoming feature which is listed above. 
 
Please make sure to update tests as appropriate.

## Author & Acknowledgment
This project has been created by [Florent Vandroy](https://florent-vandroy.fr/).  
Thanks to everyone who helped to make this project more complete. (usernames will be listed below)

## License
This project is under [MIT license](https://choosealicense.com/licenses/mit/).
