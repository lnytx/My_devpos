from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'login.html')
def current(request):
    return render(request,'current_datetme.html')