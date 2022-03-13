from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.



def main(request):
    return render(request, 'Index.html')

def about_site(request):
    return render(request, 'about_site.html')

def about_klass(request):
    return render(request, 'klass.html')

def tvort(request):
    return render(request, 'tvort.html')

def about_me(request):
    return render(request, 'about_me.html')
