from django import forms
from .models import Author

class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'last_name',
            'first_name',
            'patronymic',
            'position',
            'degree',
            'degree_year',
            'stake',
            'contract_start',
            'contract_end',
            'email',
            'annotation',
            'photo',
            'scopus_url',
            'wos_url',
            'rinz_url',
            'scholar_url',
            'orcid_url'
        ]
        widgets = {
            'contract_start': forms.DateInput(attrs={'type': 'date'}),
            'contract_end': forms.DateInput(attrs={'type': 'date'}),
            'degree_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
            'stake': forms.NumberInput(attrs={'step': 0.1, 'min': 0.1, 'max': 2.0}),
            'annotation': forms.Textarea(attrs={'rows': 3}),
        }