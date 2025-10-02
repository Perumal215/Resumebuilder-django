from django import forms

class AboutForm(forms.Form):
    about_text = forms.CharField(
        label="About Me",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 6,
            "placeholder": "Write your 'About Me' section here..."
        })
    )