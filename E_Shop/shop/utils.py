from shop.forms import AddToCarz
from shop.models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        brands = Brand.objects.all()
        genders = Gender.objects.all()
        posts = Women.objects.all()

        context['brands'] = brands
        context['posts'] = posts
        context['category'] = CATEGORY
        context['genders'] = genders

        return context

class ContextDataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['brands'] = Brand.objects.all()
        context['sort_products'] = SortProduct.objects.all()
        context['category'] = CATEGORY
        return context