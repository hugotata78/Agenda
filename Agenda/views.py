from django.views.generic import ListView
from todo.models import Todo


class IndexView(ListView):
    model = Todo
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['my_list_todo'] = Todo.objects.filter(user_id=self.request.user.id)
        context['pending_todo'] = Todo.objects.filter(user_id=self.request.user.id).filter(done='pendiente')
        return context
