import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urlencode

st.title('UMBC Invasives IDbeta')
# Load the image from URL
image_url = 'https://pbs.twimg.com/profile_images/1248247779010310146/L8X8lRyH_400x400.jpg'
image_response = requests.get(image_url)
image = Image.open(BytesIO(image_response.content))

# Display the image
st.image(image, width=200)  # Set the width of the image to 200 pixels

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
   # ... existing code ...

# Display the API results
if response.ok:
    results = response.json()
    counter = 0  # Counter variable to keep track of the number of results displayed
    for result in results['results']:
        counter += 1
        if counter > 5:  # Break out of the loop after displaying 5 results
            break

        st.markdown('**Result**')
        score_percent = result['score'] * 100  # Convert score to percentage
        st.markdown(f'<p style="font-size:24px;font-weight:bold;">ID Confidence: {score_percent:.2f}%</p>', unsafe_allow_html=True)  # Display score as a percentage with 2 decimal places, in bold and larger font
        st.write('Common name:', result['species']['commonNames'][0])
        st.write('Scientific name:', result['species']['scientificNameWithoutAuthor'])
        st.markdown('*Scientific name:*', unsafe_allow_html=True)  # Italicize "Scientific name" label
        st.markdown(f'*{result["species"]["scientificNameWithoutAuthor"]}*')  # Italicize scientific name result
        gbif_id = result['gbif']['id']
        gbif_url = f'https://www.gbif.org/species/{gbif_id}'
        st.markdown(f'GBIF: [{gbif_id}]({gbif_url})', unsafe_allow_html=True)
        st.markdown('---')
else:
    st.error(f"API request failed with status code {response.status_code}")

