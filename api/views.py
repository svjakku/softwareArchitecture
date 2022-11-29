from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def homePageView(request):
    data = {
       'Message': 'HelloWorld!'
    }
    return JsonResponse(data)
