from django.urls import path
from .views import *


urlpatterns = [
    path('list/',TransactionList.as_view()),
    path('excel/',ExcelGenerator.as_view()),
    path('pdf/',PdfGenerator.as_view()),
  
]