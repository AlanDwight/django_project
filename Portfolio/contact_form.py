from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=50)
    your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
