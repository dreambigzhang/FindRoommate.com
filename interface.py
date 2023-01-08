import user_profile
import random
import string

def create_random_dataset(size:int = 2)->list:
    output = [user_profile.user_profile()] * size
    
    # TODO randomize the user_profiles!
    for profile in output:
        profile.age = random.randint(1, 65)
        name = ""
        for i in range(random.randint(5, 12)):
            name += string.ascii_letters[random.randint(0, 51)]
        profile.name = name
    
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