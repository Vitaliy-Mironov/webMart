from django.db import models


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
