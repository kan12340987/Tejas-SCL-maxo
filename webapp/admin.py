from django.contrib import admin
from .models import QPapers, Texbook, notes
# Register your models here.
admin.site.register(QPapers)
admin.site.register(Texbook)
admin.site.register(notes)