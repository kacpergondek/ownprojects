# Load and open the word list
words = open("words.txt","r")
to_read = words.read()

solution = open("solution.txt","w")

# Retrieve the number of words, not sure what the number is for. But it is the requirement.
count = to_read[:1]
wordcount = int(count)

# Load the words
load = to_read.split()[1:]

# Abbreviate words
for word in load:
    if len(word) < 10:
        solution.write(word + '\n')
    elif len(word) > 10:
        word = ([*word])
        truelength = str(len(word) - 2)
        first = word[0]
        last = word[-1]
        string = str(first + truelength + last)
        solution.write(string + '\n')
