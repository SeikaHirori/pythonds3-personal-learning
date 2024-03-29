import pytest
import pytest_mock

# Lesson URL: https://runestone.academy/ns/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html?lastPosition=13421

### ====== Imported code - BEGINS ====== ###

class LogicGate: 

    def __init__(self, lbl:str=None):
        self.label = lbl
        self.output = None
    
    def get_label(self):
        return self.label
    
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    
    def __init__(self, lbl:str=None):
        super().__init__(lbl)
        # super(BinaryGate, self).__init__(lbl)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            output_pin_a = int(input(f'Enter pin A input for gate {self.get_label()}: '))
            return output_pin_a
        else:
            return self.pin_a.get_from().get_output()
    
    def get_pin_b(self):
        if self.pin_b == None:
            output_pin_b = int(input(f'Enter pin B input for gate {self.get_label()}: '))
            return output_pin_b
        else: 
            return self.pin_b.get_from().get_output()

    # Listing 13; in class 'BinaryGate'
    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else: # maybe change this to print later to see if it changes anything?
                print("Cannot Connect: NO EMPTY PINS on this gate.")

class UnaryGate(LogicGate):

    def __init__(self, lbl:str=None):
        super().__init__(lbl)
        # LogicGate.__init__(self, lbl)

        self.pin = None
    
    def get_pin(self):
        if self.pin == None:
            return int(input(f'Enter pin input for gate {self.get_label()}: '))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate.")
            # raise RuntimeError("Error: NO EMPTY PINS on this gate.") 

class AndGate(BinaryGate): # my code - On Deck
    def __init__(self, lbl): 
        super().__init__(lbl)
    
    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate): # My code - OKIE
    def __init__(self, lbl:str=None):
        super().__init__(lbl)
    
    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 or b == 1:
            return 1
        else:
            return 0
 
class NotGate(UnaryGate): # My code - OKIE; seems fine
    
    def __init__(self, lbl:str=None):
        super().__init__(lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1

class NorGate(OrGate): 

    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1
    
class NandGate(AndGate): 

    def perform_gate_logic(self):
        if super().perform_gate_logic() == 0:
            return 1
        else: 
            return 0

#p10
class XorGate(BinaryGate):
    
    def __init__(self, lbl:str=None):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if (a == 0 and b == 1) or (a == 1 and b == 0):
            return 1
        else:
            return 0

#p10
class XnorGate(XorGate):

    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

#p11
class HalfAdder(BinaryGate): #v1
        # Explaination of HalfAdder: https://www.circuitstoday.com/half-adder#:~:text=Half%20adder%20is%20a%20combinational,AND%20of%20A%20and%20B.
    def __init__(self,lbl:str=None):
        super().__init__(lbl)
        self.sum_bit = None
        self.carry_bit = None
        self.xor_gate = XorGate
        self.and_gate = AndGate

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if (a == 0 and b == 0) or (a == 1 and b == 1): # XOR gate
            self.sum_bit = 0
        else:
            self.sum_bit = 1

        if a == 1 and b == 1: # AND logic
            self.carry_bit = 1
        else:
            self.carry_bit = 0
                

#p12
class FullAdder(BinaryGate):
    def __init__(self, lbl:str=None):
        super().__init__(lbl)
        self.cout = None
        self.sum = None
    
    def perform_gate_logic(self):
        half1 = HalfAdder()
        half1.perform_gate_logic()

        sum_half1 = half1.sum_bit
        cout1_half1 = half1.carry_bit
        carry_in_half2 = self.get_pin_a()

        sum_output = None
        cout2_half2 = None
        # HalfAdder2
        if (sum_half1 == 0 and carry_in_half2 == 0) or (sum_half1 == 1 and carry_in_half2 == 1): # XOR gate
            sum_output = 0
        else:
            sum_output = 1
        if sum_half1 == 1 and carry_in_half2 == 1: # AND logic
            cout2_half2 = 1
        else:
            cout2_half2 = 0
        
        cout_output = None
        if cout1_half1 == 1 or cout2_half2 == 1:
            cout_output = 1
        else:
            cout_output = 0



        self.sum = sum_output
        self.cout = cout_output







class Connector: # my code - OKIE

    # Listing 12
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate
    def get_to(self):
        return self.to_gate

class Demo:
    
    def set_one(mocker):
        
        
        g1 = NorGate("G1")
        g2 = NorGate("G2")
        g3 = NandGate("G3")
        g4 = NotGate("G4")
        c1 = Connector(g1, g3)
        c2 = Connector(g2, g3)
        c3 = Connector(g3, g4)

        mocker.patch(__name__ + 'builtins.input', side_effect = ['0','0','0','0'] )

        print(g4.get_output())
## ====== Imported code - ENDS ====== ###



if __name__ == "__main__":
    pass