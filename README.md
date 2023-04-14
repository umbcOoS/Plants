UMBC Invasive Plants Identification App
This is a web application that allows users to identify invasive plants using images. It utilizes the Plant.ID API provided by PlantNet, a collaborative research platform on plant biodiversity. The app is built using Streamlit, a Python framework for building interactive web applications.

Features
Upload an image (jpeg only) of a plant for identification.
Displays identification results including ID confidence score, common name, scientific name, and a link to the species on the Global Biodiversity Information Facility (GBIF) website.
Results are limited to the top 5 matches to avoid clutter.


Installation
To run the app locally, follow these steps:

Clone the repository: git clone https://github.com/umbcOoS/Plants.git
Install the required libraries: pip install -r requirements.txt
Run the app: streamlit run app.py
Open a web browser and go to http://localhost:8501

How to Use
Open the app in a web browser.
Upload an image of a plant using the file uploader.
Click the "Identify" button to trigger the identification process.
View the results displayed on the screen, including the ID confidence score, common name, and scientific name.
Click on the GBIF link to access more information about the identified species.
Click the "Share" button to share the app with others.

Contributing
If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature-name
Make your changes and commit them: git commit -m "Description of changes"
Push your changes to your forked repository: git push origin feature-name
Create a pull request from your branch to the main repository.
Provide a clear description of your changes and why they are necessary.
Wait for feedback and address any comments or suggestions.

Credits
This app was created by the UMBC Office of Sustainability. 

License
This app is released under the MIT License. Feel free to use, modify, and distribute it according to the terms of the license.



