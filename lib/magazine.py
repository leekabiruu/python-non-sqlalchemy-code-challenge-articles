from lib.article import Article

class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine name should be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name has to be 2–16 characters long")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value.strip()) == 0:
            return
        self._category = value

    def articles(self):
        return [art for art in Article.all if art.magazine == self]

    def contributors(self):
        authors = []
        for art in self.articles():
            if art.author not in authors:
                authors.append(art.author)
        return authors

    def article_titles(self):
        titles = [art.title for art in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        result = []
        for auth in self.contributors():
            count = 0
            for art in self.articles():
                if art.author == auth:
                    count += 1
            if count > 2 and auth not in result:
                result.append(auth)
        return result if result else None 