"""
Write a script to locate all of "ERROR" messages in a text file
"""
 
def find_word_error(text_file, search_word):
  file_open = open(text_file)
  line_count = 0
  for line in file_open.readlines():
    line_count += 1
    line = line.rstrip()
    if search_word in line:
      print '%s on line %s' %(search_word, line_count)           
        

find_word_error('word.txt','ERROR' )