# Sentiment Analysis of the 2016 and 2012 Presidential Elections

This project evalautes whether the 2016 presidential election generated greater public vitriol relative to the 2012 presidential election. It uses the NYT Python API to identify all articles containing the word "election" in 2016 and 2012. The URL's of these articles are then used in a scraper that collects and stores the comments. Next, the TextBlob package is used to perform sentiment anlaysis of the comments. Each comment is rated on its emotional polarity, subjectivity, and intensity. Finally, t-tests are conudcted in R to determine wether the mean level of negativity is different for the 2016 and 2012 election periods. This represents my first serious foray into Ptyhon and is an ongoing project.

NYTDataScrape12.py: This code replies on the NYT API to identify, collect, and store the URL from all relevant articles released in the year 2012. The headlines and hyperlinks from each article are expored as a .csv file.

NYTDataScrape16.py: This code is identitical the NYTDataScrape12, except that it collects articles from 2016.

NYTSentimentAnalysisPart1: This code uses the article hyperlinks stored in the .csv files to collect the comments from each relevant article. These are organized and stored as .csv files.

obamaromney.csv: This file contains the headlines and URL's of each relevant NYT article from 2012.

trumpclinton.csv: This file contains the headlines and URL's of each relevant NYT article from 2016.

