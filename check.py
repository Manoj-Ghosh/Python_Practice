def check(text, key):
  if key > 0:
    
    result = " "
    text = str(text)
    #print(text)

    for i in range(len(text)):
        #print(text[i])

        char = text[i]

        if char.isupper():
            result += chr(ord(char) + key)

        elif char.islower():
            result += chr(ord(char) + key)

        elif char.isdigit():
            result += str(int(char) + key)

        elif char.isspace():
            result += " "

        elif char == "-":
            result += "-"

    return result
    
  else:
    print("INVALID INPUT!!")


text = input("ENTER YOUR TEXT : ")
key = int(input("ENTER KEY: "))

ans = check(text,key)

if ans != None:
  print("YOUR OUTPUT IS : ",ans)



