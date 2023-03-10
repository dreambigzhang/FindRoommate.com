import user_profile
import random
import string
import os

map=[]
for a in range (5):
    for i in range(80):
        num = random.randint(0,79)
        map.append(num)

u = 0
def get_random_person():
        global u
        if random.random() < 0.08:
            return "Rat Bastard", "./static/rat-shower.gif", "The sewer",'27',"I love to rub and scrub. Rub and scrub is what I do all day long. Some would even call me a rubbing enthusiast, or a scrubbing seargent. Anyways I'm looking for a roommate so swipe right if you value cleanliness!"
        with open('./static/manifest.txt', 'r') as f:
            lines = f.readlines()
        print(u)
        print(map[u])
        line = lines[map[u]]
        item_list = line.split(',')
        name = item_list[0]
        img_path = item_list[1]
        age = item_list[4]
        location = item_list[2] + ', ' + item_list[3]
        
        with open('./static/bios.txt', 'r') as f:
            liness = f.readlines()
        
        bio = liness[map[u]]
        u += 1
        return name, img_path, location, age, bio


def create_random_dataset(size:int = 2)->list:
    '''
    generate random name and bio info for training
    *Not to be confused with backend ML training data generator
    '''
    output = [user_profile.user_profile()] * size
    for profile in output:
        name, image_path, location, age, bio = get_random_person()
        profile.age = age
        profile.name = name
        profile.profile_picture = image_path
        profile.bio = bio
        
        # set location
        if location == None:
            loc_file = open("location.txt")
            locations = loc_file.readlines()
            total_locations = len(locations)
            location = locations[random.randint(0, total_locations-1)].strip()
        profile.location = location
    return output

def request_user_profile_from_backend()->user_profile.user_profile:
    # TODO call the backend function
    # placeholder :
    a = create_random_dataset(1)
    return a[0]

def respond_score_to_backend(score:float):
    # TODO call the backend function which is expecting a yes/no 
    # response
    # placeholder: 
    assert(score == 0 or score == 1)
    pass

if __name__ == "__main__":
    dataset = create_random_dataset(2)
    for profile in dataset:
        print(profile)