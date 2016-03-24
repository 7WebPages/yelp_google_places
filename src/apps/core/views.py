import json
from django.views.generic.edit import BaseFormView, FormMixin
from django.views.generic import FormView, View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.conf import settings

from .forms import ApiDetailForm, ApiListForm
from .utils import get_yelp_instance, get_google_instance


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
                data['form_errors'] = e.message
                data['success'] = False
        else:
            status_code = 400
            data['form_errors'] = form._errors
            data['success'] = False


        return HttpResponse(json.dumps(data),
                            status=status_code,
                            content_type='application/json')


class ApiDetailView(ApiFormView):
    form_class = ApiDetailForm


class ApiListView(ApiFormView):
    form_class = ApiListForm

    def get_data(self, cleaned_data):
        cleaned_data = super(ApiListView, self).get_data(cleaned_data)

        category_filter = cleaned_data.get('category_filter')
        location = cleaned_data.get('location')
        term = cleaned_data.get('term')
        page = cleaned_data.get('page') or 0

        data = []

        _offset_end = 50
        _page_size = 20

        #google_instance = get_google_instance(settings.GOOGLE_API_KEY)
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
            data.append({
                'id': business.id,
                'image_url': business.image_url,
                'name': business.name,
                'phone': business.phone,
                'display_phone': business.display_phone,
                'coordinate': business.location.coordinate,
            })

        return data
