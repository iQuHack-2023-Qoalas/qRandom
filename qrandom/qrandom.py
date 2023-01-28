"""
This module utilizes quantum computers 
to produce truly random numbers
"""

############################################################################### IBMQ:
from qiskit import IBMQ, QuantumCircuit, transpile, execute
# IBMQ.save_account(TOKEN)
IBMQ.load_account() # Load account from disk
IBM_provider = IBMQ.get_provider(hub='ibm-q')
ibm_nairobi = IBM_provider.backends('ibm_nairobi')
ibm_simulator = IBM_provider.backends('ibmq_qasm_simulator')

def ibm_queue(backend):
    while backend.job_limit().maximum_jobs - backend.job_limit().active_jobs <= 0:
        pass
    return

def uniform(L=7, backend=ibm_simulator):
    q = QuantumCircuit(L)
    q.h(range(L))
    q.measure_all()
    dictio = execute(q, backend, shots=1).result().get_counts()
    return int(list(dictio.keys())[0], 2)


from qiskit import QuantumRegister, ClassicalRegister, BasicAer
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.aqua.components.uncertainty_models import NormalDistribution,UniformDistribution,LogNormalDistribution

IBMQ.enable_account('Enter API key')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')

q = QuantumRegister(5,'q')
c = ClassicalRegister(5,'c')

print("\n Normal Distribution")
print("-----------------")

circuit = QuantumCircuit(q,c)
normal = NormalDistribution(num_target_qubits = 5, mu=0, sigma=1, low=- 1, high=1)
normal.build(circuit,q)
circuit.measure(q,c)

job = execute(circuit, backend, shots=8192)
job_monitor(job)
counts = job.result().get_counts()

print(counts)
sortedcounts = []
sortedkeys = sorted(counts)

for i in sortedkeys:
    for j in counts:
        if(i == j):
            sortedcounts.append(counts.get(j))

plt.suptitle('Normal Distribution')
plt.plot(sortedcounts)
plt.show()

print("\n Uniform Distribution")
print("-----------------")

circuit = QuantumCircuit(q,c)
uniform = UniformDistribution(num_target_qubits = 5,low=- 0, high=1)
uniform.build(circuit,q)
circuit.measure(q,c)

job = execute(circuit, backend, shots=8192)
job_monitor(job)
counts = job.result().get_counts()

print(counts)

sortedcounts = []
sortedkeys = sorted(counts)

for i in sortedkeys:
    for j in counts:
        if(i == j):
            sortedcounts.append(counts.get(j))
            
plt.suptitle('Uniform Distribution')
plt.plot(sortedcounts)
plt.show()

print("\n Log-Normal Distribution")
print("-----------------")

circuit = QuantumCircuit(q,c)
lognorm = LogNormalDistribution(num_target_qubits = 5, mu=0, sigma=1, low= 0, high=1)
lognorm.build(circuit,q)
circuit.measure(q,c)

job = execute(circuit, backend, shots=8192)
job_monitor(job)
counts = job.result().get_counts()

print(counts)

sortedcounts = []
sortedkeys = sorted(counts)

for i in sortedkeys:
    for j in counts:
        if(i == j):
            sortedcounts.append(counts.get(j))

plt.suptitle('Log-Normal Distribution')
plt.plot(sortedcounts)
plt.show()

input()





#this function returns a random integer
def randint():
    pass

#this function returns a random integer between x (inclusive) and y (exclusive)
def randrange(x,y):
    pass