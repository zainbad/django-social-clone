from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    user = request.user
    context={
        'user': user,
        'hi': 'Hi,',
    }
    return render(request, 'main/home.html', context)