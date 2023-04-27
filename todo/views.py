from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Todo
from .forms import TodoForm

User = get_user_model()

# Create your views here.


    

class TodoListView(ListView):
    model = Todo
    template_name = 'todo/list_view.html'

    def get_context_data(self, **kwargs):
        context = super(TodoListView,self).get_context_data(**kwargs)
        context['my_list'] = Todo.objects.filter(user_id=self.request.user.id)
        return context
    

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/detail_view.html'
    context_object_name = 'todo'
    

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/create_view.html'
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        form.instance.user_id = User.objects.get(id=self.request.user.id)
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    context_object_name = 'todo'
    template_name = 'todo/update_view.html'
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo/delete_view.html'
    success_url = reverse_lazy('todo_list')
