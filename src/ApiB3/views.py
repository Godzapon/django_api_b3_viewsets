from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    variables = {
        "site_name": "mon site web"
    }
    return render(request, 'index.html', context=variables)
    # return HttpResponse("<p>hello world</p>")