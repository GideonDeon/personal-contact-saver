from turtle import title
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Contact
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {"form":form})
 
class IndexView(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'deets'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deets'] = context['deets'].filter(user = self.request.user)
        context['count'] = context['deets'].filter(city = False).count()

        search = self.request.GET.get('searched') or ''
        if search:
            context['deets'] = context['deets'].filter(
                firstname__startswith = search
            )

        context['search'] = search

        return context

class Create(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'app/create.html'
    fields =[
            'initials',
            'firstname',
            'lastname',
            'nickname',
            'phone',
            'email',
            'home',
            'company',
            'title',
            'work',
            'state',
            'city',
            'zip',
            'country',
            'website',
            'note'
        ]
    success_url = reverse_lazy('IndexView')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Create, self).form_valid(form)


class Edit(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'app/edit.html'
    fields = [
            'initials',
            'firstname',
            'lastname',
            'nickname',
            'phone',
            'email',
            'home',
            'company',
            'title',
            'work',
            'state',
            'city',
            'zip',
            'country',
            'website',
            'note'
        ]
    success_url = reverse_lazy('IndexView')

class Delete(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'app/delete.html'
    context_object_name = 'det'
    success_url = reverse_lazy('IndexView')

