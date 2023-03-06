import os
from qiskit_ibm_runtime import QiskitRuntimeService

token = ''
instance = ''

service = QiskitRuntimeService(channel="ibm_cloud", token=token, instance=instance)

generator_data = os.path.join(
    os.getcwd(), "generator.py"
)
generator_json = os.path.join(
    os.getcwd(), "generator.json"
)

with open('generator.json', 'w') as file:
    json.dump(dictionary, file)