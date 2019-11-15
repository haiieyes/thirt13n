from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.template.html')
    
def shop(request):
    return render(request, 'shop.template.html')