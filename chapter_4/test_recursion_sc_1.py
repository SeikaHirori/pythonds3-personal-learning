from recursion_sc_1 import *


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("l") == "l"
    assert reverse("follow") == "wollof"
    assert reverse("") == ""