from django.shortcuts import render
from django.http import HttpResponse


def index(request):
        context_dict = {'boldmessage': "Rango, is, shite"}



        return render(request, 'rango/index.html', context = context_dict)

# Create your views here.


