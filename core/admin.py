from django.contrib import admin
from .models import Manager, Post, Disciplina

# Register your models here.


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cargo', 'create_at', 'active_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'active_at')


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nota']
