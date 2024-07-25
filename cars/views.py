from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    car_main = Car.objects.get(pk=1)
    cars = Car.objects.exclude(pk=car_main.pk)
    search = request.GET.get('search')
    no_results_image = '/static/images/no_results.png'  # Tratamento de quando não há o modelo pesquisado

    if search:
        car_main = Car.objects.filter(model__icontains=search).first()  # Substitui o carro principal pelo primeiro resultado da busca
        if car_main:
            cars = Car.objects.exclude(pk=car_main.pk)
        else:
            cars = Car.objects.all()
            car_main = None  # Define car_main como None se não houver o modelo buscado
    else:
        cars = Car.objects.exclude(pk=car_main.pk).order_by('-value')  # Ordena os carros pelo valor do maior para o menor

    return render(
        request,
        'cars.html',
        {
            'cars': cars,
            'car_main': car_main,
            'no_results_image': no_results_image,
        }
    )
