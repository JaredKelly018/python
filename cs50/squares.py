#python in nature files do not comuunicate
#use from to select file and import to select the name of the function you wish to use

from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")
#alt way
import functions
for i in range(10,21):
    print(f"The square of {i} is {functions.square(i)}")