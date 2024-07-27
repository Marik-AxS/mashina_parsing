from bs4 import BeautifulSoup as BS
import requests
import openpyxl

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None