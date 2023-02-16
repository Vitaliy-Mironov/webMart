from django.db import models
# from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Наименование',
        )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        null=True,
        verbose_name='Ссылка',
        )
    time_create = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='Добавлен',
        )
    time_update = models.DateTimeField(
        auto_now=True,
        null=True,
        verbose_name='Изменён',
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Наименование',
        )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        null=True,
        verbose_name='Ссылка',
        )
    time_create = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='Добавлена',
        )
    time_update = models.DateTimeField(
        auto_now=True,
        null=True,
        verbose_name='Изменена',
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Color(models.Model):
    name = models.CharField(
        max_length=50,
        db_index=True,
        verbose_name='Цвет',
        )
    time_create = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='Добавлен',
        )
    time_update = models.DateTimeField(
        auto_now=True,
        null=True,
        verbose_name='Изменён',
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвет'


class Gallery(models.Model):
    image = models.ImageField(
        upload_to='',
        verbose_name='Изображение',
        )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='images'
        )

    def __str__(self):
        return f'{self.product.slug}-{self.id}'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class Subcategory(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Наименование',
        )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        null=True,
        verbose_name='Ссылка',
        )
    single_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Штучное наименование',
        )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Категория',
        )
    time_create = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='Добавлена',
        )
    time_update = models.DateTimeField(
        auto_now=True,
        null=True,
        verbose_name='Изменена',
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    category = models.ForeignKey(
        'Subcategory',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Категория',
        )
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Бренд',
        )
    name = models.CharField(
        max_length=255,
        verbose_name='Наименование',
        )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        verbose_name='Ссылка',
        )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Размещ.на сайте',
        )
    article_number = models.CharField(
        max_length=20,
        default='',
        verbose_name='Артикул',
        )
    balance = models.IntegerField(
        default=0,
        verbose_name='Остаток',
        )
    price = models.DecimalField(
        default='0.00',
        max_digits=7,
        decimal_places=2,
        verbose_name='Цена',
        )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        )
    time_create = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='Добавлен',
        )
    time_update = models.DateTimeField(
        auto_now=True,
        null=True,
        verbose_name='Изменён',
        )
    color = models.ForeignKey(
        'Color',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Цвет',
        )

    def get_int_of_prise(self):
        return str(int(self.price))

    def get_dec_of_prise(self):
        return str(self.price).split('.')[-1]

    def __str__(self):
        return f'{str(self.category.single_name)} {str(self.brand)} {self.name}'

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category', 'brand', 'name']


# class User(models.Model):
#     first_name = models.CharField(
#         max_length=100,
#         verbose_name='Имя',
#         )
#     last_name = models.CharField(
#         max_length=100,
#         blank=True,
#         default='',
#         verbose_name='Фамилия',
#         )
#     email = models.EmailField(
#         max_length=100,
#         unique=True,
#         verbose_name='Email',
#         )
#     phone = models.PositiveBigIntegerField(
#         help_text='Только цифры с кодом, например: 375291234567',
#         verbose_name='Мобильный телефон (А1, МТС, life)',
#         )
#     adress = models.CharField(
#         max_length=255,
#         blank=True,
#         default='',
#         verbose_name='Адрес',
#         )
#     password = models.CharField(
#         max_length=20,
#         # help_text='8 - 20 знаков. A-Z, a-z, 0-9, спецсимволы.',
#         verbose_name='Пароль',
#         )
#     time_create = models.DateTimeField(
#         auto_now_add=True,
#         null=True,
#         verbose_name='Добавлен',
#         )
#     time_update = models.DateTimeField(
#         auto_now=True,
#         null=True,
#         verbose_name='Изменён',
#         )
#     favorites = models.ManyToManyField(
#         'Product',
#         blank=True,
#         )

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'

#     class Meta:
#         verbose_name = 'Покупатель'
#         verbose_name_plural = 'Покупатели'
