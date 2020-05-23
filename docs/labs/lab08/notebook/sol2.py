# create the CNN
model = Sequential()
model.add(Embedding(vocabulary_size, embedding_dim, input_length=max_review_length))
model.add(Conv1D(filters=200, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(250, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

# train the CNN
model.fit(X_train, y_train, epochs=2, batch_size=128)

# evalute the CNN
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
