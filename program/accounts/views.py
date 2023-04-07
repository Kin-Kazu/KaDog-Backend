from django.shortcuts import render
from django.http import HttpResponse
from djoser.serializers import UserCreateSerializer


def my_view(request):
    # Your code logic here
    context = {'message': 'Hello, World!'}
    return render(request, 'my_template.html', context)
