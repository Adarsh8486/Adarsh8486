from django.contrib import admin
from .models import registerUser,Ingredients

# Register your models here.
admin.site.register([registerUser,Ingredients])
