#This exercise demonstrates how to call and display external text files in #Python.

from sys import argv
#script is this files name, filename is the text file you're specifying
script, filename = argv
#for this to work, you HAVE TO specify the filename as an argument upon running
#the script.
txt = open(filename)
#This is where it actually starts displaying stuff
print "Here's your file %r:" % filename
print txt.read()
#closing the file now that we're done with it.  Note that we need to preface
#close with the VARIABLE name and not the filename
txt.close()
print "Type the filename again:"
#file_again prompts for the file name, but treats it as raw input.  You don't #have to say the same file again, you can choose a different one.  Try the 
#Shakespeare file.

#"> " is just the prompt pointing to a blank line to type in.
file_again = raw_input("> ")
#Here it opens whatever file you named in file_again
txt_again = open(file_again)
#prints the newly specified file.  Note that it calls it 'read'
print txt_again.read()
#close the file now that we're done with it
txt_again.close()