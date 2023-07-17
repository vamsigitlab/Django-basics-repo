from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def indexView(request):
    return HttpResponse("<h1>Hello World</h1>")

def person_detail_view(request, person_id):
    from person_app.models import Person
    try:
        person_details = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        return JsonResponse({"error": True, "message": "Person does not exist"})
    return JsonResponse({
        "id": person_details.id,
        "name": person_details.name,
        "age": person_details.age
    })