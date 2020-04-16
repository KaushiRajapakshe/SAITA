
import pprint

import pandas as pd

data = pd.read_pickle('data_pkl.pkl')
data

# Extract only restart paragraph
selected_text = data['restart']
selected_text[:200]


from collections import defaultdict


def markov_chain(text):

    # Tokenize the text by word, though including punctuation
    words = text.split(' ')

    # Initialize a default dictionary to hold all of the words and next words
    d_dict = defaultdict(list)


    # Create a zipped list of all the possible combinations of words
    for current_word, next_word in zip(words[0:-1], words[1:]):
        d_dict[current_word].append(next_word)

    # Convert the default dict back into a dictionary
    d_dict = dict(d_dict)
    print(d_dict)
    return d_dict

# Create the dictionary.
new_dict = markov_chain(selected_text)
new_dict


import random


def generate_sentence(chain, count=5):

    # Capitalize the first word
    word1 = 'Restating-service'
    sentence = word1.capitalize()

    # Generate the second word from the value list. Set the new word as the first word. Repeat.
    for i in range(count - 1):
        word2 = random.choice(chain[word1])
        word1 = word2
        sentence += ' ' + word2

    # End it with a period
    sentence += '.'
    return (sentence)




pprint.pprint('Prediction: ' + generate_sentence(new_dict))
