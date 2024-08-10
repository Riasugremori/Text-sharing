from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.save_text, name='save_text'),
    path('text/', views.view_text, name='view_text'), 
    path('edit/', views.edit_text, name='edit_text'),  
]
