import zipfile
import secrets
import string

def generate_password(length):
    """Generate a random password of given length."""
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def load_wordlist(file_path):
    """Load passwords from a wordlist file."""
    try:
        with open(file_path, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def hybrid_passwords(wordlist, suffixes):
    """Generate hybrid passwords combining words from a wordlist with suffixes."""
    for word in wordlist:
        yield word  
        for suffix in suffixes:
            yield f"{word}{suffix}"  

def rainbow_table_hashes(wordlist):
    """Simulate generating rainbow table hashes from a wordlist."""
    return {word: hash(word) for word in wordlist}

def dictionary_attack(zip_file, wordlist):
    """Attempt to extract using a dictionary attack."""
    for password in wordlist:
        if try_extract(zip_file, password):
            return password
    return None

def try_extract(zip_file, password):
    """Try to extract the zip file with the given password."""
    try:
        with zipfile.ZipFile(zip_file) as zf:
            zf.extractall(pwd=bytes(password, 'utf-8'))
            print(f'Success! Password is: {password}')
            return True
    except (RuntimeError, zipfile.BadZipFile):
        return False
