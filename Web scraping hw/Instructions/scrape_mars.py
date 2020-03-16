from splinter import Browser 
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def marsnews():
    try:

        url = "https://mars.nasa.gov/news/"
        browser.visit(url)

        html=browser.html
        soup = BeautifulSoup(html, "html.parser")

        headlines=[]
        paragraphs = soup.find_all("div", class_="content_title")
        for paragraph in paragraphs:
            print(paragraph.text)
            headlines.append(paragraph)

        headliners=[]
        written = soup.find_all("div", class_="article_teaser_body")
        for w in written:
            print(written.text)
            headliners.append(written)

        for x in range(10):
            print(headliners[x].text)

        written = "NASA chose a seventh-grader from Virginia as winner of the agency's 'Name the Rover' essay contest. Alexander Mather's entry for 'Perseverance' was voted tops among 28,000 entries."
        print(written)

        return written, paragraphs
def image():
    try: 

        imageurl = "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg"
        browser.visit(imageurl)
        html = browser.html
        soup = bs(html, "html.parser")

        picture = soup.find("img", class_="list_image")
        featured_image_url = "https://mars.nasa.gov/news" + picture 
        print(featured_image_url)

        return picture


def weather():
    try: 

        weatherurl = "https://twitter.com/marswxreport?lang=en"
        browser.visit(weatherurl)
        html = browser.html
        soupweather = bs(html, "html.parser")

        weatherarr = []
        weather = soup.find("div", class_="js-tweet-text-container")
        for w in weathers:
            print(weather.text)
            weatherarr.append(weather)


        return weather
        print(weatherarr)


def marsfacts():
    try:

        marsfactsdf = pd.read_html("https://space-facts.com/mars/")[0]
        print (marsfactsdf)

        marsfactsdf.columns=["Description", "Mars", "Earth"]
        
        return marsfactsdf


def marshemispheres():

    try:

        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)

        urls=[]

        return urls






        







    
