from django.urls import path
from .views import TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('add/', TodoCreateView.as_view(), name='create_todo'),
    path('update/<int:pk>',TodoUpdateView.as_view(), name='update_todo'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='delete_todo')

]
