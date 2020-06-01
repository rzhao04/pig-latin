line = raw_input("sentence: ")
vowels = ["a", "e", "i", "o", "u"]
lineList = line.split()
line = []
eachWord = []
for word in lineList:
    if word[0] in "aeiou":
        line.append(word + "way")
    else:
        for letter in word:
            if letter in "aeiou":
                line.append(word[word.index(letter):] + word[:word.index(letter)] + "ay")
print ("  " .join(line))