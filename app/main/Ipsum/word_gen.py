"""Word generator

This module generates words that will be used to create sentences
using a csv file of plant names. uses linereader module to have 
random access to the plant dictionary file. 
"""
import os
import random
import collections
import sys
import csv
import linereader

PlantName = collections.namedtuple('PlantName', ['bot', 'com', 'words'])
FILENAME = (os.getenv('DATA_SET') or 'app/static/data/plant_dictionary.csv') # location of database
LASTROW = int (os.getenv('DATA_SET_SIZE') or 1187) #size of database


def get_words(word_count):
  """Choses specified number of words
  Choses specified number of words from the csv file. 
  
  Parameters:
    word_count(int): Number of words to be generated
  Returns:
    list: list of str representing sentences.  
  """
  
  words = _word_chooser(word_count) # gets words
  sentences = []
  i = 0
  for name in words:
    count = int(name.words) #gets number of words in a name
    if i + count > word_count: #if next full name + current word count > needed word count 
      plant = (name.bot.rstrip() + ' ' + name.com.rstrip()) #add spaces
      sentences.extend(plant.split(' ')[:(word_count - i)]) #add only the number of words needed to the sentences list.
      i += count
    else:
      plant = (name.bot.rstrip() + ' ' + name.com.rstrip()) #append full common name
      sentences.extend(plant.split(' '))
      i += count #update current count
  print sentences
  return sentences
 
def _word_chooser(word_count):
  """Random Word Generator
  
  private funtion. Uses the copen function from linereader to have
  random access to a csv file. Using the numpy random function, a 
  random line is chosen decoded to UTF-8 and placed in a tuple that 
  is appended to a list. Using the word count in each line, the 
  function keeps adding words to the sample list until it the current
  line puts the word count to or above the target word count.
  
  Parameters:
    word_count(int): target word count
  Returns:
    list: list of randomly chosen plant names 
  """
  
  sample_word_count = word_count
  sample = []
  current_words = 0
  file = linereader.copen(FILENAME)
  
  while current_words < sample_word_count:
    j = random.randint(2, LASTROW) #skips the first line as it is the header line
    data = file.getline(j)
    for row in csv.reader([data]):
      sample.append(PlantName(bot = row[0].decode('utf-8').replace("'", ""), com = row[1].decode('utf-8').replace("'", ""), words = row[2]))
      words = int(row[2])
    current_words += words
  return sample
