from qiskit import QuantumCircuit


class Circuit:
    def __init__(self):
        self.circuit = QuantumCircuit(2, 2)

    def activate_bell_state(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)

    def measure(self):
        self.circuit.measure([0, 1], [0, 1])


class A0B0Circuit(Circuit):
    code = '00'
    name = 'A0B0'
    
    def __init__(self):
        Circuit.__init__(self)

        self.activate_bell_state()
        self.circuit.z(0)
        self.circuit.h(1)
        
        self.measure()


class A0B1Circuit(Circuit):
    code = '01'
    name = 'A0B1'    
    
    def __init__(self):
        Circuit.__init__(self)

        self.activate_bell_state()
        self.circuit.z(0)
        self.circuit.z(1)
        self.circuit.x(1)
        self.circuit.h(1)
        
        self.measure()


class A1B0Circuit(Circuit):
    code = '10'
    name = 'A1B0'

    def __init__(self):
        Circuit.__init__(self)

        self.activate_bell_state()
        self.circuit.x(0)
        self.circuit.h(1)
        
        self.measure()


class A1B1Circuit(Circuit):
    code = '11'
    name = 'A1B1'

    def __init__(self):
        Circuit.__init__(self)
        
        self.activate_bell_state()
        self.circuit.x(0)
        self.circuit.z(1)
        self.circuit.x(1)
        self.circuit.h(1)
        
        self.measure()
        
        
class CompactCircuit:
    def __init__(self):
        circuit = QuantumCircuit(8, 8)
        circuit.h([0, 2, 4, 6])
        [circuit.cx(0, 1), circuit.cx(2, 3), circuit.cx(4, 5), circuit.cx(6, 7)]
        # a0b0 
        circuit.z(0)
        circuit.h(1)
        # a0b1
        circuit.z(2)
        circuit.z(3)
        circuit.x(3)
        circuit.h(3)
        # a1b0
        circuit.x(4)
        circuit.h(5)
        # a1b1
        circuit.x(6)
        circuit.z(7)
        circuit.x(7)
        circuit.h(7)
        
        self.circuit = circuit
        
        self.circuit.barrier()
    
    def measure(self):
        self.circuit.measure(range(8), range(8))
