from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import *
from .forms import AddToCarz, RegisterUserForm, LoginUserForm
from .models import *
from rest_framework import generics, viewsets


from .utils import DataMixin, ContextDataMixin



def get_pagination(request, posts, number_str):
    paginator = Paginator(posts, number_str)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return posts


class RedisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/autorization.html'
    success_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login_user')


def index(request):
    post = Women.objects.filter().order_by('-time_create')[:3]
    context = {'posts': post}
    return render(request, "shop/home.html", context=context)


class ShowCategory(ContextDataMixin, ListView):
    model = Women
    template_name = 'shop/catalog.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        posts = Women.get_search_product_category(self.request.GET.get('q'), self.kwargs['cat_slug'])
        return posts


class Catalog(ContextDataMixin, ListView):
    model = Women
    template_name = 'shop/catalog.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class SearchProduct(ContextDataMixin, ListView):
    model = Women
    context_object_name = 'posts'
    template_name = "shop/catalog.html"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.get_search_product(self.request.GET.get('q'))


class Carz(ContextDataMixin, ListView):
    model = Carz
    context_object_name = 'posts'
    template_name = 'shop/carz.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ShowBrand(ContextDataMixin, ListView):
    model = Women
    template_name = "shop/catalog.html"
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        context['path'] = self.request.path.split("/")[2]
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        if self.request.GET.get('q') != '':
            return Women.get_qeryset_brand(self.request.GET.get('q'), self.kwargs['brand_slug'])
        return Women.get_qeryset_brand_id(self.kwargs['brand_slug'])


class Product(ListView):
    model = Women
    context_object_name = 'posts'
    template_name = 'shop/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        pk_t = {}
        context = super().get_context_data(**kwargs)
        pk_t['pk_t'] = int(Women.objects.get(slug=self.kwargs['product_name']).pk)
        context['form'] = AddToCarz(pk_t)
        return context

    def get_queryset(self):
        return Women.get_qeryset_product_slug(self.kwargs['product_name'])
