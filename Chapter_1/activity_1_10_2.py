import pytest



# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

def problem():
    word_list = ["cat", "dog", "rabbit"]
    letter_list = [ ]
    for a_word in word_list:
        for a_letter in a_word:
            if a_letter not in letter_list:
                letter_list.append(a_letter)
    print(letter_list)


# if __name__ == '__main__':
#     problem()

problem()