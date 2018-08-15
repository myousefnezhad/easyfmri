import tensorflow as tf
import numpy as np

class MLP:
    def __init__(self):
        self.layer   = dict()
        self.weights = dict()
        self.biases  = dict()


    def multilayer_perceptron(self, x, LayerShape=[10, 10], Activation='relu'):
        if len(LayerShape) == 1:
            self.weights['out'] = tf.Variable(tf.random_normal([np.int32(x._shape[1]), LayerShape[0]], 0, 0.1))
            self.biases['out'] = tf.Variable(tf.random_normal([LayerShape[0]], 0, 0.1))
            self.layer['out'] = tf.add(tf.matmul(x, self.weights['out']), self.biases['out'])
        else:
            for layer_index in range(0, len(LayerShape)):
                if layer_index == 0:
                    self.weights['h' + str(layer_index + 1)] = tf.Variable(tf.random_normal([np.int32(x._shape[1]), LayerShape[layer_index]], 0, 0.1))
                    self.biases['b' + str(layer_index + 1)]  = tf.Variable(tf.random_normal([LayerShape[layer_index]], 0, 0.1))
                    if   Activation == 'relu':
                        self.layer['l' + str(layer_index + 1)]   = tf.nn.relu(tf.add(tf.matmul(x, self.weights['h' + str(layer_index + 1)]), self.biases['b' + str(layer_index + 1)]))
                    elif Activation == 'sigmoid':
                        self.layer['l' + str(layer_index + 1)]   = tf.nn.sigmoid(tf.add(tf.matmul(x, self.weights['h' + str(layer_index + 1)]), self.biases['b' + str(layer_index + 1)]))
                    else:
                        self.layer['l' + str(layer_index + 1)]   = tf.nn.tanh(tf.add(tf.matmul(x, self.weights['h' + str(layer_index + 1)]), self.biases['b' + str(layer_index + 1)]))
                elif layer_index == len(LayerShape) - 1:
                    self.weights['out'] = tf.Variable(tf.random_normal([LayerShape[layer_index - 1], LayerShape[layer_index]], 0, 0.1))
                    self.biases['out']  = tf.Variable(tf.random_normal([LayerShape[layer_index]], 0, 0.1))
                    self.layer['out']   = tf.add(tf.matmul(self.layer['l' + str(layer_index)], self.weights['out']), self.biases['out'])
                else:
                    self.weights['h' + str(layer_index + 1)] = tf.Variable(tf.random_normal([LayerShape[layer_index - 1], LayerShape[layer_index]], 0, 0.1))
                    self.biases['b' + str(layer_index + 1)]  = tf.Variable(tf.random_normal([LayerShape[layer_index]], 0, 0.1))
                    if   Activation == 'relu':
                        self.layer['l' + str(layer_index + 1)]   = tf.nn.relu(tf.add(tf.matmul(self.layer['l' + str(layer_index)], self.weights['h' + str(layer_index + 1)]), self.biases['b' + str(layer_index + 1)]))
                    elif Activation == 'sigmoid':
                        self.layer['l' + str(layer_index + 1)]   = tf.nn.sigmoid(tf.add(tf.matmul(self.layer['l' + str(layer_index)], self.weights['h' + str(layer_index + 1)]), self.biases['b' + str(layer_index + 1)]))
                    else:
                        self.layer['l' + str(layer_index + 1)]   = tf.nn.tanh(tf.add(tf.matmul(self.layer['l' + str(layer_index)], self.weights['h' + str(layer_index + 1)]), self.biases['b' + str(layer_index + 1)]))
        return self.layer['out']


    def return_values(self, sess=None):
        if sess is None:
            return None, None
        weights = dict()
        biases = dict()
        for wkey in self.weights.keys():
            weights[wkey] = sess.run(self.weights[wkey])
        for bkey in self.biases.keys():
            biases[bkey] = sess.run(self.biases[bkey])
        return weights, biases