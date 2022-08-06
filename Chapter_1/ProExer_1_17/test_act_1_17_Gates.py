import pytest



from act_1_17_Gates import FullAdder, XorGate, XnorGate, HalfAdder

#p10
def test__XOR__return_0(mocker): 

    xor_1 = XorGate('XOR gate #1')
    
    mocker.patch('builtins.input', side_effect=['0', '0'])
    output_1 = xor_1.perform_gate_logic()

    assert output_1 == 0, 'If A and B are both 0, it should return 0'
    'If both A and B are same, it should return 0'


    xor_2 = XorGate('XOR gate #2')

    mocker.patch('builtins.input', side_effect=['1','1'])
    output_1 = xor_2.perform_gate_logic()

    assert output_1 == 0, 'If both A and B are 1, it should return 0'

#p10
def test__XOR__return_1(mocker): 

    xor_1 = XorGate('XOR gate #1')
    
    mocker.patch('builtins.input', side_effect=['0', '1'])
    output_1 = xor_1.perform_gate_logic()

    assert output_1 == 1, 'If A and B are 0 and 1, it should return 1'


    xor_2 = XorGate('XOR gate #2')

    mocker.patch('builtins.input', side_effect=['1','0'])
    output_1 = xor_2.perform_gate_logic()

    assert output_1 == 1, 'If A and B are 1 and 0, it should return 1'


#p10
def test__XNOR__return_0(mocker):

    xnor_1 = XnorGate('XNOR #1')

    mocker.patch('builtins.input', side_effect=['0', '1'])
    output_0_and_1 = xnor_1.perform_gate_logic()
    
    assert output_0_and_1 == 0, "A and B are 0 and 1, should result in 0"


    xnor_2 = XnorGate('XNOR #2')

    mocker.patch('builtins.input', side_effect=['1','0'])
    output_1_and_0 = xnor_2.perform_gate_logic()
    
    assert output_1_and_0 == 0, "If A and B 1 and 0, it should result in 0"


#p10
def test__XNOR__return_1(mocker):
    
    xnor_3 = XnorGate('XNOR #3')

    mocker.patch('builtins.input', side_effect=['0', '0'])
    output_1 = xnor_3.perform_gate_logic()

    assert output_1 == 1, "If both A and B are 0 and 0, it should result in 1"


    xnor_4 = XnorGate('XNOR #4')

    mocker.patch('builtins.input', side_effect=['1','1'])
    output_1 = xnor_4.perform_gate_logic()

    assert output_1 == 1, "If both A and B are 1 and 1, it should result in 1"

#p11 
def test__HalfAdder_Sum_bit_0(mocker):
    has_1 = HalfAdder('0 and 0')

    mocker.patch('builtins.input', side_effect=['0', '0'])

    has_1.perform_gate_logic()
    output_1 = has_1.sum_bit

    assert output_1 == 0, '"a = 0" and "b = 0" should return 0'


    has_2 = HalfAdder('1 and 1')

    mocker.patch('builtins.input', side_effect=['1','1'])

    has_2.perform_gate_logic()
    output_2 = has_2.sum_bit

    assert output_2 == 0, '"a = 1" and "b = 1" should return 0'

def test_HalfAdder_sum_bit_1(mocker):
    has_3 = HalfAdder('1 and 0')

    mocker.patch('builtins.input', side_effect=['1', '0'])

    has_3.perform_gate_logic()
    output_3 = has_3.sum_bit

    assert output_3 == 1, '"a = 1" and "b = 0" should return 1'

    has_4 = HalfAdder('0 and 1')

    mocker.patch('builtins.input', side_effect=['0', '1'])

    has_4.perform_gate_logic()
    output_4 = has_4.sum_bit

    assert output_4 == 1, '"a = 0" and "b = 1" should return 1'
    

def test__HalfAdder_carry_bit_0(mocker):
    
    mocker.patch('builtins.input', side_effect=['0', '1'])


    ha_cb_1 = HalfAdder('0 and 0')

    ha_cb_1.perform_gate_logic()
    output_1 = ha_cb_1.carry_bit
    assert output_1 == 0, 'If the a != 1 and b != 1, the carry bit should be 0'


    ha_cb_2 = HalfAdder('1 and 0')
    mocker.patch('builtins.input', side_effect=['1', '0']) 

    ha_cb_2.perform_gate_logic()
    output_2 = ha_cb_2.carry_bit
    assert output_2 == 0, 'If the a != 1 and b != 1, the carry bit should be 0'


    ha_cb_3 = HalfAdder('0 and 1')
    mocker.patch('builtins.input', side_effect=['0', '0'])

    ha_cb_3.perform_gate_logic()
    output_3 = ha_cb_3.carry_bit
    assert output_3 == 0, 'If the a != 1 and b != 1, the carry bit should be 0'


#p11 
def test__HalfAdder_carry_bit_1(mocker):
    
    ha_cb_4 = HalfAdder('1 and 1')
    mocker.patch('builtins.input', side_effect=['1','1'])

    ha_cb_4.perform_gate_logic()
    output_4 = ha_cb_4.carry_bit
    assert output_4 == 1, 'If A and B are both 1, the carry should be one.'

#p12 #TODO
def test__FullAdder_carry_out_0(mocker):
    pass

def test_FullAdder_carry_out_1(mocker):
    fa_co1 = FullAdder("1, 1, 1")



