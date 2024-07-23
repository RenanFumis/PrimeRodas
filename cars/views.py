from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    car_main = Car.objects.get(pk=1)
    cars = Car.objects.exclude(pk=car_main.pk)
    search = request.GET.get('search')

    if search:
        car_main = Car.objects.filter(model__contains=search).first()  # Substitui o car_main pelo primeiro resultado da busca
        cars = Car.objects.exclude(pk=car_main.pk) if car_main else Car.objects.all()
    else:
        cars = Car.objects.exclude(pk=car_main.pk)
    
    return render(
        request,
        'cars.html',
        {
            'cars': cars,
            'car_main': car_main,
            
        }
            
        )
