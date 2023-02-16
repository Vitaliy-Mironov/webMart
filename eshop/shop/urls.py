from django.urls import path
from shop import views
from .views import RegisterUser, LoginUser, Contacts


app_name = 'shop'
urlpatterns = [
    path('',
         views.index,
         name='home'),
    path('contacts/',
         Contacts.as_view(),
         name='contacts'),
    path('login/',
         LoginUser.as_view(),
         name='login'),
    path('logout/',
         views.logout_user,
         name='logout'),
    path('registration/',
         RegisterUser.as_view(),
         name='registration'),
    path('registration/success/',
         views.registration_success,
         name='registration_success'),
    path('<slug:category_slug>/',
         views.show_category,
         name='category'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.show_product,
         name='product'),
]
