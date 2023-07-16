from django.shortcuts import render

# Create your views here.

def index_page_view(request):
    data = {
        "name": "Vamsi Parupalli",
        "course": "Python Django Backend course"
    }
    return render(request, "index.html", context=data)