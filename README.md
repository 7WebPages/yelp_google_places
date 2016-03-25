# Installation

```
cd yelp_google_places
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

# Heroku deployment

```
git init .
heroku create
git add .
git commit -m 'first commit'
git push heroku master
```

# Usage Example

```
pip install httpie

http http://googleplaces.herokuapp.com/api/list/?location=US&limit=1
http http://googleplaces.herokuapp.com/api/list/?location=US&limit=1&term=fitness
http http://googleplaces.herokuapp.com/api/list/?location=US&limit=1&category_filter=fitness

```
