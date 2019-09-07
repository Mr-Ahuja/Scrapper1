from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import StockURL,StockInfoNSE

from .serializers import StockURLSerializer,StockInfoNSESerializer

# Create your views here.
def allstocknames(request):

    stock_names = StockURL.objects.values_list('name', flat=True).all()
    return JsonResponse({"data": list(stock_names)})

class StockURLView(APIView):

    def get(self, request , name = None ):
        if name != None:
            stock_urls = StockURL.objects.filter(name = name)
        else:
            stock_urls = StockURL.objects.all()

        serializer = StockURLSerializer(stock_urls, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        stock = request.data.get('data')

        # Create an article from the above data
        serializer = StockURLSerializer(data=stock)
        if serializer.is_valid(raise_exception=True):
            stock_saved = serializer.save()
        return Response({"success": "Stock URL '{}' add successfully".format(stock_saved.name)})

    def delete(self,request):
        StockURL.objects.all().delete()
        return Response({"message":"Done"})


class StockInfoNSEView(APIView):

    def get(self, request , name = None):
        StockInfoNSE_urls = StockInfoNSE.objects.filter(name = name)
        serializer = StockInfoNSESerializer(StockInfoNSE_urls, many=True)
        return Response({"data": serializer.data})

    def post(self, request , name = None):
        stock = request.data.get('data')

        # Create an article from the above data
        serializer = StockInfoNSESerializer(data=stock)
        if serializer.is_valid(raise_exception=True):
            stock_saved = serializer.save()
        return Response({"success": "Stock URL '{}' add successfully".format(stock_saved.name)})

    def delete(self,request):
        StockInfoNSE.objects.all().delete()
        return Response({"message":"Done"})
