import decimal
import json
import yelp
import googleplaces


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def get_yelp_instance(yelp_key):
    yelp_instance = yelp.Api(**yelp_key)
    return yelp_instance


def get_google_instance(google_key):
    google_instance = googleplaces.GooglePlaces(google_key)
    return google_instance
