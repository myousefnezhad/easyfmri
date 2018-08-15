# Gradient Based Representational Similarity Analysis
# Created by Muhammad Yousefnezhad
# iBRAIN, College of Computer Science and Technology
# Nanjing University of Aeronautics and Astronautics
# Example
# rsa = GradientRSA()
# beta, eps, loss = rsa.fit(data, design)

class GradientRSA:
    def __init__(self, regression_type = "regularizedreg", loss_type="norm", loss_norm='euclidean', learning_rate = 0.001, n_iter = 1000, batch_size = 50, report_step = 300, ridge_param = 0.1, elstnet_lamda1 = 0.1, elstnet_lamda2 = 0.1, lasso_param = 0.9, lasso_penalty = 99.0, random_seed = 13, verbose=True, CPU=False):
        self.regression_type    = str.lower(regression_type)  # 'linregl1', 'linregl2', 'ridgereg', 'lasso', 'elasticnet', 'regularizedreg'
        self.loss_type          = str(loss_type) # 'norm', 'mse'
        self.loss_norm          = loss_norm # 'euclidean', 2, np.inf
        self.learning_rate      = learning_rate
        self.n_iter             = n_iter
        self.report_step        = report_step
        self.ridge_param        = ridge_param
        self.elstnet_lamda1     = elstnet_lamda1
        self.elstnet_lamda2     = elstnet_lamda2
        self.lasso_param        = lasso_param
        self.lasso_penalty      = lasso_penalty
        self.random_seed        = random_seed
        self.batch_size         = batch_size
        self.verbose            = verbose
        self.loss_vec           = None
        self.Beta               = None
        self.Eps                = None
        self.CPU                = CPU


    def fit(self, data_vals, design_vals, sess=None):
        import numpy as np
        import tensorflow as tf
        from tensorflow.python.framework import ops
        import os

        if self.verbose:
            print("Type: %s with loss %s" % (self.regression_type, self.loss_type if self.loss_type == "mse" else self.loss_type + "_" + str(self.loss_norm)))
        # Initializing parameters
        np.random.seed(self.random_seed)
        tf.set_random_seed(self.random_seed)
        ops.reset_default_graph()
        if self.CPU:
            os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
            print("Switch to CPU env ...")

        if sess is None:
            sess = tf.Session()
        # Placeholder
        D = tf.placeholder(shape=[None, np.shape(design_vals)[1]], dtype=tf.float32)
        F = tf.placeholder(shape=[None, np.shape(data_vals)[1]], dtype=tf.float32)
        # Create variables for linear regression
        Beta = tf.Variable(tf.random_normal(shape=[np.shape(design_vals)[1], np.shape(data_vals)[1]]))
        Eps  = tf.Variable(tf.random_normal(shape=[1, np.shape(data_vals)[1]]))


        # Declare model operations
        model_output = tf.add(tf.matmul(D, Beta), Eps)
        if  self.regression_type == "linregl1":
            if self.loss_type == "norm":
                loss = tf.square(tf.norm(F - model_output, ord=self.loss_norm))
            else:
                loss = tf.reduce_mean(tf.abs(F - model_output))
        elif self.regression_type == "linregl2":
            if self.loss_type == "norm":
                loss = tf.square(tf.norm(F - model_output, ord=self.loss_norm))
            else:
                loss = tf.reduce_mean(tf.square(F - model_output))
        elif self.regression_type == "ridgereg":
            ridge = tf.multiply(tf.constant(self.ridge_param), tf.reduce_mean(tf.square(Beta)))
            if self.loss_type == "norm":
                loss = tf.add(tf.square(tf.norm(F - model_output, ord=self.loss_norm)), ridge)
            else:
                loss = tf.add(tf.reduce_mean(tf.square(F - model_output)), ridge)
        elif self.regression_type == "lasso":
            heavyside_step = tf.truediv(1., tf.add(1., tf.exp(tf.multiply(-50., tf.subtract(tf.reduce_max(Beta) , tf.constant(self.lasso_param))))))
            regularization_param = tf.multiply(heavyside_step, self.lasso_penalty)
            if self.loss_type == "norm":
                loss = tf.add(tf.square(tf.norm(F - model_output, ord=self.loss_norm)), regularization_param)
            else:
                loss = tf.add(tf.reduce_mean(tf.square(F - model_output)), regularization_param)
        elif self.regression_type == "elasticnet":
            e1_term = tf.multiply(tf.constant(self.elstnet_lamda1), tf.reduce_mean(tf.abs(Beta)))
            e2_term = tf.multiply(tf.constant(self.elstnet_lamda2), tf.reduce_mean(tf.square(Beta)))
            if self.loss_type == "norm":
                loss = tf.add(tf.add(tf.square(tf.norm(F - model_output, ord=self.loss_norm)), e1_term), e2_term)
            else:
                loss = tf.add(tf.add(tf.reduce_mean(tf.square(F - model_output)), e1_term), e2_term)
        elif self.regression_type == "regularizedreg":
            if self.loss_type == "norm":
                loss = tf.square(tf.norm(F - model_output, ord=self.loss_norm))
            else:
                loss = tf.add(tf.reduce_mean(tf.square(F - model_output)), tf.pow(tf.norm(Beta, ord=self.loss_norm), 2))

        my_opt = tf.train.GradientDescentOptimizer(self.learning_rate)

        train_step = my_opt.minimize(loss)
        # Performance Estimation mean((F - D * Beta)**2) / n
        perf  = tf.divide(tf.reduce_mean(tf.square(F - tf.matmul(D, Beta))), tf.constant(np.shape(data_vals)[0],dtype=tf.float32))


        sess.run(tf.global_variables_initializer())
        if self.verbose:
            print("Before Mapping, MSE:   {:20.10f}".format(sess.run(perf, {D: design_vals, F: data_vals})))
        # Training loop
        self.loss_vec = list()
        for i in range(self.n_iter):
            rand_index = np.random.choice(len(design_vals), size=self.batch_size)
            rand_design = design_vals[rand_index]
            rand_data = data_vals[rand_index]
            sess.run(train_step, {D: rand_design, F: rand_data})
            temp_loss = sess.run(loss, feed_dict={D: rand_design, F: rand_data})
            self.loss_vec.append(temp_loss)
            if self.verbose:
                if (i == 0) or ((i+1)%self.report_step == 0) or (i == self.n_iter - 1):
                    print('It: {:9d} of {:9d} \t Loss: {:20.10f}'.format(i+1, self.n_iter, temp_loss))
        MSE = sess.run(perf, {D: design_vals, F: data_vals})
        if self.verbose:
            print("After Mapping, MSE:    {:20.10f}".format(MSE))
        self.Beta   = sess.run(Beta)
        self.Eps    = sess.run(Eps)
        sess.close()
        return self.Beta, self.Eps, self.loss_vec, MSE