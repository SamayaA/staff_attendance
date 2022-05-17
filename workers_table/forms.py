from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='', 
        label_suffix='', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'placeholder':'Логин', 
                'class': 'from-input'
            }
        )
    )
    password = forms.CharField(
        label='', 
        label_suffix='', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Пароль', 
                'class': 'from-input'
            }
        )
    )