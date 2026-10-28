from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:buy_id>/', views.buy_detail,name = "shop-buy-detail"),
    path('name/<str:username>/', views.user_profile,name = "user_profile-detail")
]