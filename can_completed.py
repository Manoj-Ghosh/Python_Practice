def cancompleted(partial_word,complete_word):
  found =""
  
  
  for letter in partial_word:
    
    letter_found = False
    
    while complete_word and letter_found == False:
      
      if letter == complete_word[0]:
        
        complete_word = complete_word[1:]
        
        found += letter
        
        letter_found = True
        
      else:
        
        complete_word = complete_word[1:]
        
        letter_found = False
        
        
  if found == partial_word:
    return True
    
  else:
    return False
    
    
    
complete_word = input("word to be completed: ")
partial_word = input("partial word: ")

print(cancompleted(partial_word,complete_word))


    
        
      
    