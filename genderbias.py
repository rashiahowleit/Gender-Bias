import matplotlib.pyplot as plt

def fillListFromFile(file):
  new_file = open(file) # open file
  list_files = new_file.readlines() # prints every line of files to lists
  return list_files[1:] # returns list except 0th line since its the description

def analyze_list(list):
  rating_list = []
  gender_list = []
  comment_list = [] # put each index into a list
  for i in list:
    new_list = i.split(",") # split every list by comma
    rating_list.append(float(new_list[0].strip()))
    gender_list.append(new_list[1].strip())
    comment_list.append(new_list[2].strip()) # append each index to corresponding list
  return rating_list, gender_list, comment_list # return each list

def three_list(rating_list, gender_list, comment_list, word):
  man_bad = 0
  man_good = 0
  man_med = 0 
  woman_bad = 0
  woman_good = 0
  woman_med = 0 # sets up each variable for counting 
  
  
  for i in range(len(comment_list)):
    if word in comment_list[i].split(" "): # see if word is in the comment list 
      if gender_list[i] == "W": # if w, go to next function
        if rating_list[i] < 2.5: 
          woman_bad += 1
        elif rating_list[i] > 3.5:
          woman_good += 1
        elif rating_list[i] <= 3.5 and rating_list[i] >= 2.5:
          woman_med += 1 # add each to corresponding count if they fall between numbers
      elif gender_list[i] == "M": # if m, go to next function
        if rating_list[i] < 2.5:
          man_bad += 1
        elif rating_list[i] > 3.5:
          man_good += 1
        elif rating_list[i] <= 3.5 and rating_list[i] >= 2.5:
          man_med += 1  # add to each correspponding count if the fall between numbers
  
  print("Women professor ratings for the word: ", word) 
  print("Bad:", woman_bad)
  print("Medium:", woman_med)
  print("Good:", woman_good)
  print()
  print("Men professor ratings for the word: ", word) 
  print("Bad:", man_bad)
  print("Medium:", man_med)
  print("Good:", man_good)
  return woman_bad, woman_good, woman_med, man_bad, man_good, man_med    

if __name__ == '__main__':
  file = input("Enter filename: \n\n") # file input 
  word = input("Enter word: \n") # word input
  list = fillListFromFile(file)
  rating_list, gender_list, comment_list = analyze_list(list) # define list function
  woman_bad, woman_good, woman_med, man_bad, man_good, man_med = three_list(rating_list, gender_list, comment_list, word) # define lists of genders function

  plt.figure(figsize=(0.5, 4)) # x and y axises of figure
  fig, (ax1, ax2)  = plt.subplots(1, 2) # 2 plots on 1 graph
  ax2 = [woman_bad, woman_good, woman_med]  
  ax1 = [man_bad, man_good, man_med]
  x = ['bad', 'good', 'medium'] # x axis values
  list_max = max(ax1+ax2) # maximum value of both liist
  width1 = 0.75 # width of bars on graph
  
  plt.subplot(1,2,2) # second position of plot on graph
  plt.bar(x, ax2, width = width1, color = 'pink')
  plt.title("Women")
  plt.ylim(0, list_max) # y axis of graph stops at maximum value 
  
  plt.subplot(1,2,1) # first position of plot on graph
  plt.bar(x, ax1, width = width1, color = 'black')
  plt.title("Men")
  plt.ylim(0, list_max) # y axis of graph stops at maximum value

  plt.savefig('graphs.png')
  #plt.ion()
  plt.show()
  