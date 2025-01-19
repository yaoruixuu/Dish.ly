import os
import requests

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

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


# Main function to get user input and fetch images
def main():
    # Remove whitespaces then split by commas to get a list of ingredients
    # Put into an array user_ingredients
    user_ingredients = input("What ingredients do you have? e.g. cheese, bacon, potatoes: ")

    chat_completion_ingredients = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "I have " + user_ingredients + " so what dishes can I make with these ingredients? Output your answer only in the format 'dish1,dish2,dish3,...'",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    dishes = (chat_completion_ingredients.choices[0].message.content).split(",")
    for dish in dishes: 
        image_urls = search_stock_images(dish)
        for url in image_urls: print("name: " + dish + ", image: " + url)

if __name__ == "__main__":
    main()