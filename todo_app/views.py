from django.shortcuts import render, redirect
from todo_app.models import Todo
from django.http import HttpResponse
# Create your views here.

def list_view(request):
    search_string = request.GET.get('search', "")
    status = request.GET.get('status', "")
    todo_list = Todo.objects.all().order_by("-created_at")
    if search_string != "":
        todo_list = todo_list.filter(title__icontains=search_string)
    if status!="":
        todo_list = todo_list.filter(completed=status)
    data = {
        "todo_list": todo_list
    }
    return render(request, "list.html", context=data)

def create_view(request):
    todo_title = request.POST['todoTitle']
    todo_desc = request.POST['todoDescription']
    Todo.objects.create(
        title = todo_title,
        description = todo_desc
    )
    return redirect("todo_list_view")

def update_view(request, todo_id):
    if request.method == "GET":
        return HttpResponse("Cannot be updated with this method")
    else:
        try:
            todo_object = Todo.objects.get(pk=todo_id)
            todo_object.completed = True
            todo_object.save()
            return redirect('todo_list_view')
        except Todo.DoesNotExist:
            return redirect('todo_list_view')

def delete_view(request, todo_id):
    if request.method == 'GET':
        return HttpResponse("Error in the method format")
    else:
        if request.method == 'POST':
            try:
                todo_object = Todo.objects.get(pk=todo_id)
                todo_object.delete()
                return redirect('todo_list_view')
            except Todo.DoesNotExist:
                return redirect('todo_list_view')