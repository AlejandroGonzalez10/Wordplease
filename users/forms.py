from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignupForm(forms.Form):
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="Email de usuario", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
