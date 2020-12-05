# import numpy
import random, os

learningRate = 1
bias = 1
weights = [random.random(), random.random(), random.random()]

def Perceptron(i1, i2, out):
    pOut = i1*weights[0] + i2*weights[1] + bias*weights[2]

    if(pOut > 0): # Heavyside activation
        pOut = 1
    else:
        pOut = 0
    
    error = out - pOut
    weights[0] += error * i1 * learningRate
    weights[1] += error * i2 * learningRate
    weights[2] += error * bias * learningRate

for i in range(50):
    Perceptron(1,1,1)
    Perceptron(1,0,1)
    Perceptron(0,1,1)
    Perceptron(0,0,0)
    
# test with user input
x = int(input())
y = int(input())

pOut = x*weights[0] + y*weights[1] + bias*weights[2]
if(pOut > 0):
    pOut = 1
else:
    pOut = 0

print(x, "or", y, "is: ", pOut) # print result

# Alternate sigmoid activation
# pOut = 1/(1+numpy.exp(-pOut))

# Will produce a decimal value rather than being forced to t/f