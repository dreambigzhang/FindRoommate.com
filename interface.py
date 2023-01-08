import user_profile
import random
import string
import os

def get_random_person():

        if random.random() < 0.01:
            return "Rat Bastard", "./static/rat-shower.gif"
    
        with open('./static/manifest.txt', 'r') as f:
            lines = f.readlines()
        files = os.listdir('./static/lfw_funneled')

        name = random.choice(lines)
        line_num = lines.index(name)
        
        folders = [f for f in os.listdir('./static/lfw_funneled') if os.path.isdir(os.path.join('./static/lfw_funneled', f))]
        folder_path = os.path.join('./static/lfw_funneled', folders[line_num])
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        img_path = os.path.join(folder_path, files[0])
        return name[:-2], img_path


def create_random_dataset(size:int = 2)->list:
    output = [user_profile.user_profile()] * size
    
    for profile in output:
        person = get_random_person()
        profile.age = random.randint(1, 65)
        profile.name = person[0]
        profile.profile_picture = person[1]
    
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