from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import os
import json
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

system_prompt = {
                "role": "system",
                "content":
                "You are a helpful assistant. Your name is jack."
            }
chat_history = [system_prompt]

@csrf_exempt
def chat_view(request):
    
    if request.method=="POST":
     
        data = json.loads(request.body)
        print(data)
        user_msg = data['prompt']
        
        chat_history.append({"role": "user", "content": user_msg})
        
        response = client.chat.completions.create(
            messages=chat_history,
            model="llama-3.3-70b-versatile",
        )
        chat_history.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })
        
        this_response = response.choices[0].message.content
        print(this_response)
        return JsonResponse({'response':this_response})
    
    else:
        return render(request, "Groq/index.html",{
       
    })

def reverse(request):
    if request.method=="POST":
     
        data = json.loads(request.body)
        print(data)
        user_array = data['prompt']
        user_msg="Give me a recipe with only "
        for param in user_array:
            user_msg = f'${user_msg} + ${param}'
        
        chat_history.append({"role": "user", "content": user_msg})

        response = client.chat.completions.create(
            messages=chat_history,
            model="llama-3.3-70b-versatile",
        )
        chat_history.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })
        
        this_response = response.choices[0].message.content
        print(this_response)
        return JsonResponse({'response':this_response})
    
    else:
        return render(request, "Groq/reverse.html",{  
    })








