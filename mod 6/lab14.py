# Ivan Alejandre
# Lab 14
#
# *** Requires Python 3 ***
import os

# \\\\\\\\\\\\
# Problem 1 ||
# ////////////

# main function. Run at console.

def eggs():
  # define variables
  words = ""
  word = ""
  index = 0
  mostFrequentWord = ""
  
  # set our media directory to where our eggs.txt file is located
  # change this on your system to where your eggs.txt is located
  os.chdir('C:\\Users\\ivana\\Documents\\school')
  
  # opens the eggs.txt file and then places all the lines into one list of strings
  fin = open('eggs.txt', 'r')
  words = fin.readlines()

  totalWords = splitAllWords(words)
  
  # Now we create a dictionary in order to make an histogram of frequencies of each word
  # in the list. Then we'll invert the histogram so the count of each word is first, followed
  # by that word. Then we'll sort in ascending order and display to the user.

  histogram = createHistogram(totalWords)

  # invert the histogram
  inverse = invert_dict(histogram)

  # prints the sorted, inverted, histogram. also returns the most frequent word in the dictionary
  mostFrequentWord = printSortedDict(inverse)

  # print the total distinct words and the most frequent word.
  print("\n\nTotal distinct words : %d" % (len(histogram)-1))
  
  print("The most common word is: %s" % mostFrequentWord)

# helper functions

""" This function takes a large string, then seperates the string into individual
words and places each word in a list. The seperation points are spaces and new
line characters "\n". Each resulting word is an index in a list. """

def splitAllWords(allLinesList):
  totalWords = list()
  word = ""
  # if an element in the list is just "\n", skip
  for row in allLinesList:
    if row == "\n":
      continue
    else:
      for letter in row:
        # add each character into a word if it is not a space or newline
        if letter == " " or letter == "\n":
          totalWords.append(word)
          word = ""
          continue
        else:
          word += letter
  return totalWords

""" Takes an existing, filled dictionary and inverts the key and value
relationships. Results in a new dictionary that is [frequency] = [list of words]
at that frequency. """

def invert_dict(d):
  inverse = dict()
  for key in d:
    val = d[key]
    if val not in inverse:
      inverse[val] = [key]
    else:
      inverse[val].append(key)
  return inverse

""" The following function takes in a list of strings, and creates a dictionary
    which is a histogram of the frequencies of each word in the passed list.
    The resulting dictionary is passed back.
    """

def createHistogram(wordList):
  histogram = dict()
  for word in wordList:
    if word not in histogram:
      histogram[word] = 1
    else:
      histogram[word] += 1
  return histogram

""" Takes a dictionary and print to the console the dictionary sorted from lowest to highest.
Assumes the dictionary has key:value relationships as number:word. Returns the most frequent
word in the dictionary."""

def printSortedDict(dictionary):
  for key in sorted(dictionary):
    print("\n\nThe following word(s) appear " + str(key) + " times:")
    for word in dictionary[key]:
      print (word, end = ' ')
      last = word
  return word


# \\\\\\\\\\\\
# Problem 2 ||
# ////////////

# main function.

def news():
  # set our media directory to where our eggs.txt file is located
  # change this on your system to where your eggs.txt is located
  os.chdir('C:\\Users\\ivana\\Documents\\school')
  
  # opens the eggs.txt file and then places all the lines into one list of strings
  fin = open('foothillnews.html', 'r')
  words = fin.readlines()

  allLines = splitAllLines(words)

  headlinesList = findHeadlines(allLines)

  actualHeadlines = extractHeadlines(headlinesList[0])
  
  print(actualHeadlines)

def splitAllLines(allLinesList):
  totalWords = list()
  word = ""
  # if an element in the list is just "\n", skip
  for row in allLinesList:
    if row == "\n":
      continue
    else:
      for letter in row:
        # add each character into a word if it is not a space or newline
        if letter == "\n":
          totalWords.append(word)
          word = ""
          continue
        else:
          word += letter
  return totalWords

def findHeadlines(allLines):
  headlines = list()
  tag = "<h3>"
  for line in allLines:
    location = line.find(tag)
    #if line[0] == " ":
     # continue
    if location != -1:
      headlines.append(line)
    else:
      continue
  return headlines

def extractHeadlines(headlinesList):
  actualHeadlines = list()
  startTag = "<h3>"
  endTag = "</h3>"
  sub = ""
  index = 0
  while headlinesList.find(startTag) != -1:
    startLocation = headlinesList.find(startTag) + 4
    endLocation = headlinesList.find(endTag)
    for i in range(startLocation, endLocation):
      sub += headlinesList[i]
    actualHeadlines.append(sub)
    index += 1
  return actualHeadlines
