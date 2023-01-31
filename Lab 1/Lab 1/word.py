word = input("Enter a word: ") # get word from user
file = open("PythonSummary.txt", "r") # open file for reading
count = 0 # number of times word occurs in file 
word = word.lower() # convert word to lower case
word = word.strip(".,;:!?") # remove punctuation from word
for line in file: # for each line in file
    line = line.lower() # convert line to lower case
    line = line.strip(".,;:!?") # remove punctuation from line 
    count += line.count(word) # add number of times word occurs in line
print("The word", word, "occurs", count, "times in the file.") # display result