from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models


# Create your models here.


class Kategori(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# ANASAYFA


class CardIndex(models.Model):
    resim = models.FileField(upload_to='cards', null=True,
                             blank=True, verbose_name="card resmi")
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class ContentIndex(models.Model):
    resim = models.FileField(upload_to='contents', null=True,
                             blank=True, verbose_name="content resmi")


# ÇOCUK KISMI

class CardCocuk(models.Model):
    foto = models.FileField(upload_to='cards', null=True,
                            blank=True, verbose_name="card resmi")
    baslik = models.CharField(max_length=150)
    metin = models.CharField(max_length=200)

    def __str__(self):
        return self.baslik


class BuyukCardCocuk(models.Model):
    buyukfoto = models.FileField(upload_to='cards', null=True,
                                 blank=True, verbose_name="card resmi")
    buyukbaslik = models.CharField(max_length=150)

    def __str__(self):
        return self.buyukbaslik


class YanresimCocuk(models.Model):
    yanfoto = models.FileField(upload_to='cards', null=True,
                               blank=True, verbose_name="card resmi")

# FOOTER


class Footer(models.Model):
    Kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    footerfoto = models.FileField(upload_to='cards', null=True,
                                  blank=True, verbose_name="card resmi")
    footerbaslik = models.CharField(max_length=150)

    def __str__(self):
        return self.footerbaslik


# ERKEK
class CardErkek(models.Model):
    foto = models.FileField(upload_to='cards', null=True,
                            blank=True, verbose_name="card resmi")
    baslik = models.CharField(max_length=150)
    metin = models.CharField(max_length=200)

    def __str__(self):
        return self.baslik


class BuyukCardErkek(models.Model):
    buyukfoto = models.FileField(upload_to='cards', null=True,
                                 blank=True, verbose_name="card resmi")
    buyukbaslik = models.CharField(max_length=150)

    def __str__(self):
        return self.buyukbaslik


class YanresimErkek(models.Model):
    yanfoto = models.FileField(upload_to='cards', null=True,
                               blank=True, verbose_name="card resmi")


# KADIN

class CardKadin(models.Model):
    foto = models.FileField(upload_to='cards', null=True,
                            blank=True, verbose_name="card resmi")
    baslik = models.CharField(max_length=150)
    metin = models.CharField(max_length=200)

    def __str__(self):
        return self.baslik


class BuyukCardKadin(models.Model):
    buyukfoto = models.FileField(upload_to='cards', null=True,
                                 blank=True, verbose_name="card resmi")
    buyukbaslik = models.CharField(max_length=150)

    def __str__(self):
        return self.buyukbaslik

# SEPET


class Sepetim(models.Model):
    foto = models.FileField(upload_to='cards', null=True,
                            blank=True, verbose_name="card resmi")
    aciklama = models.TextField(max_length=200)
    fiyat = models.CharField(max_length=150)
    adet = models.CharField(max_length=50)

    def __str__(self):
        return self.aciklama
