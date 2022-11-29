The steps to execute this lab are as below:

Step 1: Run below command in terminal to install django
pip3 install django

Step 2: Creating django api
django-admin startproject hello_world_api

Step 3: Change the directory to hello_world_api
cd hello_world_api

Step 4: Start the api
python3 manage.py startapp api

Step 5: Add 'api' in INSTALLED_APPS array of settings.py file

Step 6: Navigate to hello_world_api > api > views.py
views.py code is as below:

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def homePageView(request):
    data = {
       'Message': 'HelloWorld!'
    }
    return JsonResponse(data)
    
Step 7: Start the server
python3 manage.py runserver

Step 8: Go to web browser and type 'http://127.0.0.1:8000/' in the URL
Below output will be displayed:
{"Message": "HelloWorld!"}

To push code to git:

Step 1: Create the repository on github Ex: softwareArchitecture

Step 2: Navigate to hello_world_api and type below command in terminal
git remote add origin https://github.com/svjakku/softwareArchitecture.git

Step 3: Type below command to push code into main branch
git branch -M main

Step 4: Type below command to push code into repo
git push -u origin main

Step 5: Enter username and personal access token

Code is pushed successfully.

