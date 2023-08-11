import requests
from bs4 import BeautifulSoup
import csv

product_names = []
prices = []
descriptions = []
reviews = []

url = "https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.brand%255B%255D%3DMi&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D=true&p%5B%5D=facets.availability%5B%5D=Exclude+Out+of+Stock&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Mi"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

names = soup.find_all("div", class_="_4rR01T")
for name in names:
    product_names.append(name.text)

prices_elements = soup.find_all("div", class_="_30jeq3")
for elem in prices_elements:
    prices.append(elem.text)

# Find and append descriptions using class name
description_elements = soup.find_all("div", class_="_1AtVbE")
for elem in description_elements:
    description = elem.find("div", class_="fMghEO")
    descriptions.append(description.text.strip() if description else "N/A")

# Find and append reviews using class name
review_elements = soup.find_all("div", class_="_1AtVbE")
for elem in review_elements:
    review = elem.find("span", class_="_2_R_DZ")
    reviews.append(review.text.strip() if review else "N/A")

# Write the collected data to a CSV file
with open("televisions.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Description", "Review"])  # Write header

    for i in range(len(product_names)):
        writer.writerow([product_names[i], prices[i], descriptions[i], reviews[i]])

print("Data has been written to televisions.csv")
