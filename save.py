# script for saving and loading user data to disk on the server
from user_profile import *
import pickle

class save_data:
    # username is key and data is value
    def __init__(self):
        self.user_profiles = {}


def load_user_profile(username:str):
    """
    Args:
        username (str): the username of the person 

    Returns:
        user_profile: if it exists
        None: if no data is associated with this user
    """
    file = open("savedata.dat", "br")
    save = pickle.load(file)
    file.close()
    return save.user_profiles.get(username)

def save_user_profile(username, user_profile):
    file = open("savedata.dat", "br")
    save = pickle.load(file)
    file.close()
    
    save.user_profiles[username] = user_profile

    file = open("savedata.dat", "bw")
    pickle.dump(save, file)
    file.close()

if __name__ == "__main__":
    print("helo world!")
    
    jono = load_user_profile("jono")
    print(jono)
    carl = load_user_profile("carl")
    print(carl)

    carl = user_profile()
    carl.name = "carl"
    carl.age = 99

    save_user_profile("carl", carl)


