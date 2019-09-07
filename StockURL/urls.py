
from django.urls import path

from .views import StockURLView,StockInfoNSEView
from . import views

app_name = "StockURL"

urlpatterns = [
    path('stocks/', views.allstocknames ),
    path('stockurl/<str:name>', StockURLView.as_view()),
    path('stockurl/', StockURLView.as_view()),
    path('stockinfo/<str:name>', StockInfoNSEView.as_view()),
    path('stockinfo/', StockInfoNSEView.as_view()),
]