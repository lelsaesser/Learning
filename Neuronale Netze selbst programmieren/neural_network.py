# Three layer neural network, trained with the MNIST dataset
# Copyright Tariq Rashid, 2016 (see readme for source details)

import numpy as np
import scipy.special
import matplotlib.pyplot

class NeuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        
        # weight matrices
        # wih - weights between input and hidden layer
        # who - weights between hidden and output layer
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
                
        # using sigmoid activation function
        self.activation_function = lambda x: scipy.special.expit(x)
        
        pass
    
    def train(self, inputs_list, targets_list):
        # convert lists to 2d array
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        
        # calculate signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calculate signals into final output layer
        final_inputs = np.dot(self.who, hidden_outputs)
        # calculate the signals emerging from hidden layer
        final_outputs = self.activation_function(final_inputs)
        
        # error of each layer
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, output_errors)
        
        # update weights (backpropagation)
        # between hidden and output layer
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        # and between input and hidden layer
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))

        pass
    
    def query():
        # in progress
        pass