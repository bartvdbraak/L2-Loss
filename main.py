#%Credits to Prof. Emra on his Deep Learning course at METU
import numpy as np
import pickle, gzip
import hw1_sol as hw1
import sys
from matplotlib import pyplot as plt
import plot_boundary_on_data  

# Read in training data
with gzip.open(sys.argv[1]) as f:
    data, labels = pickle.load(f)

# Starting values for w and b
w0 = np.zeros(data.shape[1])
b0 = 0

# Optimization
w,b = hw1.minimize_l2loss(data, labels, w0,b0, int(sys.argv[3]),
        float(sys.argv[4]))

# Show the result of training
#print w,b
if w.size==2:
    plot_boundary_on_data.plot(data, labels, lambda x: hw1.f(x,w,b)>.5)

if w.size==784: # special to MNIST
    plt.imshow(w.reshape(28,28));
    plt.show()


# Test on test data
with gzip.open(sys.argv[2]) as f:
    test_data, test_labels = pickle.load(f)
yhat = hw1.f(test_data, w, b)>=.5
print np.mean(yhat==test_labels)*100, "% of test examples classified correctly."

hw1.evaluate(hw1.f(test_data, w, b), test_labels)
