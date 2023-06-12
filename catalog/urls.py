from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('category/<int:pk>', views.get_category_product),
    path('product/<str:name>/<int:pk>', views.get_exact_product),
    path('add-product-to-cart/<int:pk>', views.add_pr_to_cart),
    path('cart', views.user_cart),
    path('del_item/<int:pk>', views.delete_from_cart)
]

