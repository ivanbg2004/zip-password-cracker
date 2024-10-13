# By Oblivion Forgotten
# Project: A zip pass cracker

# We have to import these stuff so it will make the program (Terminal Based) work, then the rest of the code it's to bruteforce it and send the pass.
from pwn import *
from zipfile import ZipFile
from argparse import ArgumentParser

def brute_force(zip_file,max_length):
    for password in product(chars,repeat=max_length):
        attempt = "".join(password)
        if extract_zip(zip_file,attempt):
            return attempt
    print("No password found")
    return None

def extract_zip(zip_file,password):
    try:
        with ZipFile(zip_file) as zf:
            zf.extractall(pwd=bytes(password,'utf-8'))
            print(f"Found Password : {password}")
            return True
    except:
        return False

if __name__ == "__main__":
    parser = ArgumentParser(description="Brute force zip file password")
    parser.add_argument('zip_file',type=str,help="zip file path")
    parser.add_argument('max_length',type=int,help="Maximum length of password")
    args = parser.parse_args()
    chars= "abcdefghijklmnopqrstuvwxyz0123456789"
    print("Starting Brute Force Attack")
    brute_force(args.zip_file,args.max_length)
