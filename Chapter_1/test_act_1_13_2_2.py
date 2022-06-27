import pytest

from act_1_13_2_2 import NorGate, NandGate

def test_NorGate_Both_Zero(): #TODO: write out code
    

    output = None

    assert output == 1, "If both pins are 'a = 0' and 'b = 0', output should be 1."

def test_NorGate_Either_Are_One(): #TODO: write out code

    output = None

    assert output == 0, "If either pins are '1', output should be '0'."

def test_NandGate_Both_One(): #TODO: write out code

    output = None
    
    assert output == 0, "If both pins are 'a = 1' and 'b = 1', output should be '0'."

def test_NandGate_Either_Are_Zero(): #TODO: write out code

    output = None

    assert output == 1, "If either pins are '0', output should be '1'."
