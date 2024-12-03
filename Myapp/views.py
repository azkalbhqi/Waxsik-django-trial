from django.shortcuts import render, HttpResponse, render, redirect, get_object_or_404
from .models import Car, Service
from .forms import CarForm, ServiceForm

# Create your views here.
from django.shortcuts import redirect

def home(request):
    return render(request, 'carwash/home.html')

def dashboard(request):
    return render(request, 'carwash/dashboard.html')

# Car Views
def car_list(request):
    cars = Car.objects.all()
    services = Service.objects.all()

    # Create a list to store car and its services with calculated prices
    car_with_services = []

    # Loop through each car and its associated services
    for car in cars:
        car_services = []
        for service in services:
            price = service.get_price_by_category(car.category)  # Get price based on car category
            car_services.append({
                'service': service,
                'price': price
            })

        car_with_services.append({
            'car': car,
            'services': car_services
        })

    return render(request, 'carwash/car_list.html', {'car_with_services': car_with_services})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'carwash/car_form.html', {'form': form})


def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'carwash/car_form.html', {'form': form})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('car_list')

# Service Views
def service_list(request):
    services = Service.objects.all()
    return render(request, 'carwash/service_list.html', {'services': services})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'carwash/service_form.html', {'form': form})

def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'carwash/service_form.html', {'form': form})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    return redirect('service_list')