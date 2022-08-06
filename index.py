from selenium import webdriver ##Used for testing on browsers
from bs4 import BeautifulSoup ## For parsing html and for data scrapping
import pandas as pd ## used for data anlytics
import requests
driver = webdriver.Chrome("C:/Users/ubaid/Downloads/chromedriver_win32/chromedriver.exe")
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
results2 = soup.find('div', attrs={'class':'title'})
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    a = title_element.text.strip()
    b = company_element.text.strip()
    c = location_element.text.strip()
noun = input("Choose a noun: ")

if noun == 'ubaid' :
    print("ok")


# df = pd.DataFrame({'Locations':[a] , 'Company':[b]}) 
# df.to_csv('random.csv', index=False, encoding='utf-8')

# driver = webdriver.Chrome("C:/Users/ubaid/Downloads/chromedriver_win32/chromedriver.exe")
# products=[] #List to store name of the product
# prices=[] #List to store price of the product
# ratings=[] #List to store rating of the product
# driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")
# content = driver.page_source
# soup = BeautifulSoup(content , "html.parser")
# for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
#     name=a.find('div', attrs={'class':'_3wU53n'})
#     price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
#     rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
#     products.append(name.text)
#     prices.append(price.text)
#     ratings.append(rating.text) 
# df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')
# print('ubaid')