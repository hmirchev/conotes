import src.model.IText as IText
from datetime import date
import re

class ToDo(IText.IText):
    def __init__(self, description, begin_date, end_date, *tags):
        super().__init__(description, *tags)
        self.begin_date = begin_date
        self.end_date = end_date
        self.finished = False

    def _parse_date(self, a_date):
        year, month, day = a_date.rsplit('-')
        return date(int(year), int(month), int(day))

    @property
    def begin_date(self):
        return self._begin_date

    @begin_date.setter
    def begin_date(self, beginning_date):
        if not isinstance(beginning_date, str):
            raise TypeError("Expected a string(YYYY-MM-DD) for the begin date")
        self._begin_date = self._parse_date(beginning_date)

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, ending_date):
        if not isinstance(ending_date, str):
            raise TypeError("Expected a string(YYYY-MM-DD) for the end date")
        potential_end_date = self._parse_date(ending_date)
        if self._begin_date <= potential_end_date:
            self._end_date = potential_end_date
        else:
            self._end_date = self._begin_date
            raise ValueError("End date should be later than " +\
                             self._begin_date)

    @property
    def finished(self):
        return self._finished

    @finished.setter
    def finished(self, finished_flag):
        if not isinstance(finished_flag, bool):
            raise TypeError("Expected a boolean value for finished")
        self._finished = finished_flag

    def matches(self, pattern):
        parent_match = super().matches(pattern)
        date_match = re.search(pattern, str(self._begin_date)) != None\
            or re.search(pattern, str(self._end_date)) != None
        finished_match = str(self._finished) == pattern

        return parent_match or date_match or finished_match

    def __str__(self):
        return "{}\nBegin date: {}\nEnd date: {}\nFinished: {}".format(
                super().__str__(), self._begin_date, self._end_date,
                self._finished)
