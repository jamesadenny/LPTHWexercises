# This is an interesting use of a variable, using it to call a pattern of formatting.  In this case, it's
# taking the 4 groups of data, and formatting them according the the modulus command (%r)
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) # Adding a 5 into this mix breaks the formatter variable, and it just prints 
# everything after 'print'.
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# The commas used here keep all these strings together on the same line; remember that the formatter variable
# is treating each line as an individual thing to format.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)