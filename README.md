

# Linear Regression From Scratch

## 📌 Project Overview
This project implements Linear Regression from scratch using Python, without relying on machine learning libraries like scikit-learn. The goal was to deeply understand how model training actually works under the hood.

The model is trained using Gradient Descent to learn the optimal values of slope (m) and bias (b) that minimize prediction error.

---

## 🧠 Concepts Implemented

- Linear Regression (y = mx + b)
- Mean Squared Error (MSE) Loss Function
- Gradient Descent Optimization
- Parameter Updates using Derivatives
- Effect of Learning Rate and Epochs

---

## ⚙️ How It Works

1. Initialize parameters (m and b).
2. Perform a forward pass to compute predictions.
3. Calculate the Mean Squared Error (MSE).
4. Compute gradients with respect to m and b.
5. Update parameters using Gradient Descent.
6. Repeat for multiple epochs until convergence.

---

## 📊 Observations

- Initial loss was high when parameters were poorly initialized.
- Increasing the number of epochs improved convergence.
- Higher learning rates caused unstable training or oscillation.
- With sufficient epochs and a proper learning rate, the model converged to:
  - m ≈ 2
  - b ≈ 0
- Final loss approached zero.

---

## 🚀 Key Learnings

Gradient Descent is an iterative optimization algorithm used to minimize a loss function by updating parameters in the opposite direction of the gradient. It is essential in machine learning because most models do not have a direct analytical solution, especially in neural networks with many parameters. Controlled, step-by-step updates allow the model to gradually learn the optimal parameters.

---

## 📂 How to Run

```bash
python linear_regression.py

