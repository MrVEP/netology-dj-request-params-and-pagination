import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


with open('data-398-2018-08-30.csv', newline='', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    CONTENT = []
    for row in reader:
        CONTENT.append(row['ID'])


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    ids = [id for id in page]
    with open('data-398-2018-08-30.csv', newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = []
        for row in reader:
            if row['ID'] in ids:
                stations.append(row)
    context = {
         'bus_stations': stations,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
