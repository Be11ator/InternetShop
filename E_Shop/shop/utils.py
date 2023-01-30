from shop.forms import AddToCarz
from shop.models import *

Accessories = 'accessories'
Bags = 'bags'
Hoodies_or_Sweatshirts = 'hoodies_or_sweatshirts'
Jackets_or_Coats = 'jackets_or_coats'
Polos = 'polos'
Shirts = 'shirts'
Shoes = 'shoes'
Sweaters = 'sweaters'
T_Shirts = 't_shirts'
Trousers_or_Jeans = 'trousers_or_jeans'
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        brands = Brand.objects.all()
        posts = Women.objects.all()
        context['brands'] = brands
        context['posts'] = posts
        context['category'] = CATEGORY
        return context


class ContextDataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['brands'] = Brand.objects.all()
        context['sort_products'] = SortProduct.objects.all()
        context['category'] = CATEGORY
        return context
