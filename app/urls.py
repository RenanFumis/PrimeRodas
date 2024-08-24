from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView, CarsList, RegisterView, CongratulationsView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', CarsListView.as_view(), name='cars_list'),

    path('cars/', CarsListView.as_view(), name='cars_list'),

    path('cars_list/', CarsList.as_view(), name='cars_list_view'),

    path('new_car/', NewCarCreateView.as_view(), name='new_car'),

    path('register/', register_view, name='register'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),

    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),

    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    
    path('accounts_register/', RegisterView.as_view(), name='accounts_register'),

    path('congratulations/', CongratulationsView.as_view(), name='congratulations'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #aqui no static, estamos dizendo que se a url for para media, ele vai procurar no MEDIA_ROOT
