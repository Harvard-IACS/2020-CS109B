n_samples, h, w = X_train.shape
print(f'We have {n_samples} data sample images, each with height: {h} and width: {w}')
print(f'Data dimensionality: {h*w}')
print(f'X_train shape: {X_train.shape}, X_test shape: {X_test.shape}')
print(f'y_train shape: {y_train.shape}, and y_test shape: {y_test.shape}')

# Flatten images for PCA
X_train_flat = X_train.reshape(X_train.shape[0], -1)
X_test_flat = X_test.reshape(X_test.shape[0], -1)
print(f'X_train flattened shape: {X_train_flat.shape}, X_test flattened shape: {X_test_flat.shape}')
