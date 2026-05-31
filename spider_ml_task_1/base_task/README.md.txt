# Base Task – Fashion-MNIST Classification

## Problem Statement

Implement the given neural network architecture using PyTorch and train it on the Fashion-MNIST dataset.

Requirements:

* Proper training pipeline
* Forward propagation
* Backward propagation
* Validation during training
* Accuracy and loss plotting
* Save model weights using Pickle
* Generate submission.csv

---

## Dataset

Fashion-MNIST consists of:

* 60,000 training images
* 10,000 test images
* Image size: 28 × 28 grayscale
* 10 clothing categories

---

## Model Architecture

Input Shape:

```text
28 × 28
```

Pipeline:

```text
Input
→ Flatten
→ Dense(784 → 16)

Branch 1:
16 → 8 → 8
Skip Connection

Branch 2:
16 → 12 → 8

Concatenate
→ Dense(16 → 10)
```

---

## Training Details

Loss Function:

```python
CrossEntropyLoss
```

Optimizer:

```python
Adam
```

Learning Rate:

```python
0.001
```

Batch Size:

```python
64
```

Epochs:

```python
20
```

---

## Outputs

### Training Metrics

The notebook prints:

* Training Loss
* Validation Loss
* Training Accuracy
* Validation Accuracy

for each epoch.

---

### Visualizations

Generated plots:

* Training vs Validation Loss
* Training vs Validation Accuracy

---

### Saved Model

Location:

```text
saved_models/model_weights.pkl
```

---

### Predictions

Generated file:

```text
submission.csv
```

Format:

```text
ImageId,Label
1,9
2,0
3,4
...
```

---

## How to Run

1. Open the notebook in Google Colab.
2. Upload Fashion-MNIST dataset files.
3. Run all cells sequentially.
4. Model weights and predictions will be generated automatically.

---

## Learning Outcomes

Through this task I gained practical experience with:

* Tensor operations
* Neural network implementation
* Forward propagation
* Backpropagation
* Model evaluation
* PyTorch training workflows
* Dataset preprocessing
* Model serialization
