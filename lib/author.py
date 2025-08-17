from lib.article import Article

class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if self._name is not None:
            return
        if not isinstance(value, str):
            raise TypeError("Name has to be a string")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be blank")
        self._name = value
 
    def articles(self):
      
        return [art for art in Article.all if art.author == self]

    def magazines(self):
       
        mags = []
        for art in self.articles():
            if art.magazine not in mags:
                mags.append(art.magazine)
        return mags


    def add_article(self, magazine, title):
      
        return Article(self, magazine, title)

    def topic_areas(self):
     
        if not self.magazines():
            return None
        cats = [mag.category for mag in self.magazines()]
        return list(set(cats)) 