from django.shortcuts import render

# Create your views here.
def index(request):
    # articles = Articles.objects.all()
    # context = {
    #     'articles':articles
    # }
    return render(request, 'index.html')