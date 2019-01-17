from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf

from landing.forms import ZvonkiForm, QuestionsForm
from landing.models import Company, Fabric, ProductCategory, Product, Service


def home(request):
    args = {}
    args['Text'] = "TEST TEST TEST TEST"
    return render(request, 'landing/home.html', args)


def company(request):
    args = {}
    args['aboutCompany'] = Company.objects.all()
    return render(request, 'landing/company.html', args)


def brands(request):
    args = {}
    args['brands'] = Fabric.objects.all()
    return render(request, 'landing/list_brand.html', args)


def brand(request, brand_id):
    args = {}
    args['brand'] = Fabric.objects.get(id=brand_id)
    return render(request, 'landing/brand.html', args)


def prod_serv(request, c_id):
    args = {}
    args['cat_id'] = ProductCategory.objects.get(id=c_id)
    return render(request, 'landing/prod_serv.html', args)


def condserv(request, serv_id):
    args = {}
    args['aboutService'] = Service.objects.get(category__name=serv_id)
    return render(request, 'landing/service.html', args)


def production(request, cat_id):
    args = {}
    args['prod'] = Product.objects.filter(category__name=cat_id)
    # args['cat'] = ProductCategory.objects.get(name=cat_id)
    args['cat'] = cat_id
    return render(request, 'landing/production.html', args)


def product(request, prod_id):
    args = {}
    args['product'] = Product.objects.get(id=prod_id)
    return render(request, 'landing/product.html', args)


def production_brand(request, brand_id):
    args = {}
    cat = ''
    args['prod'] = Product.objects.filter(fabric__id=brand_id)

    for elem in args['prod']:
        cat = elem.category
        print(cat)
        break
    args['cat'] = cat
    return render(request, 'landing/production.html', args)


def call(request):
    args = dict()
    args.update(csrf(request))
    args['form1'] = ZvonkiForm(request.POST or None)
    if request.POST:

        if args['form1'].is_valid():
            args['form1'].save()
            return redirect('/')
    return render(request, 'landing/zvonok.html', args)


def question(request):
    args = dict()
    args.update(csrf(request))
    args['form1'] = QuestionsForm(request.POST or None)
    if request.POST:
        # args['form1'] = ZvonkiForm(request.POST or None)
        if args['form1'].is_valid():
            args['form1'].save()
            return redirect('/')
    return render(request, 'landing/questions.html', args)

