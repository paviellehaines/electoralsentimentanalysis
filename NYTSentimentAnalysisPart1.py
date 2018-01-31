import requests as r
import json
from time import sleep
import csv
import re

#Base code taken from Neal Caren's Python Program for scraping NYT Comments

def nytimes_comments(article):
    
    article=article.replace(':','%253A') #convert the : to an HTML entity
    article=article.replace('/','%252F') #convert the / to an HTML entity
    offset=0 #Start off at the very beginning
    total_comments=1 #set a fake minimum number of contents
    comment_list=[] #Set up a place to store the results
    while total_comments>offset:
        url='http://www.nytimes.com/svc/community/V3/requestHandler?callback=NYTD.commentsInstance.drawComments&method=get&cmd=GetCommentsAll&url='+article+'&offset='+str(offset)+'&sort=newest' #store the secret URL
        sleep(1) #They don't like you to vist the page too quickly so take a one second break before downloading
        file=r.get(url).text #Get the file and read it into a string

        file=file.replace('NYTD.commentsInstance.drawComments(','') #clean the file by removing some clutter at the front end
        file=file[:-2] #clean the file by remvoings some clutter at the back end
        file=file.replace('      /**/ ', '')

        results=json.loads(file) #load the file as json
        comment_list=comment_list+results['results']['comments']
        if offset==0: #print out the number of comments, but only the first time through the loop
            total_comments=results['results']['totalCommentsFound'] # store the total number of comments
            print('Found '+str(total_comments)+' comments')

        offset=offset+25 #increment the counter
        
    return comment_list #return the list back


def get_comments(url, count):

    article_url = url #URL of the article you want to get

    comments = nytimes_comments(article_url)
    regex = re.compile('[^a-zA-Z .!?]')
    comments_to_write = []
    for comment in comments:
        com = comment['commentBody'].replace("<br/>", "")
        com = regex.sub('', com)
        dict_comment = {
            "comment": com
        }
        comments_to_write.append(dict_comment)
    if len(comments_to_write) > 0:
        with open('comments/comment%d.csv' % count, 'w', encoding='iso-8859-1') as output_file:
            dict_writer = csv.DictWriter(output_file, comments_to_write[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(comments_to_write)


def get_urls():
    urls = []
    with open("trumpclinton.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            urls.append(row['url'])
    count = 1
    for url in urls:
        print('On article %d for %s' % (count, url))
        get_comments(url, count)
        count += 1

if __name__ == "__main__":
    get_urls()