class Source:
    '''
    Sources class to define Source Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.url=url
        # self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.category = category
        self.language = language
        self.country= country

class Articles:
    # all_articles=[]
    def __init__(self,id,author,title,description,url,urlToImage,publishedAt,content):
        self.id= id
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content

    # def save_article(self):