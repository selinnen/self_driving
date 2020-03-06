import numpy as np

def norm(x):
  return x / np.sum(x)

convs = [
  np.array([
    [-1.0,  2.0, -1.0],
    [-1.0,  2.0, -1.0],
    [-1.0,  2.0, -1.0]
  ]),
  np.array([
    [-1.0, -1.0, -1.0],
    [ 2.0,  2.0,  2.0],
    [-1.0, -1.0, -1.0]
  ]),
  np.array([
    [-1.0, -1.0, -1.0],
    [-1.0,  8.0, -1.0],
    [-1.0, -1.0, -1.0]
  ]),
  np.array([
    [ 0.0, -1.0,  0.0],
    [-1.0,  4.0, -1.0],
    [ 0.0, -1.0,  0.0]
  ]),
  norm(np.array([
    [ 1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0],
    [ 1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0],
    [ 1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0],
    [ 1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0],
    [ 1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0],
    [ 1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0],
    [ 1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0]
  ])),
  norm(np.array([
    [  0.0,   0.0,   0.0,   5.0,   0.0,   0.0,  0.0],
    [  0.0,   5.0,  18.0,  32.0,  18.0,   5.0,  0.0],
    [  0.0,  18.0,  64.0, 100.0,  64.0,  18.0,  0.0],
    [  5.0,  32.0, 100.0, 100.0, 100.0,  32.0,  5.0],
    [  0.0,  18.0,  64.0, 100.0,  64.0,  18.0,  0.0],
    [  0.0,   5.0,  18.0,  32.0,  18.0,   5.0,  0.0],
    [  0.0,   0.0,   0.0,   5.0,   0.0,   0.0,  0.0]
  ]))
]

import scipy.signal

def conv2d(A, B):
    return scipy.signal.convolve2d(A, B)

grayscale_coeffs = np.array([0.299, 0.587, 0.114])

def to_grayscale(img):
    scaled_img = img * grayscale_coeffs
    return np.sum(scaled_img, axis=2)[:, :, np.newaxis]
def gs_rgb_repr(img):
    return np.stack([img[:, :, 0], img[:, :, 0], img[:, :, 0]], axis=2)