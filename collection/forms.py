from django import forms
from django.utils.html import escape


class ContactForm(forms.Form):
    """
    Validate contact-me form data and
    clean data in preparation for sending
    an email message
    """
    name = forms.CharField(label='Name', required=True)
    email = forms.EmailField(label="Email", required=True)
    phone = forms.CharField(label="Phone", required=True)
    message = forms.CharField(label="Message", required=True)

    def clean(self):
        """
        Run each of these fields through escape function
        :return: self.cleaned_data
        """
        cleaned_data = super().clean()
        for k, v in self.cleaned_data.items():
            cleaned_data[k] = escape(v)
        self.cleaned_data = cleaned_data
        return self.cleaned_data
