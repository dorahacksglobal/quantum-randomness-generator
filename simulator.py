import numpy as np

from qiskit import QuantumCircuit, execute
from qiskit.providers.aer import Aer, QasmSimulator

from circuit import Circuit


if __name__ == '__main__':
    n = int(input('number of experiments: '))
        
    # define experiment circuits
    experiment_circuits = {circuit.code: circuit for circuit in Circuit.__subclasses__()}

    # backend specification
    backend = QasmSimulator()
    
    for i in range(n):

        # choose experiments based on classical random numbers (X, Y)
        classical_input = ''.join(np.random.choice(['0', '1'], 2))
        circuit = experiment_circuits.get(classical_input)().circuit

        # run on backent (simulator)
        job = backend.run(circuit, shots=1, memory=True)
        result = job.result().get_memory()[0]

        print(result)