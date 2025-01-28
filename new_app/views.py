from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AboutMeForm, ProjectForm
from .models import AboutMe, Project
import json

# Render views
def home(request):
    return render(request, 'new_app/home.html')


def about(request):
    about_me = AboutMe.objects.first()  # Assuming there's only one "About Me" entry
    return render(request, 'new_app/about.html', {'about_me': about_me})

def projects(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'new_app/projects.html', {'projects': projects})


def contact(request):
    return render(request, 'new_app/contact.html')

# Handle form submission
@csrf_exempt
def receive_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name", "")
            email = data.get("email", "")
            message = data.get("message", "")

            # Debugging: Log received data
            print(f"Received: Name: {name}, Email: {email}, Message: {message}")

            # Validate the data
            if not name or not email or not message:
                return JsonResponse({"status": "failure", "error": "All fields are required."})

            # Simulate storing data (e.g., save to database or send email)
            # Example: save_to_database(name, email, message)
            print("Message saved or email sent successfully!")

            return JsonResponse({"status": "success", "response": "Message received successfully."})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"status": "failure", "error": "Invalid data format."})
    return JsonResponse({"status": "failure", "error": "Invalid request method."})




def edit_about(request):
    about_me = AboutMe.objects.first()
    if request.method == 'POST':
        form = AboutMeForm(request.POST, instance=about_me)
        if form.is_valid():
            form.save()
            return redirect('about')  # Redirect to the "About Me" page
    else:
        form = AboutMeForm(instance=about_me)
    return render(request, 'new_app/edit_about.html', {'form': form})


def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')  # Redirect to the projects page
    else:
        form = ProjectForm(instance=project)
    return render(request, 'new_app/edit_project.html', {'form': form})
