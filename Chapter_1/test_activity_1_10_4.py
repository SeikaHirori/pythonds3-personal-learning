import pytest

from activity_1_10_4 import comp_list

# Link: https://runestone.academy/ns/books/published/pythonds3/Introduction/ControlStructures.html


# Testing function from source code

def test_comp_list(capsys):
    comp_list() #function prints at the end
    captured = capsys.readouterr()

    assert captured.out == "['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']\n", "should be ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']\n"

    

# def test_no_duplicate_in_list(capsys)

