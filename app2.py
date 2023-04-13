import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title('UMBC Invasives IDbeta')

# Create a form for the image file
image_file = st.file_uploader('Upload an image')

# Create a button to submit the form
if st.button('Identify'):
    # Make an API request
    url = 'https://my-api.plantnet.org/v2/identify/all'
    params = {
        'include-related-images': 'true',
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
        for result in results['results']:
            st.markdown('**Result**')
            st.write('Common name:', result['species']['commonNames'][0])
            st.write('Scientific name:', result['species']['scientificNameWithoutAuthor'])
            image_url = result['images'][0]['url']
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            st.image(image, caption='Plant Image', use_column_width=True)
            st.write('Confidence:', result['score'])
            st.write('GBIF:', result['gbif']['id'])
            st.markdown('---')
    else:
        st.error(f"API request failed with status code {response.status_code}")
