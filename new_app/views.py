from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ContactMessage  # Create this model

# Render the single-page home view
def home(request):
    return render(request, 'new_app/home.html')

# Handle form submission for contact messages
@csrf_exempt  # If using an API client like Postman, otherwise remove this and use CSRF tokens
def receive_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name", "").strip()
            email = data.get("email", "").strip()
            message = data.get("message", "").strip()

            # Debugging
            print(f"Received: Name: {name}, Email: {email}, Message: {message}")

            # Validate input
            if not name or not email or not message:
                return JsonResponse({"status": "failure", "error": "All fields are required."}, status=400)

            # Save to database (if needed)
            ContactMessage.objects.create(name=name, email=email, message=message)

            return JsonResponse({"status": "success", "response": "Message received successfully."}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"status": "failure", "error": "Invalid JSON format."}, status=400)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"status": "failure", "error": "An error occurred."}, status=500)

    return JsonResponse({"status": "failure", "error": "Invalid request method."}, status=405)
