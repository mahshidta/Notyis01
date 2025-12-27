from django.shortcuts import render

def indexhome (request):
    return render(request, "home/index.html", {})



