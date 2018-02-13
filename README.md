# question-database
This python module migrates a text file with questions into a sqlite database (questions.db) into a table called table downloaded\_question. This table has a cloumn for id, answer, question and the vlaue. The value is a random integer (100, 200, 300)

The questionins in this examle are from https://quizduell-antworten.de.tl/Essen-und-Trinken.htm

### Setup
You need a text file in which the questions are sordet as follows:
* one question per line
* first the question, then the answer seperated by a ;
  * e.g. Question?;Answer

And you need python 3 installed

### How to use
```
python get-questions.py
```

And then you can move the questions.db where you need it.
