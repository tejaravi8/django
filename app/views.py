from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

# Create your views here.
def addemp(request):
    return render(request,"addemo.html")


@api_view(["POST"])
def created(request):
    data=request.POST.dict()
    print(data)
    return HttpResponse("employ Added")