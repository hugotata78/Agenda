from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView , ListView, DeleteView, UpdateView
from .models import Contact
from .forms import CreateContactForm

# Create your views here.

class ListContactView(ListView):
    model = Contact
    template_name = 'contact/list_view.html'

    def get_context_data(self, **kwargs):
        context = super(ListContactView,self).get_context_data(**kwargs)
        context['my_contacts'] = Contact.objects.filter(user=self.request.user)
        return context

class DetailContactView(DetailView):
    model = Contact
    template_name = 'contact/detail_view.html'
    context_object_name = 'contact'

class CreateContactView(CreateView):
    model = Contact
    form_class = CreateContactForm
    template_name = 'contact/create_view.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form.save()
        form.instance.user.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('contact_list')
    
class UpdateContactView(UpdateView):
    model = Contact
    template_name = 'contact/update_view.html'
    context_object_name = 'contact'
    form_class = CreateContactForm

    def get_success_url(self):
        contact = self.get_object()
        return reverse_lazy('detail_contact',kwargs={'pk':contact.id} )
    
class DeleteContactView(DeleteView):
    model = Contact
    template_name = 'contact/delete_view.html'
    context_object_name = 'contact'
    success_url = reverse_lazy('contact_list')
