from django.forms import ModelForm

from albuns.widget import *
from .models import Album, Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
class ClinicaCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=255,min_length=1,empty_value="Endereço",required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17,required=True)
    cnpj_regex = RegexValidator(regex=r'\d\d\.\d\d\d\.\d\d\d\/\d\d\d\d-\d\d', message="CNPJ must be entered in the format: 'XX.XXX.XXX/YYYY-ZZ' ")
    cnpj = forms.CharField(validators=[cnpj_regex], max_length=18,required=True, label='CNPJ')
    price = forms.FloatField()
    # image = forms.ImageField(required=True, label='Inserir foto da clínica')

    ESPECIALIDADES = [
        ('AN',"Angiologia"),
        ('DE',"Dermatologia"),
        ('EN',"Endocrinologia"),
        ('GA',"Gastroenterologia"),
        ('GI',"Ginecologia e obstetrícia"),
        ('OF',"Oftalmologia"),
        ('OR',"Ortopedia"),
        ('OT',"Otorrino"),
        ('PE',"Pediatria"),
        ('PSI',"Psicologia"),
        ('PSQ',"Psiquiatria"),
        ('NE',"Neurologia"),
        ('NU',"Nutricionista"),
        ('UR',"Urologia"),
    ]
    
    especialidades = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=ESPECIALIDADES,
         
    )
    class Meta:
        model = User
        fields = ("username", "email", "address", "phone", "cnpj", "price", "especialidades", "password1", "password2")


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        user.email = self.cleaned_data["email"]
        user.address = self.cleaned_data["address"]
        user.phone = self.cleaned_data["phone"]
        user.cnpj = self.cleaned_data["cnpj"]
        user.especialidades = self.cleaned_data["especialidades"]
        user.price = self.cleaned_data["price"]
        # user.image = self.cleaned_data["image"]
        if commit:
            user.save()
        return user

class BasicUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17,required=True)
    # image = forms.ImageField(required=True, label='Inserir foto da clínica')
    class Meta:
        model = User
        fields = ("username", "email", "phone", "password1", "password2")


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]
        if commit:
            user.save()
        return user
class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'date',
            'timeinit',
            'timefinal',
            'especialidade',
            'endereco',
            'info',
        ]
        labels = {
            'date': 'Data da Consulta',
            'timeinit': 'Horário Inicial da Consulta',
            'timefinal': 'Horário Final da Consulta',
            'especialidade' : 'Especialidade da Consulta',
            'endereco' : 'Endereço ou local da consulta',
            'info': 'Informações Adicionais (Opcional)'
        }
        widgets = {
            'date' : DateTimePickerInput(
            format='%d/%m/%Y %H:%M', attrs={'class':'form-control','type': 'date'},
        ),
            'timeinit' : DateTimePickerInput(
                format='%d/%m/%Y %H:%M', attrs={'class':'form-control','type': 'time'},
            ),
            'timefinal' : DateTimePickerInput(
                format='%d/%m/%Y %H:%M', attrs={'class':'form-control','type': 'time'},
            ),
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'especialidade',
            'text',
        ]
        labels = {
            'especialidade' : 'Marcar Consulta?',
            'text': 'Cometário adicional (opcional):',
        }
