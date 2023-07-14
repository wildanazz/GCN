import logging
import tempfile
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot():
    logging.info('Plotting...')

    # Return a path to temp folder
    tempFilePath = tempfile.gettempdir()

    train_losses = np.load(f'{tempFilePath}/train_losses.npy')
    train_accuracies = np.load(f'{tempFilePath}/train_accuracies.npy')
    validation_losses = np.load(f'{tempFilePath}/validation_losses.npy')
    validation_accuracies = np.load(
        f'{tempFilePath}/validation_accuracies.npy')
    x_embedded = np.load(f'{tempFilePath}/x_embedded.npy')

    plt.figure(figsize=(10, 5))
    plt.title('Training and Validation Loss')
    plt.plot(train_losses, label='Train')
    plt.plot(validation_losses, label='Validation')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{tempFilePath}/loss.png')

    plt.figure(figsize=(10, 5))
    plt.title('Training and Validation Accuracy')
    plt.plot(train_accuracies, label='Train')
    plt.plot(validation_accuracies, label='Validation')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig(f'{tempFilePath}/accuracy.png')

    data = np.load(f'{tempFilePath}/data.npz')
    df = pd.DataFrame(data['target'])

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(x_embedded[:, 0],
               x_embedded[:, 1],
               c=df[0].astype('category').cat.codes)
    ax.set(aspect="equal",
           xlabel="$X_1$",
           ylabel="$X_2$",
           title="Visualization of GCN embeddings")
    plt.savefig(f'{tempFilePath}/embeddings.png')
