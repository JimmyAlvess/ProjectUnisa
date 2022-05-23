

from consulta.models import Medico
from django import forms


class CadastroMedico(forms.ModelForm):
    nome_completo = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome completo'
        }),
        error_messages={
            'required': 'Este campo é obrigatorio'
        },
    )
    idade = forms.CharField(
        required=True,
        widget=forms.NumberInput(),
        error_messages={'required': 'Campo obrigatorio'}
    )

    crm = forms.CharField(
        max_length=6,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu CRM'
        }),
        error_messages={
            'required': 'Campo obrigatorio'
        }
    )
    especialidades = (

        ("Radiologista", "Radiologista"),
        ("Clinico Geral", "Clinico Geral"),
        ("Ortopedista", "Ortopedista"),
        ("Odontologia", "Odontologia"),


    )

    Categoria = forms.MultipleChoiceField(
        choices=especialidades,
        required=True,
    )

    endereco = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o endereco da sua clinica'
        }),
        error_messages={
            'required': 'Este campo é obrigatorio'
        }
    )

    cep = forms.CharField(
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o CEP da sua clinica'
        }),
        error_messages={
            'required': 'Este campo é obrigatorio'
        }
    )
    img = forms.ImageField(

        help_text='Coloque sua foto aqui'
    )
    sexos = [('Feminino', 'Feminino'), ('Masculino', 'Masculino')]
    genero = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=sexos,
    )

    class Meta:
        model = Medico
        fields = [
            'nome_completo',
            'idade',
            'crm',
            'Categoria',
            'endereco',
            'cep',
            'genero',
            'img',
        ]
