from bs4 import BeautifulSoup
import requests
from selenium import webdriver 
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def address(postcode,street):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://indexphone.ru/post-offices') 

    username_box = driver.find_element(By.NAME,'search') 
    username_box.send_keys(postcode) 

    driver.find_element(By.TAG_NAME,'span').click()

    link = driver.current_url
    driver.close()

    page = requests.get(link)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://indexphone.ru/post-offices') 
    try: 
        username_box = driver.find_element(By.NAME,'post-offices-search-list-address') 
        filteredNews = []
        allNews = []
        soup = BeautifulSoup(page.text, "html.parser")
        allNews = soup.findAll('span', class_='post-offices-search-list-address')

        for data in allNews:
            filteredNews.append(data.text.split(','))
        strees = random.choice(filteredNews)
        while strees == street:
           strees = random.choice(filteredNews)
        return strees 
    except NoSuchElementException:
        print('dwdw')
    
        filteredNews = []
        allNews = []
        soup = BeautifulSoup(page.text, "html.parser")
        allNews = soup.findAll('ul', class_='post-offices-search-list')
        if len(allNews) == 0:
            allNews = soup.findAll('ul', class_='post-object-list')
            for data in allNews:
                filteredNews.append(data.text.split(')'))
            
            strees = random.choice(filteredNews[0])+')'
            return strees
        else:
            
            for data in allNews:
                filteredNews.append(data.text.split(','))
            strees = random.choice(filteredNews)[2]
            return strees