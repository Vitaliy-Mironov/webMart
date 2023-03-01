from django.shortcuts import render, get_object_or_404
from .models import Subcategory, Product
from .forms import RegisterUserForm, LoginUserForm, ContactForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from cart.forms import CartAddProductForm
from django.http import HttpResponseRedirect


def complete(request):
    data = {
        'title': 'Спасибо за покупку!',
        'description': 'Заказ успешно оплачен. Спасибо за покупку!',
        'h1': 'Заказ успешно оплачен. Спасибо за покупку!',
        'h1_class': 'icon-ok-seccess',
        'bread': '...',
    }

    return render(request, 'complete.html', context=data)


class Contacts(FormView):
    form_class = ContactForm
    template_name = 'contacts.html'
    success_url = 'shop:contacts'

    def get_context_data(self, *args, **kwargs):
        context = super(Contacts, self).get_context_data(*args, **kwargs)
        context['title'] = 'Контакты'
        context['description'] = 'Как с нами связаться. Контактная информация.'
        context['h1'] = 'Контактная информация'
        context['bread'] = 'Контакты'
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('shop:contacts')


def index(request):
    data = {
        'title': 'WebMart',
        'description': 'Интернет-магазин WebMart. Всё продаётся.',
        'h1': 'Добро пожаловать в WebMart!',
        'bread': 'Главная'
    }

    return render(request, 'index.html', context=data)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LoginUser, self).get_context_data(*args, **kwargs)
        context['title'] = 'Вход на сайт'
        context['description'] = 'Вход на сайт'
        context['h1'] = 'Вход на сайт'
        context['h1_class'] = 'icon-user'
        context['bread'] = 'Вход'
        return context

    def get_success_url(self):
        return reverse_lazy('shop:home')


def logout_user(request):
    logout(request)
    # Возврат на страницу, вызвавшую функцию
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RegisterUser, self).get_context_data(*args, **kwargs)
        context['title'] = 'Регистрация'
        context['description'] = 'Регистрация нового пользователя'
        context['h1'] = 'Страница регистрации'
        context['bread'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('shop:registration_success')


def registration_success(request):
    data = {
        'title': 'Успешная регистрация',
        'description': 'Регистрация нового пользователя прошла успешно',
        'h1': 'Успешная регистрация',
        'h1_class': 'icon-ok-seccess',
        'bread': 'Регистрация',
    }

    return render(request, 'success.html', context=data)


def show_category(request, category_slug):
    cat = get_object_or_404(Subcategory, slug=category_slug)
    prods = Product.objects.all().filter(category=cat.id, is_published=True)
    data = {
        'title': cat.name,
        'description': f'{cat.name} в Webmart',
        'h1': cat.name,
        'prods': prods,
        'cat': cat,
        'cart_product_form': CartAddProductForm(),
    }

    return render(request, 'category.html', context=data)


data404 = {
    'title': 'Error 404',
    'description': 'Error 404',
    'h1': 'Страница не найдена. Ошибка 404',
    'bread': '...',
}


def show_product(request, category_slug, product_slug):
    prod = get_object_or_404(Product, slug=product_slug)
    if prod.is_published:
        cat = Subcategory.objects.get(slug=category_slug)
        data = {
            'title': prod.__str__,
            'description': f'{prod.__str__} в Webmart',
            'h1': prod.__str__,
            'prod': prod,
            'rub': prod.get_int_of_prise,
            'kop': prod.get_dec_of_prise,
            'cat': cat,
            'cart_product_form': CartAddProductForm(),
        }
        return render(request, 'product.html', context=data)
    else:
        return render(request, '404.html', status=404, context=data404)


def pageNotFound(request, exception):
    return render(request, '404.html', status=404, context=data404)
