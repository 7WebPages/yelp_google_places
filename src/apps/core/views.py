import json
from django.views.generic.edit import BaseFormView, FormMixin
from django.views.generic import FormView, View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.conf import settings

from .forms import ApiDetailForm, ApiListForm
from .utils import get_yelp_instance, get_google_instance, DecimalEncoder


class ApiFormView(View):

    def get_data(self, cleaned_data):
        return cleaned_data

    def get(self, request, *args, **kwargs):
        data = {}
        form = self.form_class(self.request.GET)
        if form.is_valid():
            status_code = 200
            data['success'] = True
            try:
                data['data'] = self.get_data(form.cleaned_data)
            except Exception as e:
                data['errors'] = e.message
                data['success'] = False
        else:
            status_code = 400
            data['errors'] = form._errors
            data['success'] = False


        return HttpResponse(json.dumps(data, cls=DecimalEncoder),
                            status=status_code,
                            content_type='application/json')


class ApiDetailView(ApiFormView):
    form_class = ApiDetailForm

    def get_data(self, cleaned_data):
        cleaned_data = super(ApiListView, self).get_data(cleaned_data)
        import ipdb; ipdb.set_trace()


class ApiListView(ApiFormView):
    form_class = ApiListForm

    def get_data(self, cleaned_data):
        cleaned_data = super(ApiListView, self).get_data(cleaned_data)

        category_filter = cleaned_data.get('category_filter')
        location = cleaned_data.get('location')
        term = cleaned_data.get('term')
        page = cleaned_data.get('offset') or 0
        limit = cleaned_data.get('limit') or 20

        data = []

        _offset_end = 50
        _page_size = limit

        google_instance = get_google_instance(settings.GOOGLE_API_KEY)
        yelp_instance = get_yelp_instance(settings.YELP_API_KEY)

        kwargs = {
            'location': cleaned_data.get('location'),
            'limit': _page_size,
            'offset': _page_size * page
        }

        if category_filter:
            kwargs.update({'category_filter': category_filter})

        if term:
            kwargs.update({'term': term})

        yelp_response = yelp_instance.Search(**kwargs)

        for business in yelp_response.businesses:
            places = google_instance.text_search(
                business.name,
                lat_lng={
                    'lat': business.location.coordinate['latitude'],
                    'lng': business.location.coordinate['longitude']
                }
            )

            company = {}
            for place in places.places:
                place.get_details()
                company.update(place.details)

            data.append(company)

        return data
