import streamlit as st
import openai

favicon = "favicon.ico"
st.set_page_config(page_title="PrepPal", page_icon=favicon)

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
image_url = "/"
set_background_image(image_url)

# Rest of your Streamlit app code


# Get the API key from the environment variable
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Fine-tune the GPT-3 model on recipe generation
def fine_tune_model():
    # TODO: Implement fine-tuning code
    pass

def generate_recipes(ingredients, cuisine, day, num_recipes=3, temperature=0.5, max_tokens=1024):
    recipes = []
    for _ in range(num_recipes):
        prompt = f"You are an expert cook and chef. Your task is to help generate a {cuisine} recipe using {ingredients} on how to cook a particular meal, for a particular time {day}. In your recipe, provide the name, ingredients, and steps for making the meal. Use emojis where appropriate to make the text appealing."

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        recipe = response.choices[0].text
        recipes.append(recipe)

    return recipes

import streamlit as st

def app():
    # Set the background color
    st.markdown(
        """
        <style>
            body {
                background-color: #f5f5f5;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set the container width
    st.markdown(
        """
        <style>
            .container {
                max-width: 800px;
                padding: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set the title style
    st.markdown(
        """
        <style>
            h1 {
                color: #FF6600;
                font-size: 36px;
                text-align: center;
                margin-top: 50px;
                margin-bottom: 50px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set the input style
    st.markdown(
        """
        <style>
            .input-text {
                border: 1px solid #FF6600;
                border-radius: 5px;
                padding: 10px;
                margin-bottom: 20px;
                width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set the button style
    st.markdown(
        """
        <style>
            .button {
                background-color: #FF6600;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                display: block;
                margin: 20px auto;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set the recipe style
    st.markdown(
        """
        <style>
            .recipe {
                margin-bottom: 20px;
                padding: 10px;
                background-color: #F8F8F8;
                border: 1px solid #DDDDDD;
                border-radius: 5px;
                color: #333333;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # App content
    st.title("PrepPal")

    ingredients = st.text_input("Enter ingredients (separated by commas)", key="ingredients", value="")
    cuisine = st.selectbox("Select cuisine",["Italian", "Mexican", "Chinese", "Indian", "Japanese", 
                                             "Thai", "French", "Greek", "Spanish", "Lebanese",
                                             "Korean", "Vietnamese", "Moroccan", "Turkish", 
                                             "Brazilian", "African"], key="cuisine")
    day = st.selectbox("Select time", ["Breakfast", "Lunch", "Dinner", "Snack"], key="day")

    st.markdown("<h1>Here's a recipe for {}:</h1>".format(ingredients), unsafe_allow_html=True)

    if st.button("Generate Recipe", key="generate"):
        # Generate three recipes with temperature=0.7 and max_tokens=1024
        recipes = generate_recipes(ingredients, cuisine, day, num_recipes=3, temperature=0.7, max_tokens=1024)

        for i, recipe in enumerate(recipes):
            recipe_name = f"<h3>Recipe {i+1}:</h3>"
            st.markdown(recipe_name, unsafe_allow_html=True)
            st.markdown(f"<div class='recipe'>{recipe}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    app()
