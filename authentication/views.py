from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from imdbuser.models import BaseUser
from authentication.forms import SignUpForm, LoginForm
from thecapstone.settings import AUTH_USER_MODEL

def index(request):
    my_user = BaseUser.objects.all()
    return render(request, "index.html", {'my_user': my_user, "output": AUTH_USER_MODEL})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_user = BaseUser.objects.create_user(username=data.get("username"), password=data.get("password"), display_name=data.get("display_name"), user_pic=data.get("user_pic"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    form = SignUpForm()
    return render(request, "generic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                # return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
                return HttpResponseRedirect(reverse("homepage"))
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))