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
git remote add heroku https://git.heroku.com/heroku-project-name.git
git add .
git commit -m 'first commit'
git push heroku master

# Migrations
heroku run python src/manage.py migrate

```

# Example

```
(.env) ➜  yelp_google_places git:(master) http http://127.0.0.1:8000/api/list/\?location\=US\&page\=1\&limit\=1
HTTP/1.0 200 OK
Content-Type: application/json
Date: Thu, 24 Mar 2016 03:00:50 GMT
Server: WSGIServer/0.1 Python/2.7.11
X-Frame-Options: SAMEORIGIN

{
    "data": [
        {
            "address": "1051 Market St, San Francisco, CA 94103, United States",
            "coordinate": {
                "latitude": 37.7812488,
                "longitude": -122.411304
            },
            "display_phone": "+1-415-964-1003",
            "id": "the-flying-falafel-san-francisco-3",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/jlzz6k3zJX0ypKpOwXn6iQ/ms.jpg",
            "name": "The Flying Falafel",
            "phone": "4159641003",
            "rating": "4.9",
            "website": "http://www.flyingfalafel.com/"
        }
    ],
    "success": true
}

(.env) ➜  yelp_google_places git:(master)
```
