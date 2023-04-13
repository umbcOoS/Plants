import streamlit as st
from PIL import Image
import base64
import requests

# Define Plant.id API endpoint
api_url = "https://my.plantnet.org/api/identify/all?organs=auto"
params = {
        'include-related-images': 'true',
        'no-reject': 'false',
        'lang': 'en',
        'api-key': '2b10PuYKEhDAUVIEKvdS6itjc'
    }

# Define function to send image to Plant.id API
def send_image(image):
    headers = {
        'Content-Type': 'application/octet-stream'
    }
    response = requests.post(api_url, headers=headers, data=image)
    return response.json()

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
