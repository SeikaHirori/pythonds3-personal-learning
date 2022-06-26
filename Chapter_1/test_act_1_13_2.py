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


    # Non-working code; to be removed after getting a working code
        # monkeypatch.setattr('sys.stdin', io.StringIO('1\n'))

        # monkeypatch.setattr('sys.stdin', io.StringIO('0'))

    monkeypatch.setattr('builtins.stdin', test_inputs())
    output = g1.perform_gate_logic()

    # captured = capsys.readouterr()

    assert output == 0, "Should return: 0"


