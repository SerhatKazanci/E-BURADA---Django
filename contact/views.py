import email
from email import message
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, Following
from shopping.models import *

# Create your views here.


def emailView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()
            messages.success(request, 'Mesajınız Üreticiye Gönderilmiştir.')
            return redirect('ulasin')
    else:
        form = ContactForm()
    return render(request, "ulasin.html", {'form': form})


def Follow(request):
    # girişli değil ise sayfaya  giriş yapmasına izin verme giris sayfasına  yönlendir
    if not request.user.is_authenticated:
        messages.success(request, "Lütfen Giriş Yapınız!")
        return redirect('login')

    if request.method == "POST":
        form = Following(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            number = form.cleaned_data['number']
        form.save()
        messages.success(
            request, 'Kargo Takip Linkiniz Birazdan Telefonunuza İletilecektir.')
        return redirect('takip')

    else:
        form = Following()
        footers = Footer.objects.all()
        context = {
            'footer': footers,
            'form': form
        }

    return render(request, "siparistakip.html", context)
