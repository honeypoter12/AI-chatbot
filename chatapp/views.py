from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# This renders your chat UI page
def chat_view(request):
    return render(request, 'chatapp/chat.html')

# Simple rule-based chatbot response function
def get_bot_response(user_message):
    user_message = user_message.lower()
    if "hello" in user_message:
        return "Hi there! How can I help you?"
    elif "how are you" in user_message:
        return "I'm doing great, thank you!"
    elif "bye" in user_message:
        return "Goodbye! Have a nice day!"
    elif "your name" in user_message:
        return "I'm a simple chatbot here to help you."
    else:
        return "Sorry, I didn’t understand that. Can you try something else?"

# API endpoint for chatbot
@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        bot_response = get_bot_response(user_message)

        # Optionally save chat to database here if you want

        return JsonResponse({"response": bot_response})

    return JsonResponse({"error": "POST request required"}, status=400)
