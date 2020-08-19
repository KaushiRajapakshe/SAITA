from Models.Inputs import Input
from Util.Sentence_Generator import get_final_sentence


class SentenceController:

    @classmethod
    def sentence_generator_results(cls, keywords):
        inp = Input.get_input()
        nontech_keyward = keywords[0][0]
        print(nontech_keyward)
        inp.set_keyword(nontech_keyward)
        return get_final_sentence()
