from django.shortcuts import render
import requests

from . import secrets

def index(request):
    
    # response = requests.get('https://favqs.com/api/qotd')
    # print(response.json())

    params = {}
    if request.method == 'POST':
        params['filter'] = request.POST['filter_text']
        filter_type = request.POST['filter_type']
        if filter_type != 'quote':
            params['type'] = filter_type
    


    response = requests.get('https://favqs.com/api/quotes', params=params, headers={'Authorization': 'Token token="'+secrets.favqs_api_key+'"'})
    data = response.json()
    quotes = []
    if data['quotes'][0]['body'] != 'No quotes found':
        for quote_data in data['quotes']:
            quotes.append({
                'author': quote_data['author'],
                'text': quote_data['body'],
                'tags': quote_data['tags'],
            })
    context = {
        'page': data['page'],
        'last_page': data['last_page'],
        'quotes': quotes,
    }
    return render(request, 'main/index.html', context)
