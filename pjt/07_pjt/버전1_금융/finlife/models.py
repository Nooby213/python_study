from django.db import models

# Create your models here.
class DepositProducts(models.Model):
  fin_prdt_cd = models.CharField(max_length=2048, unique=True) # 금융 상품 코드
  kor_co_nm = models.TextField()              # 금융 회사명
  fin_prdt_nm = models.TextField()            # 금융 상품명
  etc_note = models.TextField()               # 금융 상품 설명
  join_deny = models.IntegerField()           # 가입제한(1:제한x, 2:서민, 3:일부)
  join_member = models.TextField()            # 가입 대상
  join_way = models.TextField()               # 가입 방법
  spcl_cnd = models.TextField()               # 우대 조건
  
class  DepositOptions(models.Model):
  product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE) # 외래 키(DepositProducts 클래스 참조)
  fin_prdt_cd = models.TextField() # 금융 상품 코드
  intr_rate_type_nm = models.CharField(max_length=100) # 저축금리 유형명
  intr_rate = models.FloatField() # 저축금리
  intr_rate2 = models.FloatField() # 최고우대금리
  save_trm = models.IntegerField() # 저축기간 (단위: 개월)