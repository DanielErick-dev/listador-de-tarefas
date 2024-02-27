from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import CreateView, ListView, DeleteView, View, TemplateView, UpdateView
from .models import Tarefa, Academy, Programation, Faxina
from django.urls import reverse_lazy
from django.shortcuts import redirect
from urllib.parse import quote_plus
import os
import webbrowser
from time import sleep
import pyautogui
import pyttsx3

# começo da sessão de listar missões gerais (página inicial)

# listando tarefas gerais
class ProgramationView(ListView):
    model = Programation
    context_object_name = 'programation'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tarefas_totais = Programation.objects.all()
        if len(tarefas_totais) <= 0:   
            context["sem_tarefas"] = True
        return context
    
# enviando relatório de wpp com todas as tarefas gerais
class RelatorioView(TemplateView):
    tarefas = Tarefa.objects.all()
    template_name = ('app_list/tarefa_list.html')
    def enviando_relatorio():
        try: 
            arquivo = open('arquivo.txt', 'r')
            conteudo = arquivo.read()
            arquivo.close()
            telefone = '61996052272'

            link_whatsapp = (f'https:://web.whatsapp.com/send?phone={telefone}&text={quote_plus(conteudo)}')
            
            webbrowser.open(link_whatsapp)
            sleep(20)
            engine = pyttsx3.init()
            engine.say('por favor aperte enter nos próximos 10 segundos para envio da mensagem')
            engine.runAndWait()
            sleep(10)
            pyautogui.press('enter')
            sleep(1)
            
            engine.say('encerrando a página de transferência')
            engine.runAndWait()
            pyautogui.hotkey('ctrl', 'w')
            sleep(1)
            if os.path.exists('arquivo.txt'):
                os.remove('arquivo.txt')
                print('arquivo.txt apagado com sucesso')
            else:
                print('arquivo.txt não encontrado')
            
            
        except:
            print('ocorreu um erro no envio da mensagem automática')
   
    def get(self, request: HttpRequest, *args, **kwargs):
        tarefas = Tarefa.objects.all()
        with open('arquivo.txt', 'a', newline='', encoding='utf-8') as arquivo:
            for tarefa in tarefas:
                arquivo.write(f'{tarefa.nome}\n')
        engine = pyttsx3.init()
        engine.say('executando método de envio de relatório de tarefas')
        engine.runAndWait()
        RelatorioView.enviando_relatorio()
        condicao = True
        if condicao:
            return redirect('index_view')
        return super().get(request, *args, **kwargs)
    

# concluindo uma tarefa
class ProgramationConclusionView(View):
    # apagar um item da lista que tenha sido concluido
    def get(self, request, pk):
        try:
            tarefa =  Programation.objects.filter(pk=pk)
            tarefa.delete()
        except:
            print('ocorreu algum erro para apagar a tarefa')
        return redirect('programation_view')
    
# atualizando uma tarefa
class ProgramationUpdateView(UpdateView):
    model = Programation
    fields = ['nome']
    success_url = reverse_lazy('programation_view')

# criando uma tarefa
class ProgramationCreateView(CreateView):
    model = Programation
    fields = ['nome']
    success_url = reverse_lazy('programation_view')

# deletando uma tarefa
class ProgramationDeleteView(DeleteView):
    model = Programation
    success_url = reverse_lazy('programation_view')

# FIM DA SESSÃO DE LISTAGEM DE TAREFAS GERAIS


# COMEÇO DA SESSÃO DE LISTAGEM DE TAREFAS RELACIONADAS AO PROJETO DA ACADEMIA
    
# criando uma tarefa
class AppCreateView(CreateView):
    model = Tarefa
    fields = ["nome"]
    success_url = reverse_lazy('index_view')

# listando tarefas 
class AppListView(ListView):
    model = Tarefa
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tarefas = Tarefa.objects.all()
        if len(tarefas) <= 0:
            context["sem_tarefas"] = True
        return context

# deletando uma tarefa
class AppDeleteView(DeleteView):
    model = Tarefa
    success_url = reverse_lazy('index_view')

# concluindo uma tarefa
class AppConclusionView(View):
    # apagar um item da lista que tenha sido concluido
    def get(self, request, pk):
        try:
            tarefa = Tarefa.objects.filter(id=pk)
            tarefa.delete()
        except:
            print('ocorreu algum erro para apagar a tarefa')
        return redirect('index_view')
    
# atualizando uma tarefa
class AppUpdateView(UpdateView):
    model = Tarefa
    fields = ['nome']
    success_url = reverse_lazy('index_view')

# FIM DA SESSÃO DE LISTAGEM DE TAREFAS RELACIONADAS AO PROJETO DA ACADEMIA


# COMEÇO DA SESSÃO DE LISTAGEM DE TAREFAS RELACIONADAS A PROGRAMAÇÃO
    
# deletando uma tarefa
class ProjectAcademyDeleteView(DeleteView):
    model = Academy
    success_url = reverse_lazy('project_academy_view')

 # concluindo uma tarefa
class ProjectAcademyConclusionView(View):
    # apagar um item da lista que tenha sido concluido
    def get(self, request, pk):
        try:
            tarefa =  Academy.objects.filter(pk=pk)
            tarefa.delete()
        except:
            print('ocorreu algum erro para apagar a tarefa')
        return redirect('project_academy_view')
    
# atualizando uma tarefa
class ProjectAcademyUpdateView(UpdateView):
    model = Academy
    fields = ['nome']
    success_url = reverse_lazy('project_academy_view')

# criando uma tarefa
class ProjectAcademyCreateView(CreateView):
    model = Academy
    fields = ['nome']
    success_url = reverse_lazy('project_academy_view')

# listando tarefas
class ProjectAcademyListView(ListView):
    model = Academy 
    template_name = 'app_list/project_academy_list.html'
    context_object_name = 'academy'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tarefas = Academy.objects.all()
        if len(tarefas) <= 0:
            context["sem_tarefas"] = True
            
        return context




# COMEÇO DA SESSÃO DE LISTAGEM DE TAREFAS RELACIONADAS A TAREFAS CASEIRAS E FAXINA/ARREDORES
    
# deletando uma tarefa
class FaxinaDeleteView(DeleteView):
    model = Faxina
    success_url = reverse_lazy('faxina_view')

 # concluindo uma tarefa
class FaxinaConclusionView(View):
    # apagar um item da lista que tenha sido concluido
    def get(self, request, pk):
        try:
            tarefa =  Faxina.objects.filter(pk=pk)
            tarefa.delete()
        except:
            print('ocorreu algum erro para apagar a tarefa')
        return redirect('faxina_view')
    
# atualizando uma tarefa
class FaxinaUpdateView(UpdateView):
    model = Faxina
    fields = ['nome']
    success_url = reverse_lazy('faxina_view')

# criando uma tarefa
class FaxinaCreateView(CreateView):
    model = Faxina
    fields = ['nome']
    success_url = reverse_lazy('faxina_view')

# listando tarefas
class FaxinaListView(ListView):
    model = Faxina 
    template_name = 'app_list/faxina_list.html'
    context_object_name = 'faxina'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tarefas = Faxina.objects.all()
        if len(tarefas) <= 0:
            context["sem_tarefas"] = True
        return context









