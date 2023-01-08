# This is the code for generating a dataset of people.
import torch
import random
import os

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

class user_profile:
    def __init__(self):
        self.profile_picture = "https://media.tenor.com/hmsGJDnv6nMAAAAd/rat-shower.gif"
        self.name = "Larry"
        self.age = 12
        self.bio = "I love to rub and scrub. Rub and scrub is what I do all day long. Some would even call me a rubbing enthusiast, or a scrubbing seargent. Anyways I'm looking for a roommate so swipe right if you value cleanliness!"
        self.parameters = torch.rand(12, dtype=torch.float)
        # this is the 'line of best fit' for this user, last value is the offset.
        # not used since we assume there is only one user and all other profiles are simulations
        #self.preference = torch.rand(13, dtype=torch.float)

    def get_profile_picture(self):
        return self.profile_picture

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_bio(self):
        return self.bio

    def get_parameters(self):
        return self.parameters

    def __str__(self):
        return "\"{}\", \"{:d}\", \"{}\", Profile Picture URL:\"{}\"".format(self.name, self.age, self.bio, self.profile_picture)

if __name__ == "__main__":
    a = user_profile()
    print(a.get_parameters())

def get_random_person():
   
    with open('FindRoommate.com\\archive\manifest.txt', 'r') as f:
        lines = f.readlines()
    files = os.listdir('FindRoommate.com\\archive\lfw_funneled')

    name = random.choice(lines)
    line_num = lines.index(name)
    
    folders = [f for f in os.listdir('FindRoommate.com\\archive\lfw_funneled') if os.path.isdir(os.path.join('FindRoommate.com\\archive\lfw_funneled', f))]
    folder_path = os.path.join('FindRoommate.com\\archive\lfw_funneled', folders[line_num])
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    img_path = os.path.join(folder_path, files[0])

    return name[:-2], img_path

print(get_random_person())