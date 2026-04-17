# K-Means Clustering – Complete Implementation and Interview Guide

---

## 1. What is K-Means Clustering?

K-Means Clustering is an **unsupervised learning algorithm** used to **group similar data points into clusters**.

Unlike supervised learning, it does **not use labeled output data**.

Its main goal is to divide the dataset into **K clusters**, where each data point belongs to the cluster with the nearest centroid.

---

## 2. Real-World Examples

- Customer segmentation
- Student performance grouping
- Product recommendation grouping
- News/article clustering
- Image compression
- Fraud pattern detection

---

## 3. Why is it called K-Means?

- **K** → Number of clusters
- **Means** → Mean point (centroid) of each cluster

Each cluster is represented by its **centroid (center point)**.

---

## 4. How K-Means Works (VERY IMPORTANT)

K-Means follows these steps:

### Step 1: Choose K
Decide how many clusters you want.

Example:

K = 3

This means data will be divided into 3 groups.

---

### Step 2: Initialize Centroids
Randomly select K points as initial centroids.

---

### Step 3: Assign Points to Nearest Centroid
For each data point, calculate distance from each centroid.

Usually **Euclidean Distance** is used.

Assign the point to the nearest centroid.

---

### Step 4: Update Centroids
Find the mean of all points in each cluster.

That mean becomes the new centroid.

---

### Step 5: Repeat
Repeat Step 3 and Step 4 until centroids stop changing.

This is called **convergence**.

---

## 5. Important Formula

### Euclidean Distance


::contentReference[oaicite:0]{index=0}


This formula is used to calculate distance between points and centroids.

Smaller distance = more similar point.

---

## 6. Important Terms

| Term | Meaning |
|-------|---------|
| K | Number of clusters |
| Centroid | Center point of cluster |
| Inertia | Total within-cluster distance |
| Iteration | Repeated updating process |

---

## 7. Complete Implementation (Model Code)

```python
# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


# ==============================
# 2. Load Dataset
# ==============================
data = load_iris()

df = pd.DataFrame(data.data, columns=data.feature_names)

print("Dataset Preview:\n", df.head())


# ==============================
# 3. Select Features
# ==============================
X = df.iloc[:, :2]


# ==============================
# 4. Train K-Means Model
# ==============================
model = KMeans(n_clusters=3, random_state=42)

model.fit(X)


# ==============================
# 5. Cluster Labels
# ==============================
df['cluster'] = model.labels_

print("\nCluster Labels:")
print(df.head())


# ==============================
# 6. Centroids
# ==============================
print("\nCentroids:")
print(model.cluster_centers_)


# ==============================
# 7. Visualization
# ==============================
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=df['cluster'])

plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    marker='X',
    s=200
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.show()
```

---

## 8. Output Explanation

### model.labels_
Gives cluster number for each data point.

Example:

```python
[0, 1, 1, 2, 0]
```

This means each point belongs to one of the clusters.

---

### model.cluster_centers_
Returns centroids of all clusters.

Example:

```python
[[5.2, 3.1],
 [6.5, 2.9],
 [4.8, 3.8]]
```

---

## 9. How to Choose Best K? (VERY IMPORTANT)

Use **Elbow Method**

```python
inertia_values = []

for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertia_values.append(model.inertia_)

plt.plot(range(1, 11), inertia_values)
plt.xlabel("K")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()
```

---

## 10. What is Elbow Method?

Plot:

- X-axis → Number of clusters
- Y-axis → Inertia

Choose the point where graph bends like an elbow.

That is the best K.

---

## 11. What is Inertia?

Inertia = Sum of squared distances of all points from their nearest centroid.

Lower inertia means better clustering.

But too many clusters can overfit.

---

## 12. Advantages

- Easy to understand
- Fast
- Works well on grouped data
- Very common in interviews

---

## 13. Disadvantages

- Need to choose K manually
- Sensitive to outliers
- Different random initialization may give different clusters
- Works best for spherical clusters

---

## 14. Important Interview Questions

### 1. What is K-Means?

K-Means is an unsupervised learning algorithm used to group similar data points into K clusters.

---

### 2. Why is it unsupervised?

Because it does not use labeled target values.

Only input data is given.

---

### 3. What is centroid?

Centroid is the mean point of all points in a cluster.

---

### 4. How does model learn?

By minimizing distance between points and their nearest centroid.

---

### 5. What is inertia?

Inertia is the sum of squared distances of points from centroids.

---

### 6. How to choose K?

Using Elbow Method.

---

### 7. What distance metric is used?

Mostly Euclidean Distance.

---

### 8. Difference between KNN and K-Means?

- KNN → Supervised learning
- K-Means → Unsupervised learning

Very important interview question.

---

## 15. Final Interview Summary

K-Means is an unsupervised learning algorithm used for clustering similar data points.

It works by:

1. Choosing K
2. Initializing centroids
3. Assigning nearest points
4. Updating centroids
5. Repeating until convergence

Best K is found using Elbow Method.

Important terms:

- Centroid
- Inertia
- Euclidean Distance
- Elbow Method