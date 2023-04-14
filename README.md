# UMBC Invasive Plants Identification App
This is a web application that allows users to identify invasive plants using images. It utilizes the Plant.ID API provided by PlantNet, a collaborative research platform on plant biodiversity. The app is built using Streamlit, a Python framework for building interactive web applications.

### Features
- Upload an image (jpeg only) of a plant for identification.
- Displays identification results including ID confidence score, common name, scientific name, and a link to the species on the [Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/) website.
- Results are limited to the top 5 matches to avoid clutter.


## Installation
To run the app locally, follow these steps:

- Clone the repository: git clone https://github.com/umbcOoS/Plants.git
- Install the required libraries: pip install -r requirements.txt
- Run the app: streamlit run app.py
- Open a web browser and go to http://localhost:8501

## How to Use
1. Open the app in a web browser.
2. Upload a jpeg image of a plant using the file uploader.
3. Click the "Identify" button to trigger the identification process.
4. View the results displayed on the screen, including the ID confidence score, common name, and scientific name.
5. Click on the GBIF link to access more information about the identified species.


## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix: git checkout -b feature-name
3. Make your changes and commit them: git commit -m "Description of changes"
4. Push your changes to your forked repository: git push origin feature-name
5. Create a pull request from your branch to the main repository.
6. Provide a clear description of your changes and why they are necessary.
7. Wait for feedback and address any comments or suggestions.

## Credits
This app was created by the [UMBC Office of Sustainability](https://sustainability.umbc.edu/).  

## License
This app is released under the [MIT License](https://opensource.org/license/mit/). Feel free to use, modify, and distribute it according to the terms of the license.

## Contact 
If you have any questions, comments, or feedback, please feel free to contact us at sustainability@umbc.edu
