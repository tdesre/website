from django.shortcuts import render

def catalogue(request):
    return render(request, 'catalogue/index.html')

def list_items(request, category):
    context = {'category': category}
    return render(request, 'catalogue/list.html', context)
