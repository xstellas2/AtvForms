from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno
from django.shortcuts import render

# Create your views here.

def cadastro_aluno(request):
   if request.method == 'POST':
       form = AlunoForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('lista_alunos')
   else:
       form = AlunoForm()
   return render(request, 'alunos/cadastro_aluno.html', {'form': form})

def lista_alunos(request):
   alunos = Aluno.objects.all()
   return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

def home(request):
    return render(request, 'alunos/home.html')
