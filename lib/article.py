class Article:
    # list to keep track of every article made
    all = []

    def __init__(self, author, magazine, title):
        self._title = None   # start with no title
        self.author = author
        self.magazine = magazine
        self.title = title   # setter will validate this
        Article.all.append(self)

    # --- Title ---
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # don’t let title be reassigned once it’s set
        if self._title is not None:
            # just ignore if someone tries to change it later
            return
        if not isinstance(value, str):
            raise ValueError("Title must be text")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title has to be 5–50 characters long")
        self._title = value

    # --- Author ---
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        # small import here to avoid circular issues
        from lib.classes.many_to_many import Author
        if isinstance(value, Author):
            self._author = value
        else:
            raise TypeError("Expected an Author object for author")

    # --- Magazine ---
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # kind of same pattern as author
        from lib.classes.many_to_many import Magazine
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise TypeError("Expected a Magazine object for magazine") 