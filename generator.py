import requests
import json
from DataBase import *
import random

APIs = ['https://api.api-ninjas.com/v1/randomword','https://api.api-ninjas.com/v1/quotes',
        'https://api.api-ninjas.com/v1/celebrity','https://api.api-ninjas.com/v1/babynames?gender=neutral']

def generate_word(wordtype):
    response = requests.get(APIs[0] + '?type=' + wordtype, headers={'X-Api-Key': 'ONbDWidvWzVfbHawt4VJZg==KaKQdUtMORw97c0N'})
    word = response.text.lower()
    remove = ['{','}','[',']','"',' ']
    for i in remove:
        word = word.replace(i,'')
    # for i in "word:":
    #     word = word.replace(i,'')
    word = word[5:]
    # print(response.text)
    return word

def generate_country():
    country = random.choice(CountriesData)
    return {'name': country['name'], 'capital': country['capital'], 'region': country['region']}
    # return country['name'],country['capital'],country['region']

def generate_animal():
    animal = random.choice(AnimalsData)
    return animal

def generate_footballer():
    footballer = random.choice(TopFootballersData)
    return footballer

def generate_commonknowledge():
    common = random.choice(CommonKnowledgeData)
    return common


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