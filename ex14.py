#Exercise 14: Prompting and Passing
#Let's do one exercise that uses argv and raw_input together to ask the #user something specific. You will need this for the next exercise where we #learn to read and write files. In this exercise we'll use raw_input #slightly differently by having it just print a simple > prompt. This is #similar to a game like Zork or Adventure.

#Here we're importing and declaring argument variables
from sys import argv

#remember, script is the file name, so you only have to provide the user_name
#argv when running the script
script, user_name, cats = argv

#This is important because it threw me off:  prompt is just a variable that
#we're defining here.  It could called anything, and it's value could be #anything.  
#In this instance, we're simply defining prompt so we can have '> ' display
#every time we're expecting raw input.  
#So when we say variable = raw_input(prompt) it prints the value we assigned
#to prompt.  This obviously becomes more useful the longer the variable 
#string is.
prompt = '> '

#Here we get to the interactive question and answer bit
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

#This is just adding another argument per Study Drill 3
print "You have %s cats.  Right?" % cats