# TEST #
import numpy as np

class Algorithms:

    class NeuralNetwork:
        def __init__(Self, Epoch):
            Self.Epoch = Epoch
            Self.Sigmoid = lambda x : 1 / (1 + np.exp(-x))
            Self.SigmoidDX = lambda x : x * (1 - x)
        def fit(Self, lx_train, ly_train):
            x_train = np.array(lx_train)
            y_train = np.array(ly_train).T
            Self.weights = np.random.random((len(lx_train), len(lx_train[0]))).T
            for _ in range(Self.Epoch):
                x_input = x_train
                y_output = Self.Sigmoid(np.dot(x_input, Self.weights))
                loss = y_train - y_output
                adjust_weights = loss * Self.SigmoidDX(y_output)
                Self.weights += np.dot(x_input.T, adjust_weights)
            return Self.weights
        def predict(Self, x_test):
            y_output = Self.Sigmoid(np.dot(x_test, Self.weights))
            return y_output

    class KNN:
        def __init__(Self):
            Self.EuclideanDist = lambda x, y : np.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
        def fit(Self, x_train, y_train):
            Self.x_train = x_train
            Self.y_train = y_train
        def predict(Self, x_test):
            predictions = []
            for row in x_test:
                label = Self.closest(row)
                predictions.append(label)
            return predictions
        def closest(Self, data):
            best_dist = Self.EuclideanDist(data, Self.x_train[0])
            best_index = 0
            for i in range(1, len(Self.x_train)):
                dist = Self.EuclideanDist(data, Self.x_train[i])
                if dist < best_dist:
                    best_dist = dist
                    best_index = i
            return Self.y_train[best_index]

if __name__ == '__main__':
    print('Please use this as library')
    print('or do not put .py when importing')
    x = input()
