import json
from django.views.generic.edit import BaseFormView, FormMixin
from django.views.generic import FormView, View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import ApiDetailForm, ApiListForm


class ApiFormView(View):

    def get_data(self, cleaned_data):
        return cleaned_data

    def get(self, request, *args, **kwargs):
        data = {}
        form = self.form_class(self.request.GET)
        if form.is_valid():
            status_code = 200
            data['success'] = True
            data['data'] = self.get_data(form.cleaned_data)
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
