from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    API_URL = ''
    API_KEY = ''

    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }
    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
        }
        result.append(info)

    context = {
        'book': result
    }
    return render(request, 'recommend.html', context)