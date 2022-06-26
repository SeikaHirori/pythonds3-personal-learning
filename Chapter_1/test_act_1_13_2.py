import pytest
import io

from act_1_13_2 import LogicGate, BinaryGate, UnaryGate, AndGate, NotGate, OrGate, Connector

# def test_AndGate_mocker_original(monkeypatch, capsys): # Use function test 'test_AndGate_PyTest_Mocker(mocker); it's more streamlined for writing and reading... but PyTest-mocker needs to be installed.
#     g1 = AndGate('G1')

#     # Try to use mock WITH and WITHOUT pytest-mock:
#         # SFO: https://stackoverflow.com/a/56498519

#     # Method 1 | Mocker: Using stock mocker
#     def test_inputs(the_prompt):
#         prompt_to_return_val = {'Enter pin A input for gate G1: ': '1', 'Enter pin B input for gate G1: ': '0'}
#         val = prompt_to_return_val[the_prompt]
#         return val

#     monkeypatch.setattr('builtins.input', test_inputs)
#     # monkeypatch.setattr('sys.stdin', test_inputs)
#     outputValue = g1.perform_gate_logic()

#     # captured = capsys.readouterr()

#     assert outputValue == 0, "Should return: 0"

def test_AndGate_PyTest_Mocker(mocker):
    # Method 2 | Mocker; Using Pytest-mocker
    # Use this toolset: https://github.com/pytest-dev/pytest-mock


    g1 = AndGate('G1')

    mocker.patch('builtins.input', side_effect=['1', '0'])

    outputValue = g1.perform_gate_logic()

    assert outputValue == 0, 'Should return: 0'

def test_OrGate_equals_0(mocker): 
    
    or_gate_0 = OrGate("Or Gate 0")

    mocker.patch('builtins.input', side_effect=['0', '0'])
    output_OrGate_0 = or_gate_0.perform_gate_logic()

    assert output_OrGate_0 == 0, "Should return: 0"

def test_OrGate_equals_1(mocker):
    or_gate_1 = OrGate("Or Gate 1")

    mocker.patch('builtins.input', side_effect=['1','1'])
    output_OrGate_1= or_gate_1.perform_gate_logic()

    assert output_OrGate_1 == 1,"Should return: 1"

def test_NotGate(mocker): 
    not_gate = NotGate('Not Gate')

    mocker.patch('builtins.input', side_effect=['0'])
    output_notGate = not_gate.perform_gate_logic()

    assert output_notGate == 1


def test_runtime_code_from_lecture(capsys, mocker): # From ActiveCode 4
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    
    mocker.patch("builtins.input", side_effect=["0","1","1","1"])

    output_value = g4.get_output()

    assert output_value == 0, "Should return: 0"