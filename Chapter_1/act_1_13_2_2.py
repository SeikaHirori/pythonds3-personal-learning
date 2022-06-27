

# Lesson URL: https://runestone.academy/ns/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html?lastPosition=13421


class LogicGate: 

    def __init__(self, lbl):
        self.label = lbl
        self.output = None
    
    def get_label(self):
        return self.label
    
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    
    def __init__(self, lbl):
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

    def __init__(self, lbl):
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
    def __init__(self, lbl):
        super().__init__(lbl)
    
    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 or b == 1:
            return 1
        else:
            return 0
 
class NotGate(UnaryGate): # My code - OKIE; seems fine
    
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1

class NorGate(BinaryGate): #TODO: write out code
    def __init__(self, lbl):
        super().__init__(lbl)
    
    def perform_gate_logic(self):
        return -1


    
class NandGate(BinaryGate): #TODO: write out code
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        return -1

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


if __name__ == "__main__":
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())
    