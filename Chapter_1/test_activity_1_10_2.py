import pytest

from activity_1_10_2 import problem_list, print_list

def test_problem_list():
    assert problem_list() == ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

def test_stdout():
    print_list()