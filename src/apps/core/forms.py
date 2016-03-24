from django import forms


class ApiDetailForm(forms.Form):
    id = forms.CharField()


class ApiListForm(forms.Form):
    category_filter = forms.CharField()
    locations = forms.CharField()
    term = forms.CharField()
