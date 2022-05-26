from rest_framework.routers import DefaultRouter
from . import views

# router = SimpleRouter()
router = DefaultRouter()
router.register('products', views.ProductViewset)
urlpatterns = router.urls