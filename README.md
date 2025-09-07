# Web Scraping with Django

This project demonstrates web scraping using Django and BeautifulSoup. It scrapes product names and prices from a website and displays them on a web page. Additionally, it saves the scraped data to an Excel file.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

This project utilizes Django, BeautifulSoup, and Pandas to scrape product information from a specified website. It demonstrates how to make HTTP requests, parse HTML content, extract relevant data, and present it on a web page.

## Features

- Scrapes product names and prices from a website.
- Validates URLs using the validators library.
- Saves scraped data to an Excel file.
- Displays scraped data on a web page using Django templates.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/web-scraping-django.git
    ```

2. Navigate to the project directory:

    ```bash
    cd web-scraping-django
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Access the application in your web browser at `http://localhost:8000`.

3. Enter the URL of the website you want to scrape and submit the form.

4. The scraped product names and prices will be displayed on the web page, and the data will be saved to an Excel file according to the name you have entered.

5. It will be working efficiently on url obtained from bing browser shopping tab
   '''url
   https://www.bing.com/shop?q=amazon+tv+sales&FORM=SHOPTB
   '''
6. To obtain this, go to bing browser search about tv sales/phone sales as per your requirement. Then select the shopping tab and copy the url from the search bar. It will be similar to above URL.
##Note:
  1. The Excel file will be downloaded according to the name you have entered.
  2. For Instance:-
     1. If you entered, Amazon. Then it will be downloaded as Amazon.xml
  3. Make sure you have used edge to acquire the URL.Else, It won't work on the other browsers URL.
## Contributing

Contributions are welcome! Here's how you can contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/fooBar`).
3. Make your changes and commit (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.


https://github.com/Im-Mohammed/WebscrapeModel/assets/128249314/6d75b664-d94b-4468-ba65-bb39e2b35eba

