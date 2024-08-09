from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.views import View
from django.views.generic import ListView, CreateView

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

class NewCarView(View):

    def get(self, request):
        new_car_form = CarForm()
        return render(
            request,
            'new_car.html',
            {
                'new_car_form': new_car_form,
            }
            )
    
    def post(self, request):
            new_car_form = CarForm(request.POST, request.FILES)
            if new_car_form.is_valid():
                new_car_form.save()
                return redirect('cars_list')
            return render(
                request,
                'new_car.html',
                {
                    'new_car_form': new_car_form,
                }
                )
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'