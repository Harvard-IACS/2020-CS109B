# decoding architecture
decoded_layer1 = Conv2D(4, (3, 3), activation='relu', padding='same')(latent_view)
decoded_layer1 = UpSampling2D((2, 2))(decoded_layer1)
decoded_layer2 = Conv2D(32, (3, 3), activation='relu', padding='same')(decoded_layer1)
decoded_layer2 = UpSampling2D((2, 2))(decoded_layer2)
decoded_layer3 = Conv2D(64, (3, 3), activation='relu')(decoded_layer2)
decoded_layer3 = UpSampling2D((2, 2))(decoded_layer3)
# Note that the loss will be computed after every batch between the predicted output pixel and 
# the ground truth pixel using mean squared error pixel by pixel:
output_layer   = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(decoded_layer3)
