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
        results = response.json()
        for result in results['results']:
            st.markdown(f"### Plant Species: {result['plant_name']['species']}")
            st.markdown(f"**Common Names:** {', '.join(result['plant_name']['common_names']['en'])}")
            st.markdown(f"**Scientific Name:** {result['plant_name']['scientific_name']['genus']} {result['plant_name']['scientific_name']['species']}")
            st.markdown(f"**Score:** {result['score']}%")
            st.image(result['plant_name']['complete_image']['url'], width=300)
            st.markdown(f"**[PlantNet Page]({result['plant_name']['url']})**")
            st.write('---')  # Add a horizontal line for separation
        st.json(results)
    else:
        st.error(f"API request failed with status code {response.status_code}")
