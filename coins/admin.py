from django.contrib import admin

from .models import Appraisal, Coin, Photo

# Register your models here.

admin.site.register(Coin)
admin.site.register(Appraisal)
admin.site.register(Photo)
