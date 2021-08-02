from django.core.checks import messages
from django.shortcuts import redirect, render
from fastfood import settings
from home.models import Dish, Subscriber
from django.contrib import messages

def subscribe(request):
    if request.method == "POST":
        data = request.POST['email']
        if Subscriber.objects.filter(subscriber_email=data).exists():
            messages.info(request,'Email Already Exists')
            return redirect('subscribe')
        else:
            subscribe = Subscriber(subscriber_email=data)
            subscribe.save()
            return redirect('subscribe')
    return render(request, 'home/index.html', {"BASE_URL": settings.BASE_URL})


def home(request):
    dish = None
    dish = Dish.objects.all()
    data = {}
    data['BASE_URL'] = settings.BASE_URL
    data['dish'] = dish
    return render(request, 'home/index.html',data)

def order(request):
    return render(request, 'home/order.html', {"BASE_URL": settings.BASE_URL})


def about(request):
    return render(request, 'home/about.html', {"BASE_URL": settings.BASE_URL})


def contact(request):
    return render(request, 'home/contacts.html', {"BASE_URL": settings.BASE_URL})


def menu(request):
    return render(request, 'home/menu.html', {"BASE_URL": settings.BASE_URL})


def news(request):
    return render(request, 'home/news.html', {"BASE_URL": settings.BASE_URL})


def portfolio(request):
    return render(request, 'home/portfolio.html', {"BASE_URL": settings.BASE_URL})
