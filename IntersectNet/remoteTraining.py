from keras import layers, models, losses, optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import multi_gpu_model
import os
import datetime
import pickle

dataset_width = 960
dataset_height = 540

model = models.Sequential()

model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(150, 150, 3)))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(128, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(128, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())
model.add(layers.Dropout(1-0.5))
model.add(layers.Dense(512, activation="relu"))
model.add(layers.Dense(1, activation="sigmoid"))

model.summary()

model = multi_gpu_model(model, gpus=2)
model.compile(
    loss=losses.binary_crossentropy,
    optimizer=optimizers.RMSprop(lr=0.0001),
    metrics=["acc"]
)

datagen = ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_directory(
    os.path.join(os.getcwd(), "dataset/train"),
    target_size=(dataset_width, dataset_height),
    batch_size=32,
    class_mode="binary"
)
validation_generator = datagen.flow_from_directory(
    os.path.join(os.getcwd(), "dataset/validation"),
    target_size=(dataset_width, dataset_height),
    batch_size=32,
    class_mode="binary"
)

history = model.fit_generator(
    train_generator,
    steps_per_epoch=100,
    epochs=1000,
    validation_data=validation_generator,
    validation_steps=50
)
history = history.history
filename = "intersectNet_{}".format(datetime.datetime.utcnow().strftime("%m%d-%H%M"))
model.save(os.path.join(os.getcwd(), "models/{}.h5".format(filename)))
print("saved model: {}.h5".format(filename))
with open("models/{}.hist".format(filename), "wb+") as file:
    pickle.dump(history, file)
print("saved history: {}.hist".format(filename))
