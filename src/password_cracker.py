# Imported required libraries
from pwn import *
from zipfile import ZipFile
from argparse import ArgumentParser

# Function to perform the Brute-Force attack
def brute_force(zip_file,max_length):
    # Generate all possible passwords for the given length and try to unzip
    for password in product(chars,repeat=max_length):
        attempt = "".join(password)
        # Check if the password is correct 
        if extract_zip(zip_file,attempt):
            return attempt
    # If no password found for a given length
    print("No password found")
    return None

# Function to extract the zip file
def extract_zip(zip_file,password):
    try:
        with ZipFile(zip_file) as zf:
            # Try to extract the files with the current password
            zf.extractall(pwd=bytes(password,'utf-8'))
            print(f"Found Password : {password}")
            return True
    # If the password is wrong, return False and test with the next password
    except:
        return False

# Command-line interface defined here
if __name__ == "__main__":
    parser = ArgumentParser(description="Brute force zip file password")
    # Parse CLI arguments
    parser.add_argument('zip_file',type=str,help="zip file path")
    parser.add_argument('max_length',type=int,help="Maximum length of password")
    args = parser.parse_args()
    
    # Attempt characters for the password
    chars= "abcdefghijklmnopqrstuvwxyz0123456789"
    
    print("Starting Brute Force Attack")
    
    # Call the function to start brute forcing the zip file
    brute_force(args.zip_file,args.max_length)
