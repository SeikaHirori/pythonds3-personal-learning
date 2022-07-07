import pytest

from act_1_13_2_2 import NorGate, NandGate

def test_NorGate_Both_Zero(mocker): #TODO: NorGate Test not passed
    ng0 = NorGate("Nor Gate with 0s")
    
    mocker.patch('builtins.input', side_effect=['0','0'])
    output_ng0 = ng0.perform_gate_logic()

    assert output_ng0 == 1, "If both pins are 'a = 0' and 'b = 0', output should be 1."

def test_NorGate_Either_Are_One(mocker): #TODO: NorGate Test not passed

    ng1 = NorGate("Nor Gate with a 1")

    mocker.patch('builtins.input', side_effect=['0','1'])
    output_ng1 = ng1.perform_gate_logic()

    assert output_ng1 == 0, "If either pins are '1', output should be '0'."

    ng2 = NorGate("Nor Gate with both ones")


    mocker.patch('builtins.input', side_effect=['1',
    '1'])
    output_ng2 = ng2.perform_gate_logic()

    assert output_ng2 == 0, "If either pins are '1', output should be '0'."

def test_NandGate_Both_One(mocker): #TODO: NandGate test not passed

    nd_g1 = NandGate("Nand gate with both 1s")

    mocker.patch('builtins.input', side_effect = ['1', '1'])
    output_nd_g1 = nd_g1.perform_gate_logic()
    
    assert output_nd_g1 == 0, "If both pins are 'a = 1' and 'b = 1', output should be '0'."

def test_NandGate_Either_Are_Zero(mocker): #TODO: NandGate test not passed

    nd_g0 = NandGate("Nand gate with a 0")

    mocker.patch('builtins.input', side_effect = ['0', '1'])
    output_nd_g0 = nd_g0.perform_gate_logic()

    assert output_nd_g0 == 1, "If either pins are '0', output should be '1'."
