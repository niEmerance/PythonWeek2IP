import urllib.request,json
from .models import Source,Articles


# Source=source.Source
# Getting api key
api_key = None
base_url = None
articles_url=None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    articles_url=app.config['ARTICLE_API_BASE_URL']

def get_sources(category):
    get_sources_url=base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    source_results=[]
    for source_item in source_list:
        id=source_item.get('id')
        name=source_item.get('name')
        description=source_item.get('description')
        url=source_item.get('url')
        category=source_item.get('category')
        language=source_item.get('language')
        country=source_item.get('country')
        
        source_object=Source(id,name,description,url,category,language,country)
        source_results.append(source_object)
    return source_results

def get_articles(id):
    print('Hey')
    print(articles_url)
    get_articles_url=articles_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data=url.read()
        get_articles_response=json.loads(get_articles_data)

        articles_results=None

        if get_articles_response['articles']:
            articles_results_list=get_articles_response['articles']
            articles_results=process_articles(articles_results_list)

    return articles_results

def process_articles(article_list):
    articles_results=[]
    for article_item in article_list:
        id=article_item.get('id')
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        urlToImage=article_item.get('urlToImage')
        publishedAt=article_item.get('publishedAt')
        content=article_item.get('content')
        if urlToImage:
            article_object=Articles(id,author,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(article_object)

    return articles_results