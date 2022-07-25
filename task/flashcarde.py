# Write a program to making a flash card in which each flashcard will consists of a word and meaning.
class card(object):
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        
    def getmeaning(self):
        return self.meaning
    
    def __str__(self):
        return self.word + ' : ' + self.getmeaning()
  

def flashcard(flash, words, meanings):
    flash.append(card(words, meanings))
    return flash

lists = []
y = input("Want to add a flashcard? ")
while y == 'yes' or y == 'Yes':
    word = input("Word you want to add to your Flashcards: ")
    meaning = input("Meaning of the word in flashcard: ")
    lists = flashcard(lists, word, meaning)
    y = input("for adding another flashcard, press Yes/yes :")

print("----Following are the flashcards you made----")
for el in lists:
    print(el)    