from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Application, Bounty
from .forms import BountyForm
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
    application_id = -1
    
    applications = Application.objects.filter(applicant=request.user, bounty=bounty)
    if applications.count() > 0:
        application_id = applications[0].id

    return render(request, 'app/bounty.html', {'bounty': bounty, 'applied': application_id})

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

@login_required(login_url='/app/login')
def apply(request, bounty_id):
    if request.method == 'POST':
        bounty = get_object_or_404(Bounty, pk=bounty_id)
        applications = Application.objects.filter(applicant=request.user, bounty=bounty)
        if applications.count() < 1:
            application = Application(applicant=request.user, bounty=bounty)
            application.save()
    return redirect("app:bounty", bounty_id=bounty_id)

@login_required(login_url='/app/login')
def unapply(request, bounty_id, application_id):
    if request.method == 'POST':
        application = get_object_or_404(Application, pk=application_id)
        if application.applicant == request.user:
            application.delete()
        
    return redirect("app:bounty", bounty_id=bounty_id)