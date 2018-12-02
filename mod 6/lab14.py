import os

def eggs():
  
  # set our media directory to where our eggs.txt file is located
  # change this on your system to where your eggs.txt is located
  os.chdir('D:\\Users\\Ivan\\Documents\\school\\CST 205\\CST-205\\mod 6\\')
  
  # opens the eggs.txt file and then places all the lines into one string variable
  fin = open('eggs.txt', 'r')
  words = ""
  word = ""
  index = 0
  totalWords = list()
  words = fin.readlines()

  # the words variable is a list containing each line in the file with formatting
  # commands like \n. this nested loop goes through each element in the words list
  # and then each string in the list, splitting the strings into individual words
  # at each space and each \n. if a line only contains the \n command, it is skipped
  # over. This results in a new list containing only one word at each index.
  
  for row in words:
    if row == "\n":
      continue
    else:
      for letter in row:
        if letter == " " or letter == "\n":
          totalWords.append(word)
          word = ""
          continue
        else:
          word += letter
  
  # Now we create a dictionary in order to make an histogram of frequencies of each word
  # in the list. Then we'll invert the histogram so the count of each word is first, followed
  # by that word. Then we'll sort in ascending order and display to the user.
  histogram = dict()
  for word in totalWords:
    if word not in histogram:
      histogram[word] = 1
    else:
      histogram[word] += 1

  inverse = invert_dict(histogram)

  last = ""
  for key in sorted(inverse):
    print("\n\nThe following word(s) appear " + str(key) + " times:")
    for word in inverse[key]:
      print word,
      last = word
      
  print("\n\nTotal distinct words : %d" % (len(histogram)-1))
  
  print("The most common word is: %s" % word)
  
def invert_dict(d):
  inverse = dict()
  for key in d:
    val = d[key]
    if val not in inverse:
      inverse[val] = [key]
    else:
      inverse[val].append(key)
  return inverse
