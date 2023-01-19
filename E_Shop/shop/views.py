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

from .serializer import *
from .utils import DataMixin, ContextDataMixin

a = ''


class ProductViewSetAPI(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all().order_by('-price')  # переопредtление запроса для бд
        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def brand(self, request, pk=None):
        brand= Brand.objects.get(pk=pk)
        return Response({'brand': brand.name})


# class ProductAPI(APIView):
#     def get(self, request):
#         lst = Gender.objects.all()
#         return Response({"posts": GenderSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer  = GenderSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # new_gender = Gender.objects.create(
#         #     name=request.data['name'],
#         #     slug=request.data['slug']
#         # )
#         # return Response({"post": GenderSerializer(new_gender).data})
#         return Response({"post": serializer.data})
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Gender.objects.get(pk=pk)
#         except:
#             return Response({"error": "Method PUT not allowed"})
#
#         serializer = GenderSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"posts": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         Gender.objects.get(pk=pk).delete()
#         return Response({'post': "delete post" + str(pk)})

# class ProductAPI(generics.ListAPIView):
#     def get(self, requset):

# queryset = Women.objects.all()
# serializer_class = ProductSerializer

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
    return redirect('login')


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
        a = self.request.GET.get('q')
        context['q'] = a
        context['q'] = a
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        # posts = Women.objects.filter(title__contains=self.request.GET.get('q')).filter(category=self.kwargs['cat_slug'])
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
        a = self.request.GET.get('q')
        context['q'] = a
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
        a = self.request.GET.get('q')
        context['q'] = a
        print(self.request.GET.get('q'))
        context['path'] = self.request.path.split("/")[2]
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        if self.request.GET.get('q') != '':
            return Women.get_qeryset_brand(self.request.GET.get('q'), self.kwargs['brand_slug'])
            # return Women.objects.filter(title__contains=self.request.GET.get('q')).filter(
            #     brand_id__slug=self.kwargs['brand_slug'])
        # return Women.objects.filter(brand_id__slug=self.kwargs['brand_slug'])
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
        # return Women.objects.filter(slug=self.kwargs['product_name'])

        return Women.get_qeryset_product_slug(self.kwargs['product_name'])
