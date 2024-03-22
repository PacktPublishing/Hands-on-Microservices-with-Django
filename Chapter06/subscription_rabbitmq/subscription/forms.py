from django import forms


class SubscriptionForm(forms.Form):
    name = forms.CharField(label="Your name")
    address = forms.CharField(label="Address")
    postalcode = forms.CharField(label="Postal code")
    city = forms.CharField(label="City")
    country = forms.CharField(label="Country")
    email = forms.EmailField(label="Email")
