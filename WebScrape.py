import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.rjcarrier.com"

# Make a GET request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all anchor tags on the page
links = soup.find_all("a")

# Extract the href attribute from each link
with open('csvfile.csv','w') as file:
    for link in links:
        tmp_link = link.get("href")
        print(tmp_link)
        file.write(tmp_link)
        file.write('\n')

# Convert csv to excel
df = pd.read_csv('csvfile.csv') # if your file is comma separated
df.to_excel('output.xlsx', 'Sheet1')