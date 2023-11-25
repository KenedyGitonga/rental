from django.urls import path
from .views import car_list, car_detail
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, register, CustomLoginView, CustomLogoutView, dealer_dashboard
from .views import orders, post_vehicle, ReservationListView, ReservationDetailView
# , vehicle_list, earning_history
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('car-list/', car_list, name='car_list'),
    path('car/<int:pk>/', car_detail, name='car_detail'),
    path('dealer/', dealer_dashboard, name='dealer_dashboard'),
    path('orders/', orders, name='orders'),
    path('post_vehicle/', post_vehicle, name='post_vehicle'),
    path('reservations/', ReservationListView.as_view(), name='reservation_list'),
    path('reservation/<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
    # path('vehicle_list/', vehicle_list, name='vehicle_list'),
    # path('earning_history/', earning_history, name='earning_history'),
]
