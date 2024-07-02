import os
import streamlit as st

# Import necessary libraries
def display_images_from_folder(folder_path, image_width=500):
    # List all files in the folder
    files = os.listdir(folder_path)
    # Filter only image files
    image_files = [file for file in files if file.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    
    # Display images one by one
    col1, col2 = st.columns(2)
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(folder_path, image_file)
        if i % 2 == 0:
            with col1:
                st.image(image_path,UseColumnWith='always')
        else:
            with col2:
                st.image(image_path, UseColumnWith='always')




def key_metrics_price(value,icon_link):
    icon_url = icon_link

    box_width = "1300px"
    box_height = "200px"

    component_html = f"""
    <div style="
        display: flex;
        align-items: center;
        justify-content: start;
        border: 1px solid #F1F1F1;
        background-color: white;
        border-radius: 5px;
        padding: 10px;
        color: black;
        height: {box_height};
    ">
        <img src="{icon_url}" alt="Icon" style="width: 450px; height: 400px; margin-right: 20px;">
        <div style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
            <div style="font-size:1.5em; padding: 0px 0px 0px 0px ;ont-family: HelveticaLTPro-Bold, Helvetica-bold, Arial, sans-serif;">{value}</div>
            
        
    </div>
    """

    st.markdown(component_html, unsafe_allow_html=True)