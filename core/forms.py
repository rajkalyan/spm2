from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.db import models
from django.forms import fields, widgets
from .models import Products, User,Rolereq

class RegForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Confirm Password"
    }))
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","mobilenumber","address","uimg"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter First Name",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Last name",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Email",
            }),
            "mobilenumber":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Mobile Number",
            }),
            "address":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Address",
            }),
            "uimg":forms.FileInput(attrs={
                "class":"form-control my-2",
            }),

        }

class Chgepwd(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter Old Password"
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter New Password"
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Confirm New Password"
    }))
    class Meta:
        model = User
        fields =  ["old_password","new_password1","new_password2"]

class Pfupd(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","mobilenumber","address","uimg"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
                "readonly":True
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter First Name",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Last name",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Email",
            }),
            "mobilenumber":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Mobile Number",
            }),
            "address":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Address",
            }),
            "uimg":forms.FileInput(attrs={
                "class":"form-control my-2",
            }),

        }

class Rltype(forms.ModelForm):
    class Meta:
        model = Rolereq
        fields= ["uname","rltype","pfe"]
        widgets= {
            # "uname":forms.TextInput(attrs={
            #     "class":"form-control my-2",
            #     "readonly":True,
            # }),
            "rltype":forms.Select(attrs={
                "class":"form-control my-2",

            })
        }

class Rlupd(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","role"]
        widgets= {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":True
            }),
            "role":forms.Select(attrs={
                "class":"form-control my-2"
            })
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['pno','pname','pcost','pimg']
        widgets = {
            "pno":forms.NumberInput(attrs={
                "class": "form-control my-2",
                "placeholder":"Enter The Product Id"
            }),
            "pname":forms.Textarea(attrs= {
                "class":"form-control my-2",
                "placeholder":"Enter the name of the Product",
                "rows":"3"
            }),
            "pcost":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Price"
            }),
            "pimg":forms.FileInput(attrs={
                "class":"form-control my-2"
            })
        }