from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Salon, Service, Worker


def get_index(request):
    salons = Salon.objects.all()
    services = Service.objects.all()
    masters = Worker.objects.all()

    context = {'salons': [
        {
            'name': salon.name,
            'address': salon.address,
            'image': salon.image
         }
        for salon in salons],
        'services': [
        {
            'name': service.name,
            'price': service.price,
            'image': service.image
         }
        for service in services],
        'masters': [
        {
            'name': master.name,
            'specialization': master.specialization,
            'image': master.foto,
            'experience': master.experience,
            'reviews_qty': master.reviews_qty
         }
        for master in masters]
    }

    return render(request, template_name="index.html", context=context)