from django.urls import path
from . import views

urlpatterns = [
    path('analisar/', views.AnaliseCSVView.as_view()),
]
