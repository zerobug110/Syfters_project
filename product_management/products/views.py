from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


from .models import Product, New, LatestNew, About 

# Create your views here.

def Home(request):
    products = Product.objects.all()
    
    context = {
        'products':products, 
        
    }

    products = LatestNew.objects.all()
    return render(request, 'index.html', {'products':products, 'latestnew':products})


def portfolio(request,):
    products = Product.objects.all()
    return render(request, 'properties.html',{'products':products})

def news(request):
    products = New.objects.all()
    return render(request, 'news.html', {'products':products})

def contacts(request):
    products = LatestNew.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message,settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
        # return render(request, 'products/email_sent.html', {'email': email})
    return render(request, 'contact.html', {'products':products})
    
def about(request):
    products = About.objects.all()
    return render(request, 'about.html', {'products':products})

def details(request,pk):
    eachproduct = Product.objects.get(id = pk)

    context = {
        'eachproduct':eachproduct
        
    }
    return render(request, 'details.html', context)


