from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})



def login(response):
    return render(response,'registration/login.html')



def profile(request):
    if request.method == "POST":
        upd_form = UserUpdateForm(request.POST, instance=request.user)
        pf_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if upd_form.is_valid() and pf_form.is_valid():
            upd_form.save()
            pf_form.save()

    else:
        upd_form = UserUpdateForm(instance=request.user)
        pf_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'upd_form': upd_form,
        'pf_form': pf_form
    }
    return render(request, "profile/profile.html", context)
