import pytest

from ActiveCode4 import test_code
from Chapter_1.ActiveCode.ActiveCode4 import AndGate, Connector, NotGate, OrGate

def test_main(mocker, capsys):
    
    mocker.patch('sys.stdin', side_effect=['0','1','1','1'])

    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    
    
    output_value = g4.get_output()

    assert output_value == 0, "Should return: 0"