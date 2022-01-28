import imp
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Application, Bounty
from .forms import BountyForm
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from urllib import parse

def index(request):
    latest_bounties = Bounty.objects.order_by('-created_on')[:5]
    context = {
        'latest_bounties': latest_bounties,
    }
    return render(request, 'app/index.html', context)

def browse(request):
    bounties = Bounty.objects.order_by('-created_on')
    #TODO: Pagination
    context = {
        'bounties': bounties
    }
    return render(request, 'app/browse.html', context)

def bounty(request, bounty_id):
    bounty = get_object_or_404(Bounty, pk=bounty_id)

    if request.method == 'POST' and bounty.status == Bounty.NEW:
        bounty_form = BountyForm(request.POST, instance=bounty)
        if bounty_form.is_valid():
            bounty_form.save()
            return redirect('app:bounty', bounty_id=bounty_id)

    bounty_form = BountyForm(instance=bounty)

    application_id = -1
    applications = []

    if request.user.is_authenticated and bounty.status == Bounty.NEW:
        applications = Application.objects.filter(bounty=bounty)

    if request.user.is_authenticated:
        my_application = Application.objects.filter(applicant=request.user, bounty=bounty)
        if my_application.count() > 0:
            application_id = my_application[0].id

    context = {
        'bounty': bounty, 
        'bounty_form': bounty_form, 
        'applications': applications, 
        'application_id': application_id, 
        'is_me': request.user == bounty.author,
    }

    return render(request, 'app/bounty.html', context)

@login_required(login_url='/app/login')
def create(request):
    if request.method == 'POST':
        bounty_form = BountyForm(request.POST)
        if bounty_form.is_valid():
            bounty = bounty_form.save(commit=False)
            bounty.author = request.user
            bounty.save()
            return redirect("app:bounty", bounty_id=bounty.id)

    bounty = Bounty(author=request.user)
    bounty_form = BountyForm(instance=bounty)
    return render(request, 'app/create.html', {'bounty_form': bounty_form})

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
def unapply(request, application_id):
    if request.method == 'POST':
        application = get_object_or_404(Application, pk=application_id)
        if application.applicant == request.user:
            application.delete()
            
    return redirect("app:bounty", bounty_id=application.bounty.id)

@login_required(login_url='/app/login')
def unapply_jobs(request, application_id):
    if request.method == 'POST':
        application = get_object_or_404(Application, pk=application_id)
        if application.applicant == request.user:
            application.delete()
            
    return redirect("app:my_jobs")

@login_required(login_url='/app/login')
def my_bounties(request):
    bounties = Bounty.objects.order_by('-created_on').filter(author=request.user)
    context = {
        'bounties': bounties,
    }
    return render(request, 'app/my_bounties.html', context)

@login_required(login_url='/app/login')
def my_jobs(request):
    applied = Application.objects.filter(applicant=request.user, bounty__status=Bounty.NEW, bounty__assigned_to=None)
    working = Application.objects.filter(applicant=request.user, bounty__status=Bounty.WORKING, bounty__assigned_to=request.user)
    completed = Application.objects.filter(applicant=request.user, bounty__status=Bounty.COMPLETE, bounty__assigned_to=request.user)
    cancelled = Application.objects.filter(applicant=request.user, bounty__status=Bounty.CANCELLED, bounty__assigned_to=request.user)

    context = {
        'applied': applied,
        'working': working,
        'completed': completed,
        'cancelled': cancelled,
    }
    return render(request, 'app/my_jobs.html', context)

@login_required(login_url='/app/login')
def select_applicant(request, application_id):
    if request.method == 'POST':
        application = get_object_or_404(Application, pk=application_id)
        bounty: Bounty = application.bounty
        bounty.assigned_to = application.applicant
        bounty.status = Bounty.WORKING
        bounty.save()
        return redirect("app:bounty", bounty_id=bounty.id)

@login_required(login_url='/app/login')
def delete_bounty(request, bounty_id):
    if request.method == 'POST':
        bounty = get_object_or_404(Bounty, pk=bounty_id)
        if bounty.author == request.user:
            bounty.delete()
    return redirect("app:my_bounties")