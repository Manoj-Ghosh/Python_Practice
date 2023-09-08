def ispalindrome(string):
  
  ls = []
  
  for i in range(len(string)):
    if string[i] in ls:
      ls.remove(string[i])
    else:
      ls.append(string[i])
      
  if len(string) % 2 == 0 and len(ls) == 0:
    return True
    
  elif len(string) % 2 !=0 and len(ls) == 1:
    return True
    
  else:
    return False
    
    
string = input()
print(ispalindrome(string))
  
  
    
    