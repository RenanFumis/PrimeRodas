from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from gemini_api.client import get_car_ai_bio, get_summary_car

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.description:
        ai_description = get_car_ai_bio(instance.model, instance.brand, instance.model_year)
        instance.description = ai_description

    if not instance.summary_car:
        ai_summary = get_summary_car(instance.model, instance.brand, instance.model_year)
        instance.summary_car = ai_summary

@receiver(post_save, sender=Car)
def car_post__save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post__delete(sender, instance, **kwargs):
    car_inventory_update()
