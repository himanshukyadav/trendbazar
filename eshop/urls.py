from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('register',views.register,name="register"),
    path('collections',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pid>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('cart',views.cart_page,name="cart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('contact',views.contact,name="contact"),
    path('user',views.user_profile,name="user")
]