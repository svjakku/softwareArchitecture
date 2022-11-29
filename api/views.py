from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
#def homePageView(request):
#     'Message': 'HelloWorld!'
#  }
# return JsonResponse(data)

def homePageView(request):
   return render(request, 'helloworld.html')
