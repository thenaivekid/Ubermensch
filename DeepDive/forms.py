from django import forms
from django import forms

class EmailForm(forms.Form):
    """Form to send email."""

    sent_from = forms.CharField(
        max_length=100,
        required=True
    )

    subject = forms.CharField(
        max_length=100,
        required=True
    )

    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
