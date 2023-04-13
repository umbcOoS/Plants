import streamlit as st
import requests
from retool import Retool

# Create a Retool instance
retool = Retool('https://umbcsustainability.retool.com/apps/45db685c-d956-11ed-b982-cf060df0d768/Plant') # Replace with your Retool app URL and API key

st.title('UMBC Invasives ID')

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
        
        # Send results to Retool
        retool.send_data('plantnet_results', results) # Replace 'plantnet_results' with the name of the Retool query or variable you want to update
    else:
        st.error(f"API request failed with status code {response.status_code}")
