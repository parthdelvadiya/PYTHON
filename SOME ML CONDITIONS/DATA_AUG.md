# Data Augmentation

Data Augmentation is a technique used to artificially increase the size of a dataset by creating modified versions of existing data.

Purpose:

* Increase training data
* Reduce overfitting
* Improve model generalization

---

# Simple Example

Original Image:

```python
Cat Image
```

Augmented Images:

```python
Rotated Cat
Flipped Cat
Zoomed Cat
Brightened Cat
```

Now one image becomes multiple training samples.

---

# Common Data Augmentation Techniques

### Image Data

```python
Rotation
Flipping
Cropping
Zooming
Brightness Adjustment
Noise Addition
```

### Text Data

```python
Synonym Replacement
Word Insertion
Word Deletion
Back Translation
```

### Audio Data

```python
Noise Addition
Pitch Change
Speed Change
Time Shifting
```

---

# Why Use Data Augmentation?

Without Augmentation:

```python
1000 Images
```

With Augmentation:

```python
1000 → 5000+ Images
```

Model learns more variations and performs better on unseen data.

---

# Real-Life Example

Suppose you have:

```python
500 Dog Images
```

Instead of collecting more data:

```python
Flip
Rotate
Zoom
```

to create thousands of new training samples.

---

# Advantages

* Reduces Overfitting
* Improves Accuracy
* Works Well with Small Datasets
* Better Generalization

---

# Final Summary

| Concept | Meaning |
|----------|----------|
| Data Augmentation | Creating modified versions of existing data |
| Goal | Increase dataset size artificially |
| Common Methods | Rotate, Flip, Zoom, Crop |
| Main Benefit | Better model generalization |
| Mostly Used In | Computer Vision, NLP, Audio |

---

# One-Line Definition

```python
Data Augmentation is the process of creating new training samples from existing data by applying transformations to improve model performance and reduce overfitting.
```