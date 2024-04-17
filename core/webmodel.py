import requests
from bs4 import BeautifulSoup
import validators
import pandas as pd
from django.http import HttpResponse

def scrape(url,nm):
    if validators.url(url):
        print("URL is Valid. JAM!!!")
    else:
        print("Invalid URL")
        return HttpResponse("Invalid URL")
    
    # Make a request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract product names and prices
    product_names = []
    product_prices = []
    product_info_divs = soup.find_all('div', class_='br-pdInfo')
    
    # Loop through each product info div
    for data in product_info_divs:
        # Find the product name
        name = data.find('div', class_='br-title br-freeGridFontChange')
        if name:
            product_names.append(name.text.strip())
        else:
            product_names.append('Name not available')
        # Find the product price
        pr = data.find('div', class_='pd-price br-standardPrice promoted')
        if pr:
            product_prices.append(pr.text.strip())
        else:
            product_prices.append('Price not available')
    
    # Create a DataFrame
    df = pd.DataFrame({"Product-Names": product_names, "Product-Prices": product_prices})
    data = df.head(100)
    
    # Save DataFrame to Excel file
    file_path = nm+".xlsx"
    data.to_excel(file_path, index=False)
    
    # Prepare response for file download
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = f'attachment; filename="{file_path}"'
    return response
