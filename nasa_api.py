import requests
import streamlit as st

url = "https://api.nasa.gov/planetary/apod?api_key=DxqXgtzkZHGlC9whz57AaytuuGUxNe9gWp8xcGq4"
# Make request
r = requests.get(url)
content = r.json()

# Get title of the image
title = content["title"]

# Get description of the image
description = content["explanation"]

# Get today's image url
image_url = content["hdurl"]

# Make request
req = requests.get(image_url)

# Binary code
image = req.content

# Create image with jpg extension in root directory
with open("image.jpg", "wb") as file:
    file.write(image)

# FRONTEND with streamlit
st.title(title)
st.image("image.jpg")
st.write(description)

