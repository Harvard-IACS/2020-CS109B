loss = keras.losses.mse
optimizer = Adam() #RMSprop(learning_rate=0.001)
metrics = ['accuracy'] 

ae_model.compile(optimizer=optimizer, loss=loss, metrics=metrics) 
