from lib.article import Article

class Author:
    def __init__(self, name):
        self._name = None
        self.name = name  # will go through the setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # don’t let name be reassigned later
        if self._name is not None:
            return
        if not isinstance(value, str):
            raise TypeError("Name has to be a string")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be blank")
        self._name = value

    # --- Relationships ---
    def articles(self):
        # grab all articles written by this author
        return [art for art in Article.all if art.author == self]

    def magazines(self):
        # return the magazines this author has written for
        mags = []
        for art in self.articles():
            if art.magazine not in mags:
                mags.append(art.magazine)
        return mags

    # --- Helper to add ---
    def add_article(self, magazine, title):
        # kinda shortcut to make a new article
        return Article(self, magazine, title)

    def topic_areas(self):
        # unique categories of magazines they contribute to
        if not self.magazines():
            return None
        cats = [mag.category for mag in self.magazines()]
        return list(set(cats)) 