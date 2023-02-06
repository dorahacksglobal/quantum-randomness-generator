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
    def __init__(self):
        Circuit.__init__(self)
        self.name = 'A0B0'

        self.activate_bell_state()
        self.circuit.z(0)
        self.circuit.h(1)


class A0B1Circuit(Circuit):
    def __init__(self):
        Circuit.__init__(self)
        self.name = 'A0B1'

        self.activate_bell_state()
        self.circuit.z(0)
        self.circuit.z(1)
        self.circuit.x(1)
        self.circuit.h(1)


class A1B0Circuit(Circuit):
    def __init__(self):
        Circuit.__init__(self)
        self.name = 'A1B0'

        self.activate_bell_state()
        self.circuit.x(0)
        self.circuit.h(1)


class A1B1Circuit(Circuit):
    def __init__(self):
        Circuit.__init__(self)
        self.name = 'A1B1'

        self.activate_bell_state()
        self.circuit.x(0)
        self.circuit.z(1)
        self.circuit.x(1)
        self.circuit.h(1)