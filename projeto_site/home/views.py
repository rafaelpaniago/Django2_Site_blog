from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contato(request):
    return render(request, 'home/contato.html')