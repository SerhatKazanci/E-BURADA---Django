
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from shopping.models import *

# Create your views here.


def Login(request):
    # girişli ise logine giriş yapmasına izin verme anasayfaya yönlendir
    if request.user.is_authenticated:
        return redirect('anasayfa')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Giriş yapıldı")
            return redirect('anasayfa')
        else:
            messages.warning(request, "Böyle Bir Kullanıcı Bulunmamaktadır.")
            return redirect('login')

    footers = Footer.objects.all()
    context = {
        'footer': footers,
    }
    return render(request, 'login.html', context)


def Register(request):
    # girişli ise registera giriş yapmasına izin verme anasayfaya yönlendir
    if request.user.is_authenticated:
        return redirect('anasayfa')

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.warning(request, "Username Kullanılmaktadır.")
                return render(request, "register.html", {
                    "username": username,
                    "email": email,
                    "firstname": firstname,
                    "lastname": lastname
                })

            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, "Email Kullanılmaktadır.")
                    return render(request, "register.html",
                                  {
                                      "username": username,
                                      "email": email,
                                      "firstname": firstname,
                                      "lastname": lastname
                                  })
                else:
                    user = User.objects.create_user(
                        username=username, email=email, first_name=firstname, last_name=lastname, password=password)
                    user.save()
                    return redirect('login')

        else:
            messages.warning(request, "Parola Eşleşmiyor.")
            return render(request, "register.html", {
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname
            })

    footers = Footer.objects.all()
    context = {
        'footer': footers,
    }
    return render(request, 'register.html', context)


def Logout(request):
    logout(request)
    messages.warning(request, "Çıkış Yapıldı.")
    return redirect('anasayfa')
