from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django.core.mail import send_mail


class BookingForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    phone = forms.CharField(label='Phone', max_length=100, required=True)
    date = forms.DateField(label='Date', required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    time = forms.TimeField(label='Time', required=True, widget=forms.TextInput(attrs={'type': 'time'}))
    people = forms.IntegerField(label='Number of People', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'rows': 4}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-lg-4 col-md-6 mb-0'),
                Column('email', css_class='form-group col-lg-4 col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phone', css_class='form-group col-lg-4 col-md-6 mb-0'),
                Column('date', css_class='form-group col-lg-4 col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('time', css_class='form-group col-lg-4 col-md-6 mb-0'),
                Column('people', css_class='form-group col-lg-4 col-md-6 mb-0'),
                css_class='form-row'
            ),
            'message',
        )
        
    def send_email(self):
        # Get the form data
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        date = self.cleaned_data['date']
        time = self.cleaned_data['time']
        people = self.cleaned_data['people']
        message = self.cleaned_data['message']

        # Create the email message
        subject = f'Booking Request from {name}'
        body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nTime: {time}\nNumber of People: {people}\nMessage: {message}'
        from_email = 'your-email@example.com'
        to_email = ['scotties234@gmail.com']

        # Send the email
        send_mail(subject, body, from_email, to_email, fail_silently=False)
