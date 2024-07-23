from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    car_main = Car.objects.get(pk=1)
    cars = Car.objects.exclude(pk=car_main.pk)
    search = request.GET.get('search')

    if search:
        car_main = Car.objects.filter(model__icontains=search).first()  #Substitui o carro princcipal pelo primeiro resultado da busca
        cars = Car.objects.exclude(pk=car_main.pk) if car_main else Car.objects.all()
    else:
        cars = Car.objects.exclude(pk=car_main.pk).order_by('-value')#Ordena os carros pelo valor do Maior para o Menor
    
    return render(
        request,
        'cars.html',
        {
            'cars': cars,
            'car_main': car_main,
            
        }
            
        )
