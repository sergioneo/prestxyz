from django.shortcuts import render, redirect
from lists.models import Item, List
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text, list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text, list=list_)
    return redirect(f'/lists/{list_.id}/')

def check_item(request, list_id, item_id):
    item = Item.objects.get(id=item_id)
    if item.list_id == int(list_id):
        item_checked = request.POST["checked"] == "true"
        item.checked = item_checked
        item.save()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def update_title(request, list_id):
    list_ = List.objects.get(id=list_id)
    new_title = request.POST['title']
    list_.title = new_title
    list_.save()
    return HttpResponse()