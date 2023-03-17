from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Brand, Category, Color, Subcategory, Product, Gallery, Order, OrderContent
from django.contrib.auth.models import User

admin.site.site_title = 'WebMart'
admin.site.site_header = 'WebMart'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', )
    search_fields = ('name', )
    # show_full_result_count = False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category')
    search_fields = ('name', )
    list_filter = ('category', )


class GalleryInline(admin.TabularInline):
    model = Gallery
    fk_name = 'product'
    readonly_fields = ('id', 'image_tag',)
    classes = ('collapse', )
    extra = 0
    can_delete = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'article_number')}
    list_display = ('__str__', 'image_show', 'is_published', 'article_number',
                    'balance', 'price',)
    # list_editable = ('is_published',)
    search_fields = ('name', 'article_number',)
    search_help_text = 'Поиск ведётся по наименованию, или артикулу.'
    list_filter = (('is_published', admin.BooleanFieldListFilter),
                   ('description', admin.EmptyFieldListFilter),
                   'category', 'brand')
    show_full_result_count = False
    actions = ['published', 'no_published']
    inlines = [GalleryInline,]

    def image_show(self, obj):
        if obj.images:
            i = obj.images.all()[:1].get()
            return mark_safe("<img src='{}' height='50' />".format(i.image.url))
        return "None"
    image_show.__name__ = 'Изображение'

    @admin.action(description='Разместить товар на сайте')
    def published(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description='Отменить размещение на сайте')
    def no_published(self, request, queryset):
        queryset.update(is_published=False)


class ItemsInline(admin.TabularInline):
    model = OrderContent
    fk_name = 'order'

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'username_show', 'usercontacts_show',
                    'manager_comment', 'total_value', 'status',
                    'is_paid', 'is_delivered', 'time_create', 'time_update')
    search_fields = ('id', )
    search_help_text = 'Поиск по номеру заказа.'
    actions = ['paid', 'no_paid', 'delivered', 'no_delivered']
    inlines = [ItemsInline,]
    readonly_fields = ('customer_id', 'customer_comment', 'total_value',
                       'time_create', 'time_update',)

    def has_add_permission(self, request, obj=None):
        return False

    def username_show(self, obj):
        user = User.objects.get(id=obj.customer_id)
        return f'{user.first_name} {user.last_name} ({user.username})'
    username_show.__name__ = 'Покупатель'

    def usercontacts_show(self, obj):
        user = User.objects.get(id=obj.customer_id)
        return f'{user.email}'
    usercontacts_show.__name__ = 'Контакты'

    @admin.action(description='Заказ оплачен')
    def paid(self, request, queryset):
        queryset.update(is_paid=True)

    @admin.action(description='Заказ не оплачен')
    def no_paid(self, request, queryset):
        queryset.update(is_paid=False)

    @admin.action(description='Заказ доставлен')
    def delivered(self, request, queryset):
        queryset.update(is_delivered=True)

    @admin.action(description='Заказ не доставлен')
    def no_delivered(self, request, queryset):
        queryset.update(is_delivered=False)
