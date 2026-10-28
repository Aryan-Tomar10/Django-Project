from django.urls import path, re_path
from . import views

urlpatterns = [
    path('buy/<int:buy_id>/', views.buy_detail,name = "shop-buy-detail"),
    path('name/<str:username>/', views.user_profile,name = "user_profile-detail"),
    re_path(r'^section/(?P<year>[0-9]{4})/$',views.section_by_years,name = "section-by-year")
]