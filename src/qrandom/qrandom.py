def get_seed(distribution):
    #pass distribution with the GET request to determine the queue random number comes from
    return 0.5

#Function name: randint
#Parameters: start (int), stop(int), seed (float)
#Return: integer 
#Description: returns an integer between start (inclusive) and stop (inclusive)
def randint(start, stop, distribution=1):
    new_float = get_seed(distribution) * ((stop+1) - start) + start - 0.5
    return round(new_float)

#Function name: randrange 
#Parameters: start (int), stop(int), step(int)
#Return: integer 
#Description: returns an integer between start (inclusive) and stop (inclusive), incrementing by step
def randrange(start,stop, step=1, distribution=1):
    random_int = randint(0, (stop - start)/step, distribution)
    return start + random_int * step

#Function name: randfloat
#Parameters: start (float), stop(float), step(int)
#Return: float
#Description: returns a float between start (inclusive) and stop (inclusive)
def randfloat(start, stop, distribution=1):
    return start + (stop - start) * get_seed(distribution)

#Function name: randchoice 
#Parameters: user_list []
#Return: element of user_list
def randchoice(user_list, distribution=1):
    random_int = randint(0, len(user_list)-1, distribution)
    return user_list[random_int]
