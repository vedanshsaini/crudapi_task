from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,Productviewset,registerview


router=DefaultRouter()
router.register('user',UserViewSet,basename='user')
router.register('product',Productviewset,basename='products')

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('login/', CustomAuthToken.as_view()),
    path('register/', RegisterView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
]
