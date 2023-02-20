# Import package 
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
# Extraire le code html et le stocker dans une variable
url = 'https://www.francefleurs.com/383-nos-fleurs-sechees-et-stabilisees'
response = get(url)
# Convertir la variable response en un objet BeautifulSoup
html_soup = BeautifulSoup(response.text)
# Récupérer les items
items = html_soup.find_all('li', class_= 'ajax_block_product col-xs-12 col-sm-6 col-md-4')
len(items)
item  = items[0]
item
Name = item.find('div', class_="right-block").a.text.strip()
Price = item.find('div', class_="content_price").find("span", class_="price product-price").text.strip().strip(' €').replace(',', '.')
Description = item.find('div', class_="right-block").p.text.strip()
data = []

for item in items: 
  try :
    Name = item.find('div', class_="right-block").a.text.strip()
    Price = item.find('div', class_="content_price").find("span", class_="price product-price").text.strip().strip(' €').replace(',', '.')
    Description = item.find('div', class_="right-block").p.text.strip()
  except:
    pass
  obj = {
      'Name': Name, 
      'Price': float(Price),
      'Description': Description
  }
  data.append(obj)
df = pd.DataFrame(data)
df.shape
df = pd.DataFrame()
for i in range(1,12):
  url ='https://www.francefleurs.com/383-nos-fleurs-sechees-et-stabilisees?p={}'.format(i)
  response = get(url)
  html_soup = BeautifulSoup(response.text)
  items= html_soup.find_all('li', class_= 'ajax_block_product col-xs-12 col-sm-6 col-md-4')
  data = []

  for item in items: 
    try :
      Name = item.find('div', class_="right-block").a.text.strip()
      Price = item.find('div', class_="content_price").find("span", class_="price product-price").text.strip().strip(' €').replace(',', '.')
      Description = item.find('div', class_="right-block").p.text.strip()
    except:
      pass
    obj = {
        'Name': Name, 
        'Price': float(Price),
        'Description': Description
    }
    data.append(obj)
  DF =pd.DataFrame(data)
  df = pd.concat([df,DF], axis =0)
df.shape
df.duplicated().sum()
df.head()
