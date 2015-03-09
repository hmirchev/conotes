import re
import src.model.IText as IText

class Note(IText.IText):
    def __init__(self, title, description, *tags):
        self.title = title
        super().__init__(description, *tags)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, a_title):
        if not isinstance(a_title, str):
            raise TypeError("Expected a string for title")
        self._title = a_title

    def matches(self, pattern):
        parent_match = super().matches(pattern)
        title_match = re.search(pattern, self._title) != None

        return parent_match or title_match

    def __str__(self):
        return "Title: {}\n{}".format(self._title, super().__str__())
