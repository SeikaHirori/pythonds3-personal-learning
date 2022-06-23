
# def act_1_10_1_code(): # code from activity 1.10.1 ; use as reference
#     word_list = ["cat", "dog", "rabbit"]
#     letter_list = [ ]
#     for a_word in word_list:
#         for a_letter in a_word:
#             letter_list.append(a_letter)
#     print(letter_list)

import functools


def comp_list():
    # the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']

    word_list = ["cat", "dog", "rabbit"]
    
    # Option 1
    word_string = (''.join(word_list))
    letter_list = [letter for letter in word_string]

    # Option 2
    letter_list = [word[i] for word in word_list for i in range(len(word))]


    print(list(letter_list))

    
def no_duplicate():
    # the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

    word_list = ["cat", "dog", "rabbit"]
    
    # Option 1
    # word_string = (''.join(word_list))
    # letter_list =[letter for letter in word_string]

    # Option 2
    letter_list = [word[i] for word in word_list for i in range(len(word))]


    seen = list(set(letter_list))


    print (list(seen))

