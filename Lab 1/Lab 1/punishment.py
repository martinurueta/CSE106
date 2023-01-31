sentence = input("enter a sentence: ")
numbertimes = int(input("enter number of times to repeat sentence: "))
text = open("CompletedPunishment.txt", "w")
for i in range(numbertimes):
    text.write(sentence + '\n')

text.close()

