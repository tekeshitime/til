from django.shortcuts import render
from .models import List

def index(request):
    all_list_items = List.objects.all()
    context = {
        'all_list_items': all_list_items,
    }
    return render(request, 'todolist/index.html', context)
