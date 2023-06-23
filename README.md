# Image To Text Converter

### This project is a user-friendly web application that employs OCR technology to extract text from images, enabling effortless conversion of scanned documents, photos, and handwritten notes into editable and searchable text.

### PDF to Text

https://github.com/lep13/Image-To-Text-Converter/assets/126688687/f4de4b2f-807d-4064-a76a-43a3c7079271


### PNG To Text

https://github.com/lep13/Image-To-Text-Converter/assets/126688687/5793dfe0-bdf3-4d5f-b8ea-3f97eb30bf7e



### JPEG To Text

https://github.com/lep13/Image-To-Text-Converter/assets/126688687/56d0206b-6e5e-484f-8955-0eeabeed9f1a



## PDF Data Extraction and Rapid Prototyping

### Part 1: Data Extraction

The goal of this part is to create a Python script capable of extracting text from a given PDF document and saving the data into a CSV file. The PDF may contain both header data and tabular data.

#### Solution Overview
To tackle this task, a Python script was developed that utilizes the PyPDF2 and tabula-py libraries for extracting the data. The script supports both PDF and image file types (JPEG, JPG, PNG) for data extraction.

##### Assumptions
- The PDF document follows a consistent structure, including identifiable header and tabular sections.
- The text can be extracted using a combination of text extraction techniques.
- The script will be run in an environment with the required dependencies installed.

##### Challenges Faced
- Ensuring the script can handle different types of PDF documents with varying layouts and formats.
- Ensuring it supports PDF/PNG/JPG files.
- Handling image file types required additional image processing techniques for optimal OCR results.

#### Usage
The script, `pdf_data_extraction.py`, can be executed from the command line as follows:
python pdf_data_extraction.py <file_path>


Where `<file_path>` is the path to the input PDF or image file.

#### Output
The script generates a CSV file named `extracted_data.csv`, which contains the extracted text.

### Part 2: Rapid Prototyping

The objective of this part is to design and develop a simple web application that allows users to upload a PDF file, extract data using the script from Part 1, and display the extracted data on the webpage.

#### Solution Overview
For rapid prototyping, a Django web application was developed with the following components:

- A web form that enables users to upload a PDF file.
- Integration with the script from Part 1 to extract data from the uploaded file.
- Displaying the extracted data on a webpage.

##### Assumptions
- The web application is built using the Django framework.
- Users have a basic understanding of operating web applications.
- The required dependencies are installed in the development environment.

##### Challenges Faced
- Integrating the data extraction script into the Django application.
- Designing an intuitive user interface for file upload and displaying extracted data.
- Handling potential errors during file upload, data extraction, and data display processes.

#### Usage
To run the web application, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Run the Django development server with the command `python manage.py runserver`.
3. Access the web application through a web browser using the provided URL. `http://127.0.0.1:8000/`

#### Source Code
The source code for the web application can be found in the provided GitHub repository link.
