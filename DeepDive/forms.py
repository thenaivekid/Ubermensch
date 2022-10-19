from django import forms
from django import forms

class EmailForm(forms.Form):
    """Form to send email."""

    subject = forms.CharField(
        max_length=100,
        required=True
    )

    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
