from django.contrib import admin
from .models import Country,States,Districts,City
# Register your models here.
admin.site.register(Country)
admin.site.register(States)
admin.site.register(Districts)
admin.site.register(City)