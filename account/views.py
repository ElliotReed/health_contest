from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import UserAccount
from .forms import UserAccountForm, UserAccountCreationForm


def accountLogin(request):
    if request.user.is_authenticated:
        return redirect("contest:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = UserAccount.objects.get(email=email)
        except:
            messages.error(request, "UserAccount does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("contest:index")
        else:
            messages.error(request, "Username Or password does not exist")

    context = {}
    return render(request, "account/login.html", context)


def accountLogout(request):
    logout(request)
    return redirect("contest:index")


def accountRegister(request):
    form = UserAccountCreationForm(auto_id=True)

    if request.method == "POST":
        form = UserAccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("contest:index")
        else:
            messages.error(request, "Invalid information")

    context = {"form": form}
    return render(request, "account/register.html", context)


def index(request):
    context = {}

    return render(request, "account/index.html", context)


@login_required(login_url="account/login")
def accountProfile(request, pk):
    user = request.user
    form = UserAccountForm(instance=user)

    if request.method == "POST":
        form = UserAccountForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("account:profile", pk=user.id)

    context = {"form": form}
    return render(request, "account/profile.html", context)
