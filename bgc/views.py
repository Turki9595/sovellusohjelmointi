from django.shortcuts import render

# Create your views here.
def index(request):
    #homepage
    return render(request, 'bgc/index.html')