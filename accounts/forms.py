from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adını veya şifreyi yanlış girdiniz!")
        return super(LoginForm, self).clean()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    first_name = forms.CharField(max_length=100, label='Ad')
    last_name = forms.CharField(max_length=100, label='Soyad')
    email = forms.CharField(max_length=50, label='Email')
    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)

    #tip = forms.ChoiceField(required=True, choices=[('', '-- Seçiniz --'), ('1', 'İş Veren'), ('2', 'İş Arayan')], initial='2')
    type = forms.CharField(label='Tip')
    bio = forms.ChoiceField(required=False, choices=[('', '-- Seçiniz --'), ('1', 'DevOps Mühendisi'),  ('2', 'Görsel Sanatlar Öğretmeni'), ('3', 'İç Mimar'), ('4', 'Mekatronik Teknisyeyi')], label='Aranan Pozisyon')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'type',
            'bio',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Şifreler eşleşmiyor")
        return