import numpy as np

def step_function(soma):
    if soma >= 1:
        return 1
    return 0

def sigmoid_function(soma):
    return 1 / (1 + np.exp(-soma))

def tanh_function(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

def relu_function(soma): # não funciona com uma lista como parametro
    return soma >= 0

def linear_function(soma):
    return soma

def softmax_function(x):
    ex = np.exp(x)
    return ex / ex.sum()
x = 2.1

sigmoid_function(x)
tanh_function(x)
relu_function(x)
linear_function(x)