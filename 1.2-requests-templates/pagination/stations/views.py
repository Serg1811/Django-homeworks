import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        stations_info = []
        for row in reader:
            stations_info += [{'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}]
    paginator = Paginator(stations_info, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)
    context = {'page': page}
    return render(request, 'stations/index.html', context)
