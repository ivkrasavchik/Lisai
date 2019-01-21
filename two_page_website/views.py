from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from landing.forms import ZvonkiForm, QuestionsForm
from landing.models import Company


def home(request):
    args = {}
    args['Text'] = "TEST TEST TEST TEST"
    return render(request, 'two_page_website/t_home.html', args)


def cond(request):
    args = {}
    args['Text'] = "TEST TEST TEST TEST"
    # args['cat_id'] = ProductCategory.objects.get(id=c_id)
    return render(request, 'two_page_website/conditions.html', args)

def vent(request):
    args = {}
    args['Text'] = "TEST TEST TEST TEST"
    # args['cat_id'] = ProductCategory.objects.get(id=c_id)
    return render(request, 'two_page_website/vent.html', args)

