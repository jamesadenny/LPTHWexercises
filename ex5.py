# Declaring variables below
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
# trying to convert inches to feet and pounds to kilos here
centimeters = height * 2.54
kilos = weight * 0.453592
# Variables declared above

# Now we're going to print some stuff
print "Let's talk about %s." % name
print "He's %d centimeters tall." % centimeters
print "He weighs %d kilos." % kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)