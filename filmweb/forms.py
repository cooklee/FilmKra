from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"autocomplete":"off"}))
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError("Hasła się nie zgadzają")


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'groups', 'is_superuser', 'is_active', 'is_staff', 'user_permissions']
        widgets = {
            'user_permissions': forms.CheckboxSelectMultiple
        }



