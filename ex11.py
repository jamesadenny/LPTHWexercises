print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input() #5'10" breaks the output, it adds a slash like so 5\'10"
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %s tall and %r heavy." % (
	age, height, weight)