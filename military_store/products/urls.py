from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('machines/', views.MachinesView.as_view(), name='machine_list'),
    path('machines/<slug:slug>/', views.MachineDetailView.as_view(), name='machine_detail'),
    path('combat_nutrion', views.CombatNutrionView.as_view(), name='combat_nutrion_list'),
    path('combat_nutrion/<slug:slug>/', views.CombatNutrionDetailView.as_view(), name='combat_nutrion_detail'),
    path('buy/', views.BuyView.as_view(), name='buy'),
]

