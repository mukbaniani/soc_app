from django.views.generic import CreateView
from .models import User
from .forms import UserRegister


class Register(CreateView):
    model = User
    form_class = UserRegister
    template_name = 'user/register.html'