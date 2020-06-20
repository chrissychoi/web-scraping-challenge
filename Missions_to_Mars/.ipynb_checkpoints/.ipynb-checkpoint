{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "from selenium import webdriver\n",
    "from splinter import Browser\n",
    "import requests\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "executable_path = {'executable_path': 'chromedriver'}\n",
    "\n",
    "options = webdriver.ChromeOptions()\n",
    "options.add_argument(\"--diable-notifactions\")\n",
    "\n",
    "browser = Browser('chrome', **executable_path, headless=False, options = options)\n",
    "nasa_url ='https://mars.nasa.gov/news/'\n",
    "browser.visit(nasa_url)\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA Perseverance Mars Rover Scientists Train in the Nevada Desert\n",
      "Team members searched for signs of ancient microscopic life there, just as NASA's latest rover will on the Red Planet next year.\n"
     ]
    }
   ],
   "source": [
    "### 1. using beautifulsoup to scrape news title and teaser passage\n",
    "\n",
    "soup = BeautifulSoup(browser.html, 'html.parser')\n",
    "article = soup.find(\"div\",{\"class\":'list_text'})\n",
    "news_title = article.find(\"div\", {\"class\":\"content_title\"}).text\n",
    "news_p = article.find(\"div\",{\"class\":\"article_teaser_body\"}).text\n",
    "\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'featured_news': 'NASA Perseverance Mars Rover Scientists Train in the Nevada Desert'}"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nasa_news = {}\n",
    "nasa_newsP = {}\n",
    "\n",
    "nasa_news[\"featured_news\"] = news_title\n",
    "nasa_newsP[\"featured_teaser\"] = news_p\n",
    "\n",
    "### as backup, including static news titles\n",
    "news_title = \"NASA's Perseverance Rover Will Look at Mars Through These 'Eyes'\"\n",
    "news_p = \"A pair of zoomable cameras will help scientists and rover drivers with high-resolution color images.\"\n",
    "\n",
    "nasa_news"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 2 mars image\n",
    "jpl_url=\"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(jpl_url)\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "full_image = browser.find_by_id(\"full_image\").first.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19631_ip.jpg\n"
     ]
    }
   ],
   "source": [
    "### 2.1 figured it is more intuitive for me to use splinter to scrape than beautifulsoup\n",
    "\n",
    "nasa_image = {}\n",
    "\n",
    "for link in browser.find_by_css('img[class=\"fancybox-image\"]'):\n",
    "    print(link['src'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'featured_image': 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19631_ip.jpg'}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nasa_image[\"featured_image\"] = link['src']\n",
    "\n",
    "### as backup, included a non instant link\n",
    "image_src = \"https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17171_ip.jpg\"\n",
    "nasa_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 3. mars weather tweet\n",
    "browser.visit(\"https://twitter.com/marswxreport?lang=en\")\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "latest_tweet = browser.find_by_css('div[class=\"css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep\"]').first.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 511 (2020-05-04) low -93.2ºC (-135.8ºF) high -3.6ºC (25.5ºF)\n",
      "winds from the SW at 4.9 m/s (11.0 mph) gusting to 16.8 m/s (37.6 mph)\n",
      "pressure at 6.80 hPa\n"
     ]
    }
   ],
   "source": [
    "target_tweet = browser.find_by_css('span[class=\"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0\"]')[6]\n",
    "print(target_tweet.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'featured_temp': 'InSight sol 511 (2020-05-04) low -93.2ºC (-135.8ºF) high -3.6ºC (25.5ºF)\\nwinds from the SW at 4.9 m/s (11.0 mph) gusting to 16.8 m/s (37.6 mph)\\npressure at 6.80 hPa'}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "marsTemp_tweet = {}\n",
    "marsTemp_tweet['featured_temp'] = target_tweet.text\n",
    "\n",
    "marsTemp_tweet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "### just in case, static value\n",
    "\n",
    "marsTemp = \"InSight sol 511 (2020-05-04) low -93.2ºC (-135.8ºF) high -3.6ºC (25.5ºF)winds from the SW at 4.9 m/s (11.0 mph) gusting to 16.8 m/s (37.6 mph)pressure at 6.80 hPa\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "###4. mars fact and pandas\n",
    "browser.visit(\"https://space-facts.com/mars/\")\n",
    "time.sleep(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pandas.io.html import read_html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Extracted 1 table\n"
     ]
    }
   ],
   "source": [
    "page = \"https://space-facts.com/mars/\"\n",
    "marsTable = read_html(page, index_col=0, attrs={\"id\":\"tablepress-p-mars\"} )\n",
    "\n",
    "print( \"Extracted {num} table\".format(num=len(marsTable)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                  1\n",
       "0                                                  \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "marsTable_df = pd.DataFrame(marsTable[0])\n",
    "marsTable_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>1</th>\\n    </tr>\\n    <tr>\\n      <th>0</th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Equatorial Diameter:</th>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>Polar Diameter:</th>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Distance:</th>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Period:</th>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>Surface Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>First Record:</th>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>Recorded By:</th>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "marsTable_html = marsTable_df.to_html()\n",
    "marsTable_html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "###5. Mars Hemispheres\n",
    "browser.visit(\"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\")\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemi_dict = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "browser.find_by_text('Cerberus Hemisphere Enhanced').click()\n",
    "time.sleep(1)\n",
    "for link in browser.find_by_text('Sample'):\n",
    "    print(link['href'])\n",
    "    img_url = link['href']\n",
    "\n",
    "hemi_name =  browser.find_by_css('h2').text\n",
    "hemi_name = hemi_name.replace(' Enhanced','')\n",
    "dictionary={\"title\":hemi_name,\"img_url\":img_url}\n",
    "hemi_dict.append(dictionary)\n",
    "browser.back()\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "browser.find_by_text('Schiaparelli Hemisphere Enhanced').click()\n",
    "time.sleep(1)\n",
    "for link in browser.find_by_text('Sample'):\n",
    "    print(link['href'])\n",
    "    hemisphereImgUrl.append(link['href'])\n",
    "    \n",
    "hemi_name =  browser.find_by_css('h2').text\n",
    "hemi_name = hemi_name.replace(' Enhanced','')\n",
    "dictionary={\"title\":hemi_name,\"img_url\":img_url}\n",
    "hemi_dict.append(dictionary)\n",
    "browser.back()\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "browser.visit(\"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\")\n",
    "time.sleep(1)\n",
    "browser.find_by_text('Syrtis Major Hemisphere Enhanced').click()\n",
    "time.sleep(1)\n",
    "for link in browser.find_by_text('Sample'):\n",
    "    print(link['href'])\n",
    "    hemisphereImgUrl.append(link['href'])\n",
    "    \n",
    "hemi_name =  browser.find_by_css('h2').text\n",
    "hemi_name = hemi_name.replace(' Enhanced','')\n",
    "dictionary={\"title\":hemi_name,\"img_url\":img_url}\n",
    "hemi_dict.append(dictionary)\n",
    "browser.back()\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "browser.visit(\"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\")\n",
    "time.sleep(1)\n",
    "browser.find_by_text('Valles Marineris Hemisphere Enhanced').click()\n",
    "time.sleep(1)\n",
    "for link in browser.find_by_text('Sample'):\n",
    "    print(link['href'])\n",
    "    hemisphereImgUrl.append(link['href'])\n",
    "    \n",
    "hemi_name =  browser.find_by_css('h2').text\n",
    "hemi_name = hemi_name.replace(' Enhanced','')\n",
    "dictionary={\"title\":hemi_name,\"img_url\":img_url}\n",
    "hemi_dict.append(dictionary)\n",
    "browser.back()\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemi_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
