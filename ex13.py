# Here we import the argument variable module, this holds the arguments you pass to the script when 
# you run it
from sys import argv

# Here we "unpack" argv.  "Take whatever is in argv, unpack it, and assign it to all of these 
# variables on the left in order."
script, first, second, third = argv

print "The script is called:", script # This prints the file name, in this case it's ex13.py
# script seems to be only changeable via the file name.
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# For this to run correctly in the shell, it needs the correct arguments, as follows:
# python ex13.py first 2nd 3rd
# This is interesting as what gets printed is totally dependent on the shell arguments, and they
# can be pretty much anything! 

# Adding some raw_input at the bottom here just to see what happens

grasp = raw_input("On a scale of 1-10, how much do you enjoy using raw input?")
print "%s?  Wow, that much?" % grasp # Don't forget to reference the variable!