#Linear Regression from Scratch
# Step 1: Create a simple dataset
x = [1,2,3,4,5]
y = [2,4,6,8,10]

print("Input (x):", x)
print("Output (y):", y)

# Step 2: Initialize parameters
m = 0
b = 0

# Step 3: Make predictions
predictions = []

for i in x:
    p = m * i + b
    predictions.append(p)


print("Predictions: ",predictions)