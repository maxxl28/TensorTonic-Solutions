import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.clip(x, -100, 100)
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))