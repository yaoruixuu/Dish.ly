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
        'per_page': 5,  # Number of results per page
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

# Main function to get user input and fetch images
def main():
    user_input = input("What dish would you like: ")
    image_urls = search_stock_images(user_input)
    
    if isinstance(image_urls, list):
        print("\nFound image URLs:")
        for url in image_urls:
            print(url)
    else:
        print(image_urls)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "give ingredients and preparation steps for "+user_input,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    ai_response=chat_completion.choices[0].message.content
    print(ai_response)

if __name__ == "__main__":
    main()

