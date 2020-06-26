
#Import Dependencies
import time
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
from splinter.exceptions import ElementDoesNotExist
from selenium import webdriver
import pymongo
from time import sleep

#Set chromedriver
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

# URL of page to be scraped nasa's news web page
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

#Scrape and print article's date, title and article teaser (text paragraph)
    article_date=soup.find('div', class_='list_date').text
    news_title = soup.find('div', class_='bottom_gradient').find('h3').text
    news_p = soup.find('div', class_='article_teaser_body').text

# ##JPL Mars Space Images - Featured Image

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    image_html = browser.html
    soup_image = BeautifulSoup(image_html, 'html5lib')
    image= soup_image.find('ul', class_='articles')
    edge=image.find("a",class_='fancybox')['data-fancybox-href']
    nasa_url='https://www.jpl.nasa.gov'
    featured_image_url=nasa_url + edge

# ## Mars Weather
    weather_url='https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    time.sleep(5)
    weather_html=browser.html
    soup_weather=BeautifulSoup(weather_html, 'html5lib')
    weather_tweet=soup_weather.find_all("article", role="article")[0]
    mars_weather = weather_tweet.find_all('span')[4].text


# ## Mars Facts

    facts_url='https://space-facts.com/mars/'
    mars_facts=pd.read_html(facts_url)
    df = mars_facts[0]
    df.columns=['Description', 'Values']
    df.set_index('Description', inplace=True)
    df.to_html()
    facts_html=df.to_html()


# ## Mars Hemispheres

    hemispheres_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    sleep(3)
    browser.visit(hemispheres_url)
    hemispheres_html=browser.html
    soup_hemispheres=BeautifulSoup(hemispheres_html, 'html.parser')
    images = soup_hemispheres.find_all('div', class_='item')

    hemisphere_image_urls = []

    main_url = 'https://astrogeology.usgs.gov'

    for image in images: 
   
        title = image.find('h3').text
        image_url = image.find('a', class_='itemLink product-item')['href']
        browser.visit(main_url + image_url)
        sleep(1)
        image_html = browser.html
        soup = BeautifulSoup( image_html, 'html.parser')
        image_url = main_url + soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"title" : title, "image_url" : image_url})

    website={"article_date": article_date, "news_title": news_title, "news_p": news_p,
    "mars_weather":mars_weather,"featured_image": featured_image_url, "mars_facts": facts_html,"hemisphere_image": hemisphere_image_urls}

    browser.quit()

    return website
