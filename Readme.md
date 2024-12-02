# Character Recognition Model

A convolutional neural network (CNN) model for character recognition with an impressive accuracy of 99.29%. This model was trained on images of characters ranging from 0 to 9 and A to Z, and it is capable of predicting the character.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Model Architecture](#model-architecture)
- [Dataset](#dataset)
- [Training](#training)
- [Using the Model](#using-the-model)
- [Results](#results)



---

## Overview

This project provides a deep learning model for character recognition using Python and TensorFlow. The model has been trained to recognize digits (0-9) and uppercase English alphabets (A-Z) with high accuracy. This repository also includes a PyQt5-based GUI application that allows users to draw characters, which the model will then predict.

## Installation

1. Clone the repository:
- download model: https://drive.google.com/drive/folders/1MjVkjrx4MKfA0HH2v_oLXgGNsmSo1rKv?usp=drive_link
   ```bash
   git clone https://github.com/Mtgama/English_alphab_detection.git
   cd Character-Recognition-Model
   pip install tensorflow==2.18.0

# Character Recognition Model

This project is a character recognition model trained to classify images of characters ranging from `0` to `9` and `a` to `z` using a VGG16-based convolutional neural network. The model achieved an impressive accuracy of **99.22%** and is implemented using TensorFlow 2.18.0.

## Model Architecture

The model uses a VGG16 architecture, which is well-suited for image classification tasks. This architecture consists of multiple convolutional layers followed by fully connected layers, achieving high accuracy for image recognition.

![VGG16 Architecture](https://production-media.paperswithcode.com/methods/vgg_7mT4DML.png)

## Dataset

The dataset comprises images of characters from `0` to `9` and `a` to `z`. Each class contains **2400 images**, with variations in fonts and styles to ensure robust training. This balanced dataset enables the model to generalize well across different styles.

## Results

The model achieved a **99.22% accuracy** on the test set, showing its reliability in classifying both digits and alphabets.

