import sys
sys.path.append('/home/space_radish/MyProjects/PlantIpsum/app/main/Ipsum')
from paragraph_gen import paragraph_gen

def generate(number, size):
  return paragraph_gen(size, number)
