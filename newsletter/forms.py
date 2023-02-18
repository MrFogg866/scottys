# forms.py
from django import forms
from newsletter.models import Subscriber
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )
        self.helper.form_method = 'post'
        self.helper.add_input(forms.HiddenInput())
        self.helper.form_class = 'form-inline'
        self.helper.form_show_labels = False
        self.helper.html5_required = True
        self.helper.label_class = 'form-label'
