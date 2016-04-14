from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'cont': ['If you would like to contact me, please email me:', 'dariusz.swiderski@protonmail.com']})