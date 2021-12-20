from django import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from .models import Bounty, BountyForm
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/app/login')
def create(request):
    BountyFormSet = modelform_factory(
        Bounty, form=BountyForm, 
        fields = ('title', 'description', 'reward', 'due_date'), 
        localized_fields = ('due_date',)
    )
    if request.method == 'POST':
        formset = BountyFormSet(request.POST, request.FILES)
        if formset.is_valid():
            bounty = formset.save(commit=False)
            bounty.author = request.user
            bounty.save()
    else:
        bounty = Bounty(author=request.user)
        formset = BountyFormSet(instance=bounty)
    return render(request, 'app/create.html', {'formset': formset})