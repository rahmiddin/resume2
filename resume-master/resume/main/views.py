from django.shortcuts import render, redirect
# Create your views here.
from .models import Project

def main_view(request):
    template = 'main/index.html'
    object_list = Project.objects.all()
    object = Project.objects.latest('date')
    context = {
        'object_list': object_list,
        'object': object
    }
    return render(request, template, context=context)

