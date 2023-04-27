from django.urls import path
from .views import CreateContactView,ListContactView, DetailContactView, DeleteContactView, UpdateContactView

urlpatterns = [
    path('',ListContactView.as_view(), name='contact_list'),
    path('create/', CreateContactView.as_view(), name='create_contact' ),
    path('detail/<int:pk>', DetailContactView.as_view(), name='detail_contact'),
    path('delete/<int:pk>', DeleteContactView.as_view(), name='delete_contact'),
    path('update/<int:pk>', UpdateContactView.as_view(), name='update_contact')
]