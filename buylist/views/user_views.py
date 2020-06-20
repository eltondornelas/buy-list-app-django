from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def register_user(request):
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('buylist_list_route')

    else:
        form_user = UserCreationForm()

    return render(request, 'users/form_user.html', {'form_user': form_user})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # se não baterem retorna None, se não retorna o user do db

        if user is not None:
            login(request, user)
            # loga o user no app/session

            return redirect('buylist_list_route')

        else:
            messages.error(request, 'Credenciais incorretas')
            return redirect('login_user_route')

    else:
        form_login = AuthenticationForm()

    return render(request, 'users/login.html', {'form_login': form_login})


def logout_user(request):
    logout(request)
    return redirect('login_user_route')
