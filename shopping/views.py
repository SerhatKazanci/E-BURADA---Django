from ast import Return
from multiprocessing import context
from re import search
from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.


def Anasayfa(request):
    cards = CardIndex.objects.all()
    footers = Footer.objects.all()
    contents = ContentIndex.objects.all()
    # search
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        cards = cards.filter(title__icontains=search)

    context = {
        'card': cards,
        'footer': footers,
        'content': contents,
        'search': search
    }

    return render(request, "anasayfa.html", context)


def Cocuk(request):
    # girişli değil ise sayfaya  giriş yapmasına izin verme giris sayfasına  yönlendir
    if not request.user.is_authenticated:
        messages.success(request, "Lütfen Giriş Yapınız!")
        return redirect('login')

    karts = CardCocuk.objects.all()
    buyukkarts = BuyukCardCocuk.objects.all()
    yanresims = YanresimCocuk.objects.all()
    footers = Footer.objects.all()
    # search
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        karts = karts.filter(baslik__icontains=search)
    context = {
        'kart': karts,
        'buyukkart': buyukkarts,
        'yanresim': yanresims,
        'footer': footers,
        'search': search

    }
    return render(request, "cocuk.html", context)


def Erkek(request):
 # girişli değil ise sayfaya  giriş yapmasına izin verme giris sayfasına  yönlendir
    if not request.user.is_authenticated:
        messages.success(request, "Lütfen Giriş Yapınız!")
        return redirect('login')

    kart1 = CardErkek.objects.all()
    buyukkarts1 = BuyukCardErkek.objects.all()
    footers = Footer.objects.all()
    yanresims = YanresimErkek.objects.all()
    # search
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        kart1 = kart1.filter(baslik__icontains=search)
    context = {
        'karte': kart1,
        'buyukkarte': buyukkarts1,
        'yanresime': yanresims,
        'footer': footers,
        'search': search
    }
    return render(request, "erkek.html", context)


def Kadin(request):
 # girişli değil ise sayfaya  giriş yapmasına izin verme giris sayfasına  yönlendir
    if not request.user.is_authenticated:
        messages.success(request, "Lütfen Giriş Yapınız!")
        return redirect('login')

    kart2 = CardKadin.objects.all()
    buyukkart2 = BuyukCardKadin.objects.all()
    yanresims = YanresimErkek.objects.all()
    footers = Footer.objects.all()
    # search
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        kart2 = kart2.filter(baslik__icontains=search)
    context = {
        'kartk': kart2,
        'buyukkartk': buyukkart2,
        'yanresimk': yanresims,
        'footer': footers,
        'search': search
    }
    return render(request, "kadin.html", context)


def Magazalar(request):
    footers = Footer.objects.all()
    context = {
        'footer': footers,
    }
    return render(request, "magazalar.html", context)


def Sepet(request):
    sepets = Sepetim.objects.all()

    footers = Footer.objects.all()
    context = {
        'footer': footers,
        'sepet': sepets
    }
    return render(request, "sepet.html", context)
