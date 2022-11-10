from django.shortcuts import render, redirect
# Create your views here.
from .models import Project

def main_view(request):
    template = 'main/index.html'
    object_list = Project.objects.all()
    context = {
        'object_list': object_list,
    }
    return render(request, template, context=context)

