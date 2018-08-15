# Gradient Based Representational Similarity Analysis
# Created by Muhammad Yousefnezhad
# iBRAIN, College of Computer Science and Technology
# Nanjing University of Aeronautics and Astronautics
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class DeepGroupRSA:
    def __init__(self, layers=[10,10], kernel_iter = 2000, rsa_iter = 1000, learning_rate=0.001, loss_norm = 'euclidean', activation = 'relu', batch_size = 50, report_step=300, verbose=True, NVoxel=None, NCat = None, CPU=False):
        self.loss_norm      = loss_norm  # 'euclidean', 2, np.inf
        self.activation     = str.lower(activation) # 'relu', 'sigmoid', 'tanh'
        self.learning_rate  = learning_rate
        self.rsa_iter       = rsa_iter
        self.kernel_iter    = kernel_iter
        self.batch_size     = batch_size
        self.report_step    = report_step
        self.Layers         = layers
        self.verbose        = verbose
        self.Beta           = None
        self.Eps            = None
        self.Weights        = None
        self.Biases         = None
        self.loss_mat       = None
        self.AMSE           = None
        self.NVoxel         = NVoxel
        self.NCat           = NCat
        self.CPU            = CPU


    def fit(self, data_vals, design_vals, sess=None):
        import tensorflow as tf
        import numpy as np
        from Network.MLP import MLP
        import os
        # RSA Parameters
        F = tf.placeholder("float", [None, self.NVoxel])
        D = tf.placeholder(shape=[None, self.NCat], dtype=tf.float32)
        Beta = tf.Variable(tf.random_normal(shape=[self.NCat, self.Layers[-1]]))
        Eps  = tf.Variable(tf.random_normal(shape=[1, self.Layers[-1]]))
        # Kernel Optimization
        MappedF = tf.placeholder("float", [None, self.Layers[-1]])
        mlp = MLP()
        kernelmapping = mlp.multilayer_perceptron(F, LayerShape=self.Layers, Activation=self.activation)
        kernel_loss = tf.reduce_mean(tf.square(kernelmapping - tf.matmul(D, Beta)))
        kernel_train = tf.train.AdamOptimizer(learning_rate=self.learning_rate).minimize(kernel_loss)
        # RSA optimization
        rsa_loss  = tf.square(tf.norm(MappedF - tf.add(tf.matmul(D, Beta), Eps), ord=self.loss_norm))
        rsa_train = tf.train.GradientDescentOptimizer(learning_rate=self.learning_rate).minimize(rsa_loss)
        # Performance Estimation MSE( F - D * Beta + Eps )
        perf  = tf.divide(tf.reduce_mean(tf.square(MappedF - tf.matmul(D, Beta))), tf.constant(np.shape(data_vals)[0],dtype=tf.float32))
        if self.CPU:
            os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
            print("Switch to CPU env ...")

        if sess is None:
                sess = tf.Session()

        sess.run(tf.global_variables_initializer())
        # Tuning Kernel Parameters
        for i in range(self.kernel_iter):
            data_index  = np.random.choice(len(data_vals), size=1)[0]
            data        = data_vals[data_index]
            if np.shape(data)[0] == 1:
                data = data[0]
            design      = design_vals[data_index]
            if np.shape(design)[0] == 1:
                design = design[0]
            rand_index  = np.random.choice(len(data), size=self.batch_size)
            rand_design = design[rand_index]
            rand_data = sess.run(kernelmapping, {F:data[rand_index]})
            sess.run(rsa_train, {D: rand_design, MappedF: rand_data})
            sess.run([kernel_train, kernel_loss, kernelmapping], {D: rand_design, F: data[rand_index]})
            if self.verbose:
                if (i == 0) or ((i + 1)%self.report_step == 0) or (i == self.kernel_iter - 1):
                    print('Tuning Kernel Parameters: \t It {:9d} of {:9d}'.format(i + 1, self.kernel_iter))

        # Estimating Betas
        self.Beta        = list()
        self.Eps         = list()
        self.loss_mat    = list()
        self.AMSE        = list()
        for data_index, data in enumerate(data_vals):
            loss_vec = list()
            for i in range(self.rsa_iter):
                design      = design_vals[data_index]
                rand_index  = np.random.choice(len(data), size=self.batch_size)
                rand_design = design[rand_index]
                rand_data = sess.run(kernelmapping, {F:data[rand_index]})
                sess.run(rsa_train, {D: rand_design, MappedF: rand_data})
                loss_temp = sess.run(rsa_loss, feed_dict={D: rand_design, MappedF: rand_data})
                loss_vec.append(loss_temp)
                if self.verbose:
                    if (i == 0) or ((i + 1)%self.report_step == 0) or (i == self.rsa_iter - 1):
                        print('Estimating RSA: View {:d} of {:d} \t It {:9d} of {:9d} \t Loss: {:20.10f}'.format(data_index + 1, len(data_vals), i + 1, self.rsa_iter, loss_temp))
            MSE = sess.run(perf, {D: design_vals[data_index], MappedF: sess.run(kernelmapping, {F: data_vals[data_index]})})
            self.AMSE.append(MSE)
            if self.verbose:
                print("View {:d} MSE: {:20.10f}".format(data_index + 1, MSE))
            self.loss_mat.append(loss_vec)
            self.Beta.append(sess.run(Beta))
            self.Eps.append(sess.run(Eps))

        self.Weights, self.Biases   = mlp.return_values(sess)
        sess.close()
        return self.Beta, self.Eps, self.Weights, self.Biases, np.mean(self.AMSE), self.loss_mat