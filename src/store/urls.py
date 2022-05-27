from rest_framework_nested import routers
from . import views

# router = SimpleRouter()
router = routers.DefaultRouter()
router.register('products', views.ProductViewset)


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewset, basename='product_reviews')

urlpatterns = router.urls + products_router.urls 
