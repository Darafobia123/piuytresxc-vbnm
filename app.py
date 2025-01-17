from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
import requests
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

scraped_data = []
def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs={"class","wikitable"})
    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all("tr")
    for row in table_rows:
        table_cols = row.find_all("td")
        temp_list=[]
        print(table_cols)
        for col_data in table_cols:
            print(col_data.text)
            data = col_data.text.strip()
            print(data)
            temp_list.append(data)
        scraped_data.append(temp_list)
scrape()
stars_data = []
for i in range (0,len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]
    required_data = [Star_names,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)
data=[]
def scrape_more_data(hyperlink):
        page = requests.get(hyperlink)

      
        soup = BeautifulSoup(page.content, "html.parser")

        temp_list = []

        information_to_extract = soup.find_all()
        
        for info_name in information_to_extract:
                try:
                    value= soup.find('div', text=info_name).find_next('span').text.strip()
                    print(value)
                    temp_list.append(value)
                except:
                    temp_list.append('Unknown')

        data.append(temp_list)
headers = ["Star_name","Distance","Mass","Radius","Luminosity"]
star_df_1 = pandas.DataFrame(stars_data,columns=headers)
star_df_1.to_csv("scraped_data.csv",index=True,index_label="id")
data=[]
