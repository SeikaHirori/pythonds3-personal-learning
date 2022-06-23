
# def act_1_10_1_code(): # code from activity 1.10.1 ; use as reference
#     word_list = ["cat", "dog", "rabbit"]
#     letter_list = [ ]
#     for a_word in word_list:
#         for a_letter in a_word:
#             letter_list.append(a_letter)
#     print(letter_list)

import functools

from collections import OrderedDict


def comp_list():
    # the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']

    word_list = ["cat", "dog", "rabbit"]
    
    # Option 1 ; my code
        # Example of using .join()
        #   Link: https://stackoverflow.com/a/11178075
    word_string = (''.join(word_list))
    letter_list = [letter for letter in word_string]

    # # Option 2
    # letter_list = [word[i] for word in word_list for i in range(len(word))]
    # print(list(letter_list))

    return list(letter_list)

def print_list():
    print (comp_list())

    
def no_duplicate():
    original_list = comp_list()

    # https://stackoverflow.com/a/480227
        # - How to handle duplicates WHILE maintaining order

    seen = set()
    seen_add = seen.add

    freedom_list = [letter for letter in original_list if not (letter in seen or seen_add(letter))]

    print (freedom_list)

