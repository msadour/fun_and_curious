from django.contrib import admin

from .models import Category, Question

admin.site.register(Question)
admin.site.register(Category)
