from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Kategori)

# Anasayfa
admin.site.register(CardIndex),
admin.site.register(ContentIndex),
# ÇOCUK
admin.site.register(CardCocuk),
admin.site.register(BuyukCardCocuk),
admin.site.register(YanresimCocuk),
# FOOTER
admin.site.register(Footer),
# ERKEK
admin.site.register(CardErkek,)
admin.site.register(BuyukCardErkek)
admin.site.register(YanresimErkek),
# KADIN
admin.site.register(CardKadin)
admin.site.register(BuyukCardKadin)
# SEPET
admin.site.register(Sepetim)
