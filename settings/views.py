from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Course, Profile
from .forms import ProfileFrom


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)


def category_page(request):
    category = Course.objects.all()
    context = {'category': category}
    return render(request,'category.html', context)

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(
        user = request.user
    )
    if request.method == 'POST':
        form = ProfileFrom(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileFrom(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/profile.html', context)