from django import forms
from .models import ShegarLandForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ShegarLandFormForm(forms.ModelForm):
    guyya_qophae = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',  # HTML5 date input type
            'class': 'form-control',  # Bootstrap class for styling
        })
    )

    class Meta:  # Make sure this is correctly indented
        model = ShegarLandForm
        fields = ['magaalaa', 'aanaa', 'iddo_adda', 'lakk_adda', 'gosa_tajajila',
                  'madda_lafa', 'tajajila_iddo', 'haala_beenya', 'qamaa_qophaef',
                  'tajajila_qophaef', 'balina_lafa', 'kan_qophesse', 'guyya_qophae', 
                  'shapefile', 'suura_iddoo', 'Mallattoo']

    def clean_lakk_adda(self):
        lakk_adda = self.cleaned_data.get('lakk_adda')
        if lakk_adda < 0:
            raise forms.ValidationError("Lakk adda must be a positive integer.")
        return lakk_adda