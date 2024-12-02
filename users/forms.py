from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile


from django.forms.widgets import ClearableFileInput

class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(required=True, label="Sünniaeg",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control' }))
    

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2',]
        labels = {
            'username': 'Kasutajanimi',
            'first_name': 'Eesnimi',
            'last_name': 'Perekonnanimi',
            'email': 'E-mail',
            'date_of_birth': 'Sünniaeg',
            'password1': 'Salasõna',
            'password2': 'Kinnita salasõna',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'star_sign', 'bio']
        labels = {
            'profile_photo': 'Profiilpilt',
           'star_sign': 'Tähtkuju',
            'bio': 'Bio',
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['first_name', 'last_name','email']




class MultiPhotoUploadForm(forms.Form):
    images = MultipleFileField(label="Vali pildid", required=False)