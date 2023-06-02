import streamlit as st
import openai

# Get the API key from the environment variable
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate recipes
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

def app():
    # Set the background color and font style
    st.markdown(
        """
        <style>
            body {
                background: #53BE5B;
                font-family: Arial, sans-serif;
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
                color: #53BE5B;
                font-size: 42px;
                text-align: center;
                margin-top: 10px;
                margin-bottom: 20px;
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
                background-color: #53BE5B;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                display: block;
                margin: 20px auto;
                text-align: center;
                font-size: 18px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #53BE5B;
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
st.title("PrepPal 🍽️✨")


ingredients = st.text_input("Enter ingredients (separated by commas)", key="ingredients", value="")
cuisine = st.selectbox("Select cuisine",["Italian", "Mexican", "Chinese", "Indian", "Japanese", 
                                         "Thai", "French", "Greek", "Spanish", "Lebanese",
                                         "Korean", "Vietnamese", "Moroccan", "Turkish", 
                                         "Brazilian", "African"], key="cuisine")
day = st.selectbox("Select time", ["Breakfast", "Lunch", "Dinner", "Snack"], key="day")

st.markdown("<h1>🌟 Here's a recipe for {}:</h1>".format(ingredients), unsafe_allow_html=True)

if st.button("Generate Recipe 🍳", key="generate"):
    # Generate three recipes with temperature=0.7 and max_tokens=1024
    recipes = generate_recipes(ingredients, cuisine, day, num_recipes=2, temperature=0.7, max_tokens=1024)

    # Display recipes results on the right column
    col1, col2 = st.columns(2)

    with col1:
        # Show the first recipe
        if len(recipes) >= 1:
            st.markdown(f"<div class='recipe'>{recipes[0]}</div>", unsafe_allow_html=True)

    with col2:
        # Show the second and third recipes
        if len(recipes) >= 2:
            st.markdown(f"<div class='recipe'>{recipes[1]}</div>", unsafe_allow_html=True)


# Run the app
app()
