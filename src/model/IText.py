import re

class IText(object):
    def __init__(self, description, *tags):
        self.description = description
        self._tags = set(*tags)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, a_description):
        if not isinstance(a_description, str):
            raise TypeError("Expected a string for the description")
        self._description = a_description

    @property
    def tags(self):
        return self._tags

    def add_tag(self, tag):
        self._tags.add(tag)

    def remove_tag(self, tag):
        self._tags.discard(tag)

    def matches(self, pattern):
        if not re.search(pattern, self._description):
            tag_pattern = re.compile(pattern)
            for tag in self._tags:
                if tag_pattern.search(tag):
                    return True
            return False
        return True

    def __str__(self):
        return "Description: {} \nTags: {}".format(self._description, \
                                                   self._tags)
