from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from fcuser.decorators import admin_required
from product.serializers import ProductSerializer
from rest_framework import generics
from rest_framework import mixins
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm

# Create your views here.

class ProductListApi(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailApi(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'
@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.date('name'),
            price=form.date('price'),
            description=form.date('description'),
            stock=form.date('stock')
        )
        product.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = OrderForm(self.request)
        return context
