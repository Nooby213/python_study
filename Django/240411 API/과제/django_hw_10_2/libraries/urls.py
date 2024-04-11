from django.urls import path
from . import views

urlpatterns = [
    path('libraries/', views.libraries),
    path('libraries/<int:book_pk>/', views.detail),
]
