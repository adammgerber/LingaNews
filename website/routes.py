from flask import render_template
from website.init import app
from flask import request
from newsapi.newsapi_client import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY= os.getenv("API_KEY")

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == "POST":

        chosen_language = request.form.get('language-select')
        newsapi = NewsApiClient(api_key=API_KEY)
        topheadlines = newsapi.get_top_headlines(category=request.form.get('category-select'), language=chosen_language)
        articles = topheadlines['articles']


        desc = []
        news = []
        img = []
        url = []

        for i in range(len(articles)):
            my_articles = articles[i]
            
            url.append(my_articles['url'])
            news.append(my_articles['title'])
            desc.append(my_articles['description'])
            img.append(my_articles['urlToImage'])

        my_list = zip(news, desc, img, url)

        return render_template('main.html', context= my_list)
    
    return render_template('main.html')

