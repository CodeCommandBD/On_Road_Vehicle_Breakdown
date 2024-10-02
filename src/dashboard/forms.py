from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'logo', 'icon', 'phone_number', 'email', 'address', 'facebook_url', 'instagram_url', 'x_url']

    def __init__(self, *args, **kwargs):
        super(SiteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Site'))
