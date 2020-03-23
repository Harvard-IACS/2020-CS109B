
# encoding architecture
encoded_layer1 = Conv2D(64, (3, 3), activation='relu', padding='same')(input_layer)
encoded_layer1 = MaxPooling2D( (2, 2), padding='same')(encoded_layer1)
encoded_layer2 = Conv2D(32, (3, 3), activation='relu', padding='same')(encoded_layer1)
encoded_layer2 = MaxPooling2D( (2, 2), padding='same')(encoded_layer2)
encoded_layer3 = Conv2D(4, (3, 3), activation='relu', padding='same')(encoded_layer2)
latent_view    = MaxPooling2D( (2, 2), padding='same', name='latent_view')(encoded_layer3)

# call this the "encoder", we will use it later
encoder  = Model(input_layer, latent_view, name='encoder_model')
