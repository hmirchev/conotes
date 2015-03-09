# Console System for Notes

This is a project for a university course on "Programming in Python".

The main goal of the project is to build a simple extensible system for taking and organizing notes through the console. There are two types of notes:
- Note - a note is text with a title and an arbitrary amount of tags. A note can be added to the system, edited or deleted.
- Todo - a todo is text with a begin date, an end date, a flag that marks if it is completed or not, and an arbitrary amount of tags. A todo can be added to the sytem, edited, deleted or marked as completed.

The system should allow the user to search through all the notes or todos. 

The system should support extension through the use of plugins. A plugin is a python file (.py) that gets loaded automatically, as long as it is placed in the right place. An example plugin should also be provided:
- Week - everywhere there is a tag "week", it should be processed as "<<< week >>>". All the other tags should be left untouched. 

## Run the Project

Make sure to have Python 3 installed.

* Clone the repo
```shell
git clone git@github.com:hmirchev/conotes.git
```

* Run the project
```shell
python CoNotes.py
```

* Run the tests
```shell
test/python ITextTest.py
test/python NoteTest.py
test/python ToDoTest.py
```
