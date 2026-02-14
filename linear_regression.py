#Linear Regression from Scratch
# Step 1: Create a simple dataset
x = [1,2,3,4,5]
y = [2,4,6,8,10]

print("Input (x):", x)
print("Output (y):", y)

# Step 2: Initialize parameters
m = 0
b = 0
learning_rate = 0.01
epochs = 100
n = len(x)

for epoch in range(epochs):

    # Step 1: Make predictions
    predictions = []

    for i in x:
        p = m * i + b
        predictions.append(p)




    # Step 2: Calculate Mean Squared Error

    total_error = 0

    for i in range(len(y)):
        error = (y[i] - predictions[i]) ** 2
        total_error += error

    mse = total_error/len(y)




    # Step 3: Calculate gradient for m

    
    gradient_m = 0

    for i in range(n):
        gradient_m +=x[i] * ( y[i] - predictions[i])

    gradient_m = (-2 / n) * gradient_m

    # Step 3b: Compute Gradient for b

    gradient_b = 0
    for i in range(n):
        gradient_b += (y[i] - predictions[i])

    gradient_b = (-2 / n) * gradient_b


    # Step 4: Update m and b using Gradient Descent

    b = b - learning_rate * gradient_b


    m = m - learning_rate * gradient_m
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {mse}")

print("Final m:", m)

