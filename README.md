# Web Scraper with Flask

A basic web scraper built using Python and Flask that extracts and displays domain information from provided URLs. The application supports various TLDs (Top-Level Domains) such as `.com`, `.co.uk`, `.ac.in`, etc.

## Features

- **Web Scraper:** Extracts the base domain (e.g., `www.example.com`) from a given URL, including complex domains like `www.college.ac.in`.
- **Flask Web Interface:** A simple web interface to input URLs and view the extracted domain information.
- **Error Handling:** Handles common HTTP errors (e.g., 400, 500) gracefully.

## Technologies Used

- Python 3.7+
- Flask 2.3.3
- tldextract 3.4.0
- Requests 2.31.0
- BeautifulSoup4 4.12.2

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Create a virtual environment:
- python -m venv venv
### Activate the virtual environment:
- On Windows
- - venv\Scripts\activate
- On macOS/Linux
- - source venv/bin/activate
### Install the required packages:
- pip install -r requirements.txt

## Run the Flask application:
- python app.py

## Access the web application:
- Open your web browser and navigate to http://127.0.0.1:5000.


## Project Structure

web-scraper-flask/
- │
- ├── app.py                 
- ├── requirements.txt       
- ├── templates/
- |   └── index.html         
- ├── static/
- │   └── style.css          
- └── README.md              
