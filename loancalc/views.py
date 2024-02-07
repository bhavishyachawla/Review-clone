from django.shortcuts import render

# Create your views here.
def loancalc(request):
    return render(request,'loancalc.html')