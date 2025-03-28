import numpy as np 

def sigmoid(x):
    return 1 / (1+np.exp(-x))

training_inputs = np.array([[0, 0, 1],
                           [1, 1, 1],
                           [1, 0, 1],
                           [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weights = np.random.normal(0, (1 / 3), size=(3, 1))

print("random weights: " + str(synaptic_weights))

for i in range(2000):

    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    synaptic_weights += adjustments

print("weights after")
print(synaptic_weights)

print("result")
print(outputs)

new_inputs = np.array([1, 1, 1])
output = sigmoid(np.dot(new_inputs, synaptic_weights))

print("new situation")
print(output)