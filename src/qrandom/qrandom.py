#Function name: randint
#Parameters: start (int), stop(int), seed (float)
#Return: integer 
#Description: returns an integer between start (inclusive) and stop (inclusive)

def get_seed():
    return 0.5

def randint(start, stop):
    new_float = get_seed() * ((stop+1) - start) + start - 0.5
    return round(new_float)

#Function name: randrange 
#Parameters: start (int), stop(int), step(int)
#Return: integer 
#Description: returns an integer between start (inclusive) and stop (inclusive), incrementing by step
def randrange(start,stop, seed, step=1):
    random_int = randint(0, (stop - start)/step)
    return start + randint * step

#Function name: randloat
#Parameters: start (float), stop(float), step(int)
#Return: float
#Description: returns a float between start (inclusive) and stop (inclusive)
def randfloat(start, stop):
    return start + (stop - start) * get_seed()

#Function name: randchoice 
#Parameters: user_list []
#Return: element of user_list
def randchoice(user_list):
    random_int = randint(0, len(user_list)-1)
    return user_list[random_int]
