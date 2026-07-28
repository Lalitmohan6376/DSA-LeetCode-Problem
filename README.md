# 📘 DSA LeetCode Solutions Repository

This repository contains my solutions to various DSA (Data Structures & Algorithms) problems from LeetCode. It is used for consistent practice, improving problem-solving skills, and preparing for coding interviews.

---

## 🧠 About This Repository

Here I regularly upload solved problems from different DSA topics such as arrays, strings, recursion, linked list, stack, queue, trees, graphs, dynamic programming, and more.

Each solution is written with a focus on:

* Clear logic 💡
* Optimized approach ⚡
* Clean and readable code 🧹

---

## 🚀 Purpose

The main goal of this repository is to:

* Strengthen DSA fundamentals 📊
* Improve coding speed and accuracy ⏱️
* Track my daily/regular practice 📈
* Prepare for technical interviews 🎯

---

## 🧩 Topics Covered

* Arrays & Strings
* Sorting & Searching
* Recursion & Backtracking
* Stack & Queue
* Linked List
* Trees & Binary Trees
* Graphs
* Dynamic Programming
* Greedy Algorithms

---

## 🛠️ Language Used

* Python 🐍 (primary language)



  from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

path = "/content/drive/MyDrive/hotel_review_sentiment.csv"
df = pd.read_csv(path)

df["review"] = df["Cleaned_Reviews"].fillna(df["review"])
df["sentiment"] = df["Sentiment"].fillna(df["sentiment"])

df.head(10)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import resample

df["review"] = df["Cleaned_Reviews"].fillna(df["review"])

df["sentiment"] = df["Sentiment"].fillna(df["sentiment"])

df = df[["review", "sentiment"]]

df.dropna(inplace=True)

df.reset_index(drop=True, inplace=True)

df["sentiment"] = (
    df["sentiment"]
    .astype(str)
    .str.strip()
    .str.lower()
)

label_mapping = {
    "positive": "positive",
    "negative": "negative",
    "neutral": "neutral",
    "2": "positive",
    "1": "neutral",
    "0": "negative"
}

df["sentiment"] = df["sentiment"].map(label_mapping)

df = df[df["sentiment"].notna()]

print(df["sentiment"].value_counts())

print("Before :", len(df))

df.drop_duplicates(subset="review", inplace=True)

df.reset_index(drop=True, inplace=True)

print("After :", len(df))

positive = df[df["sentiment"] == "positive"]

negative = df[df["sentiment"] == "negative"]

neutral = df[df["sentiment"] == "neutral"]

print("Positive :", len(positive))
print("Negative :", len(negative))
print("Neutral  :", len(neutral))

positive = resample(
    positive,
    replace=False,
    n_samples=300000,
    random_state=42
)

negative = resample(
    negative,
    replace=True,
    n_samples=250000,
    random_state=42
)

neutral = resample(
    neutral,
    replace=True,
    n_samples=250000,
    random_state=42
)

df = pd.concat([
    positive,
    negative,
    neutral
])

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print(df["sentiment"].value_counts())

print(df.shape)

encoder = LabelEncoder()

df["label"] = encoder.fit_transform(df["sentiment"])

for i, label in enumerate(encoder.classes_):
    print(f"{label} -> {i}")

train_texts, test_texts, train_labels, test_labels = train_test_split(
    df["review"].tolist(),
    df["label"].tolist(),
    test_size=0.20,
    stratify=df["label"],
    random_state=42
)

print("Training Samples :", len(train_texts))

print("Testing Samples :", len(test_texts))

import tensorflow as tf
from transformers import (
    DistilBertTokenizerFast,
    TFDistilBertForSequenceClassification
)

MODEL_NAME = "distilbert-base-uncased"

tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_NAME)

BATCH_SIZE = 32

train_encodings = tokenizer(
    train_texts,
    truncation=True,
    padding=True,
    max_length=96
)
test_encodings = tokenizer(
    test_texts,
    truncation=True,
    padding=True,
    max_length=96
)

train_dataset = tf.data.Dataset.from_tensor_slices(
    (
        dict(train_encodings),
        train_labels
    )
)

test_dataset = tf.data.Dataset.from_tensor_slices(
    (
        dict(test_encodings),
        test_labels
    )
)

train_dataset = train_dataset.shuffle(10000).batch(BATCH_SIZE)

test_dataset = test_dataset.batch(BATCH_SIZE)

model = TFDistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=3
)

optimizer = tf.keras.optimizers.Adam(learning_rate=2e-5)

loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(
    optimizer=optimizer,
    loss=loss,
    metrics=["accuracy"]
)

early_stop = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=2,
    restore_best_weights=True
)

checkpoint = tf.keras.callbacks.ModelCheckpoint(
    "/content/drive/MyDrive/distilbert_best_model.weights.h5",
    monitor="val_accuracy",
    save_best_only=True,
    save_weights_only=True,
    mode="max"
)

reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=1,
    min_lr=1e-7
)

history = model.fit(
    train_dataset,
    validation_data=test_dataset,
    epochs=5,
    callbacks=[
        early_stop,
        checkpoint,
        reduce_lr
    ]
)

test_loss, test_accuracy = model.evaluate(test_dataset)

print(f"Test Loss     : {test_loss:.4f}")
print(f"Test Accuracy : {test_accuracy:.4f}")

import numpy as np

predictions = model.predict(test_dataset)

y_pred = np.argmax(predictions.logits, axis=1)

y_true = np.array(test_labels)

from sklearn.metrics import classification_report

print(classification_report(
    y_true,
    y_pred,
    target_names=encoder.classes_,
    digits=4
))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_true, y_pred)

cm

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=encoder.classes_,
    yticklabels=encoder.classes_
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()
