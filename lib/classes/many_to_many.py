# lib/classes/many_to_many.py

class Article:
    def __init__(self, author, magazine, title):
    
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 chars")

        self.author = author
        self.magazine = magazine

    
        if not hasattr(Article, "all"):
            Article.all = []
        Article.all.append(self)

    @property
    def title(self):
       
        return self._title

    @title.setter
    def title(self, value):
       
        pass


class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name
        else:
            raise ValueError("Author name must be a non-empty string")

        if not hasattr(Author, "all"):
            Author.all = []
        Author.all.append(self)

    @property
    def name(self):
        
        return self._name

    @name.setter
    def name(self, value):
       
        pass
 
    def articles(self):
        return [a for a in Article.all if a.author == self]

   
    def magazines(self):
        return list({a.magazine for a in self.articles()})

   
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
 
    def topic_areas(self):
        cats = {m.category for m in self.magazines()}
        return list(cats) if cats else None


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

        if not hasattr(Magazine, "all"):
            Magazine.all = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
    
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
       

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
      
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value
      

    def articles(self):
        return [a for a in Article.all if a.magazine == self]
 
    def contributors(self):
        return list({a.author for a in self.articles()})
 
    def article_titles(self):
        titles = [a.title for a in self.articles()]
        return titles if titles else None
 
    def contributing_authors(self):
        authors = [
            auth for auth in self.contributors()
            if len([a for a in self.articles() if a.author == auth]) > 2
        ]
        return authors if authors else None 