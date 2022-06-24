#Author: Chatchawal Sangkeettrakarn
#Date: September 20,2020.

from fastapi import FastAPI
import uvicorn
import numpy as np
import re
import math
import requests
from bs4 import BeautifulSoup
from fastapi.responses import PlainTextResponse


import pandas as pd
import math
from scipy.stats.stats import pearsonr
from pandas.core.frame import DataFrame
from google.colab import drive


app = FastAPI()

def result(res):
    return {"result":res}

@app.get("/")
async def main():
    return 'Hello World'

@app.get("/test")
async def test():
    return 'Test Tutorial'

@app.get("/add")
async def add(a: int = 0, b: int = 0):
    return a+b

@app.get("/mul")
async def mul(a: int = 0, b: int = 0):
    return a*b

@app.get("/pow")
async def pow(a: int = 0, b: int = 0):
    return math.pow(a,b)


def tonumlist(li):
    ls = li.split(',')
    for i in range(len(ls)):
        ls[i] = float(ls[i])
    return list(ls)

@app.get("/asc")
async def asc(li):
    ls = tonumlist(li)
    ls.sort()
    return ls

@app.get("/desc")
async def desc(li):
    ls = tonumlist(li)
    ls.sort(reverse=True)
    return ls

@app.get("/sum")
async def sum(li):
    ls = tonumlist(li)
    return np.sum(np.array(ls))

@app.get("/avg")
async def avg(li):
    ls = tonumlist(li)
    return np.average(ls)

@app.get("/mean")
async def mean(li):
    ls = tonumlist(li)
    return np.mean(ls)

@app.get("/max")
async def max(li):
    ls = tonumlist(li)
    return np.amax(ls)

@app.get("/min")
async def min(li):
    ls = tonumlist(li)
    return np.amin(ls)

@app.get("/validation-ctzid")
async def validation_ctzid(text):
    if(len(text) != 13):
        return False
    
    sum = 0
    listdata = list(text)
    
    for i in range(12):
        sum+=int(listdata[i])*(13-i)

    d13 = (11-(sum%11))%10
        
    return d13==int(listdata[12])

@app.get("/validation-email")
async def validation_email(text):  
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex,text):
        return True
    else:
        return False
    
    
@app.get("/google-search",response_class=PlainTextResponse)
def google_search(text):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    url = 'https://www.google.com/search?q=' + str(text)
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    t = soup.findAll('div', {'class':"r"})
    i = 0
    result = ''
    for a in t:
        href = a.a['href']
        head = a.h3.text
        result = result + head + '<br>' + href + '<br><br>'
        i += 1
        if(i >= 5):
            break
    
    return(result)

@app.get("/countlength")
async def countlength(text):
    return len(text)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80, debug=True)


@app.get("/echo")
async def echo():
    drive.mount('/content/drive')
    a = pd.read_csv('/content/drive/My Drive/ml-25m/A.csv')
    movies = pd.read_csv('/content/drive/My Drive/ml-25m/movies.csv')
    ratings = pd.read_csv('/content/drive/My Drive/ml-25m/ratings.csv')
    ratings.drop('timestamp', inplace=True, axis=1)
    ratings = ratings.merge(movies, on = 'movieId', how ='left')
    a = a.merge(movies, on = 'movieId', how ='left')
    b = a['genres'].value_counts().index.tolist()
    topGenres = []
    for i in range(len(b)):
        topGenres.append(b[i])
    movielist = []
    for i in range(len(ratings)):
        if(ratings['movieId'][i] == a['movieId'][1]):
                x = ratings['userId'][i]
                movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][2]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][3]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][4]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][5]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][6]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][7]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][8]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][9]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][10]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][11]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][12]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][13]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][14]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][15]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][16]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    movielist = []
    for i in range(len(df)):
        if(df['movieId'][i] == a['movieId'][17]):
            x = df['userId'][i]
            movielist.append(x)
    df = DataFrame(movielist)
    df = pd.DataFrame({'userId': df[0]})
    df = df.merge(ratings, on = 'userId', how ='left')
    
    def merge_data(x, y):
        merge_data = x.merge(y, on = 'movieId')
        return merge_data

    def total(merge_data):
        math_x = merge_data['rating_x']
        math_y = merge_data['rating_y']
        pearsonr(math_x, math_y)
        return pearsonr(math_x, math_y)

    def function_merge(x, y) :
        merge_data = x.merge(y, on = 'movieId' ,how ='outer' ,indicator=True)
        return merge_data

    def save_data(merge_data):
        movielist = []
        for i in range(len(merge_data)):
            if(merge_data['_merge'][i] == 'right_only'):
                x = merge_data['movieId'][i], merge_data['title'][i], merge_data['rating_y'][i], merge_data['genres_y'][i]
                movielist.append(x)
        return movielist

    def create_table(x, y):
        movielist =  save_data(function_merge(x, y))
        df = DataFrame(movielist)
        df = pd.DataFrame({
            'movieId': df[0],
            'title' : df[1],
            'rating': df[2],
            'genres': df[3]})
        try :
            moviel = []
            for i in range(len(df)):
                if(df['genres'][i] == topGenres[0]):
                    x = df['movieId'][i], df['title'][i], df['rating'][i], df['genres'][i]
                    moviel.append(x)
            dd = DataFrame(moviel)
            dd = pd.DataFrame({
                'movieId': dd[0],
                'title' : dd[1],
                'rating': dd[2],
                'genres': dd[3]})
            df = dd.sort_values(by=['rating'])[::-1]
            return df.head(5)
        except:
            moviel = []
            for i in range(len(df)):
                if(df['genres_y'][i] == topGenres[1]):
                    x = df['movieId'][i], df['title'][i], df['rating'][i], df['genres'][i]
                    moviel.append(x)
            dd = DataFrame(moviel)
            dd = pd.DataFrame({
                'movieId': dd[0],
                'title' : dd[1],
                'rating': dd[2],
                'genres_y': dd[3]})
            df = dd.sort_values(by=['rating'])[::-1]
            return df.head(5)
    
    merge_data(a, df)

    dfMean = total(merge_data(a, df))
    dfMean

    function_merge(a, df)

    save_data(function_merge(a, df))

    create_table(a, df)