import numpy as np
from scipy.signal import lfilter
from imageio import imread
import matplotlib.pyplot as plt
from scipy.signal import convolve

def rot_imag(A, B, Ac, Bc):
    # Read the image
    X = imread('arco_triunfo.jpg').astype(np.double) / 255.0
    dim1, dim2, _ = X.shape
    
    # Split the image into RGB components
    X1 = X[:, :, 0].flatten()
    X2 = X[:, :, 1].flatten()
    X3 = X[:, :, 2].flatten()
    
    # Corrupt the image
    Y1 = lfilter(A, B, X1)
    Y2 = lfilter(A, B, X2)
    Y3 = lfilter(A, B, X3)
    
    Y1 = (Y1 + abs(np.min(Y1))) / np.max((Y1 + abs(np.min(Y1))))
    Y2 = (Y2 + abs(np.min(Y2))) / np.max((Y2 + abs(np.min(Y2))))
    Y3 = (Y3 + abs(np.min(Y3))) / np.max((Y3 + abs(np.min(Y3))))
    
    Y = np.zeros_like(X)
    Y[:, :, 0] = Y1.reshape(dim1, dim2)
    Y[:, :, 1] = Y2.reshape(dim1, dim2)
    Y[:, :, 2] = Y3.reshape(dim1, dim2)
    
    # Recover the image
    Z1 = lfilter(Ac, Bc, Y1)
    Z2 = lfilter(Ac, Bc, Y2)
    Z3 = lfilter(Ac, Bc, Y3)
    
    Z1[:10] = 0
    Z2[:10] = 0
    Z3[:10] = 0
    
    Z1 = (Z1 + abs(np.min(Z1))) / np.max((Z1 + abs(np.min(Z1))))
    Z2 = (Z2 + abs(np.min(Z2))) / np.max((Z2 + abs(np.min(Z2))))
    Z3 = (Z3 + abs(np.min(Z3))) / np.max((Z3 + abs(np.min(Z3))))
    
    Z = np.zeros_like(X)
    Z[:, :, 0] = Z1.reshape(dim1, dim2)
    Z[:, :, 1] = Z2.reshape(dim1, dim2)
    Z[:, :, 2] = Z3.reshape(dim1, dim2)
    
    return X, Y, Z

A = [1, -2.0]
B = convolve([1, -0.95], [1, -0.98])

# Compensator filter (complete these values as needed)
Ac = convolve([1, -0.95], [1, -0.98])  # Example values
Bc = [1, -0.5] # Example values

X, Y, Z = rot_imag(A, B, Ac, Bc)

# Display the images
fig, axes = plt.subplots(3, 1, figsize=(5, 6))
axes[0].imshow(X)
axes[0].set_title('Imagem original')
axes[0].axis('off')

axes[1].imshow(Y)
axes[1].set_title('Imagem corrompida')
axes[1].axis('off')

axes[2].imshow(Z)
axes[2].set_title('Imagem recuperada')
axes[2].axis('off')

plt.tight_layout()

plt.savefig('1d.png')
plt.show()
