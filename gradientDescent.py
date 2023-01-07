import torch

# Define the model
model = torch.nn.Linear(12, 1)

# Define the loss function and optimizer
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# Generate some random data
x = torch.randn(100, 12)
y = torch.randn(100, 1)

# Training loop
for i in range(10):
  # Forward pass
  y_pred = model(x)
  loss = loss_fn(y_pred, y)

  # Print gradient and bias
  print('Iteration:', i)
  print('Gradient:', model.weight.grad)
  print('Bias:', model.bias.grad)

  # Backward pass
  optimizer.zero_grad()
  loss.backward()

  # Update weights
  optimizer.step()

