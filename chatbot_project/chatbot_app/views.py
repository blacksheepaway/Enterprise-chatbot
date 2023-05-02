from django.shortcuts import render
from .models import Message
from django.http import HttpResponse, JsonResponse
from chatbot_app.models import Message
from .chatbot_logic import generate_response



def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST['user_message']
        bot_response = "Sample chatbot response"

        message = Message(user_message=user_message, bot_response=bot_response)
        message.save()
        print(f"User message: {user_message}, Bot response: {bot_response}")

    messages = Message.objects.order_by('timestamp')
    return render(request, 'chatbot_app/chat.html', {'messages': messages})



def chat_message(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message', '')
        
        bot_response = generate_response(user_message)
        
        message = Message(user_message=user_message, bot_response=bot_response)
        message.save()

        response = {
            'message': bot_response
        }
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Invalid request method.'})

