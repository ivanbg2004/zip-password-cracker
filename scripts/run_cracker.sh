#!/bin/bash

# Initialize variables for zip file path, maximum allowed password length and retries
zip_file=""
max_length=""
retries=10

# Function to show usage information and exit if arguments are not valid
usage() {
    echo "Usage: $0 -z zip_file -m max_length [-r retries]"
    exit 1
}

# Loop through all options passed to the script
while getopts ":z:m:r:" opt; do
  case ${opt} in
    # Save zip file path in zip_file
    z ) 
      zip_file=$OPTARG
      ;;
    # Save maximum allowed password length in max_length
    m )
      max_length=$OPTARG
      ;;
    # Save number of retries in retries
    r )
      retries=$OPTARG
      ;;
    # Show usage info if an invalid option is passed
    \? )
      usage
      ;;
    # Show error message and usage info if an option requiring argument is given without the argument
    : ) 
      echo "Invalid option: $OPTARG requires an argument"
      usage
      ;;
  esac # end of options parsing
done

# Show usage info and exit if zip_file or max_length was not specified
if [[ -z "$zip_file" || -z "$max_length" ]]; then
    usage
    exit 1
fi

# Call python script to crack password the specified number of times
for i in $(seq 1 "$retries"); do
    python3 src/password_cracker.py "$zip_file" "$max_length"
    
    # If the python script exits successfully, break the loop
    if [ "$?" -eq 0 ]; then
        echo "Password cracking completed successfully."
        break
    else
        # If the password was not cracked, retry
        echo "Password not found, retrying attempt: $i..."
    fi
    
    # If the maximum number of attempts has been reached, exit
    if [ "$i" -eq "$retries" ]; then
        echo "Exceeded maximum number of attempts. Exiting..."
        exit 1
    fi
done
