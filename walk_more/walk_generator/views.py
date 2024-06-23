from django.shortcuts import render
from .forms import RouteForm
from .utils import generate_random_location, generate_walking_route
from django.templatetags.static import static
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def route_generator(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            time = form.cleaned_data['time']
            radius = 1000  # Adjust the radius based on the time input
            destination = generate_random_location(location, radius)
            route_result = generate_walking_route(location, destination)
            if route_result:
                route_steps, distance = route_result
                context = {
                    'form': form,
                    'destination': destination,
                    'distance': distance,
                    'steps': route_steps,
                }
            else:
                context = {
                    'form': form,
                    'error': 'No walking route found',
                }
            return render(request, 'routes.html', context)
    else:
        form = RouteForm()
    return render(request, 'routes.html', {'form': form})