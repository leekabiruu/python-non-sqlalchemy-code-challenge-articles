class Article: 
    all = []

    def __init__(self, author, magazine, title):
        self._title = None  
        self.author = author
        self.magazine = magazine
        self.title = title   
        Article.all.append(self)
 
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        
        if self._title is not None: 
            return
        if not isinstance(value, str):
            raise ValueError("Title must be text")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title has to be 5–50 characters long")
        self._title = value
 
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value): 
        from lib.classes.many_to_many import Author
        if isinstance(value, Author):
            self._author = value
        else:
            raise TypeError("Expected an Author object for author")
 
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value): 
        from lib.classes.many_to_many import Magazine
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise TypeError("Expected a Magazine object for magazine") 