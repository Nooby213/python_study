from django.shortcuts import render, redirect
from .models import Garage

# Create your views here.
def index(request):
    # 전체 차고지 정보
    # Model.manage.querySet API()
    # all 메서드 호출 결과를 garages 변수에 할당하고,
    garages = Garage.objects.all()
    context = {
        'garages': garages
    }
    return render(request, 'garages/index.html', context)

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save()
    return redirect('garages:index')