##https://newsapi.org/docs/get-started

api_key='e8b1ec980d9d493682ba80d44fd69f58'
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=api_key)##Key)
from pandas.io.json import json_normalize
import pandas as pd

from bs4 import BeautifulSoup

##Latest News
def top_headlines():    
   country=input("Which country are you interested in?") 
   category=input("""Which category are you interested in? \nHere 
   are the categories to choose from:\nbusiness\nentertainment   
   \ngeneral\nhealth\nscience\ntechnology""")        
   top_headlines =newsapi.get_top_headlines(category=category,
   language='en',country=country)     
   top_headlines=json_normalize(top_headlines['articles'])   
   newdf=top_headlines[["title","url"]]    
   dic=newdf.set_index('title')['url'].to_dict()

##GetData
get_everything(query,language,sort_by='relevancy',from_param,to)

##DateFunction
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


#Query

def func(query): 
    newd={}    
    newdf=pd.DataFrame()    
    for (from_dt,to_dt) in zip(from_list,to_list):           
        all_articles =   
        newsapi.get_everything(q=query,language='en',
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


    def wordcld(dictionary):        
    newd={}    
    for (k,v) in dictionary.items():        
    if v!='[]':            
        wordcloud = WordCloud().generate(str(dictionary[k]))                
        fig, axes= plt.subplots(figsize=(20,12),clear=True)                     
        plt.imshow(wordcloud, interpolation='bilinear')            
        plt.show()                 
    else:            
        print(str(k[0])+"_"+str(k[1][5:10])+"_"+str(k[1][11:13])              
        +"_"+str(k[1][14:16]) +"_"+str(k[1][17:19])+"_"+str(k[2]))             
        print("Wordcloud Not applicable")
dic=func("Indian Economy")
wordcld(dic)