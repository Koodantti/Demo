from newsapi.newsapi_client import NewsApiClient
#from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='e8b1ec980d9d493682ba80d44fd69f58')

import pandas as pd
from pandas.io.json import json_normalize

from bs4 import BeautifulSoup
#if problems with pipenv install Beautifulsoup run following command
#pipenv install BeautifulSoup4

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='EU',
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='us')

#va
all_articles = newsapi.get_everything(q='EU',
                                      #sources='bbc-news,the-verge',
                                      #domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-01-17',
                                      to='2021-02-17',
                                      language='en',
                                      sort_by='relevancy',
                                      page=4)



top_headlines = json_normalize(top_headlines['articles']) 

top_articles = json_normalize(all_articles['articles'])

print(top_headlines)
print(top_articles)
newdf = top_articles.get(['title','source.name','url'])

print (newdf)

dic=newdf.set_index('title','content','url').to_dict() #['url']

import datetime
from datetime import datetime, timedelta
def date(base):    
    date_list=[]    
    yr=datetime.today().year    
    if (yr%400)==0 or ((yr%100!=0) and (yr%4==0)):          
        numdays=366        
        date_list.append([base - timedelta(days=x) for x in    
        range(366)])   
    else:        
        numdays=365        
        date_list.append([base - timedelta(days=x) for x in    
        range(365)])    
        newlist=[]    
        for i in date_list:        
           for j in sorted(i):            
               newlist.append(j)    
        return newlist 
def last_30(base):     
    date_list=[base - timedelta(days=x) for x in range(30)]      
    return sorted(date_list)  
def from_dt(x):    
    from_dt=[]    
    for i in range(len(x)):          
        from_dt.append(last_30(datetime.today())[i-1].date())         
    return from_dt        
def to_dt(x):    
    to_dt=[]    
    for i in range(len(x)):        
        to_dt.append(last_30(datetime.today())[i].date())    
    return to_dt
from_list=from_dt(last_30(datetime.today()))
to_list=to_dt(last_30(datetime.today()))

def func(query): 
    newd={}    
    newdf=pd.DataFrame()    
    for (from_dt,to_dt) in zip(from_list,to_list):           
        all_articles = newsapi.get_everything(q=query,language='en',
        sort_by='relevancy',from_param=from_dt,to=to_dt)          
        d=json_normalize(all_articles['articles'])         
        newdf=d[["url","publishedAt","source.name","author"]]
        dic=newdf.set_index(["source.name","publishedAt","author"]) 
        ["url"].to_dict()        
        for (k,v) in dic.items():            
            page = requests.get(v)            
            html = page.content            
            soup = BeautifulSoup(html, "lxml")            
            text = soup.get_text()            
            d2=soup.find_all("p")            
            newd[k]=re.sub(r'<.+?>',r'',str(d2))     
    return newd

    print(newd)

##Later user interface like this
#def top_headlines():    
   #country=input("Which country are you interested in?") 
   #category=input("""Which category are you interested in? \nHere 
   #are the categories to choose from:\nbusiness\nentertainment   
   #\ngeneral\nhealth\nscience\ntechnology""")        
   #top_headlines =newsapi.get_top_headlines(category=category,
   #language='en',country=country)     
   #top_headlines=json_normalize(top_headlines['articles'])   
   #newdf=top_headlines[["title","url"]]    
   #dic=newdf.set_index('title')['url'].to_dict()




# /v2/everything
#all_articless = newsapi.get_everything(q='Putin',
#                                      #sources='bbc-news,the-verge',
#                                      #domains='bbc.co.uk,techcrunch.com',
#                                      from_param='2021-01-17',
#                                      to='2021-02-17',
#                                      language='en',
#                                      sort_by='relevancy',
#                                      page=2)
#
#all_articless = json_normalize(all_articless['Articles'])
#newdff = all_articless.get(['title','source.name','url'])
#print(newdff)

# /v2/sources
sources = newsapi.get_sources()

#print (all_articles)

