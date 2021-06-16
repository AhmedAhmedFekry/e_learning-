from django import forms
from courses.models import Course
from usersapp.models import User
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)



class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email', 'birth_date','profile_image')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'birth_date', 'is_active')
        

   
#  first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=30, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#     receive_newsletter = models.BooleanField(default=False)
#     birth_date = models.DateTimeField(blank=True, null=True)
#     address = models.CharField(max_length=300,  blank=True, null=True)
#     city = models.CharField(max_length=30, blank=True, null=True)
#     about_me = models.TextField(max_length=500, blank=True, null=True)
#     profile_image = models.ImageField(blank=True, null=True)
