


# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

def problem_list():
    word_list = ["cat", "dog", "rabbit"]
    letter_list = [ ]
    for a_word in word_list:
        for a_letter in a_word:
            if a_letter not in letter_list:
                letter_list.append(a_letter)
    return letter_list # this is mainly for testing

def print_list():
    word_list = ["cat", "dog", "rabbit"]
    letter_list = [ ]
    for a_word in word_list:
        for a_letter in a_word:
            if a_letter not in letter_list:
                letter_list.append(a_letter)
    print(list(letter_list))



# if __name__ == '__main__':
#     problem()

