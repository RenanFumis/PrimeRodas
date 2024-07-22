from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    car_main = Car.objects.get(pk=1)
    cars = Car.objects.exclude(pk=car_main.pk)
    filters = Car.objects.filter(model__contains='C')
    print(filters)
    

    return render(
        request,
        'cars.html',
        {
            'cars': cars,
            'car_main': car_main,
            'filters': filters
        }
            
        )
