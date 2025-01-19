

input = "https://images.unsplash.com/photo-1513104890138-7c749659a591?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2OTg2NTN8MHwxfHNlYXJjaHwxfHxwaXp6YXxlbnwwfHx8fDE3MzcyNzU3MDF8MA&ixlib=rb-4.0.3&q=80&w=1080#**Pizza Ingredients:** - 2 cups of flour - 1 cup of water - 1 tsp of salt - 1 tsp of sugar - 1 tbsp of yeast - 1 cup of tomato sauce - 1 cup of shredded cheese - Toppings (your choice) **5 Preparation Steps:** 1. Mix flour, salt, sugar, and yeast. 2. Add water and knead the dough. 3. Spread tomato sauce on the dough. 4. Add shredded cheese and toppings. 5. Bake in the oven at 425°F (220°C) for 15-20 minutes."


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

link=0

for i in range(len(input)):
    if input[i]=='#':
        link = input[:i]
        new_input = input[i+1:]
    
def split_steps(steps_string):
    # Use regular expression to split the string by the pattern "number. space"
    steps = re.findall(r'\d+\.\s*(.*?)(?=\s*\d+\.|$)', steps_string)
    return steps

ingredients, steps = process_recipe(new_input)

print(ingredients)
steps = split_steps(steps[0])
print(steps)


    



