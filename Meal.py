import streamlit as st
import openai

openai.api_key = "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"


# Fine-tune the GPT-3 model on recipe generation
def fine_tune_model():
    # TODO: Implement fine-tuning code
    pass

def generate_recipe(ingredients, cuisine,  temperature=0.5, max_tokens=1024):
    prompt = f"You are an expert cook and chef. Your task is to help generate a {cuisine}  recipe using {ingredients} on how to cook a particular meal, for a particular time {day}."

    response = openai.Completion.create(
         engine="text-davinci-002", 
         prompt=prompt, 
         max_tokens=max_tokens,
         temperature=temperature)
    recipe = response.choices[0].text
    return recipe


# Evaluate the quality of the generated recipe
def evaluate_recipe(recipe):
    # TODO: Implement recipe evaluation metrics
    return True

def app():
    st.title("Recipe Generator")
    st.write(f"Here's a recipe for {ingredients}:")
ingredients = st.text_input("Enter ingredients (separated by commas)")
cuisine = st.selectbox("Select cuisine", ["Italian", "Mexican", "Chinese"])
day = st.selectbox("Select time", ["Breakfast", "Lunch", "Dinner","Snack"])
if st.button("Generate Recipe"):
        # Generate a recipe with temperature=0.7 and max_tokens=256
        recipe = generate_recipe(ingredients,cuisine, temperature=0.7, max_tokens=1024)
        if evaluate_recipe(recipe):
            st.write(recipe)
        else:
            st.write("Sorry, could not generate a recipe. Please try again.")

if __name__ == "__main__":
    fine_tune_model()
    app()
