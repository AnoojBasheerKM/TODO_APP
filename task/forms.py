from django import forms

from django.contrib.auth.forms import UserCreationForm

from task.models import User,Todo

class SignUpForm(UserCreationForm):
    
    class Meta():
        
        model = User
        
        fields = ["username","password1","password2","phone","email"]
        
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            
            
        }
        
class SignInForm(forms.Form):
    
    user_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
class TodoForm(forms.ModelForm):
    
    class Meta:
        
        model = Todo
        
        fields = ["title"]
        
        