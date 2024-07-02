import os
import json
import cohere
import requests
import pandas as pd
from PIL import Image
import streamlit as st
from io import BytesIO
from annoy import AnnoyIndex
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from css_style import render_navbar2
from utils import display_images_from_folder, key_metrics_price
from streamlit_extras.stylable_container import stylable_container
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Sigmoid Style",
    layout="wide",
)

# Function to get API key (from environment or user input)
def get_api_key(key_name, env_var_name):
    user_api_key = st.sidebar.text_input(f"Enter your {key_name} API Key", type="password")
    return user_api_key if user_api_key else os.getenv(env_var_name)

# Get API keys
openai_api_key = get_api_key("OpenAI", 'openai_api_key')
cohere_key = get_api_key("Cohere", 'cohere')

# Check if API keys are available
if not openai_api_key or not cohere_key:
    st.info("Please provide both OpenAI and Cohere API keys to use this application.")
    st.stop()

# Render navigation bar
render_navbar2()

# Functions
def generate_star_rating(rating):
    """Generate a star rating string."""
    full_star = "★" * int(rating)
    half_star = "☆" * (5 - int(rating))
    return full_star + half_star

def formating_price(price):
    """Format and display price with buttons."""
    html_content = f"""
    <div style="margin-bottom: 20px;">
    <span style="font-size: 30px; color: black;">${price}</span>
    </div>
    <div style="margin-top: 10px;">
    <button style="padding: 10px 80px; background-color: black; color: white; border: none; cursor: pointer; border-radius: 0px; margin-bottom: 10px;">Add to Bag</button><br>
    <button style="padding: 10px 86px; background-color: #81ce74; color: black; border: none; cursor: pointer; border-radius: 0px;">Buy Now</button>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

def load_image_from_url(url, size=(700, 500)):
    """Load and resize an image from a URL."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content
            img = Image.open(BytesIO(image_data))
            img = img.resize(size)
            return img
        else:
            print("Failed to fetch image from URL:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def search(query, co, df_coach):
    """Search for products based on the query."""
    query_embed = co.embed(texts=[query], model='embed-english-v2.0').embeddings
    
    search_index_men = AnnoyIndex(4096, 'angular')
    search_index_men.load('./data/coach_new.ann')
    similar_item_ids = search_index_men.get_nns_by_vector(query_embed[0], 1, include_distances=True)
    
    for i in similar_item_ids[0]:
        image = load_image_from_url(df_coach.iloc[i]["Image link"])
        if image:
            p1, p2 = st.columns([6, 4])
            with p1:
                with stylable_container(
                    key="container_with_border",
                    css_styles="""
                        {
                            border: 1px solid rgba(49, 51, 63, 0.2);
                            border-radius: 0.5rem;
                            padding: calc(1em - 1px)
                        }
                        """,
                ):
                    st.image(image)
            with p2:
                with stylable_container(
                    key="container_price",
                    css_styles="""
                        {
                            border: 1px solid rgba(49, 51, 63, 0.2);
                            border-radius: 0.5rem;
                            padding: calc(1em - 1px)
                        }
                        """,
                ):
                    temp_df = df_coach.iloc[i]
                    display_name = temp_df["Prodct Name"]
                    st.write(f"### {display_name}")
                    st.write(generate_star_rating(4))
                    price = temp_df["Price"]
                    pd = temp_df["Product Description"]
                    formating_price(price)
                    st.markdown("<div style='color: grey; font-size: small'>4 interest-free payments of $31.25 with Klarna. <a href='#'>Learn More</a></div>", unsafe_allow_html=True)
                    st.write(" ")
                    st.markdown("Product Details")
                    st.write(pd)

# Main app
def main():
    # Display header image
    st.image('./data/image folder/Screenshot 2024-03-22 at 3.18.01 PM.png', use_column_width="always")

    # Set up ChatOpenAI
    llm_model = "gpt-3.5-turbo"
    chat = ChatOpenAI(temperature=0, model=llm_model, openai_api_key=openai_api_key)

    # Define output format and instructions
    output_format = """
        {   "Description": Introduce why these accessories will be helpful,
            "Accessory-1 name": accessory 1-line descriptions,
            "Accessory-2 name": accessory 1-line descriptions,
            "Accessory-3 name": accessory 1-line descriptions
        }
    """

    instruction_existing = """
        Role: Fashion expert for Coach New York.
        Objective: Engage users by suggesting three Coach products tailored to their interests.
        Approach: Friendly and engaging manner, focusing on specific needs.
        Suggestions: Three Coach products per query.
        Content: Product name, basic features, 1 line descriptions.
        Concise yet engaging responses.
        Personalized touch reflecting Coach's commitment to quality and style.
        Multiple options offered to help users find perfect items.
        Do not include the gender in name
    """

    template_string = """Generate a list of products tailored to the user's question {User_question}.
        Follow the instructions meticulously: {Instructions}
        and adhere to the output format {output_format} that is a python dictionary.
    """

    # Set up Cohere client and load data
    co = cohere.Client(cohere_key)
    pd.set_option('display.max_colwidth', None)
    df_coach = pd.read_csv("./coach.csv")

    # User input section
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                background-color: white;
                color: black;
                border-radius: 12px;
                padding: 10px;
            }
        """,
    ):
        st.markdown("🛒 Your Fashion Guide")
        question = st.text_input(label="Enter Your thoughts here", placeholder="Discover the latest buzz! Share what's on your mind today..")
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns(9)
        with c9:
            Clickme = st.button("Search")

    # Process user input
    if question and Clickme:
        prompt_template = ChatPromptTemplate.from_template(template_string)
        customer_messages = prompt_template.format_messages(
            User_question=question,
            Instructions=instruction_existing,
            output_format=output_format,
        )
        with st.spinner("Thank you for your patience as I search for the most optimal options for you"):
            customer_response = chat(customer_messages)
            item_dict = json.loads(customer_response.content)
            key_metrics_price(item_dict[list(item_dict.keys())[0]], 'https://i.im.ge/2024/03/30/WUqc4C.c.png')
            st.write(" ")    
            
            for k in list(item_dict.keys())[1:]:
                search(k, co, df_coach)

if __name__ == "__main__":
    main()