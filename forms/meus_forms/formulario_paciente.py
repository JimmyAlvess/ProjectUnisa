
from consulta.models import Paciente
from django import forms


class CadastroPaciente(forms.ModelForm):
    nome_completo = forms.CharField(
        required=True,
        help_text='Digite seu nome completo',
        error_messages={'required': 'Campo obrigatorio'}
    )

    idade = forms.CharField(
        required=True,
        widget=forms.NumberInput,
        error_messages={'required': 'Campo obrigatorio'}
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu email aqui'})
    )

    sexos = [('Feminino', 'Feminino'), ('Masculino', 'Masculino')]
    genero = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=sexos,
    )
    data = forms.DateField(
        input_formats='%m/%d/%Y',
        required=False,
        widget=forms.TextInput,
    )

    class Meta:
        model = Paciente
        fields = 'nome_completo', 'idade', 'genero',\
            'email', 'telefone', 'data',
