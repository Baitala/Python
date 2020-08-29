import numpy as np, tensorflow as tf
n_samples, batch_size, num_steps = 1000, 100, 20000
X_data = np.random.uniform(l, 10, (n_samples, 1))
y_data = 2*X_data+1+np.random.normal(0, 2, (n_samples, 1))

X = tf.placeholder(tf.float32, shape=(batch_size, 1))
y = tf.placeholder(tf.float32, shape=(batch_size, 1))


with tf.variable_scope('linear-regression'):
    k = tf.Variable(tf.random_normal((l, 1)), name = 'slope')
    b = tf.Variable(tf.zeros((l, )), name = 'bias')

y_pred = tf.matmul(X, k)+b
loss = tf.reduce_sum((y-y_pred)**2)
optimizer = tf.train.GradientDescentOptimizer().minimize(loss)

display_step = 100
with tf.Session() as sess:
    sess.run(tf.initialize__global_variables())
    for i in range(num_steps):
        indices = np.random.choice(n_samples, batch_size)
        X_batch, y_batch = X_data[indices], y_data[indices]
        _, loss_val, k_val, b_val = sess.run([optimizer, loss, k, b],
            feed_dict={X:X_batch, у:y_batch})
        if(i+1)%display_step == 0:
            print('Эпоха%d:%.8f, k = %.4f, b = %.4f'%
                (i+1, loss_val, k__val, b_val))
