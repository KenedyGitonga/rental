from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Reservation
from django.views import View
from django.contrib.auth.decorators import user_passes_test
from .models import Dealer, CarPost, Reservation
from .forms import CarForm
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('car_list')  # Redirect to the car listing page or any other desired page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
def car_list(request):
    # Get a list of available cars
    available_cars = Car.objects.filter(availability=True)

    context = {'cars': available_cars}
    return render(request, 'car/car_list.html', context)

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        # Handle reservation form submission
        if car.availability:
            car.availability = False
            car.save()

            # Create a reservation record
            Reservation.objects.create(car=car, user=request.user)

            return redirect('car_list')

    context = {'car': car}
    return render(request, 'car/car_detail.html', context)

class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'

def is_dealer(user):
    return hasattr(user,'dealer') and user.dealer is not None



@user_passes_test(is_dealer)
def dealer_dashboard(request):
    # Retrieve the current user's dealer instance
    dealer = Dealer.objects.get(user=request.user)

    # Retrieve car posts associated with the dealer
    car_posts = CarPost.objects.filter(dealer=dealer)

    # You can add more logic here to retrieve additional dealer-specific information

    context = {
        'dealer': dealer,
        'car_posts': car_posts,

    }

    return render(request, 'dealer/dealer_dashboard.html', context)

def orders(request):
    # Your logic to get orders data
    orders_data = ...

    return render(request, 'dealer/orders.html', {'orders': orders_data})

def post_vehicle(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = CarForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            car = form.save(commit=False)  # Create a Car instance but don't save it to the database yet
            car.availability = True  # Set availability as needed
            car.save()  # Save the Car instance to the database

            # Redirect to the vehicle list page or another page
            return redirect('car_detail', pk=car.pk)
    else:
        # If the request method is not POST, create a blank form
        form = CarForm()
        return render(request, 'dealer/post_vehicle.html', {'form': form})

class ReservationListView(View):
    def get(self, request):
        reservations = Reservation.objects.all()  # Adjust this based on your model structure
        return render(request, 'car/reservation_list.html', {'reservations': reservations})

class ReservationDetailView(View):
    def get(self, request, pk):
        reservation = Reservation.objects.get(pk=pk)  # Adjust this based on your model structure
        return render(request, 'car/reservation_detail.html', {'reservation': reservation})