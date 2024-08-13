from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.register, name='login'),  # Можно использовать стандартный LoginView
    path('logout/', views.register, name='logout'),  # Можно использовать стандартный LogoutView
    path('bouquets/', views.bouquet_list, name='bouquet_list'),
    path('order/<int:bouquet_id>/', views.order_bouquet, name='order_bouquet'),
    path('order/confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]
