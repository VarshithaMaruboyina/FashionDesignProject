
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,render

def mainhomefunction(request):
	return render(request,"mainhome.html")