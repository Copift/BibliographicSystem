from django import forms

from BibliographicSystem.conference.models import Conference


class ConferenceForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Conference
        fields = ['title', 'location', 'start_date', 'end_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
           # 'website': forms.URLInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Название конференции',
            'location': 'Место проведения',
            'status': 'Статус конференции',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].choices = [
            ('', '--- Не указано ---'),
            ('regional', 'Региональная'),
            ('national', 'Всероссийская'),
            ('international', 'Международная'),
        ]