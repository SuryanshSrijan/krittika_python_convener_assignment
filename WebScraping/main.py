import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://krittikaiitb.github.io/team/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

year = []
name = []
designation = []

contents = soup.find_all('div', class_="card shadow-lg container mt-4 mb-5 aboutCard")

for content in contents:
    y = content.find('p').get_text()[-4:]
    morecontents = content.find_all('div', class_="card-body")
    for morecontent in morecontents:
        name.append(morecontent.find('h5').text)
        designation.append(morecontent.find('p').text)
        year.append(y)

df = pd.DataFrame({"name":name, "designation":designation, "year":year})
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df.to_csv('Krittika_Members.csv')
print(df)
