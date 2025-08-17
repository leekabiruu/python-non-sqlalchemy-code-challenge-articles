# lib/classes/many_to_many.py

class Article:
    def __init__(self, author, magazine, title):
        # titles should always be strings with reasonable length
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 chars")

        self.author = author
        self.magazine = magazine

        # quick way to track every article that gets made
        if not hasattr(Article, "all"):
            Article.all = []
        Article.all.append(self)

    @property
    def title(self):
        # title can be read but never changed later
        return self._title

    @title.setter
    def title(self, value):
        # do nothing (title is frozen)
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
        # once set, the name can’t be updated
        return self._name

    @name.setter
    def name(self, value):
        # ignore attempts to change author name
        pass

    # return all articles by this author
    def articles(self):
        return [a for a in Article.all if a.author == self]

    # return unique magazines this author has written for
    def magazines(self):
        return list({a.magazine for a in self.articles()})

    # helper to make + link an article quickly
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # grab all unique categories of mags this author wrote for
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
        # name should be a short string (2–16 chars)
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # if invalid, just skip instead of crashing

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # must be a non-empty string
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value
        # silently ignore bad input

    # list of all articles in this mag
    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    # list of unique authors who contributed
    def contributors(self):
        return list({a.author for a in self.articles()})

    # return just the titles of all its articles
    def article_titles(self):
        titles = [a.title for a in self.articles()]
        return titles if titles else None

    # authors who wrote more than 2 pieces for this mag
    def contributing_authors(self):
        authors = [
            auth for auth in self.contributors()
            if len([a for a in self.articles() if a.author == auth]) > 2
        ]
        return authors if authors else None 