from django.shortcuts import render

# Create your views here.

def index_page_view(request):
    data = {
        "show_data": True,
        "name": "Vamsi Parupalli",
        "course": "Python Django Backend course",
        "list": [1,2,3,4,5]
    }
    return render(request, "index.html", context=data)