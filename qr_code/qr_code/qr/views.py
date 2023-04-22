from django.shortcuts import render
from .models import Website
# Create your views here.

def qr_codes(request):
    webs = Website.objects.all()
    return render(request , 'qr_codes.html' , {"items" : webs})