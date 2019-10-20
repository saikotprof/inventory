from django.urls import path
from .views import index, product, apple, xiaomi, samsung

urlpatterns = [
    path('', index, name='home'),
    path('product-details/', product, name='product-details'),
    path('apple/', apple, name='apple'),
    path('samsung/', samsung, name='samsung'),
    path('xiaomi/', xiaomi, name='xiaomi'),
]
