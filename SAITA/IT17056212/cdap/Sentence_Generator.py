import pprint

import pandas as pd
import Sentence_PostProcessor
from collections import defaultdict
import random
from Inputs import Input

#keywords = ['Drive-letter', 'because']



def get_key_words():
    inp = Input.get_input()
    keywords=[]
    #keywords = ['Drive-letter', 'because']
    key = inp.keywords
    keywords.append(key)
    keywords.append("because")
    return keywords

def get_selected_text():
    data = pd.read_pickle('data_pkl.pkl')

    # Extract only restart paragraph
    key_w=get_key_words()
    selected_text = data[key_w[0]]
    return selected_text[:300]


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
def create_dict():
    new_dict = markov_chain(get_selected_text())
    return new_dict


def generate_sentence(chain, k_word, count):
    # Capitalize the first word
    word1 = k_word
    unrepeated_word = word1
    sentence = word1.capitalize()

    # Generate the second word from the value list. Set the new word as the first word. Repeat.
    for i in range(count - 1):
        word2 = random.choice(chain[word1])
        j = 0
        while word2 == unrepeated_word:
            j = j + 1
            if j <= 3:
                print("Keyword repeated: " + word2)
                word2 = random.choice(chain[word1])
            else:
                break
        j = 0
        word1 = word2
        sentence += ' ' + word2

    # End it with a period
    sentence += '.'
    sentence_split = sentence.split('.')
    sentence1 = sentence_split[0]
    sentence = sentence1
    sentence += '.'
    return sentence


# print('Prediction: ' + generate_sentence(new_dict))


def sentence_verifier(k_word):
    x = 1
    while x == 1:
        try:

            y = 1
            while y == 1:
                created_dict=create_dict()
                pred = generate_sentence(created_dict, k_word, 10)
                validation = Sentence_PostProcessor.sentence_validate(pred)
                if validation == "correct":
                    print('Prediction: ' + pred)
                    y = 0
                    return pred
                elif validation == "incorrect":
                    print('Incorrect sentence')
                    y = 1

            x = 0
        except:
            print('Prediction: error')
            x = 1


def get_final_sentence():
    final_sen = ""
    for key_no in get_key_words():
        final_sen += sentence_verifier(key_no)
    print("Output Sentence: " + final_sen)
    return final_sen


#get_final_sentence()
