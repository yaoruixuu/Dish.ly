import re

input = "https://images.unsplash.com/photo-1513104890138-7c749659a591?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2OTg2NTN8MHwxfHNlYXJjaHwxfHxwaXp6YXxlbnwwfHx8fDE3MzcyNzU3MDF8MA&ixlib=rb-4.0.3&q=80&w=1080#**Pizza Ingredients:** - 2 cups of flour - 1 cup of water - 1 tsp of salt - 1 tsp of sugar - 1 tbsp of yeast - 1 cup of tomato sauce - 1 cup of shredded cheese - Toppings (your choice) **5 Preparation Steps:** 1. Mix flour, salt, sugar, and yeast. 2. Add water and knead the dough. 3. Spread tomato sauce on the dough. 4. Add shredded cheese and toppings. 5. Bake in the oven at 425°F (220°C) for 15-20 minutes."


def process_response(input):
    link = get_link(input)
    ingredient_s = ingredients(input)
    step_s = steps(input)
   
    print(link)
    print('------')
    print(ingredient_s)
    print('-------')
    print(step_s)
    
    

def get_link(input):
    for i in range(len(input)):
        if input[i]=='#':
            link = input[:i]
            return link
        
def ingredients(input):
    find1 = "**Pizza Ingredients:**"
    find2 = "**5 Preparation Steps:**"
    start = input.find(find1)
  
    end = input.find(find2)
    ingredient_s = input[start+22:end]
    return ingredient_s

def steps(input):
    find1 = "**5 Preparation Steps:**"
    start = input.find(find1)
    start = start+24
    steps = input[start:]
    return steps

process_response(input)
    



