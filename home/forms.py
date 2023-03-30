from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django import forms
from django.utils.safestring import mark_safe
from .models import Review, Product, Subscriber
from django.contrib.auth.models import User


RATING_CHOICES = [(i, mark_safe('<i class="fas fa-star rating"></i>' * i)) for i in range(1, 6)]


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'rating-input'}),
    )
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Review
        fields = ['name', 'email', 'comment', 'rating', 'products']
        widgets = {'rating': forms.RadioSelect}

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        initial_rating = int(self.initial.get('rating', 1))
        for i in range(1, 6):
            checked = ' checked' if i == initial_rating else ''
            self.fields['rating'].widget.choices[i-1] = (i, mark_safe(f"<i class='fas fa-star{checked}'></i>" * i))

        review_instance = kwargs.get('instance')
        if review_instance:
            initial_products = review_instance.products.all().values_list('id', flat=True)
            self.initial['products'] = initial_products

        self.fields['products'].choices = [(product.id, product.name) for product in Product.objects.all()]

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('rating', css_class='form-group col-md-6 mb-0'),
                Column('products', css_class='form-group col-md-6 mb-0'),
                css_class='row',
            ),
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='row',
            ),
            Row(
                Column('comment', css_class='form-group col-md-12 mb-0'),
                css_class='row',
            ),
        )

        # Add the crispy-forms class to the fields to apply styling
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'style': 'flex-direction: column; align-items: stretch;'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'style': 'flex-direction: column; align-items: stretch;'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        review = super().save(commit=False)
        review.user = self.user
        if commit:
            review.save()
            self.save_m2m()
        return review


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
                css_class='form-row',
            ),
        )
        self.helper.form_method = 'post'
        self.helper.add_input(forms.HiddenInput())
        self.helper.form_class = 'form-inline'
        self.helper.form_show_labels = False
        self.helper.html5_required = True
        self.helper.label_class = 'form-label'
