from django import forms

# Create your forms here.
class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Insira o seu Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 
                                      'placeholder': 'Digite o seu Nome'})
    )
    senha_login = forms.CharField(
        label='Insira a sua Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 
                                          'placeholder': 'Digite a sua Senha'})
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Preencha com o seu Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 
                                      'placeholder': 'Digite o seu Nome'})
    )
    email_cadastro = forms.EmailField(
        label='Preencha com o seu Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 
                                       'placeholder': 'Exemplo: davisilva@hotmail.com'})
    )
    senha_1 = forms.CharField(
        label='Insira uma Senha',
        required=True,
        max_length=70,
        widget=forms.TextInput(attrs={'class': 'form-control', 
                                      'placeholder': 'Coloque a sua Senha'})
    )
    senha_2 = forms.CharField(
        label='Confirme a Senha',
        required=True,
        max_length=70,
        widget=forms.TextInput(attrs={'class': 'form-control', 
                                      'placeholder': 'Confirme a sua Senha'})
    )
    