from django.urls import path
from .views import RegisterView, \
    CustomLoginView, CustomLogOutView, AddingCustomerView, \
    UpdateCustomerView, CustomerListView, \
    CustomerRecordView, DeleteCustomerView, \
    LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    # path('home/', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('custom_login/', CustomLoginView.as_view(), name='custom_login'),
    path('custom_logout/', CustomLogOutView.as_view(), name='custom_logout'),
    path('customer_list/', CustomerListView.as_view(), name='customer_list'),
    path('customer_record/<int:id>/', CustomerRecordView.as_view(), name='customer_record'),
    path('add_customer/', AddingCustomerView.as_view(), name='add_customer'),
    path('update_customer/<int:id>/', UpdateCustomerView.as_view(), name='update_customer'),
    path('delete_customer/<int:id>/', DeleteCustomerView.as_view(), name='delete_customer'),
]