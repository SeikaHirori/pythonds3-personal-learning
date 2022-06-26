import pytest
import io

from act_1_13_2 import AndGate, LogicGate, BinaryGate, UnaryGate

def test_AndGate(monkeypatch, capsys):
    g1 = AndGate('G1')

    # Try to use mock WITH and WITHOUT pytest-mock:
        # SFO: https://stackoverflow.com/a/56498519
    # Method #1: Using 'the_prompt'
    def test_inputs(the_prompt):
        prompt_to_return_val = {'Enter pin A input for gate G1: ': '1', 'Enter pin B input for gate G1: ': '0'}
        val = prompt_to_return_val[the_prompt]
        return val

    monkeypatch.setattr('builtins.input', test_inputs)
    output = g1.perform_gate_logic()

    # captured = capsys.readouterr()

    assert output == 0, "Should return: 0"


