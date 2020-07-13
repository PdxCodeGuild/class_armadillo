from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import State, City

def index(request):
    
    context = {
        'states': State.objects.order_by('name')
    }
    return render(request, 'main/index_vue.html', context)


# localhost:8000/cities/5/
# localhost:8000/cities/?state_id=5
def cities(request):
    state_id = request.GET['state_id']

    state = State.objects.get(id=state_id)
    # cities = state.cities.all()
    # cities = City.objects.filter(state=state)

    cities = City.objects.filter(state_id=state_id)
    cities = cities.order_by('name')
    cities_json = []
    for city in cities:
        cities_json.append({
            'id': city.id,
            'name': city.name,
        })
    return JsonResponse({'state': state.name, 'cities': cities_json})

