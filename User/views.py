from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Forms
from .forms import UserProfileForm
# Models 
from .models import UserProfile
# Create your views here.

@login_required(login_url="/login")
def new_user(request):

    user = request.user
    
    if user.userprofile:
        return redirect("/profile")

    if request.method == "POST":
        user_profile_form = UserProfileForm(request.POST, request.FILES)
        if user_profile_form.is_valid():
            user_profile_instance = user_profile_form.save(commit=False)
            user_profile_instance.user = request.user
            user_profile_instance.save()
            return redirect("/")
    else:
        user_profile_form = UserProfileForm()

    
    context = {"user_profile_form" : user_profile_form, "user" : user}

    return render(request, "new_user.html", context)

@login_required(login_url="/login")
def profile(request, pk=None):
        # User Profile

    if pk:
        user = User.objects.get(pk=pk)
    
    else:
        user = request.user

 

    user_related = UserProfile.objects.get(user=request.user)
    user_products = user_related.product.all()


    context = {"user" : user, "user_products" : user_products,}
    return render(request, "user_profile.html", context)