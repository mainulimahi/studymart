from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Data_Analysis(request):
    return render(request,'Data Analysis/data_analysis.html')