from django.shortcuts import render

def cars_view(request):
    return render(
        request,
        'cars.html',
        {
            'cars': {
                'Toyota': {
                    'model': 'Corolla',
                    'year': 2020,
                    'price': 20000,
                },
            }
        }
        )
