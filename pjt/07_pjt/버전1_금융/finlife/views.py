from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse
from .models import DepositOptions, DepositProducts
from .serializer import DepositOptionsSerializer, DepositProductsSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
API_KEY = settings.API_KEY

@api_view(['GET'])
def save_deposi_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json().get('result')
    
    for base_item in response.get('baseList'):
        fin_prdt_cd = base_item.get('fin_prdt_cd')

        for key, value in base_item.items():
            if not value:
                if key == 'join_deny':
                    base_item[key] = -1
                else:
                    base_item[key] = ''

        deposit_product, created = DepositProducts.objects.update_or_create(
            fin_prdt_cd=fin_prdt_cd,
            defaults={
                'kor_co_nm': base_item.get('kor_co_nm'),
                'fin_prdt_nm': base_item.get('fin_prdt_nm'),
                'etc_note': base_item.get('etc_note'),
                'join_deny': int(base_item.get('join_deny')),
                'join_member': base_item.get('join_member'),
                'join_way': base_item.get('join_way'),
                'spcl_cnd': base_item.get('spcl_cnd'),
            }
        )

        options = [opt for opt in response.get('optionList') if opt['fin_prdt_cd'] == fin_prdt_cd]

        for option in options:
            for key, value in option.items():
                if not value:
                    if key in ('fin_prdt_cd', 'intr_rate_type_nm'):
                        option[key] == ''
                    else:
                        option[key] = -1

            DepositOptions.objects.create(
                product=deposit_product,
                fin_prdt_cd=fin_prdt_cd,
                intr_rate_type_nm=option.get('intr_rate_type_nm'),
                intr_rate=option.get('intr_rate'),
                intr_rate2=option.get('intr_rate2'),
                save_trm=option.get('save_trm'),
            )

    return JsonResponse({'message':'okay'})



@api_view(['GET', 'POST'])
def deposit_products(request):
  if request.method == 'GET':
    products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(products, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = DepositProductsSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'message':"이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."})

@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
  product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
  serializer = DepositProductsSerializer(product)
  return Response(serializer.data)

@api_view(['GET'])
def top_rate(request):
    options = DepositOptions.objects.order_by('intr_rate2')
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)
    