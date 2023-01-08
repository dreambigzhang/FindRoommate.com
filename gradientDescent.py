import torch

batch_size = 10
parameter_size = 12
# Define the model
model = torch.nn.Linear(parameter_size, 1)


# Define the loss function and optimizer
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# Generate some random data

x = torch.tensor([])
y = torch.tensor([])

i = 0
while i < batch_size:
  newInput = torch.randn(1, parameter_size)
  #print(newInput)
  '''
  newResponse = float(input('Response: '))
  newResponse = torch.tensor([[newResponse]])
  '''
  #print(newResponse)
  newResponse = torch.randn(1, 1)
  x = torch.cat((x, newInput),0)
  y = torch.cat((y, newResponse),0)
  print('Accummulative input:', x, '\nAccummulative response:', y)
  i+=1


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


newUserParameters = torch.randn(100, 13)
for i, x in enumerate(newUserParameters):
  #print(i)
  rating = torch.dot(model.weight.grad[0], x[:-1])
  rating = rating.item() + model.bias.grad.item()
  newUserParameters[i][-1] = rating
  #print('Rating:',rating)
  #print(newUserParameters[i])

newUserParameters = sorted(newUserParameters, key = lambda x: x[-1], reverse = True)
#newUserParameters.tolist()
for i in range(100):
  print(newUserParameters[i].tolist()[12])
  newUserParameters[i] = newUserParameters[i].tolist()[:12]
newUserParameters = newUserParameters[:10]
item = newUserParameters[0]
print('size:', len(item))
'''
for item in newUserParameters:
  print(item)
  '''
'''
newUserParameters = [x in newUserParameters]
print(newUserParameters)
'''