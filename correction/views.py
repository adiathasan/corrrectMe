from django.shortcuts import render

# Create your views here.


def HomePage(request):
    return render(request, 'correction/base.html')