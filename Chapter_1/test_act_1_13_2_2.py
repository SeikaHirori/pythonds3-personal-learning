import pytest

from act_1_13_2_2 import NorGate, NandGate

def test_NorGate_Both_Zero(mocker): #TODO: write out code
    ng0 = NorGate("Nor Gate with Zeros")
    
    mocker.patch('builtins.input', side_effect=['0','0'])
    output_ng0 = ng0.perform_gate_logic()

    assert output_ng0 == 1, "If both pins are 'a = 0' and 'b = 0', output should be 1."

def test_NorGate_Either_Are_One(mocker): #TODO: write out code

    ng1 = NorGate("Nor Gate with a 1")

    mocker.patch('builtins.input', side_effect=['0','1'])
    output_ng1 = ng1.perform_gate_logic()

    assert output_ng1 == 0, "If either pins are '1', output should be '0'."

    ng2 = NorGate("Nor Gate with both ones")

    mocker.patch('builtins.input', side_effect=['1',
    '1'])
    output_ng2 = ng2.perform_gate_logic()

    assert output_ng2 == 0, "If either pins are '1', output should be '0'."




def test_NandGate_Both_One(mocker): #TODO: write out code

    output = None
    
    assert output == 0, "If both pins are 'a = 1' and 'b = 1', output should be '0'."

def test_NandGate_Either_Are_Zero(mocker): #TODO: write out code

    output = None

    assert output == 1, "If either pins are '0', output should be '1'."
