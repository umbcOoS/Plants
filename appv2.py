import streamlit as st
import requests

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
        if 'suggestions' in results:
            for result in results['suggestions']:
                image_url = result['plant_name']['complete_image']['url']
                st.image(image_url, caption=result['plant_name']['common_names']['en'], width=300)
                # Display the stylized text
                st.markdown(f"**Common Name:** {result['plant_name']['common_names']['en']}")
                st.markdown(f"**Family:** {result['plant_name']['family']['scientific_name']['genus']} {result['plant_name']['family']['scientific_name']['species']}")
                st.markdown(f"**Genus:** {result['plant_name']['genus']['scientific_name']['genus']} {result['plant_name']['genus']['scientific_name']['species']}")
        else:
            st.warning('No plant suggestions found.')
    else:
        st.error(f"API request failed with status code {response.status_code}")
