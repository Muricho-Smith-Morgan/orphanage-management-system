from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('response/', views.response, name='response'),
    path('login_donor/', views.login_donor, name='login_donor'),
    path('panel/', views.panel, name='panel'),
    path('orphanage/', views.orphanage, name='orphanage'),
    path('donate/<str:pk>', views.donate, name='donate'),
]