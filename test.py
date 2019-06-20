#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app
from app.main.Ipsum.word_gen import get_words
from app.main.Ipsum.sentence_gen import sentence_gen
from app.main.Ipsum.paragraph_gen import paragraph_gen
from config import Config

class TestConfig(Config):
  TESTING = True
class FunctModuleSetup(unittest.TestCase):
  def setUp(self):
    self.app = create_app(TestConfig)
    self.app_context = self.app.app_context()
    self.app_context.push()
    
  def tearDown(self):
    self.app_context.pop()
    
  def test_word_gen(self):
    #checks if word_gen() generates correct number of words
    self.assertEqual(0, len(get_words(0)))
    self.assertEqual(1, len(get_words(1)))
    self.assertEqual(5, len(get_words(5)))
    self.assertEqual(10, len(get_words(10)))
    self.assertEqual(100, len(get_words(100)))
    self.assertEqual(1187, len(get_words(1187)))
    self.assertEqual(1188, len(get_words(1188))) #size of data set
    
  def test_sentence_gen_word_num(self):
    #checks to see if correct number of sentences are being created
    self.assertEqual(0, sentence_gen('small', 0).count('.'))
    self.assertEqual(1, sentence_gen('small', 1).count('.')) 
    self.assertEqual(10, sentence_gen('small', 10).count('.')) 
    self.assertEqual(0, sentence_gen('medium', 0).count('.'))
    self.assertEqual(1, sentence_gen('medium', 1).count('.')) 
    self.assertEqual(10, sentence_gen('medium', 10).count('.'))
    self.assertEqual(0, sentence_gen('large', 0).count('.'))
    self.assertEqual(1, sentence_gen('large', 1).count('.')) 
    self.assertEqual(10, sentence_gen('large', 10).count('.'))
    
  def test_sentence_gen_paragraph_size(self):
    #checks if words in each sentence is within the range. 
    self.assertTrue(len(sentence_gen('small', 1).split()) in range(5, 25))
    self.assertTrue(len(sentence_gen('medium', 1).split()) in range(5, 25))
    self.assertTrue(len(sentence_gen('large', 1).split()) in range(5, 25))

  def test_paragraph_gen_paragraph_size(self):
    #tests if generates correct number of paragraphs
    self.assertEqual(1, len(paragraph_gen('small', 1)))
    self.assertEqual(5, len(paragraph_gen('small', 5)))
    self.assertEqual(1, len(paragraph_gen('medium', 1)))
    self.assertEqual(5, len(paragraph_gen('medium', 5)))
    self.assertEqual(1, len(paragraph_gen('large', 1)))
    self.assertEqual(5, len(paragraph_gen('large', 5)))
    
if __name__ == '__main__':
  unittest.main()