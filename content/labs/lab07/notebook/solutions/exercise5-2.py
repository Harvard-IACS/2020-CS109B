batch_size = 1048
epochs = 2 # do 2 for now, 20 when you have time

logdir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
callbacks = [ tf.keras.callbacks.EarlyStopping(
                    # Stop training when `val_loss` is no longer improving
                    monitor='val_loss',
                    # "no longer improving" being further defined as "for at least `patience` epochs
                    patience=10,
                    verbose=5, mode='auto'),
             tf.keras.callbacks.TensorBoard(logdir, histogram_freq=1)
            ]

history = ae_model.fit(X_train_n, X_train, epochs=epochs, batch_size=batch_size, 
                      validation_data=(X_test_n, X_test), callbacks=callbacks)
