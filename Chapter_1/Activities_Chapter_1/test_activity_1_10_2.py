import pytest

from activity_1_10_2 import problem_list, print_list

# Link: https://runestone.academy/ns/books/published/pythonds3/Introduction/ControlStructures.html

def test_problem_list():
    assert problem_list() == ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

def test_stdout(capsys):
    # # https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html 
    #     - Doc: how to test for "print" lines
    #     - this function was needed for the problem

    print_list()
    captured = capsys.readouterr()
    assert captured.out == "['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']\n"