import random

def random_num_generator():
    askuser = str(
        input("Hi, please choose heads or tails, and type in yes when you do. "))
    if askuser == "yes":
        randomnum = random.randint(0, 1)
        if randomnum == 1:
            print("heads")
            number_of_times = 100000000
            while number_of_times > 0:
             random_num_generator_recursion()
             number_of_times = number_of_times - 1 
        elif randomnum == 0:
            print("tails")
            number_of_times = 100000000
            while number_of_times > 0:
             random_num_generator_recursion()
             number_of_times = number_of_times - 1 
    else:
        print("user input error")
        number_of_times = 100000000
        while number_of_times > 0:
          random_num_generator_recursion()
          number_of_times = number_of_times - 1 

def random_num_generator_recursion():
    askuser = str(input("Would you like to try again?, if yes, type in yes. "))
    if askuser == "yes":
        randomnum = random.randint(0, 1)
        if randomnum == 1:
            print("heads")
        elif randomnum == 0:
            print("tails")
    else:
        exit()

random_num_generator()
