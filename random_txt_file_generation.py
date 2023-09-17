import os
import random
import string

length = 8

# Function to generate random string of specified length
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Create a directory to store the text files
os.makedirs("generated_files", exist_ok=True)

# Generate 30 text files
for i in range(30):
    random_string = generate_random_string(5)  # Generate a random string of length 5
    file_name = f"generated_files/{random_string}data_scientist_file.txt"
    
    with open(file_name, "w") as file:
        file.write(f"This is the content of {random_string}data_scientist_file.txt")

print("30 text files generated successfully.")
