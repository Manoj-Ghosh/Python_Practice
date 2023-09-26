# Python code to demonstrate 
# conversion of a hex string
# to the binary string
  
# Initialising hex string
ini_string = "1a"
scale = 16
  
# Printing initial string
print ("Initial string", ini_string)
  
# Code to convert hex to binary
res = bin(int(ini_string, scale)).zfill(8)
  
# Print the resultant string
print ("Resultant string", str(res))