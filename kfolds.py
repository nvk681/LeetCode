import os
import numpy as np
import cv2
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

# Define the path to the folder containing the image dataset
data_dir = 'path/to/dataset/folder'

# Define the number of classes
num_classes = 10

# Define the image size
img_size = (224, 224)

# Define the batch size
batch_size = 32

# Define the number of epochs
num_epochs = 10

# Define the number of folds for k-fold cross-validation
num_folds = 5

# Create a custom PyTorch dataset class to load the image data
class ImageDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        img = self.data[index]
        img = cv2.resize(img, img_size)
        img = np.transpose(img, (2, 0, 1))
        label = self.labels[index]
        return img, label

# Create empty lists to store the image data and labels
data = []
labels = []

# Loop over each class folder in the dataset folder
for class_folder in os.listdir(data_dir):
    class_folder_path = os.path.join(data_dir, class_folder)
    if os.path.isdir(class_folder_path):
        # Loop over each image file in the class folder
        for file_name in os.listdir(class_folder_path):
            if file_name.endswith('.jpg'):
                # Load the image and add it to the data list
                img = cv2.imread(os.path.join(class_folder_path, file_name))
                data.append(img)
                labels.append(int(class_folder))

# Convert the image data and labels to NumPy arrays
data = np.array(data)
labels = np.array(labels)

# Define the convolutional neural network model
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(64, 128, 3, padding=1)
        self.pool3 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * (img_size[0] // 8) * (img_size[1] // 8), 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = nn.functional.relu(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = nn.functional.relu(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = nn.functional.relu(x)
        x = self.pool3(x)
        x = x.view(-1, 128 * (img_size[0] // 8) * (img_size[1] // 8))
        x = self.fc1(x)
        x = nn
