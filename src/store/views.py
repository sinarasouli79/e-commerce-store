from rest_framework.viewsets import ModelViewSet
from .models import Product, Reviews
from .serializers import ProductSerializer, ReviewSerializer

# Create your views here.

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewViewset(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

