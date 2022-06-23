
# def act_1_10_1_code(): # code from activity 1.10.1 ; use as reference
#     word_list = ["cat", "dog", "rabbit"]
#     letter_list = [ ]
#     for a_word in word_list:
#         for a_letter in a_word:
#             letter_list.append(a_letter)
#     print(letter_list)

def comp_list():
    # the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']

    word_list = ["cat", "dog", "rabbit"]
    word_string = (''.join(word_list))

    print(word_string)


    # letter_list = [ word.join(', ', ) for word in word_list]

    # print(letter_list)
    
comp_list()

