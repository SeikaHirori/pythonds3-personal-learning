import pytest
import io

from act_1_13_2 import AndGate, LogicGate, BinaryGate, UnaryGate

def test_AndGate(monkeypatch, capsys):
    g1 = AndGate('G1')


    # Non-working code; to be removed after getting a working code
        # monkeypatch.setattr('sys.stdin', io.StringIO('1\n'))

        # monkeypatch.setattr('sys.stdin', io.StringIO('0'))

    output = g1.perform_gate_logic()

    # captured = capsys.readouterr()

    assert output == 0, "Should return: 0"


