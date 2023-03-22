from django import forms
from django.contrib.auth.models import User
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationFoorm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeFoorm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтвердение пароля", widget=forms.PasswordInput)

    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароль не совпадают!")
        
        return cd["password2"]


    class Meta:
        model = CustomUser
        fields = ("email",)

    