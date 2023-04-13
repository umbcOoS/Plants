import streamlit as st
import requests

# Define the HTML and CSS code
html_template = '''
<template id="aitaxonomist-attachments-template">
    <style>
        button {
            border: 1px solid #8888FF;
            background: transparent;
        }
        button:hover {
            filter: brightness(1.2);
        }
    </style>
    <button>SELECT SPECIES</button>
</template>
<ai-taxonomist> </ai-taxonomist>
'''

# Render the HTML and CSS using st.markdown
st.markdown(html_template, unsafe_allow_html=True)

st.title('PlantNet API')

# Create a form for the image file
image_file = st.file_uploader('Upload an image')

# Create a button to submit the form
if st.button('Identify'):
    # Make an API request
    url = 'https://my-api.plantnet.org/v2/identify/all'
    params = {
        'include-related-images': 'false',
        'no-reject': 'false',
        'lang': 'en',
        'api-key': '2b10PuYKEhDAUVIEKvdS6itjc'
    }
    files = {
        'images': image_file.read()
    }
    response = requests.post(url, params=params, files=files)

    # Display the API results
    if response.ok:
        results = response.json()
        st.json(results)
    else:
        st.error(f"API request failed with status code {response.status_code}")
