from qiskit import transpile

from circuit import Circuit

def prepare_circuits(backend):
    """Generate CHSH game circuits.

    Args:
        backend: Backend used for transpilation.

    Returns:
        Generated circuits. Each circuit corresponds to a CHSH game experiment.
    """
    circuits = [circuit().circuit for circuit in Circuit.__subclasses__()]
    
    return transpile(circuits, backend)


def main(backend, user_messenger, **kwargs):
    """Main entry point of the program.

    Args:
        backend: Backend to submit the circuits to.
        user_messenger: Used to communicate with the program consumer.
        kwargs: User inputs.
    """
    iterations = kwargs.pop("iterations", 4)
    shots = kwargs.pop("shots", 1024)
    memory = kwargs.pop("memory", True)
    for it in range(iterations):
        qc = prepare_circuits(backend)
        result = backend.run(qc, memory=memory, shots=shots).result()
        bits = [result.get_memory(i) for i in range(4)]
        user_messenger.publish({"iteration": iterations, "memory": bits})

    return "Shots: {}, iterations: {}, memory: {}.".format(shots, iterations, bits)
