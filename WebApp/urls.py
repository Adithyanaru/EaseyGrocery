from WebApp import views
from django.urls import path


urlpatterns=[
    path("home/",views.home,name="home"),
    path("all_products/",views.all_products,name="all_products"),
    path("filtered_product/<cat_name>/",views.filtered_product,name="filtered_product"),
    path("single_item/<product_id>/",views.single_item,name="single_item"),
    path("contact/",views.contact,name="contact"),
    path("save_contact/",views.save_contact,name="save_contact"),
    path("sign_in/",views.sign_in,name="sign_in"),
    path("sign_up/",views.sign_up,name="sign_up"),
    path("save_account/",views.save_account,name="save_account"),
    path("shoping_cart/",views.shoping_cart,name="shoping_cart"),
    path("user_loging/",views.user_loging,name="user_loging"),
    path("user_logout/",views.user_logout,name="user_logout"),
    path("service/",views.service,name="service"),
    path("save_cart/",views.save_cart,name="save_cart"),
    path("check_out/",views.check_out,name="check_out"),
    path("delete_cart/<int:it_id>",views.delete_cart,name="delete_cart"),
    path("save_checkout/",views.save_checkout,name="save_checkout"),

]