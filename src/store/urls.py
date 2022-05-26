from django.urls import path 
from . import views
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProdcutDetail.as_view())
]