import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
import numpy as np
import os
from math import floor, ceil, pi


IMAGE_SIZE = 224
#Image size is defined as what our FC layer accepts.

def get_image_paths():
    folder = r'D:\TestingAugmentation\Broken HeadLamp'
    files = os.listdir(folder)
    files.sort()
    files = ['{}/{}'.format(folder, file) for file in files]
    return files


X_img_paths = get_image_paths()
print(X_img_paths)


def tf_resize_images(X_img_file_paths):
    X_data = []
    tf.reset_default_graph()
    X = tf.placeholder(tf.float32, (None, None, 3))
    tf_img = tf.image.resize_images(X, (IMAGE_SIZE, IMAGE_SIZE),
                                    tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        # Each image is resized individually as different image may be of different size.
        for index, file_path in enumerate(X_img_file_paths):
            img = mpimg.imread(file_path)[:, :, :3]  # Do not read alpha channel.
            resized_img = sess.run(tf_img, feed_dict={X: img})
            X_data.append(resized_img)

    X_data = np.array(X_data, dtype=np.float32)  # Convert to numpy
    return X_data


X_imgs = tf_resize_images(X_img_paths)
print(X_imgs.shape)

'''
def display_all_images(X_imgs, n_cols = 4):
    n_rows = ceil(len(X_imgs) / n_cols)
    display_image = np.zeros([n_rows * IMAGE_SIZE, n_cols * IMAGE_SIZE, 3], dtype = np.float32)
    for i in range(n_rows):
        for j in range(n_cols):
            X_img = X_imgs[i * n_cols + j]
            disp_padded = np.pad(X_img, ((i * IMAGE_SIZE, (n_rows - 1 - i) * IMAGE_SIZE),
                                         (j * IMAGE_SIZE, (n_cols - 1 - j) * IMAGE_SIZE), (0, 0)), 'constant')
            display_image = np.add(display_image, disp_padded)

    plt.figure(figsize = (n_rows * 3, n_cols * 3))
    plt.imshow(display_image)
    plt.axis('off')
    plt.show()
'''

def central_scale_images(X_imgs, scales):
    # Various settings needed for Tensorflow operation
    boxes = np.zeros((len(scales), 4), dtype=np.float32)
    for index, scale in enumerate(scales):
        x1 = y1 = 0.5 - 0.5 * scale  # To scale centrally
        x2 = y2 = 0.5 + 0.5 * scale
        boxes[index] = np.array([y1, x1, y2, x2], dtype=np.float32)
    box_ind = np.zeros((len(scales)), dtype=np.int32)
    crop_size = np.array([IMAGE_SIZE, IMAGE_SIZE], dtype=np.int32)

    X_scale_data = []
    tf.reset_default_graph()
    X = tf.placeholder(tf.float32, shape=(1, IMAGE_SIZE, IMAGE_SIZE, 3))
    # Define Tensorflow operation for all scales but only one base image at a time
    tf_img = tf.image.crop_and_resize(X, boxes, box_ind, crop_size)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for img_data in X_imgs:
            batch_img = np.expand_dims(img_data, axis=0)
            scaled_imgs = sess.run(tf_img, feed_dict={X: batch_img})
            X_scale_data.extend(scaled_imgs)

    X_scale_data = np.array(X_scale_data, dtype=np.float32)
    return X_scale_data


scaled_imgs = central_scale_images(X_imgs, [0.90, 0.75, 0.60])
print(scaled_imgs.shape)


def get_translate_parameters(index):
    if index == 0:  # Translate left 20 percent
        offset = np.array([0.0, 0.2], dtype=np.float32)
        size = np.array([IMAGE_SIZE, ceil(0.8 * IMAGE_SIZE)], dtype=np.int32)
        w_start = 0
        w_end = int(ceil(0.8 * IMAGE_SIZE))
        h_start = 0
        h_end = IMAGE_SIZE
    elif index == 1:  # Translate right 20 percent
        offset = np.array([0.0, -0.2], dtype=np.float32)
        size = np.array([IMAGE_SIZE, ceil(0.8 * IMAGE_SIZE)], dtype=np.int32)
        w_start = int(floor((1 - 0.8) * IMAGE_SIZE))
        w_end = IMAGE_SIZE
        h_start = 0
        h_end = IMAGE_SIZE
    elif index == 2:  # Translate top 20 percent
        offset = np.array([0.2, 0.0], dtype=np.float32)
        size = np.array([ceil(0.8 * IMAGE_SIZE), IMAGE_SIZE], dtype=np.int32)
        w_start = 0
        w_end = IMAGE_SIZE
        h_start = 0
        h_end = int(ceil(0.8 * IMAGE_SIZE))
    else:  # Translate bottom 20 percent
        offset = np.array([-0.2, 0.0], dtype=np.float32)
        size = np.array([ceil(0.8 * IMAGE_SIZE), IMAGE_SIZE], dtype=np.int32)
        w_start = 0
        w_end = IMAGE_SIZE
        h_start = int(floor((1 - 0.8) * IMAGE_SIZE))
        h_end = IMAGE_SIZE

    return offset, size, w_start, w_end, h_start, h_end


def translate_images(X_imgs):
    offsets = np.zeros((len(X_imgs), 2), dtype=np.float32)
    n_translations = 4
    X_translated_arr = []

    tf.reset_default_graph()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(n_translations):
            X_translated = np.zeros((len(X_imgs), IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.float32)
            X_translated.fill(1.0)  # Filling background color
            base_offset, size, w_start, w_end, h_start, h_end = get_translate_parameters(i)
            offsets[:, :] = base_offset
            glimpses = tf.image.extract_glimpse(X_imgs, size, offsets)

            glimpses = sess.run(glimpses)
            X_translated[:, h_start: h_start + size[0], w_start: w_start + size[1], :] = glimpses
            X_translated_arr.extend(X_translated)
    X_translated_arr = np.array(X_translated_arr, dtype=np.float32)
    return X_translated_arr

translated_imgs = translate_images(X_imgs)
gs = gridspec.GridSpec(1, 5)
gs.update(wspace = 0.30, hspace = 2)

fig, ax = plt.subplots(figsize = (16, 16))
plt.subplot(gs[0])
plt.imshow(X_imgs[5])
plt.title('Base Image')
plt.subplot(gs[1])
plt.imshow(translated_imgs[5])
plt.title('Left 20 percent')
plt.subplot(gs[2])
plt.imshow(translated_imgs[11])
plt.title('Right 20 percent')
plt.subplot(gs[3])
plt.imshow(translated_imgs[17])
plt.title('Top 20 percent')
plt.subplot(gs[4])
plt.imshow(translated_imgs[23])
plt.title('Bottom 20 percent')
plt.show()




