# This is the code for generating a dataset of people.
import torch

"""
1. What is your gender
2. Do you smoke / vape
3. Do you burn candles or incense
4. Do you have a pet
5. How much do you play a musical instrument
6. How much do you clean
7. How much do you cook
8. How much do  enjoy having friends over
9. How early / late do you wake up in the morning?
10. How early / late do you go to bed at night?
11. How much do you customize the appearance of your room?
12. How much noise do you produce?
"""

def generate_random_user_profile()->torch.Tensor:
    """generates a user profile with random parameters from uniform distribution on interval [0, 1]"""
    return torch.rand(12, dtype=torch.float)

def generate_n_random_user_profiles(n:int)->torch.Tensor:
    return torch.rand(n, 12, dtype=torch.float)

if __name__ == "__main__":
    a = generate_n_random_user_profiles(10)
    print(a)