from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#groq demo
import os

from groq import Groq

def index(request):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of fast language models",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    message=chat_completion.choices[0].message.content
    print(message)
    return render(request, "Groq/index.html",{
        "msg":message
    })






