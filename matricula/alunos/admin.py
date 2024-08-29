from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'curso', 'email')
    list_filter = ('cidade', 'curso')

admin.site.register(Aluno, AlunoAdmin)
