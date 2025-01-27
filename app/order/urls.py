from django.urls import path


from order import views

app_name = 'order'

urlpatterns = [
    path('', views.order, name='order'),
    path('order-list', views.orderList, name='order_list'),
    path('order-item/<int:id>/', views.orderItem, name='order_item'),
    ]