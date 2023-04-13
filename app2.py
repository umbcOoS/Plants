import streamlit as st
import requests

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
        for result in results:
            st.markdown('**Result**')
            st.write('Common name:', result['plant_name']['common_name'])
            st.write('Scientific name:', result['plant_name']['scientific_name'])
            image_url = result['images'][0]['url']
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            st.image(image, caption='Plant Image', use_column_width=True)
            st.write('Confidence:', result['score'])
            st.write('Family:', result['plant_name']['family'])
            st.write('Genus:', result['plant_name']['genus'])
            st.write('Species:', result['plant_name']['species'])
            st.write('Plant ID:', result['plant_id'])
            st.markdown('---')
    else:
        st.error(f"API request failed with status code {response.status_code}")
