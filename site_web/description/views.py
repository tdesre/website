from django.shortcuts import render

def item_detail(request, item_id):
    context = {'item_id': item_id}
    return render(request, 'description/detail.html', context)
