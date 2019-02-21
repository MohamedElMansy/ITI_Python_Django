from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_custom


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')



class ImgForm(forms.ModelForm):

    class Meta:
        model = User_custom
        fields = ('user_img',)