from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha_login'].value()

        usuario = auth.authenticate(
            username=nome,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Login efetuado com Sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'ERRO: Falha ao realizar o Login.')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, 'ERRO: Senhas Diferentes!')
                return redirect('cadastro')
            
            nome=form['nome_cadastro'].value()
            senha=form['senha_1'].value()
            email=form['email_cadastro'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'ERRO: Usuario ja Registrado!')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                password=senha,
                email=email
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com Sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'LogOut efetuado com Sucesso... Tchau.')
    return redirect('login')