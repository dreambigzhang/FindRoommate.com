# This is the code for generating a dataset of people.
import torch
import random

"""
What is your gender
Do you smoke / vape
Do you burn candles or incense
Do you have a pet
How much do you play a musical instrument
How much do you clean
How much do you cook
How much do  enjoy having friends over
How early / late do you wake up in the morning?
How early / late do you go to bed at night?
How much do you customize the appearance of your room?
How much noise do you produce?
"""
class user_profile:
    """    
    A container for a user profile that contains all 12 parameters as a python list
    """
    def __init__(self, parameters:torch.Tensor=torch.zeros(12, dtype=torch.float)):
        """

        Args:
            parameters (torch.Tensor, optional): Tensor of ordered parameters. Defaults to torch.zeros(12, dtype=torch.float).
        """
        self.parameters = parameters

def generate_random_user_profile()->user_profile:
    profile = user_profile()
    for i in range(len(profile.parameters)):
        profile.parameters[i] = random.random()
    return profile

if __name__ == "__main__":
    a = generate_random_user_profile()
    print(a.parameters)
