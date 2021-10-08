from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
        # context = {
        #         "variable":"this is something"
        # }
        return render(request, 'index.html')
        
#     return HttpResponse("this is home page")

def about(request):
        return render(request, 'about.html')

def cart(request):
        return render(request, 'cart.html')

def contact(request):
        return render(request, 'contact.html')
