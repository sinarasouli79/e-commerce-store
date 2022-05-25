from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import Response
from .models import Product

# Create your views here.


@api_view()
def product_list(request):
    queryset = Product.objects.all()
    return Response('ok')

@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return Response(id)
