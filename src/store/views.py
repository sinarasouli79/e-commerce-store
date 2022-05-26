from rest_framework.viewsets import ModelViewSet
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer

# Create your views here.

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewViewset(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer