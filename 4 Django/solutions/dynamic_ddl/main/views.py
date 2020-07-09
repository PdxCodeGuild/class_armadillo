from django.shortcuts import render
from django.http import JsonResponse

from .models import City, State

def index(request):
    context = {
        'states': State.objects.order_by('name')
    }
    return render(request, 'main/index.html', context)


# localhost:8000/get_cities/?state_id=2
def get_cities(request):
    state_id = request.GET['state_id']
    cities = City.objects.filter(state_id=state_id).order_by('name')
    cities_json = []
    for city in cities:
        cities_json.append({
            'id': city.id,
            'name': city.name
        })
    return JsonResponse({'cities': cities_json})