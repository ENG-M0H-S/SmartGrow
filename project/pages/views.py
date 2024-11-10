from django.shortcuts import render
# Create your views here.


def index(request):
   x={'name':'mohammed','age':22}
   return render(request, 'pages/index.html',x)

def about(request):
   return render(request, 'pages/about.html')