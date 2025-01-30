import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

file1 = open("Computing_Machinery.txt", 'r')
file2 = open("Intelligent_Machinery.txt", 'r')

text1 = file1.read()
text2 = file2.read()

words = text1.split() + text2.split()
occurenceMap = {}
for word in words:
    if word in occurenceMap:
        occurenceMap[word] += 1
    else:
        occurenceMap[word] = 1

words = list(occurenceMap.keys())
occurences = list(occurenceMap.values())
x_axis = np.arange(len(words))
slope, intercept, r, p, std_err = stats.linregress(x_axis, occurences)

def calc_line(x_axis):
    return slope * x_axis + intercept


testWord = input("Enter a word to be predicted: ")
if testWord in words:
    result_y = int(occurenceMap[testWord] / 2)
    print("The word ", testWord ," would likely appear ", result_y, " time(s) in any random Alan Turing paper")
    plt.scatter(words.index(testWord), occurenceMap[testWord], color="red")
else:
    print("The word " + testWord + " would not likely appear in any random Alan Turing paper")
plt.scatter(x_axis, occurences)
plt.ylabel("Occurences of word")
plt.xlabel("Index of word in list of words")
plt.plot(x_axis, calc_line(x_axis), color='red')
plt.show()
