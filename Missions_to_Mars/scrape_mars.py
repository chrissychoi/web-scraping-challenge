from bs4 import BeautifulSoup
from selenium import webdriver
from splinter import Browser
import requests
import time
import pandas as pd
from pandas.io.html import read_html
import shutil

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    options = webdriver.ChromeOptions()
    options.add_argument("--diable-notifactions")
    return Browser("chrome", **executable_path, headless=False, options = options)

def scrape_info():
    
    browser = init_browser()

    
    nasa_url ='https://mars.nasa.gov/news/'
    browser.visit(nasa_url)
    time.sleep(1)

    ### 1. using beautifulsoup to scrape news title and teaser passage

    soup = BeautifulSoup(browser.html, 'html.parser')
    article = soup.find("div",{"class":'list_text'})
    news_title = article.find("div", {"class":"content_title"}).text
    news_p = article.find("div",{"class":"article_teaser_body"}).text

    



    ### 2 mars image
    jpl_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    time.sleep(1)

    browser.find_by_id("full_image").first.click()



    for link in browser.find_by_css('img[class="fancybox-image"]'):
        featured_img = link['src']

    ### 2.1 downloading image
    response = requests.get(link['src'], stream=True)
    local_file = open('mars_image.jpg', 'wb')
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, local_file)

    ### 3. mars weather tweet
    browser.visit("https://twitter.com/marswxreport?lang=en")
    time.sleep(1)

    browser.find_by_css('div[class="css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep"]').first.click()

    try:
        target_tweet = browser.find_by_css('span[class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]')[6].text
        marsTemp_tweet_clean = target_tweet
        marsTemp_tweet_clean = marsTemp_tweet_clean .replace('\n','')
    except:
        target_tweet = "Tweet unavailable at the moment, please try again later."
        marsTemp_tweet_clean = target_tweet

    ### 3.1 cleaning tweet

    marsTemp_tweet = {}

    marsTemp_tweet['featured_temp'] = marsTemp_tweet_clean
    
    ###4. mars fact and pandas
    browser.visit("https://space-facts.com/mars/")
    time.sleep(1)

    page = "https://space-facts.com/mars/"
    marsTable = read_html(page, index_col=0, attrs={"id":"tablepress-p-mars"} )

    marsTable_df = pd.DataFrame(marsTable[0])

    marsTable_to_html = marsTable_df.to_html(classes='marsTable_to_html')
    marsTable_to_html = marsTable_to_html.replace('<table border="1" class="dataframe marsTable_to_html">','')
    marsTable_to_html = marsTable_to_html.replace('</table>','')
    marsTable_to_html = marsTable_to_html.replace('<th>1</th>\n    </tr>\n    <tr>\n      <th>0</th>\n  ', '')

    

    ###5. Mars Hemispheres
    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    time.sleep(1)

    hemi_dict = []

    browser.find_by_text('Cerberus Hemisphere Enhanced').click()
    time.sleep(1)
    for link in browser.find_by_text('Sample'):
        img_url = link['href']

    hemi_name =  browser.find_by_css('h2').text
    hemi_name = hemi_name.replace(' Enhanced','')
    dictionary={"title":hemi_name,"img_url":img_url}
    hemi_dict.append(dictionary)
    browser.back()
    time.sleep(1)

    browser.find_by_text('Schiaparelli Hemisphere Enhanced').click()
    time.sleep(1)
    for link in browser.find_by_text('Sample'):
        img_url = link['href']
    
    hemi_name =  browser.find_by_css('h2').text
    hemi_name = hemi_name.replace(' Enhanced','')
    dictionary={"title":hemi_name,"img_url":img_url}
    hemi_dict.append(dictionary)
    browser.back()
    time.sleep(1)

    browser.find_by_text('Syrtis Major Hemisphere Enhanced').click()
    time.sleep(1)
    for link in browser.find_by_text('Sample'):
        img_url = link['href']
    
    hemi_name =  browser.find_by_css('h2').text
    hemi_name = hemi_name.replace(' Enhanced','')
    dictionary={"title":hemi_name,"img_url":img_url}
    hemi_dict.append(dictionary)
    browser.back()
    time.sleep(1)

    browser.find_by_text('Valles Marineris Hemisphere Enhanced').click()
    time.sleep(1)
    for link in browser.find_by_text('Sample'):
        img_url = link['href']
    
    hemi_name =  browser.find_by_css('h2').text
    hemi_name = hemi_name.replace(' Enhanced','')
    dictionary={"title":hemi_name,"img_url":img_url}
    hemi_dict.append(dictionary)
    time.sleep(1)

   
    marsDict = {
        "featured_news": news_title,
        "featured_teaser": news_p,
        "featured_temp": marsTemp_tweet_clean,
        "featured_img": featured_img,
        "mars_df": marsTable_to_html,
        "mars_hemi": hemi_dict
    }

    browser.quit()

    return marsDict