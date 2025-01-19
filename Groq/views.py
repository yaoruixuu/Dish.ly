from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import re
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
        to process, dont add unessesary stuff"""})
        
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

        #################
        image_urls = search_stock_images(user_msg)

        img_url=image_urls[0]
        
        return JsonResponse({'response':img_url+"#"+this_response})
    
    #######################
    
    

    

    ###################
    
    else:
        return render(request, "Groq/index.html",{
       
    })

def process_recipe(recipe_string):
    # Split the recipe string into ingredients and preparation steps
    sections = recipe_string.split("**5 Preparation Steps:**")
    
    # Extract ingredients and steps
    ingredients_section = sections[0].replace("**Pizza Ingredients:**", "").strip()
    steps_section = sections[1].strip()
    
    # Process the ingredients into an array
    ingredients = [item.strip() for item in ingredients_section.split('-') if item.strip()]

    # Process the preparation steps into an array
    steps = [step.strip() for step in steps_section.split('\n') if step.strip()]

    return ingredients, steps

def split_steps(steps_string):
    # Use regular expression to split the string by the pattern "number. space"
    steps = re.findall(r'\d+\.\s*(.*?)(?=\s*\d+\.|$)', steps_string)
    return steps

link=0

for i in range(len(input)):
    if input[i]=='#':
        link = input[:i]
        new_input = input[i+1:]

steps = split_steps(steps[0])
ingredients, steps = process_recipe(new_input)

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

user_input = ""




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







    


    



