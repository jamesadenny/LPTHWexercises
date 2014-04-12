#Importing the argument variables, as usual
from sys import argv
#script is the file name of this script, filename is the text file you'll 
#create
script, filename = argv

"""
Here we have the text saying we're going to erase the file.  The option not to do that is CTRL-C, which breaks out of the script.
"""
print "We're going to erase %r." % filename
"""
I had to copy and paste the ^ character.  At first I tried a similar ASCII
char that broke the code.
"""
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#this is waiting for you to hit RETURN
raw_input("?")

print "Opening the file..."
"""
What are the modifiers to the file modes we can use?
    The most important one to know for now is the + modifier, so you can do 'w+', 'r+', and 'a+'. This will open the file in both read and write mode, and depending on the character use position the file in different ways.
"""
target = open(filename, 'w')#'w' opens the file in write mode

#target.truncate() erases and resaves the file as a blank with the same name
print "Truncating the file.  Goodbye!"
target.truncate() #The file is blank now

print "Now I'm going to ask you for three lines."

"""
Here we're inputting the text, and it gets held in memory until it's written.  It doesn't go directly from raw_input into the text file.  I can see this being a resource issue with larger amounts of data, where it would be necessary to break what gets written into smaller chunks.

Large chunks of text within the raw_input can also break the code.
"""
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#This is where the variables actually get written, each on a new line via \n
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#Never forget to close the file!
print "And finally, we close it."
target.close()