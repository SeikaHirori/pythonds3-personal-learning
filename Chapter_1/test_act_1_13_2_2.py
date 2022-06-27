import pytest

from act_1_13_2_2 import NorGate, NandGate

def test_NorGate_Both_Zero(mocker): #TODO: write out code
    ng1 = NorGate("Nor Gate")
    
    # output = None
    mocker.patch('builtins.input', side_effect=['0','0'])
    output = ng1.perform_gate_logic()

    assert output == 1, "If both pins are 'a = 0' and 'b = 0', output should be 1."

def test_NorGate_Either_Are_One(mocker): #TODO: write out code



    output = None

    assert output == 0, "If either pins are '1', output should be '0'."


def test_NandGate_Both_One(mocker): #TODO: write out code

    output = None
    
    assert output == 0, "If both pins are 'a = 1' and 'b = 1', output should be '0'."

def test_NandGate_Either_Are_Zero(mocker): #TODO: write out code

    output = None

    assert output == 1, "If either pins are '0', output should be '1'."
