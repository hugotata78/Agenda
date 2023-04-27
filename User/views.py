from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CreateUserForm, LoginForm, UpdateUserForm

User = get_user_model()

# Create your views here.

class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'user/create_user_view.html'
    

    def form_valid(self, form):
        form.save()

        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1']
        )

        login(self.request, user)
        return redirect('index')

class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'user/login_view.html'

class DetailUserView(DetailView):
    model = User
    template_name = 'user/detail_view.html'

class UpdateUserView(UpdateView):

    model = User
    template_name = 'user/update_view.html'
    form_class = UpdateUserForm
    success_url = reverse_lazy('index')

class DeleteUserView(DeleteView):
    model = User
    template_name = 'user/delete_view.html'
    success_url = reverse_lazy('index')