from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpUsuario.as_view(), name='signup'),
]