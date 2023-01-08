# This is the code for generating a people's profiles
import torch
import random
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

class random_name_generator():
    def __init__(self):
        # open first name file
        first_name_file = open("./NameDatabases/NamesDatabases/first names/us.txt")
        self.first_names = first_name_file.readlines()
        self.first_names_count = len(self.first_names)
        # open last name file
        last_name_file = open("./NameDatabases/NamesDatabases/surnames/us.txt")
        self.surnames = last_name_file.readlines()
        self.surnames_count = len(self.surnames)
        

    def generate_random_name(self)->str:
        return self.first_names[random.randint(0, self.first_names_count-1)].strip() + " " + self.surnames[random.randint(0, self.surnames_count-1)].strip()

if __name__ == "__main__":
    a = user_profile()
    print(a.get_parameters())

    rng = random_name_generator()
