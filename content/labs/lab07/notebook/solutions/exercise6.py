# plot the original noisy images
n = np.random.randint(0,len(X_test)-5)
f, ax = plt.subplots(1,5,figsize=(20,10))
for i,a in enumerate(range(n,n+5)):
    ax[i].imshow(X_test_n[a, :, :, 0].reshape(28, 28), cmap='gray')
plt.show()

# print the predictions
preds = encoder.predict(X_test_n[n:n+5])
print(f'Shape of the predictions matrix: {preds.shape}')

latent_channels = 4

f, ax = plt.subplots(latent_channels,5, figsize=(20,10))
ax = ax.ravel()
for j in range(latent_channels):
    for i,a in enumerate(range(n,n+5)):
        ax[j*5 + i].imshow(preds[i, :, :, j], cmap='gray')
plt.show()
