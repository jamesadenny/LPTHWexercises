# This is an exercise in using raw_input to gather data, rather than having to program the data in
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

# I changed tall to %s instead of %r so it will display better.
print "So, you're %r old, %s tall, and %r heavy." % (
age, height, weight)