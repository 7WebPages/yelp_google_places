# Installation

```
django-admin startproject projectname --template=https://github.com/aliev/django-skeleton/archive/master.zip
cd projectname
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

# Heroku deployment

```
git init .
heroku create
git remote add heroku https://git.heroku.com/heroku-project-name.git
git add .
git commit -m 'first commit'
git push heroku master

# Migrations
heroku run python src/manage.py migrate

```
