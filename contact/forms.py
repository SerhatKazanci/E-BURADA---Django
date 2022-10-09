from dataclasses import field
from django import forms
from .models import Contact, Follow


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class Following(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ['phone', 'number']

    def __init__(self, *args, **kwargs):
        super(Following, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
