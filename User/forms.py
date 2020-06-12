from django.forms import ModelForm
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["user_bio", "user_pic", "user_background"]

        widget = {
            "user_bio" : forms.TextInput(attrs={"placeholder" : "Add bio"})
        }