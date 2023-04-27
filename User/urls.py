from django.urls import path
from .views import CreateUserView, LoginUserView, DetailUserView, UpdateUserView,DeleteUserView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', DetailUserView.as_view(), name= 'user_detail' ),
    path('update/<int:pk>', UpdateUserView.as_view(), name='update_user'),
    path('delete/<int:pk>', DeleteUserView.as_view(), name='delete_user')
]