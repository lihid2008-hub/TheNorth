import streamlit as st
from PIL import Image  # Import Image from Pillow
import restcoffe
import pandas as pd

# st.markdown("<h1 style='text-align: center; color: black;'>מצפינים</h1>", unsafe_allow_html=True)

img = Image.open("Gemini_Generated_Image_jch7jhjch7jhjch7.jpg") # Open the image file
st.image(img, width=1000) # Display the image with a specified width
st.markdown("<h2 style='text-align: center; color: black;'>מחזקים-ציונות-ישראלית</h2>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: black;'>תכננו את הטיול המושלם לצפון, מחזירים את הצפון לחיים!</h3>", unsafe_allow_html=True)



if st.button("עגלות קפה ומסעדות",type = "primary",icon="🍽️",width = "stretch"):
  st.switch_page(restcoffe)

if st.button("התנדבויות" ,type = "primary", icon="🧑‍🌾",width = "stretch"):
  st.switch_page(restcoffe)

if st.button("טיולים ומצפים",type = "primary", icon="🗺️",width = "stretch"):
  st.switch_page(restcoffe)

if st.button("אחר",type = "primary", icon="🎉",width = "stretch"):
  st.switch_page(restcoffe)

if st.button("תכנן את היום שלנו!",type = "primary", icon="📆",width = "stretch"):
  st.switch_page(restcoffe)








