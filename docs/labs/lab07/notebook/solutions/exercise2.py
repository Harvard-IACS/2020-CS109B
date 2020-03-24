# Let's find the first 2 PCA components
num_components = 2
pca = PCA(n_components=num_components).fit(X_train_flat)

# take a look at them
print(f'Shape of the 2 component vector (First and Second): {pca.components_.shape}')
print(f'Shape of first PC: {pca.components_[0].shape}')
print(f'Shape of second PC: {pca.components_[0].shape}')

# reshape so they resemble images and we can print them
eigenclothes = pca.components_.reshape((num_components, h, w))
print(f'Shape of reshaped eigenclothes: {eigenclothes.shape}, shape of the first article of eigenclothing: {eigenclothes[0].shape}')

# show the reshaped principal components (eigenclothes)
f, ax = plt.subplots(1,2)
ax[0].imshow(eigenclothes[0], cmap='gray');
ax[0].set_xlabel('First Principal Component');
ax[1].imshow(eigenclothes[1], cmap='gray');
ax[1].set_xlabel('Second Principal Component');
