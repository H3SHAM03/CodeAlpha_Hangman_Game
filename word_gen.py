import requests
import json

APIs = ['https://api.api-ninjas.com/v1/randomword?type=noun','https://api.api-ninjas.com/v1/quotes']
def generate_word():
    response = requests.get(APIs[0], headers={'X-Api-Key': 'ONbDWidvWzVfbHawt4VJZg==KaKQdUtMORw97c0N'})
    word = response.text.lower()
    remove = ['{','}','[',']','"',' ']
    for i in remove:
        word = word.replace(i,'')
    for i in "word:":
        word = word.replace(i,'')
    print(word)
    return word

# def play_word(word):
#     plain = ''
#     for i in range(len(word)):
#         plain = plain + '_'

#     finished = False
#     while finished == False:
#         print(plain)
#         guess = input('Guess a letter: ')
#         if guess in word:
#             for i,letter in enumerate(word):
#                 if guess == letter:
#                     plain = plain[:i] + letter + plain[i+1:]
#         print(plain)
#         if '_' not in plain:
#             finished = True

#     print("congrats")
