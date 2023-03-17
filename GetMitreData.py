import requests
from bs4 import BeautifulSoup

# specify the URL of the website to scrape
url = 'https://www.example.com'

# specify the class name of the table to extract
table_class = 'my-table-class'

# download the HTML page using the requests library
response = requests.get(url)

# parse the HTML page using the BeautifulSoup library
soup = BeautifulSoup(response.content, 'html.parser')

# find the table with the specified class using the find() method
table = soup.find('table', {'class': table_class})

# check if the table was found
if table is not None:
    # iterate over each row in the table and print the second and third columns
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) >= 3:
            print(cells[1].text + '/' + cells[2].text)
else:
    print('Table not found on the page.')
