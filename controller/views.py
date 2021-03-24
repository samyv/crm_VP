from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django import forms
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Member, Dog, Address, Race
from .forms import MemberForm, MemberModelForm, UserLoginForm, DogForm, DogModelForm

def index(request):
    return render(request, "controller/alsobase.html")

class ListMembers(LoginRequiredMixin, ListView):
    print("list")
    template_name = "controller/member/member_list.html"
    queryset = Member.objects.all()
    context_object_name = "members"

class DetailMember(LoginRequiredMixin, DetailView):
    template_name = "controller/member/member_detail.html"
    queryset = Member.objects.all()
    context_object_name = "member"

class CreateMember(LoginRequiredMixin, CreateView):
    template_name = "controller/member/member_form.html"
    form_class = MemberModelForm()
    
    def get_success_url(self):
        return reverse("member/list")

class UpdateMember(LoginRequiredMixin, UpdateView):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add in a QuerySet of all the books
        context['addresses'] = Address.objects.all()
        return context

    template_name = "controller/member/member_update.html"
    form_class = MemberModelForm
    queryset = Member.objects.all()
    
    def get_success_url(self, *args, **kwargs):
        #TODO reverse to detail page
        return reverse("controller:member-list")

class DeleteMember(LoginRequiredMixin, DeleteView):
    template_name = "controller/member/member_delete.html"
    queryset = Member.objects.all()

    def get_success_url(self, *args, **kwargs):
        return reverse("controller:member-list")


class ListDogs(LoginRequiredMixin, ListView):
    print("list")
    template_name = "controller/dog/dog_list.html"
    queryset = Dog.objects.all()
    context_object_name = "dogs"

class DetailDog(LoginRequiredMixin, DetailView):
    template_name = "controller/dog/dog_detail.html"
    queryset = Dog.objects.all()
    context_object_name = "dog"

class CreateDog(LoginRequiredMixin, CreateView):
    template_name = "controller/dog/dog_form.html"
    form_class = DogModelForm()
    
    def get_success_url(self):
        return reverse("dog/list")

class UpdateDog(LoginRequiredMixin, UpdateView):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add in a QuerySet of all the books
        context['addresses'] = Address.objects.all()
        return context

    template_name = "controller/dog/dog_update.html"
    form_class = DogModelForm
    queryset = Dog.objects.all()
    
    def get_success_url(self, *args, **kwargs):
        #TODO reverse to detail page
        return reverse("controller:dog-list")

class DeleteDog(LoginRequiredMixin, DeleteView):
    template_name = "controller/dog/dog_delete.html"
    queryset = Dog.objects.all()

    def get_success_url(self, *args, **kwargs):
        return reverse("controller:dog-list")
