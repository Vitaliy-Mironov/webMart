from django import template
from shop.models import Category, Subcategory

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all().order_by('id')


@register.simple_tag()
def get_subcategories(filter=None):
    if not filter:
        return Subcategory.objects.all().order_by('name')
    else:
        return Subcategory.objects.filter(category=filter)
