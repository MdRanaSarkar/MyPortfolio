from django.shortcuts import render

# Create your views here.
def Main(request):
	context={}
	return render(request,'Main.html',context)