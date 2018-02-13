# food question database (German)
This python module migrates a text file providing questions into a sqlite database (questions.db) as a table called "downloaded\_question". This table has a cloumn for id, answer, question and vlaue. The value is a random integer (100, 200, 300) and is used to add a score component.

The questions in this example are from https://quizduell-antworten.de.tl/Essen-und-Trinken.htm

### Setup
You need a text file in which the questions are sorted as follows:
* one question plus correct answer per line
* first the question, then the answer seperated by a ";"
  * e.g. Question?;Answer

You need python 3 installed

### How to use
```
python get-questions.py
```

Then you can move the questions.db where you need it.
