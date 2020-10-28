import requests
from bs4 import BeautifulSoup

def make_price(url_ta):
    url = 'https://www.tripadvisor.ru' + url_ta
    result = {'URL_TA': url_ta, 'Price Range': "Nan", "Cuisine Style": "Nan", 'Number of Reviews': "Nan"}
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    rest_data = [d.text for d in soup.find_all('a', class_="_2mn01bsa")]
    reviews_count = soup.find('span', class_="_3Wub8auF")
    if reviews_count:
        reviews_count = reviews_count.text
        result['Number of Reviews'] = reviews_count[:reviews_count.rfind(" ")].replace(" ", "")
    if len(rest_data) > 1:
        if rest_data[0] in ['$','$$ - $$$', '$$$$']:
            result['Price Range'] = rest_data[0]
        else:
            result['Cuisine Style'] = rest_data
    if len(rest_data) > 2:
        result['Cuisine Style'] = rest_data[1:]
    return result
