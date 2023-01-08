import torch
import random

'''
backend = MLBackend() # to create new backend class object
backend.dataLoad(float[12], float) # give the backend the user response to a profile after every like and dislike
backend.getProfile() return float[12] a list of 12 floats
'''
class MLBackend:
  def __init__(self):
    self.batch_size = 10
    self.parameter_size = 12
    self.sample_size = 100
    # Define the model
    self.model = torch.nn.Linear(self.parameter_size, 1)

    # Define the loss function and optimizer
    self.loss_fn = torch.nn.MSELoss()
    self.optimizer = torch.optim.SGD(self.model.parameters(), lr=0.1)

    self.x = torch.tensor([])
    self.y = torch.tensor([])
    
    self.initTrain()

    self.profileCache = self.initProfileGenerate()
    self.pageNum = 0

    

  def initTrain(self):
    for i in range(self.batch_size):
      newInput, newResponse = self.generateTrainingData()
      self.dataLoad(newInput, newResponse)


  def dotProduct(self, list1, list2):
    return sum([x*y for x,y in zip(list1,list2)])

  def clearCache(self):
    self.x = torch.tensor([])
    self.y = torch.tensor([])

  # Generate some random data
  def dataLoad(self, newInput, newResponse):
    self.x = torch.cat((self.x, torch.tensor([newInput])),0)
    self.y = torch.cat((self.y, torch.tensor([[newResponse]])),0)
    if self.y.size()[0] >= self.batch_size:
      self.updateGD()
  
  def updateGD(self):
    print('Gradient Descent Updated')
    # Training loop
    for i in range(self.batch_size):
      # Forward pass
      y_pred = self.model(self.x)
      self.loss = self.loss_fn(y_pred, self.y)

      # Print gradient and bias
      #print('Iteration:', i)
      #print('Gradient:', self.model.weight.grad)
      #print('Bias:', self.model.bias.grad)

      # Backward pass
      self.optimizer.zero_grad()
      self.loss.backward()

      # Update weights
      self.optimizer.step()
    self.clearCache()

  def generateTrainingData(self):
    i = 0
    while i < self.batch_size:
      newInput = []
      for j in range(self.parameter_size):
          newInput.append(random.random())
      '''
      newResponse = float(input('Response: '))
      newResponse = torch.tensor([[newResponse]])
      '''
      #print(newResponse)
      newResponse = random.random()
      i+=1
    return newInput, newResponse

  
  def initProfileGenerate(self):
    newUserParameters = []
    for i in range(self.batch_size):
        singleUser = []
        for j in range(self.parameter_size):
            singleUser.append(random.random())
        newUserParameters.append(singleUser)
    return newUserParameters


  def recommendProfile(self):
    print('New Profiles Recommended')
    newUserParameters = []
    for i in range(self.sample_size // self.batch_size):
      newUserParameters += self.initProfileGenerate()
    for i in range(self.sample_size):
      rating = self.dotProduct(self.model.weight.grad[0], newUserParameters[i][:-1])
      rating = rating.item() + self.model.bias.grad.item()
      newUserParameters[i][-1] = rating
      #print('Rating:',rating)
      #print(newUserParameters[i])

    newUserParameters = sorted(newUserParameters, key = lambda x: x[-1], reverse = True)

    for i in range(self.sample_size):
      #print(newUserParameters[i][0])
      newUserParameters[i] = newUserParameters[i][:self.parameter_size]
    newUserParameters = newUserParameters[:self.batch_size]
    return newUserParameters

  def getProfile(self):
    if self.pageNum >= self.batch_size-1:
      self.profileCache = self.recommendProfile()
      self.pageNum = 0
    else:
      self.pageNum+=1
    return self.profileCache[self.pageNum]

if __name__ == '__main__':
  backEnd = MLBackend()
  for i in range(32):
    backEnd.dataLoad(backEnd.getProfile(), 1.0)
