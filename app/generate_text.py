import sys
sys.path.append('/main/Ipsum')
from paragraph_gen import paragraph_gen

def generate(number, size):
  return paragraph_gen(size, number)
