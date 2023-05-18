from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    item_list = Item.objects.all()
    return HttpResponse('HelloWorld')


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)


class FoodDetail(DetailView):
    model = Item
