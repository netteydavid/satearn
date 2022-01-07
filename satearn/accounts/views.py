from django.shortcuts import redirect, render, get_object_or_404
from .forms import NewUserForm, ProfileForm, UserForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('app:login')
    template_name = 'registration/signup.html'

@login_required(login_url='/app/login')
def user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:user')
    user_form = UserForm(instance=request.user)
    return render(request, "registration/user.html", {"user": request.user, "user_form": user_form})

def profile(request, user_id):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:profile', user_id=user_id)
    user = get_object_or_404(get_user_model(), pk=user_id)
    profile_form = ProfileForm(instance=user.profile)
    return render(request, "registration/profile.html", {"is_me": request.user.id == user_id, "user": user, "profile_user": profile_form})

#TODO: Edit profile
#TODO: Edit user account