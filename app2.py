import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urlencode

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
            st.write('Confidence:', result['score'])
            st.write('Common name:', result['species']['commonNames'][0])
            st.write('Scientific name:', result['species']['scientificNameWithoutAuthor'])
            gbif_id = result['gbif']['id']
            gbif_url = f'https://www.gbif.org/species/{gbif_id}'
            st.markdown(f'GBIF: [{gbif_id}]({gbif_url})', unsafe_allow_html=True)
            st.markdown('---')
    else:
        st.error(f"API request failed with status code {response.status_code}")
