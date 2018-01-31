from nytimesarticle import articleAPI #Import NYT API
import requests
import setuptools
import csv
from time import sleep

api = articleAPI('f7b3eecf64dc46e5a8387c39bc17db51') #Input API Key


#Get articles from the 2016 election

bad_pages = [] #Empty list for storing pages that fail


def get_one_page_of_articles(page): #Function that returns one speficied article page
    articles = {}
    try:
        articles = api.search( q = 'election', 
            fq = {'source':['The New York Times']},
            fl = ['headline', 'web_url'],
            begin_date = 20160101,
            end_date = 20161231,
            page = page)
    except: #Return empty dictionary for pages that fail
        pass
    return articles


def parse_articles(articles, page): #Function that parses one page of articles to create a dictionary
    news = []
    if "status" in articles and articles['status'] == "OK":
        for i in articles['response']['docs']:
            dic = {}
            dic['headline'] = i['headline']['main'].encode("utf8")
            dic['url'] = i['web_url']
            news.append(dic)
    else:
        print "Bad Page: %d" % page #Identify pages that fail to parse
        bad_pages.append(page)
    return(news)



def fetch_articles(): # Get and parse multiple pages of articles
    master_articles = [] #Loop
    for i in range(1, 101):
        sleep(2) #Prevent API rate limiting
        print "On Page: %d" % i #Track page number for visiual progress
        master_articles = master_articles + parse_articles(get_one_page_of_articles(i), i)

    keys = master_articles[0].keys() #Print
    with open('trumpclinton.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(master_articles)

    print(bad_pages)

if __name__ == "__main__":
    fetch_articles()


