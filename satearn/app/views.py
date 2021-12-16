from django import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from .models import Bounty

def index(request):
    latest_bounties = Bounty.objects.order_by('-created_on')[:5]
    context = {
        'latest_bounties': latest_bounties,
    }
    return render(request, 'app/index.html', context)

def bounty(request, bounty_id):
    bounty = get_object_or_404(Bounty, pk=bounty_id)
    return render(request, 'app/bounty.html', {'bounty': bounty})

def invoice(request, bounty_id):
    response = "You're looking at the invoice of bounty %s"
    return HttpResponse(response % bounty_id)