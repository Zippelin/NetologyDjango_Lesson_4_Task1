from django.core.exceptions import FieldError
from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_field = request.GET.get('sort') or 'name'
    sort_order = request.GET.get('order') or ''
    try:
        phones_data = Phone.objects.all().order_by(sort_order + sort_field)
    except FieldError:
        phones_data = Phone.objects.all().all()
    sort_order = (lambda x: '-' if x == '' else '')(sort_order)
    context = {
        'phones_list': phones_data,
        'order': sort_order,
        'sort': sort_field
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
