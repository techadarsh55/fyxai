from django.shortcuts import render

# Create your views here.
def index(request):
	
	return render(request,'index.html')

def service(request):

	return render(request, 'service.html')

def about_us(request):

	return render(request,'aboutus.html')