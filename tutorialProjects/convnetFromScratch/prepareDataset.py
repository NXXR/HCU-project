import os
import shutil

original_dataset_dir = "./dogs-vs-cats-dataset"

base_dir = "./dataset"
os.mkdir(base_dir)

train_dir = os.path.join(base_dir, "train")
os.mkdir(train_dir)
train_cats_dir = os.path.join(train_dir, "cats")
os.mkdir(train_cats_dir)
train_dogs_dir = os.path.join(train_dir, "dogs")
os.mkdir(train_dogs_dir)

validation_dir = os.path.join(base_dir, "validation")
os.mkdir(validation_dir)
validation_cats_dir = os.path.join(validation_dir, "cats")
os.mkdir(validation_cats_dir)
validation_dogs_dir = os.path.join(validation_dir, "dogs")
os.mkdir(validation_dogs_dir)

test_dir = os.path.join(base_dir, "test")
os.mkdir(test_dir)


