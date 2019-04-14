from django.shortcuts import render, get_object_or_404, redirect
# from .models import DaEun

# # Create your views here.
def main(request):
    # posts = DaEun.objects
    return render (request, 'Hi/main.html')
    

def introduction(request):
    return render(request, 'Hi/introduction.html')