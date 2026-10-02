from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Project, Task,Comment


def dashboard(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()

    return render(request, 'tasks/dashboard.html', {
        'projects': projects,
        'tasks': tasks,
    })


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('/login/')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

        return render(request, 'tasks/login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'tasks/login.html')


def user_logout(request):
    logout(request)
    return redirect('/login/')
def create_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        Project.objects.create(
            name=name,
            description=description,
            created_by=request.user
        )

        return redirect('/')

    return render(request, 'tasks/create_project.html')
def create_task(request):
    if request.method == 'POST':
        project_id = request.POST['project']
        title = request.POST['title']
        description = request.POST['description']
        assigned_to_id=request.POST.get('assigned_to')
        project = Project.objects.get(id=project_id)

        Task.objects.create(
    project=project,
    title=title,
    description=description,
    assigned_to_id=assigned_to_id if assigned_to_id else None
)

        return redirect('/')

    projects = Project.objects.all()
    users = User.objects.all()

    return render(request, 'tasks/create_task.html', {
        'projects': projects,
        'users': users
    })
def update_task_status(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.status = request.POST['status']
        task.save()

        return redirect('/')

    return render(request, 'tasks/update_task.html', {
        'task': task
    })
def add_comment(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        text = request.POST['text']

        Comment.objects.create(
            task=task,
            user=request.user,
            text=text
        )

    return redirect('/')