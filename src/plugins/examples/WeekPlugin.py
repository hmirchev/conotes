import re
from src.model.Note import Note
from src.model.ToDo import ToDo
from src.controller.Controller import Controller

class WeekPlugin(object):
    def __init__(self): pass
    def activate(self):
        Controller._get_note = self._new_get_note
        Controller._get_todo = self._new_get_todo

    def _new_get_note(self):
        title = input("Enter title: ")
        description = input("Enter description: ")
        tags = input("Enter tags (comma-separated): ")
        tags = re.split(r'[,\s]\s*', tags)
        new_tags = ["<<<week>>>" if tag == "week" else tag for tag in tags]

        return Note(title, description, new_tags)

    def _new_get_todo(self):
        description = input("Enter description: ")
        begin_date = input("Enter begining date (e.g. 2001-12-25): ")
        end_date = input("Enter end date (e.g. 2001-12-25): ")
        tags = input("Enter tags (comma-separated): ")
        tags = re.split(r'[,\s]\s*', tags)
        new_tags = ["<<<week>>>" if tag == "week" else tag for tag in tags]

        return ToDo(description, begin_date, end_date, new_tags)
