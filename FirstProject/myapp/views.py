from django.shortcuts import render

# Create your views here.


def home_page(request):
	dicts={
		"slogan":"chalo django sikhte hai"
	}
	return render(request,'index.html',dicts)