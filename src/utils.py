# Import necessary libraries
import zipfile
import secrets
import string

# Function to generate a random password of a specific length
def generate_password(length):
    """Generate a random password of given length."""
    # Define the characters that could be part of the password  
    characters = string.ascii_letters + string.digits
    # Randomly select `length` characters from the list
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Function to load a wordlist from a file
def load_wordlist(file_path):
    """Load passwords from a wordlist file."""
    try:
        with open(file_path, 'r') as f:
            # Read each line of the file (each password)
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# Function to generate 'hybrid' passwords
def hybrid_passwords(wordlist, suffixes):
    """Generate hybrid passwords combining words from a wordlist with suffixes."""
    for word in wordlist:
        yield word  
        # Append each possible suffix to the word
        for suffix in suffixes:
            yield f"{word}{suffix}"

# Function to generate hashes - this mimics a rainbow table
def rainbow_table_hashes(wordlist):
    """Simulate generating rainbow table hashes from a wordlist."""
    return {word: hash(word) for word in wordlist}

# Function to attempt to crack a zip file using a dictionary attack
def dictionary_attack(zip_file, wordlist):
    """Attempt to extract using a dictionary attack."""
    for password in wordlist:
        # Attempt to extract the file
        if try_extract(zip_file, password):
            return password
    return None

# Function to try and extract a zip file given a password
def try_extract(zip_file, password):
    """Try to extract the zip file with the given password."""
    try:
        with zipfile.ZipFile(zip_file) as zf:
            zf.extractall(pwd=bytes(password, 'utf-8'))
            print(f'Success! Password is: {password}')
            return True
    except (RuntimeError, zipfile.BadZipFile):
        return False
