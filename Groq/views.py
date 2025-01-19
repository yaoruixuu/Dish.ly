from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import os
import json
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@csrf_exempt
def chat_view(request):
    
    if request.method=="POST":
     
        data = json.loads(request.body)
        print(data)
        user_msg = data['prompt']
        
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_msg,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        ai_response=chat_completion.choices[0].message.content
        print(ai_response)
        return JsonResponse({'response':ai_response})
    
    else:
        return render(request, "Groq/index.html",{
       
    })






