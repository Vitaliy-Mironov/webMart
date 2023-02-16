from django import forms
# from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        label='Фамилия', required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Повтор пароля', required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password1',)


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=150)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(
        attrs={'cols': 60, 'rows': 2}))
    captcha = CaptchaField(label='Защита от спама. Напишите ответ на уравнение:')


# class RegForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'password', 'adress',
#                   'phone')

#     def clean_phone(self):
#         phone = self.cleaned_data['phone']
#         number = str(phone)
#         codes = ['25', '29', '33', '44']
#         check = bool(
#             len(number) == 12
#             and number[0:3] == '375'
#             and number[3:5] in codes
#             )
#         if not check:
#             raise ValidationError('Номер телефона указан неверно.')
#         return phone

#     def clean_password(self):
#         password = self.cleaned_data['password']
#         if ' ' in password:
#             raise ValidationError('Пароль не должен содержать пробелы.')
#         check1 = bool(len(password) >= 8)
#         if not check1:
#             raise ValidationError('Пароль слишком короткий.')
#         check2 = bool(len(password) < 21)
#         if not check2:
#             raise ValidationError('Пароль слишком длинный.')
#         alphabet = {'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
#                     'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
#                     'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'}
#         check3 = bool(alphabet.intersection(set(password.lower())))
#         if check3:
#             raise ValidationError(
#                 'Пароль не должен содержать символы русского алфавита.')
#         return password
