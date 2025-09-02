# Write a Program to develop simple single layer perceptron 
# to implement AND, OR Boolean functions.

from sklearn.linear_model import Perceptron

def perceptron_logic_gate(gate="AND"):
    if gate == 'AND':
        X = [[0,0],[0,1],[1,0],[1,1]]
        y = [0,0,0,1]
    elif gate == 'OR':
        X = [[0,0],[0,1],[1,0],[1,1]]
        y = [0,1,1,1]

    model = Perceptron()
    model.fit(X, y)

    print(f"{gate} Gate Predictions:")
    for x in X:
        print(f"{x} -> {model.predict([x])[0]}")

perceptron_logic_gate('AND')
perceptron_logic_gate('OR')
