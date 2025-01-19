from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import os
import json
from groq import Groq
import requests

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
        
        user_msg = data['prompt']
        
        chat_history.append({"role": "user", "content": "give ingredients and 5 preparation steps for "+user_msg+"""give to me in easy format
        to process, dont add unessesary stuff, it should be ingredients, and steps for the subtitles"""})
        
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

    
        image_urls = search_stock_images(user_msg)

        img_url=image_urls[0]
        
        unprocessed = img_url+"#"+this_response

        link, ingredient_s, step_s =  process_response(unprocessed)

        
        return JsonResponse({
            'link': link,
            'ingredients' : ingredient_s,
            'steps' : step_s
            })
    
   
    
    
    else:
        return render(request, "Groq/index.html",{
       
    })

# sorting response
def process_response(input):
    link = get_link(input)
    ingredient_s = ingredients(input)
    step_s = steps(input)
    return link, ingredient_s, step_s

def get_link(input):
    for i in range(len(input)):
        if input[i]=='#':
            link = input[:i]
            return link
        
def ingredients(input):
    find1 = "Ingredients"
    find2 = "Steps"
    start = input.find(find1)
  
    end = input.find(find2)
    ingredient_s = input[start+16:end]
    return ingredient_s

def steps(input):
    find1 = "Steps"
    start = input.find(find1)
    start = start+9
    steps = input[start:]
    return steps


# Function to search stock images using Unsplash API based on a prompt
def search_stock_images(prompt):
    # Unsplash API endpoint for searching photos
    url = "https://api.unsplash.com/search/photos"
    
    # Your Unsplash API key
    api_key = "b20qCLE5GNlNQb6ineHLQnJAnFUpzTAO_tDQx2PyVSA"  # Replace with your API key
    
    # Parameters for the API request
    params = {
        'query': prompt,  # The search keyword based on user input
        'per_page': 1,  # Number of results per page
        'client_id': api_key  # API key for authorization
    }
    
    # Send GET request to Unsplash API
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        # If the request is successful, parse the JSON response
        results = response.json()['results']
        
        # Return the URLs of the images
        image_urls = [result['urls']['regular'] for result in results]
        return image_urls
    else:
        # If there's an error, return a message
        return f"Error: Unable to fetch images. Status code: {response.status_code}"






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







    


    



