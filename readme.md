```
#run these before starting:
    pipenv shell

#the libraries needed before using program
    pipenv install numpy pandas sklearn

#You’ll need to install Jupyter Lab to run your code. Get to your command prompt and run the following command:
    pipenv install jupyter lab

#if you face error message "'jupyter' is not recognized as an internal or external command,
#operable program or batch file.", please install Anaconda into your operating system
#(https://repo.anaconda.com/archive/Anaconda3-2020.11-Windows-x86_64.exe)


##NEWS API
#https://newsapi.org/docs/get-started

Installation
$ pipenv install newsapi-python
$ pipenv install beautifulsoup
Usage
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='e8b1ec980d9d493682ba80d44fd69f58')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/sources
sources = newsapi.get_sources()



```
