import streamlit as st
import google.generativeai as genai
import random

# Configure your API key
api_key = "AIzaSyAfIoAlpsTFypcIcWv_1mygZ3GuJGcemsQ"
genai.configure(api_key=api_key)
generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
def get_joke():
    jokes = [
        "Why do Java developers wear glasses? Because they don't C#.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the JavaScript developer sad? Because he didn’t ‘null’ his feelings.",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Python programmers prefer using snake_case? Because it's easier to read!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
        "Why did the programmer get kicked out of the beach? Because he kept using the 'C' language!",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)
def generate_recipe(topic, word_count):
    st.write("### Generating your recipe...")
    st.write(f"Here's a joke while you wait: \n\n**{get_joke()}**")

    # Start a chat session
    chat_session = genai.GenerativeModel("gemini-1.5-flash").start_chat()
    
    prompt = f"Write a {word_count}-word detailed recipe blog on '{topic}'."
    
    try:
        response = chat_session.send_message(prompt)
        st.success("Your recipe is ready!")
        return response.text
    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None
st.title("Flavour Fusion: AI-Driven Recipe Blogging ")

topic = st.text_input("Enter your recipe topic:")
word_count = st.slider("Select word count:", 500, 2000, 1000)

if st.button("Generate Recipe"):
    recipe = generate_recipe(topic, word_count)
    if recipe:
        st.text_area("Generated Recipe", recipe, height=400)

st.title("Flavour Fusion: AI-Driven Recipe Blogging")
st.write("Welcome! Enter a topic to generate a recipe blog.")