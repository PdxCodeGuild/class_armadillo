from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Tag, Quote

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
            favqs_id = quote_data['id']
            favorited = Quote.objects.filter(favqs_id=favqs_id).exists()
            quotes.append({
                'favqs_id': quote_data['id'],
                'author': quote_data['author'],
                'text': quote_data['body'],
                'tags': quote_data['tags'],
                'favorited': favorited
            })
    context = {
        'page': data['page'],
        'last_page': data['last_page'],
        'quotes': quotes,
    }
    return render(request, 'main/index.html', context)




def save_quote(request):
    quote_data = json.loads(request.body)
    print(quote_data)

    quote = Quote.objects.filter(favqs_id=quote_data['favqs_id']).first()
    if quote is not None:
        quote.delete()
        return HttpResponse('deleted')

    quote = Quote(text=quote_data['text'],
                    author=quote_data['author'],
                    favqs_id=quote_data['favqs_id'])
    quote.save()
    for tag_name in quote_data['tags']:
        tag, created = Tag.objects.get_or_create(name=tag_name)
        quote.tags.add(tag)

    return HttpResponse('saved')


