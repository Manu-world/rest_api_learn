from django.http import JsonResponse
import json  # Import the json module

def api_home(request, *args, **kwargs):
    # Use request.json() to parse JSON data
    body = request.body
    print(body)

    return JsonResponse({"message": "This is the json message"})
