from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    car_main = Car.objects.get(pk=1)
    cars = Car.objects.all()
    

    return render(
        request,
        'cars.html',
        {
            'cars': cars,
            'car_main': car_main
        }
            
        )
