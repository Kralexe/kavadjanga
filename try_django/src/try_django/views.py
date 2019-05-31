from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    context = {'title': 'example'}
    template_name = 'hellow_world.html'
    template_obj = get_template(template_html)
    rendered_item = template_object.render(context)
    return HttpResponse(rendered_item)