
import pandas




#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for index, row in data.iterrows()}
print(nato_alphabet)


# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# def generate_phonetic():
#     word = input('Enter the word: ').upper()
#     try:
#         output_list = [nato_alphabet[letter] for letter in word]
#     except KeyError:
#         print('Sorry, only letters in the alphabet please.')
#         generate_phonetic()
#     else:
#         print(output_list)
#
# generate_phonetic()