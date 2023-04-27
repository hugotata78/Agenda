
from django.contrib import admin
from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('user/', include('User.urls')),
    path('', IndexView.as_view(), name='index'),
    path('contact/', include('contact.urls'))

]
