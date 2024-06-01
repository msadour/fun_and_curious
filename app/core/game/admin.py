from django.contrib import admin

from app.core.game.models import Category, Game, Question

admin.site.register(Game)
admin.site.register(Question)
admin.site.register(Category)
