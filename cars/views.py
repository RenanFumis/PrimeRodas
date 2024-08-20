from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cars.models import Car
from cars.forms import CarForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        search = self.request.GET.get('search')
        
        if search:
            car_main = Car.objects.filter(model__icontains=search).first()
            if car_main:
                queryset = Car.objects.exclude(pk=car_main.pk)
            else:
                queryset = Car.objects.all()
        else:
            car_main = Car.objects.get(pk=1)
            queryset = Car.objects.exclude(pk=car_main.pk).order_by('-value')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search = self.request.GET.get('search')
        no_results_image = '/static/images/no_results.png'

        if search:
            car_main = Car.objects.filter(model__icontains=search).first()
        else:
            car_main = Car.objects.get(pk=1)

        context['car_main'] = car_main
        context['no_results_image'] = no_results_image

        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

class CarsList(ListView):
    model = Car
    template_name = 'cars_list_view.html'
    context_object_name = 'cars'

    def get_queryset(self):
        # No need for search or highlighting, return all cars
        return Car.objects.all()