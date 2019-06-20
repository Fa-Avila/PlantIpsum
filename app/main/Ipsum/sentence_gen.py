"""Sentence Generator

This module is used to format strings of plant names into paragraphs.
The size of paragraphs and the number of paragraphs are passed into 
the paragraph_gen method. This method uses random from the numpy 
module to determine the number of sentences in each paragraph based 
on a pre determined paragraph size.

"""

from word_gen import get_words
import collections
from numpy import random #needed in order to put weights on the probability of each sentence size

sent_options = ['small', 'medium', 'large'] 

small_par_prob = [0.60, 0.30, 0.10] # probability of a small paragraph  containing [small sentences, medium sentences, or large sentences]  
med_par_prob = [0.40, 0.45, 0.15]   # this is used to have an variety in sentence size.
large_par_prob = [0.30, 0.45, 0.25]

small_sent_length = range(5, 10)
medium_sent_length = range(10, 20)
large_sent_length = range(20, 25)

# sentence generater 
def sentence_gen(par_size, sent_num):
    """ Generates Sentences
    
    Generates sentences using the paragraph size and number of 
    sentences. 
    
   Parameters:
      par_size (str): user defined size of paragraph either 'small',
        'medium', or 'large'
      sent_num (int): number of sentences to be created.
    
    Returns:
      str: representing all the words contained in a paragraph.  
    """
    
    if par_size not in sent_options: 
        print "Input not valid paragraph size"
    try:
        length_prob = [] #The probability list that will be used as weights for sentence lengths.
        if par_size == 'small':
            length_prob = small_par_prob
        if par_size == 'medium':
            length_prob = med_par_prob
        if par_size == 'large':
            length_prob = large_par_prob
            
        paragraphs = _gen_words(sent_num, length_prob)
        print paragraphs
        return paragraphs
    except ValueError:
        print "Input not valid"

def _gen_words(sentence_count, weights):
    """ Generates all the words in a paragraph 
    
    Generates a list of sentences. gen_words uses the weights 
    associated in paragraph size and the number of sentences in the 
    paragraph to create a list of sentences (strings) of varying 
    lengths. The frequence of these lengths are determined by the 
    weights associated with the size of the paragraphs.
    
    For example, in a small paragraph, the weight associated with 
    small sentences is 0.70, medium is 0.25 and large is 0.05. 
    Meaning it is more probable that a sentence will be small. 
    
    this will help determine the lengths of each sentence.
    
    Parameters:
      sentence_count (int): number of sentences in the paragraph.
      weights (list): a list of weights associated with the size 
        chosen for the paragraphs.
    Returns:
      str: returns a string of all the sentences in a paragraph
    """
    
    sentence_length_list = [] # list to contain a list of sentence lengths
    
    for i in range(0, sentence_count):
        sent_size = random.choice(sent_options, p = weights) #choose either 'small' 'medium' or 'large' but weighted depending on the paragraph size.
        if sent_size == 'small':
            sentence_length_list.append(random.choice(small_sent_length))
        if sent_size == 'medium':
            sentence_length_list.append(random.choice(medium_sent_length))
        if sent_size == 'large':
            sentence_length_list.append(random.choice(large_sent_length))

    sentences = get_words(sum(sentence_length_list))
    
    print(sentence_length_list)
    return _format_sent(sentences, sentence_length_list) 

def _format_sent(words, sentence_length_list):
  """ Formats str of words into sentences
  
  Generates sentences by appending words to a sentence string until
  it is of the length specified in the sentence_length_list and 
  adding periods at the end of the string. 
  
  Parameters:
    words (list): list of all the words in the paragraph. 
    sentence_length_list (list): a list of sentence lengths.
  Returns:
    str: returns a string of all the sentences in a paragraph
  """
  sentence_string = "" #holds a paragraph.
  count = 0 #counts the number of words currently in  sentence_string
  i = 0 #keeps track of the sentence being created from sentence_length_list

  for names in words:
    try:
      if (count+1) == sentence_length_list[i]:
        sentence_string += names.lower() + '. ' #ends a sentence
        i += 1
        count = 0
      elif count == 0:
        sentence_string += names.capitalize() + ' '
        count += 1
      else:
        sentence_string+=names.lower() + ' ' #adds spaces between words
        count += 1
    except IndexError:
        continue
  return sentence_string