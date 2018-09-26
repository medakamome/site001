from django.contrib import admin
from .models import Difinition

# Register your models here.
'''
@admin.register(Difinition)
class Difinition(admin.ModelAdmin):
    pass
'''
admin.site.register(Difinition)