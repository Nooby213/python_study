from django.shortcuts import render

# Create your views here.
def index(request):
    work = request.GET.get('work')
    if work == None:
        work = '아직 할 일이 없습니다.'
    context = {
        'work': work
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')