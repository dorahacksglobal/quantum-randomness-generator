from braket.circuits import Circuit
from braket.aws import AwsDevice

class TwoBitCircuit():
    def __init__(self, code, control, act):
        self.__name__ = code
        self.control = control
        self.act = act
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
        self.circuit.h(self.control).cnot(self.control, self.act)
        return 
        
    def _apply_a0b0(self):
        self.circuit.s(self.act).h(self.act).t(self.act).h(self.act)
        return 
    
    def _apply_a0b1(self):
        self.circuit.s(self.act).h(self.act).ti(self.act).h(self.act)
        return 
    
    def _apply_a1b0(self):
        self.circuit.h(self.control)
        self.circuit.s(self.act).h(self.act).t(self.act).h(self.act)
        return 
    
    def _apply_a1b1(self):
        self.circuit.h(self.control)
        self.circuit.s(self.act).h(self.act).ti(self.act).h(self.act)
        return 