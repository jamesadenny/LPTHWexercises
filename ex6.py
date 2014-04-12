# Variables declared below
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # this is calling two strings into another
#Variables declared above

# Printing some variables
print x
print y

# printing some strings, using the %r modulus displays the sentence properly, whereas using %s in its place 
# would print an extra '.' afterwards.  This is because %r displays the "raw" data of the variable, and 
# is usually used for debugging.  
print "I said: %r." % x
# If you change this %s to an %r, it adds in extraneous double quotes.
print "I also said:  '%s'." % y # This is combining a manually printed string with a string var.

# Here, we declare the variable of hilarious which is a T/F type, and joke_evaluation which is a string.  
# Neither is printed yet.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# Calling the previously declared variables 
print joke_evaluation % hilarious
# This simply shows how two string-type variables can be combined to form a longer string.
w = "This is the left side of..."
e = "a string with a right side."
print w + e