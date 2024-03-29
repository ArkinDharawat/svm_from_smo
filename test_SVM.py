from __future__ import division, print_function
import csv, os, sys
import numpy as np
from SVM import SVM
from sklearn import datasets
from sklearn.model_selection import train_test_split

def calc_acc(y, y_hat):
    idx = np.where(y_hat == 1)
    TP = np.sum(y_hat[idx] == y[idx])
    idx = np.where(y_hat == -1)
    TN = np.sum(y_hat[idx] == y[idx])
    return float(TP + TN)/len(y)

def main(C=1.0, epsilon=0.001):
    # Split data
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    class_chosen = 1 # only this class is chosen
    y = np.asarray([-1 if y[i]!=class_chosen else 1 for i in range(y.shape[0])])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    # Initialize model
    model = SVM(X_train, y_train, C=C, tolerance=epsilon)

    # Fit model
    support_vectors, iterations = model.fit()
    # Support vector count
    sv_count = support_vectors.shape[0]

    # Make prediction
    y_hat = model.predict(X_test)

   #  print(y_hat.shape, y_test.shape)

    # Calculate accuracy
    acc = calc_acc(y_test, y_hat)

    print("Support vector count: %d" % (sv_count))
    # print("bias:\t\t%.3f" % (model.b))
    # print("w:\t\t" + str(model.w))
    print("accuracy:\t%.3f" % (acc))
    print("Converged after %d iterations" % (iterations))

if __name__ == '__main__':
    # if ('--help' in sys.argv) or ('-h' in sys.argv):
    #     print("")
    #     print("Trains a support vector machine.")
    #     print("Usage: %s FILENAME C kernel eps" % (sys.argv[0]))
    #     print("")
    #     print("FILENAME: Relative path of data file.")
    #     print("C:        Value of regularization parameter C.")
    #     print("kernel:   Kernel type to use in training.")
    #     print("          'linear' use linear kernel function.")
    #     print("          'quadratic' use quadratic kernel function.")
    #     print("eps:      Convergence value.")
    # else:
    #     kwargs = {}
    #     if len(sys.argv) > 1:
    #         kwargs['filename'] = sys.argv[1]
    #     if len(sys.argv) > 2:
    #         kwargs['C'] = float(sys.argv[2])
    #     if len(sys.argv) > 3:
    #         kwargs['kernel_type'] = sys.argv[3]
    #     if len(sys.argv) > 4:
    #         kwargs['epsilon'] = float(sys.argv[4])
    #     if len(sys.argv) > 5:
    #         sys.exit("Not correct arguments provided. Use %s -h for more information"
    #                  % (sys.argv[0]))
        main()
