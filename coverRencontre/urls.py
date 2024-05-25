from django.urls import path
from coverRencontre import views

urlpatterns = [
    path('inscription/<int:even_id>', views.inscription, name='inscription'),
    path('avis/<int:even_id>', views.note_form, name='avis'),
    path('export_avis', views.export_avis_to_excel, name='export_avis_to_excel'),
    path('participants_avis', views.export_participants_to_excel, name='export_participants_to_excel')]