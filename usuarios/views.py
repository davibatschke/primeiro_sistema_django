from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'post':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha_1'].value() != form['senha_2']:
                return redirect('cadastro')
            nome = form['nome_cadastro'].value()
            email = form['email_cadastro'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
            usuario = User.objects.create_user(
                username=nome,
                password=senha,
                email=email
            )
            usuario.save()
            return redirect('login')   

    return render(request, 'usuarios/cadastro.html', {'form': form})