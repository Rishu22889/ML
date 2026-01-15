# Machine Learning Models from Scratch

This repository contains implementations of core Machine Learning and basic Deep Learning algorithms **from scratch using Python and NumPy**, without relying on high-level ML libraries.

The goal of this project is to deeply understand the mathematical foundations of ML algorithms and how they are implemented internally.

---

## Algorithms Implemented

### 1. Linear Regression
- Implemented using:
  - Normal Equation
  - Gradient Descent
- Includes:
  - Cost function (MSE)
  - Feature normalization
  - Vectorized NumPy implementation
- Visualized loss convergence using plots

📁 Folder: `ML_from_Scratch/LinearRegression/`

---

### 2. Logistic Regression
- Binary classification using sigmoid activation
- Implemented:
  - Cost function (Log Loss)
  - Gradient Descent optimization
  - Decision boundary visualization
- No use of `sklearn` for training

📁 Folder: `ML_from_Scratch/LogisticRegression/`

---

### 3. K-Means Clustering
- Unsupervised clustering from scratch
- Implemented:
  - Random centroid initialization
  - Distance computation
  - Cluster assignment and centroid updates
- Visualized clusters using matplotlib

📁 Folder: `ML_from_Scratch/KMeansClustering/`

---

### 4. Decision Tree (from Scratch)
- Implemented basic decision tree logic
- Used entropy / information gain for splitting
- Recursive tree construction

📁 Folder: `ML_from_Scratch/DecisionTree/`

---

### 5. Anomaly Detection
- Statistical anomaly detection approach
- Identified outliers based on probability distribution
- Applied threshold-based anomaly classification

📁 Folder: `ML_from_Scratch/AnomalyDetection/`

---

## Key Learnings
- How gradient descent actually updates parameters
- Importance of vectorization for performance
- Effect of learning rate on convergence
- How loss functions guide optimization
- How clustering and tree-based models work internally

---

## Tech Stack
- Python
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

---

## Note
These implementations are done **for learning purposes**, focusing on clarity and correctness rather than production optimization.
