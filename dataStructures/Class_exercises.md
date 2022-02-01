# Exercises on Python Class Data Structures

## Exercice 1 - Class Chapter & Book

You work on a text edition software and need to handle the text that is written by a user.

### Question 1

Create a class *Chapter* that handles the text written:
- it will have three attributes:
    - an *id* attribute that corresponds to the chapter number.
    - a *title* attribute that corresponds to the chapter name.
    - a *text* attribute containing some text.
- it will have three methods:
    - *add_text*: add some text to the *text* attribute.
    - *remove_text*: remove some text from the *text* attribute.
    - *save*: save the value of the *text* attribute into a file.
    - *search*: look for a word or group of words in the *text* attribute. (return true or false).

### Question 2

Create a class *Book* that handles the different chapters:
- it will contain three attributes:
    - a title
    - an author name
    - a list of Chapter classes
- it will contain three methods:
    - *add_chapter*: add a chapter to the book.
    - *delete_chapter*: delete a chapter given a specific id.
    - *print_chapters*: print the list of chapter where each line has the following format:
        ```Chapter <id>: <title>```
    - *check_forbidden_words*: check if some chapters contain forbidden words. Print the list of chapters containing them, or "No forbidden word found".
      These forbidden words are contained in a list. ```forbidden_words = ["pikachu", "google"]``` 
    
### Question 3

Implement unit tests testing the previous methods with *pytest*.
- run ```pip install pytest``` to be able to user pytest
- create files named *test_book.py* and *test_chapter.py* which will contain your tests.
- to create a test:

     ```
         def test_chapter_text():
            # instantiate a Chapter class (don't forget to import it), try to add or remove some text
            # use *assert* keywork to test if everything is working as expected``` 
  
- to run your tests: ```pytest -k <test_name>``` or ```pytest <path_of_you_test_file>```
      
