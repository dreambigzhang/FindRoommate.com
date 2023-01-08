import torch
import random

def dotProduct(list1, list2):
  return sum([x*y for x,y in zip(list1,list2)])

batch_size = 10
parameter_size = 12
sample_size = 100
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
  newInput = []
  for j in range(parameter_size):
      newInput.append(random.random())
  '''
  newResponse = float(input('Response: '))
  newResponse = torch.tensor([[newResponse]])
  '''
  #print(newResponse)
  newResponse = [random.random()]

  x = torch.cat((x, torch.tensor([newInput])),0)
  y = torch.cat((y, torch.tensor([newResponse])),0)
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


newUserParameters = []
for i in range(100):
    singleUser = []
    for j in range(parameter_size+1):
        singleUser.append(random.random())
    newUserParameters.append(singleUser)

for x in newUserParameters:
  #print(i)
  rating = dotProduct(model.weight.grad[0], x[:-1])
  rating = rating.item() + model.bias.grad.item()
  newUserParameters[i][-1] = rating
  #print('Rating:',rating)
  #print(newUserParameters[i])

newUserParameters = sorted(newUserParameters, key = lambda x: x[-1], reverse = True)

for i in range(sample_size):
  print(newUserParameters[i][0])
  newUserParameters[i] = newUserParameters[i][:parameter_size]
newUserParameters = newUserParameters[:batch_size]

print(len(newUserParameters), len(newUserParameters[0]))