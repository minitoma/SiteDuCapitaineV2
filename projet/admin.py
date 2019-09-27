from django.contrib import admin
from .models import Projet, ProjetImage

# Register your models here.

class ProjetImageInline(admin.TabularInline):
    model = ProjetImage
    extra = 1

class ProjetAdmin(admin.ModelAdmin):
    inlines = [ProjetImageInline, ]

admin.site.register(Projet, ProjetAdmin)
