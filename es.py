# python program that gets areguement from command line.

#import sys module
import sys

# create variable that takes input from command line.
# sys.argv allows us to treat the inputs on the command line as a list,
# where sys.argv[0] would be the actual program, sys.argv[1] would be the 
# following input, etc.
fileName = sys.argv[1]

# Then we create a funtion that will take the above arguement and count 
# the number of e's in the doc.
def ECounter(fileName):
    # Open the given file in read-text mode as 'f':
    with open(fileName, "rt") as f:
        # create variable equal to the text within the doc
        text = f.read()
        # creat a counter starting at 0:
        count = 0
        # Use for loop to count number of 'e's in doc:
        for letter in text:
            if letter == 'e':
                count += 1
            elif letter == 'E':
                count += 1
        return count

# create variable equal to output of function:
number = ECounter(fileName)

# Finally print results:
print("Number of es in document: " + str(number))