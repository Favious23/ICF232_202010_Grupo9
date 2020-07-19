from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm

class SignUpUsuario(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')