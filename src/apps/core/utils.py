import yelp
import googleplaces


def get_yelp_instance(yelp_key):
    yelp_instance = yelp.Api(**yelp_key)
    return yelp_instance


def get_google_instance(google_key):
    google_instance = googleplaces.GooglePlaces(google_key)
    return google_instance
