from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ListingViewSet, ProductViewSet 

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
