from __future__ import absolute_import, division, print_function

import os
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow.contrib.eager as tfe
from keras.callbacks import TensorBoard
import keras

# tf.enable_eager_execution()

# print("TensorFlow version: {}".format(tf.VERSION))
# print("Eager execution: {}".format(tf.executing_eagerly()))


train_dataset_url = "http://download.tensorflow.org/data/iris_training.csv"
train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url),
                                           origin=train_dataset_url)

print(type(train_dataset_fp))
print("Local copy of the dataset file:{}".format(train_dataset_fp))


def load_data(file):
    tmp = np.loadtxt(file, dtype=np.str, delimiter=',')
    features = tmp[1:, 0:-1].astype(np.float)
    label = tmp[1:, -1].astype(np.int)
    return features, label


model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu", input_dim=4),  # input shape required
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(3)
])

model.summary()

train_dataset = load_data(train_dataset_fp)

model.compile(loss='sparse_categorical_crossentropy', optimizer='RMSprop', metrics=['accuracy'])
model.fit(train_dataset[0], train_dataset[1], batch_size=32, epochs=201,
          callbacks=[TensorBoard(log_dir='tensorboard/iris', histogram_freq=0, batch_size=32, write_graph=True,
                                 write_grads=False,
                                 write_images=False, embeddings_freq=0, embeddings_layer_names=None,
                                 embeddings_metadata=None, embeddings_data=None)])

