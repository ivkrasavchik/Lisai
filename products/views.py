from django.shortcuts import render


def product(request):
    args = {}
    args['Text'] = "TEST TEST TEST TEST"
    return render(request, 'products/products.html', args)
