from django.shortcuts import render, redirect
from .models import Car


def cars_list(request):
    cars = Car.objects.all()
    ctx = {'cars': cars}
    return render(request, 'cars/cars-list.html', ctx)

def cars_form(request):
    car_name = request.POST.get('car_name')
    model = request.POST.get('model')
    year = request.POST.get('year')
    print(car_name, model, year)
    if car_name and model and year:
        Car.objects.create(
        car_name=car_name,
        model=model,
        year=year,
    )
        return redirect('cars:cars_list')
    return render(request, 'cars/cars-form.html')




