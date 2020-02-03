class Source:
    """
    class source defines objects of the news sources
    """

    def __init__(self, id, name, description, url, category, country, language):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language


class NewsArticle:
    """
    class newsArticle defines objects of the news articles
    """
    def __init__(self,id,author,title,description,url,image_url,date_published):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url
        self.date_published = date_published