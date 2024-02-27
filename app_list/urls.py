from django.urls import path
from .views import AppCreateView, AppListView, AppDeleteView, ProjectAcademyListView, ProjectAcademyCreateView, ProjectAcademyDeleteView, AppConclusionView, RelatorioView, AppUpdateView, ProgramationView, ProgramationCreateView, ProgramationUpdateView, ProgramationDeleteView, ProjectAcademyUpdateView, ProgramationConclusionView, ProjectAcademyConclusionView, FaxinaDeleteView, FaxinaUpdateView, FaxinaCreateView, FaxinaListView, FaxinaConclusionView
urlpatterns = [
    # sessões urls de tarefas de missões gerais (página inicial)
    path('', AppListView.as_view(), name='index_view'),
    path('cadastro/', AppCreateView.as_view(), name='create_view'),
    path('deletar/<int:pk>', AppDeleteView.as_view(), name='delete_view'),
    path('update/<int:pk>/', AppUpdateView.as_view(), name='update_view'),
    path('complete/<int:pk>', AppConclusionView.as_view(), name='conclusion_view'),
    path('relatorio', RelatorioView.as_view(), name='relatorio_view'),


    # sessões urls de tarefas do projeto academia
    path('projeto_academia/', ProjectAcademyListView.as_view(), name='project_academy_view'),

    path('projeto_academia_update/<int:pk>', ProjectAcademyUpdateView.as_view(), name='project_academy_update_view'),

    path('projeto_academia_cadastro/', ProjectAcademyCreateView.as_view(), name='project_academy_create_view'),

    path('projeto_academia_deletar/<int:pk>', ProjectAcademyDeleteView.as_view(), name='project_academy_delete_view'),


    path('projeto_academia_concluir/<int:pk>', ProjectAcademyConclusionView.as_view(), name='project_academy_conclusion_view'),


    # sessões urls de tarefas relacionadas a programação no geral
    path('programacao/', ProgramationView.as_view(), name='programation_view'),

    path('cadastro_programacao/', ProgramationCreateView.as_view(), name='programation_create_view'),

    path('update_programacao/<int:pk>', ProgramationUpdateView.as_view(), 
    name='programation_update_view'),

    path('deletar_programacao/<int:pk>', ProgramationDeleteView.as_view(), name='programation_delete_view'),

    path('concluir_programacao/<int:pk>', ProgramationConclusionView.as_view(), name='programation_conclusion_view'),

    # sessões urls de tarefas relacionadas tarefas caseiras e faxinas

    path('faxina/', FaxinaListView.as_view(), name='faxina_view'),

    path('cadastro_faxina/', FaxinaCreateView.as_view(), name='faxina_create_view'),

    path('update_faxina/<int:pk>', FaxinaUpdateView.as_view(), 
    name='faxina_update_view'),

    path('deletar_faxina/<int:pk>', FaxinaDeleteView.as_view(), name='faxina_delete_view'),

    path('concluir_faxina/<int:pk>', FaxinaConclusionView.as_view(), name='faxina_conclusion_view'),
]
