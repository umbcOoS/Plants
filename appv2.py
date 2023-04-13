import streamlit as st
import requests
from PIL import Image
import base64
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
# Streamlit app
def main():
    st.title("Plant.id Web Component Example")
    st.write("Upload an image of a plant and get the identification result using the Plant.id API.")

    # Upload image file
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Process uploaded image
    if uploaded_file is not None:
        # Convert image to bytes
        image_bytes = uploaded_file.read()
        image = Image.open(uploaded_file)

        # Display uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert image to base64 string
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        # Call Plant.id API and display results
        response = send_image(image_bytes)
        if "results" in response:
            st.subheader("Identification Results:")
            for result in response["results"]:
                st.write("Genus:", result["genus"])
                st.write("Species:", result["species"])
                st.write("Score:", result["score"])
                st.write("---")
        else:
            st.error("Failed to get identification results")

if __name__ == "__main__":
    main()
