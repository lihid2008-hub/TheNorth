import streamlit as st
from PIL import Image  # Import Image from Pillow
import pandas as pd


img = Image.open("Gemini_Generated_Image_jch7jhjch7jhjch7.jpg") # Open the image file
st.image(img, width=1000) # Display the image with a specified width
st.header("מצפינים")
st.subheader("מחזקים-ציונות-ישראלית")
st.write("תכננו את הטיול המושלם לצפון, מחזירים את הצפון לחיים!")


name = st.text_input("Enter your name")

if st.button("Submit"):
  st.write(f"Hello {name}, lets start planning!")











