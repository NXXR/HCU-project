from keras import layers, models, losses, optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import multi_gpu_model
import os
import datetime
import pickle

dataset_width = 150
dataset_height = 84

epochs = 60

model = models.Sequential()

model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(dataset_width, dataset_height, 3)))
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

pano_model = models.clone_model(model)
norm_model = models.clone_model(model)

pano_model = multi_gpu_model(pano_model, gpus=2)
norm_model = multi_gpu_model(norm_model, gpus=2)
pano_model.compile(
    loss=losses.binary_crossentropy,
    optimizer=optimizers.RMSprop(lr=0.0001),
    metrics=["acc"]
)
norm_model.compile(
    loss=losses.binary_crossentropy,
    optimizer=optimizers.RMSprop(lr=0.0001),
    metrics=["acc"]
)

datagen = ImageDataGenerator(rescale=1./255)

norm_train_generator = datagen.flow_from_directory(
    os.path.join(os.getcwd(), "dataset/normal/train"),
    target_size=(dataset_height, dataset_width),
    batch_size=32,
    class_mode="binary"
)
pano_train_generator = datagen.flow_from_directory(
    os.path.join(os.getcwd(), "dataset/pano/train"),
    target_size=(dataset_height, dataset_width),
    batch_size=32,
    class_mode="binary"
)
norm_validation_generator = datagen.flow_from_directory(
    os.path.join(os.getcwd(), "dataset/normal/validation"),
    target_size=(dataset_height, dataset_width),
    batch_size=32,
    class_mode="binary"
)
pano_validation_generator = datagen.flow_from_directory(
    os.path.join(os.getcwd(), "dataset/pano/validation"),
    target_size=(dataset_height, dataset_width),
    batch_size=32,
    class_mode="binary"
)

time_start = datetime.datetime.now()
pano_history = pano_model.fit_generator(
    pano_train_generator,
    steps_per_epoch=100,
    epochs=epochs,
    validation_data=pano_validation_generator,
    validation_steps=50
)
pano_traintime = datetime.datetime.now() - time_start

time_start = datetime.datetime.now()
norm_history = norm_model.fit_generator(
    norm_train_generator,
    steps_per_epoch=100,
    epochs=epochs,
    validation_data=norm_validation_generator,
    validation_steps=50
)
norm_traintime = datetime.datetime.now() - time_start

print("Training Time: {}(normal) {}(panorama)".format(norm_traintime, pano_traintime))

norm_history = norm_history.history
norm_history["traintime"] = norm_traintime
pano_history = pano_history.history
pano_history["traintime"] = pano_traintime

filename = "intersectNet_{}".format(datetime.datetime.utcnow().strftime("%m%d-%H%M"))
os.makedirs("models/{}".format(filename))
norm_model.save(os.path.join(os.getcwd(), "models/{}/norm.h5".format(filename)))
pano_model.save(os.path.join(os.getcwd(), "models/{}/pano.h5".format(filename)))
with open("models/{}/norm.hist".format(filename), "wb+") as file:
    pickle.dump(norm_history, file)
with open("models/{}/pano.hist".format(filename), "wb+") as file:
    pickle.dump(pano_history, file)
print("saved {} files".format(filename))
