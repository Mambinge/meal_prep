# PrepPal

PrepPal is a recipe generation web application that helps you discover delicious meals based on the ingredients you have, your desired cuisine, and the type of meal. It's designed to inspire your culinary creativity and make cooking enjoyable and hassle-free.

## Technologies Used

PrepPal is built using the following technologies:

- Python: The core programming language used for developing the application.
- Streamlit: The web framework used for creating the user interface and interactive components.
- OpenAI API: The API used for generating recipe suggestions based on user inputs.
- Streamlit Cloud: The cloud platform used for deploying and hosting the application.

## How to Run PrepPal Locally

To run PrepPal locally on your machine, follow these steps:

1. Clone the repository:

```
git clone https://github.com/your-username/prep-pal.git
```

2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

3. Set up the necessary API keys:

   - OpenAI API key: Obtain an API key from OpenAI and set it as an environment variable named `OPENAI_API_KEY`.

4. Run the application:

```
streamlit run app.py
```

5. Open your web browser and visit `http://localhost:8501` to access PrepPal.

## How to Use PrepPal

Using PrepPal is simple and straightforward:

1. Enter the ingredients you have, separating them by commas.
2. Choose your desired cuisine from the provided options.
3. Select the type of meal: breakfast, lunch, dinner, or snack.
4. Click on the "Generate Recipe" button.
5. PrepPal will generate three recipe suggestions based on your inputs.
6. Explore the recipes and get inspired to create a delicious meal using the provided instructions and ingredients.

## Deploying PrepPal to Streamlit Cloud

To deploy PrepPal to Streamlit Cloud, follow these steps:

1. Sign up for a Streamlit Cloud account if you haven't already.
2. Create a new app in Streamlit Cloud.
3. Set up the necessary environment variables in the app settings:

   - `OPENAI_API_KEY`: Set it to your OpenAI API key.

4. Connect your GitHub repository to the Streamlit Cloud app.
5. Configure the deployment settings and specify the branch to deploy.
6. Trigger a manual deployment or enable automatic deployments for changes in the specified branch.
7. Once the deployment is complete, access your PrepPal app on the provided Streamlit Cloud URL.

## Contributing

Contributions to PrepPal are welcome! If you have any ideas, improvements, or bug fixes, feel free to submit a pull request. Please ensure that your changes align with the project's coding style and guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

---

We hope you enjoy using PrepPal to unleash your culinary creativity and discover amazing recipes! If you have any questions or feedback, please don't hesitate to reach out. Happy cooking!
