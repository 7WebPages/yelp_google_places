from django import forms


class ApiDetailForm(forms.Form):
    id = forms.CharField()


class ApiListForm(forms.Form):
    category_filter = forms.CharField(required=False)
    location = forms.CharField(required=True, max_length=2)
    term = forms.CharField(required=False)
    page = forms.IntegerField(required=False)
