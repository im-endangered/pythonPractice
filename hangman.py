import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def makeWord(haha):
    sabda=''
    for i in haha:
        sabda+=i
    return sabda


list_of_words=["apple","banana","cucumber","hotdog","watermelon","orange","pear","cherry","strawberry","nectarine","grape"]

word=random.choice(list_of_words)

characters=[]

lives=6

for i in range(0,len(word)):
    characters.append(" _ ")

print(makeWord(characters))

game_over=False

while game_over==False:

    guess=input("Enter your guess ").lower()

    for i in range(0,len(word)):
        if word[i]==guess:
            characters[i]=guess
    if guess not in word:
        lives-=1

    print(makeWord(characters))
    print(stages[lives])
    if " _ " not in characters:
        print("You win")
        game_over=True
    if lives==0:
        print("You lose")
        game_over=True

