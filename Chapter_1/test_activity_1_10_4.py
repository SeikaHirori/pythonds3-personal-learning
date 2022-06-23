import pytest

from activity_1_10_4 import comp_list

def test_comp_list(capsys):
    comp_list() #function prints at the end
    captured = capsys.readouterr()

    assert captured.out == "['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']\n"
