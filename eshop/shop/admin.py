from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Brand, Category, Color, Subcategory, Product, Gallery

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
    fk_name = 'product'
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'article_number')}
    list_display = ('__str__', 'image_show', 'is_published', 'article_number',
                    'balance', 'price',)
    list_editable = ('is_published',)
    search_fields = ('name', 'article_number',)
    list_filter = (('is_published', admin.BooleanFieldListFilter),
                   ('description', admin.EmptyFieldListFilter),
                   'category', 'brand')
    search_help_text = 'Поиск ведётся по наименованию, или артикулу.'
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
