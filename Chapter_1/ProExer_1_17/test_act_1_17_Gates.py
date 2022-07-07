import pytest

from act_1_17_gates import XorGate

#p10
def test__XOR__return_0(mocker): # TODO

    xor_1 = XorGate('XOR gate #1')
    
    mocker.patch('builtins.input', side_effect=['0', '1'])
    output_1 = xor_1.perform_gate_logic()

    assert output_1 == 0, 'If both A and B are same, it should return 0'


    xor_2 = XorGate('XOR gate #2')

    mocker.patch('builtins.input', side_effect=['1','0'])
    output_2 = xor_2.perform_gate_logic()

    assert output_2 == 0, 'If both A and B are 1, it should return 0'

#p10
def test__XOR__return_1(mocket): # TODO


    output = None
    assert output == 1, 'If A and B are 0 and 1, it should return 1'


    output = None
    assert output == 1, 'If A and B are 1 and 0, it should return 1'


# #p10
# def test__XNOR__return_0(mocker): #TODO

#     output_0_and_0 = None
#     assert output_0_and_0 == 0, "A and B are 0 and 1, should result in 0"


#     output_1_and_1 = None
#     assert output_1_and_1 == 0, "If A and B 1 and 0, it should result in 0"


# #p10
# def test__XNOR__return_1(mocker):
    
#     output_1 = None
#     assert output_1 == 1, "If both A and B are 0 and 0, it should result in 1"

#     output_2 = None
#     assert output_2 == 1, "If both A and B are 1 and 1, it should result in 1"