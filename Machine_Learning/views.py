from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def Machine_Learning(request):
    f_name = "Mainul Islam"
    l_name = "Mahi"
    Address = "Chittagong, Bangladesh"
    Age = 25
    return render(request,'Machine Learning/Machine_Learning.html', context={'first_name':f_name, 'last_name':l_name,'age':Age, 'address':Address})

def Decison (request):
    return render(request,'Machine Learning/DT.html')