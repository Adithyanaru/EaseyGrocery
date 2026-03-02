from django.urls import path
from AdminApp import views


urlpatterns=[
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_products/',views.add_products,name='add_products'),
    path('view_products/',views.view_products,name='view_products'),
    path('delete_product/<int:p_id>/',views.delete_product,name='delete_product'),
    path('update_product/<int:pro_id>/',views.update_product,name='update_product'),
    path('edit_product/<int:pro_id>/', views.edit_product, name='edit_product'),




    #--------Category----------------


    path('add_catagory/',views.add_catagory,name='add_catagory'),
    path('view_catagory/',views.view_catagory,name='view_catagory'),
    path('save_category/',views.save_category,name='save_category'),
    path('delete_category/<int:cat_id>',views.delete_category,name='delete_category'),
    path('edit_category/<int:cat_id>',views.edit_category,name='edit_category'),
    path('update_category/<int:catg_id>/',views.update_category,name='update_category'),





    path('',views.login,name='login'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('save_category/', views.save_category, name='save_category'),

    path('save_product/',views.save_product,name='save_product'),


    path('contact_details/',views.contact_details,name='contact_details'),

]