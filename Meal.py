import streamlit as st
import openai


def set_background_image(image_url):
    """
    Function to set the background image of the app.
    """
    background_image = f"""
        <style>
            .stApp {{
                background-image: url("{image_url}");
                background-size: cover;
            }}
        </style>
    """
    st.markdown(background_image, unsafe_allow_html=True)

# Set the background image
image_url = "https://www.freepik.com/free-photo/green-turkish-delights-bowl-marble-background-high-quality-photo_12630428.htm"
set_background_image(image_url)

# Rest of your Streamlit app code



openai.api_key = "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"


# Fine-tune the GPT-3 model on recipe generation
def fine_tune_model():
    # TODO: Implement fine-tuning code
    pass

def generate_recipes(ingredients, cuisine, day, num_recipes=3, temperature=0.5, max_tokens=1024):
    recipes = []
    for _ in range(num_recipes):
        prompt = f"You are an expert cook and chef. Your task is to help generate a {cuisine} recipe using {ingredients} on how to cook a particular meal, for a particular time {day}."

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        recipe = response.choices[0].text
        recipes.append(recipe)

    return recipes

def app():
    st.title("PrepPal")
    ingredients = st.text_input("Enter ingredients (separated by commas)")
    cuisine = st.selectbox("Select cuisine",["Italian", "Mexican", "Chinese", "Indian", "Japanese", 
                                             "Thai", "French", "Greek", "Spanish", "Lebanese",
                                               "Korean", "Vietnamese", "Moroccan", "Turkish", 
                                               "Brazilian", "African"])

    day = st.selectbox("Select time", ["Breakfast", "Lunch", "Dinner", "Snack"])

    st.write(f"Here's a recipe for {ingredients}:")

    if st.button("Generate Recipe"):
        # Generate three recipes with temperature=0.7 and max_tokens=1024
        recipes = generate_recipes(ingredients, cuisine, day, num_recipes=3, temperature=0.7, max_tokens=1024)

        for i, recipe in enumerate(recipes):
            recipe_name = f"Recipe {i+1}:"
            st.write(recipe_name)
            st.write(recipe)

if __name__ == "__main__":
    fine_tune_model()
    app()
