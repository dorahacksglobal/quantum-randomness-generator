from braket.circuits import Circuit
from braket.aws import AwsDevice

class TwoBitCircuit():
    def __init__(self, code):
        self.__name__ = code
        self.circuit = Circuit()
        self._activate_bell_state()
    
        if code == 'a0b0':
            self._apply_a0b0()
        elif code == 'a0b1':
            self._apply_a0b1()
        elif code == 'a1b0':
            self._apply_a1b0()
        elif code == 'a1b1':
            self._apply_a1b1()
        else:
            raise ValueError('Wrong code.')
            
    
    def _activate_bell_state(self):
        self.circuit = Circuit()
        self.circuit.h(0).cnot(0, 1)
        return 
        
    def _apply_a0b0(self):
        self.circuit.h(0)
        self.circuit.s(1).h(1).t(1).h(1)
        return 
    
    def _apply_a0b1(self):
        self.circuit.h(0)
        self.circuit.s(1).h(1).ti(1).h(1)
        return 
    
    def _apply_a1b0(self):
        self.circuit.s(1).h(1).t(1).h(1)
        return 
    
    def _apply_a1b1(self):
        self.circuit.s(1).h(1).ti(1).h(1)
        return 