from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('staff', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:id>/', views.staff_detail,
         name='dashboard-staff-detail'),
    path('order', views.order, name='dashboard-order'),
    path('product', views.product, name='dashboard-product'),
    path('product/edit/<int:id>/', views.product_edit,
         name='dashboard-product-edit'),
    path('product/delete/<int:id>/', views.product_delete,
         name='dashboard-product-delete'),

]
