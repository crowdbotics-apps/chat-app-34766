from django.contrib import admin
from .models import Content, Creator

admin.site.register(Creator)
admin.site.register(Content)

# Register your models here.
