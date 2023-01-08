import user_profile
import random
import string

# global variable
random_name_generator = user_profile.random_name_generator()

def create_random_dataset(size:int = 2)->list:
    output = [user_profile.user_profile()] * size
    
    # TODO randomize the user_profiles!
    for profile in output:
        profile.age = random.randint(1, 65)
        profile.name = random_name_generator.generate_random_name()
    
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